# Content Studio (Valentina + Mito)

Start here. This folder holds everything from the first independent run on 16 Oct 2026.
It sits apart from the Humanizer package and does not change it.

## What's inside

| Path | What it is | Who uses it |
|---|---|---|
| `dashboard.html` | Board of everything: video links, posting kit, rules, costs, blind spots | You |
| `crash-course.html` | 7 short lessons with quick questions | You |
| `storyboard-director.html` | Paste a script, get beats, timing, prompts, rule checks, credit estimate and an edit list | You and Claude |
| `tools/assemble.py` | Free editor: cuts clips, adds voice, captions, hook title, AI label, loudness | Claude (or you) |
| `tools/example-edit.json` | The edit list that made the Instagram cut | Claude |
| `skills/*.skill` | 3 new skills, zipped. Unzip into `~/.claude/skills/` | Claude |
| `skills-src/` | Readable copies of the skills (`SKILL.md.txt`) | You |
| `first-video/POSTING-KIT.md` | Captions, hashtags, settings, checklist | You |
| `first-video/SCRIPT-FINAL.md` | Final script per cut and what changed | You |
| `research/` | Platform rules and the video-technique research, with sources | Both |

## Install the skills (on your laptop)

1. Download the `.skill` files.
2. Unzip each one into `~/.claude/skills/` so you get `~/.claude/skills/idea-to-film/SKILL.md`.
3. In Claude Code, say "use ugc-avatar-video to make the next Valentina video".

## Run the editor yourself (optional)

Needs ffmpeg and Python with `faster-whisper` (`pip install faster-whisper`).

```
python3 tools/assemble.py tools/example-edit.json
```

## Live links

| What | Link |
|---|---|
| Dashboard | https://claude.ai/artifact/Rb6CmTWpw8U9vS6LL6iiiE |
| Storyboard Director | https://claude.ai/artifact/S7aeaYgrTSaYCu6e8VwtaR |
| Crash course | https://claude.ai/artifact/Rb3yb8AB3MFcsCHctvtC76 |
| Video: Instagram + Facebook (1:24) | https://d2ol7oe51mr4n9.cloudfront.net/user_3FW0qSkjzKWAUJN0XG5WfibZZ6V/9eccf096-bd6e-4cb0-856d-4b7e6227282e.mp4 |
| Video: TikTok (1:25) | https://d2ol7oe51mr4n9.cloudfront.net/user_3FW0qSkjzKWAUJN0XG5WfibZZ6V/7762fb6a-67ca-4591-9399-ccbc8bc987ab.mp4 |
| Video: sales cut, after 1,000 followers (1:29) | https://d2ol7oe51mr4n9.cloudfront.net/user_3FW0qSkjzKWAUJN0XG5WfibZZ6V/462858c6-6df8-4c0c-a17d-2011fe5ad4fb.mp4 |
| SOP doc (Drive, AICL folder) | https://docs.google.com/document/d/1HzbXIuDqe4StaZIXnaUF13ZEvE1iGHO8TAuKgrpSNXg/edit |

Credits used: 279 of 752 (473 left).
