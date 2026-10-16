#!/usr/bin/env python3
"""Assemble a vertical short from clips, voice-over and an edit list.

A free stand-in for CapCut's auto captions + timeline. It reads an edit list
(JSON), cuts each clip to its voice line, lays the clean voice on top, burns
word-by-word captions inside the platform safe zone, adds a hook title, and
normalises loudness.

Needs: ffmpeg with libass, Python 3.9+, faster-whisper (for caption timing).

Usage:
    python3 assemble.py edit.json

Edit list fields (see example-edit.json):
    output        output file path
    width, height default 1080 x 1920
    fps           default 30
    font          caption font name (default Montserrat)
    loudness      target LUFS (default -14)
    hook          {"text", "start", "end"} big title at the top (works with sound off)
    label         {"text", "start", "end"} small disclosure line (for example "AI-generated host")
    captions      true to burn captions
    segments      list of:
        audio       voice file for this beat (its length sets the beat length)
        text        the exact words in the audio (captions use these words)
        pad         seconds of silence after the line (default 0.15)
        videos      list of {"file", "start"} clips that fill the beat in order
        fit         "cut" (default) or "stretch" (slow the clip to fill the beat)
        zoom        true for a slow push-in on static talking shots
        title       optional on-screen title for the whole beat (for example "1/3 GUM LINE")
    accent        list of words to colour gold in the captions (for example ["ONE", "GUT"])
"""

from __future__ import annotations

import difflib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"Command failed: {' '.join(cmd[:6])}...\n{result.stderr[-2000:]}")


def duration(path: str) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def build_segment(seg: dict, idx: int, cfg: dict, tmp: Path) -> tuple[Path, float]:
    """Render one beat as a normalised clip with its voice line."""
    w, h, fps = cfg["width"], cfg["height"], cfg["fps"]
    voice = seg["audio"]
    length = duration(voice) + float(seg.get("pad", 0.15))
    parts = []
    remaining = length
    videos = seg["videos"]
    for n, v in enumerate(videos):
        if remaining <= 0.01:
            break
        start = float(v.get("start", 0))
        available = duration(v["file"]) - start
        is_last = n == len(videos) - 1
        take = remaining if is_last else min(available, remaining)
        speed = 1.0
        if seg.get("fit") == "stretch" and is_last and available < take:
            speed = available / take
        vf = [f"setpts=(PTS-STARTPTS)/{speed}"] if speed != 1.0 else ["setpts=PTS-STARTPTS"]
        vf += [
            f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos",
            f"crop={w}:{h}",
            f"fps={fps}",
        ]
        if seg.get("zoom"):
            frames = max(1, int(take * fps))
            vf.append(
                f"zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                f":d=1:s={w}x{h}:fps={fps}"
            )
        # Hold the last frame if the clip is shorter than the beat.
        vf.append(f"tpad=stop_mode=clone:stop_duration={take + 1:.2f}")
        vf.append(f"trim=duration={take:.3f},setpts=PTS-STARTPTS,format=yuv420p")
        part = tmp / f"seg{idx:02d}_{n}.mp4"
        run([
            "ffmpeg", "-v", "error", "-y", "-ss", f"{start:.3f}", "-i", v["file"],
            "-an", "-vf", ",".join(vf), "-c:v", "libx264", "-preset", "medium",
            "-crf", "16", str(part),
        ])
        parts.append(part)
        remaining -= take
    listing = tmp / f"seg{idx:02d}.txt"
    listing.write_text("".join(f"file '{p}'\n" for p in parts))
    silent = tmp / f"seg{idx:02d}_v.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
         "-c", "copy", str(silent)])
    out = tmp / f"seg{idx:02d}_av.mp4"
    run([
        "ffmpeg", "-v", "error", "-y", "-i", str(silent), "-i", voice,
        "-filter_complex", f"[1:a]aresample=48000,apad,atrim=0:{length:.3f}[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-t", f"{length:.3f}", str(out),
    ])
    return out, length


def word_times(audio: str, text: str) -> list[tuple[float, float, str]]:
    """Time the authored words with Whisper, keeping the authored spelling."""
    from faster_whisper import WhisperModel

    model = word_times.model = getattr(word_times, "model", None) or WhisperModel(
        "small.en", compute_type="int8"
    )
    segments, _ = model.transcribe(audio, word_timestamps=True)
    heard = [(w.start, w.end, w.word.strip()) for s in segments for w in s.words]
    authored = text.split()

    def norm(word: str) -> str:
        return re.sub(r"[^a-z0-9]", "", word.lower())

    matcher = difflib.SequenceMatcher(
        a=[norm(w) for w in authored], b=[norm(w[2]) for w in heard], autojunk=False
    )
    timed: list[tuple[float, float, str] | None] = [None] * len(authored)
    for block in matcher.get_opcodes():
        tag, a0, a1, b0, b1 = block
        if tag == "equal" or (tag == "replace" and a1 - a0 == b1 - b0):
            for k in range(a1 - a0):
                st, en, _ = heard[b0 + k]
                timed[a0 + k] = (st, en, authored[a0 + k])
    # Fill gaps by spreading time between known neighbours.
    last_end = 0.0
    for i, item in enumerate(timed):
        if item is None:
            nxt = next((t[0] for t in timed[i + 1:] if t), last_end + 0.3)
            timed[i] = (last_end, max(last_end + 0.12, nxt), authored[i])
        last_end = timed[i][1]
    return timed  # type: ignore[return-value]


def ass_time(t: float) -> str:
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def build_ass(cfg: dict, words: list[tuple[float, float, str]], path: Path) -> None:
    w, h, font = cfg["width"], cfg["height"], cfg.get("font", "Montserrat")
    # Safe zone: keep captions above the bottom 670 px and out of the right 160 px.
    lines = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {w}", f"PlayResY: {h}", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
        "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        f"Style: Cap,{font},90,&H00FFFFFF,&H0000FFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,2,2,90,170,720,1",
        f"Style: Hook,{font},70,&H00FFFFFF,&H00FFFFFF,&H00000000,&HB4000000,-1,0,0,0,100,100,0,0,3,18,0,8,90,170,300,1",
        f"Style: Label,{font},34,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,3,8,0,8,90,170,250,1",
        "", "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    hook = cfg.get("hook")
    if hook:
        lines.append(f"Dialogue: 1,{ass_time(hook['start'])},{ass_time(hook['end'])},Hook,,0,0,0,,{hook['text']}")
    label = cfg.get("label")
    if label:
        lines.append(f"Dialogue: 1,{ass_time(label['start'])},{ass_time(label['end'])},Label,,0,0,0,,{label['text']}")
    for start, end, title in cfg.get("_titles", []):
        lines.append(f"Dialogue: 1,{ass_time(start)},{ass_time(end)},Hook,,0,0,0,,{title}")
    accent = {a.upper() for a in cfg.get("accent", [])}
    # Group words into 1-3 word chunks; break on punctuation.
    chunk: list[tuple[float, float, str]] = []
    chunks = []
    for item in words:
        chunk.append(item)
        if len(chunk) == 3 or re.search(r"[.,?!]$", item[2]):
            chunks.append(chunk)
            chunk = []
    if chunk:
        chunks.append(chunk)
    for i, c in enumerate(chunks):
        start = c[0][0]
        end = chunks[i + 1][0][0] if i + 1 < len(chunks) else c[-1][1] + 0.3
        end = min(end, c[-1][1] + 0.6)
        shown = []
        for x in c:
            word = re.sub(r"[,.]$", "", x[2].upper())
            if re.sub(r"[^A-Z0-9]", "", word) in accent:
                word = "{\\c&H00C8FF&}" + word + "{\\c&HFFFFFF&}"
            shown.append(word)
        text = " ".join(shown)
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Cap,,0,0,0,,{text}")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 assemble.py edit.json")
    cfg = json.loads(Path(sys.argv[1]).read_text())
    cfg.setdefault("width", 1080)
    cfg.setdefault("height", 1920)
    cfg.setdefault("fps", 30)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        clips, words, t = [], [], 0.0
        cfg["_titles"] = []
        for i, seg in enumerate(cfg["segments"]):
            clip, length = build_segment(seg, i, cfg, tmp)
            clips.append(clip)
            if seg.get("title"):
                cfg["_titles"].append((t, t + length, seg["title"]))
            if cfg.get("captions", True) and seg.get("text"):
                for st, en, wd in word_times(seg["audio"], seg["text"]):
                    words.append((st + t, en + t, wd))
            t += length
            print(f"beat {i + 1}: {length:.2f}s")
        listing = tmp / "all.txt"
        listing.write_text("".join(f"file '{c}'\n" for c in clips))
        joined = tmp / "joined.mp4"
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
             "-c", "copy", str(joined)])
        ass = tmp / "captions.ass"
        build_ass(cfg, words, ass)
        Path(cfg["output"]).with_suffix(".ass").write_text(ass.read_text())
        lufs = cfg.get("loudness", -14)
        run([
            "ffmpeg", "-v", "error", "-y", "-i", str(joined),
            "-vf", f"subtitles={ass}", "-af", f"loudnorm=I={lufs}:TP=-1.5:LRA=11",
            "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-profile:v", "high",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", cfg["output"],
        ])
        print(f"done: {cfg['output']} ({duration(cfg['output']):.2f}s)")


if __name__ == "__main__":
    main()
