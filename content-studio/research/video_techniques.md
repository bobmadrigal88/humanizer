# Video techniques: CapCut AI travel vlog and Buzzy idea-to-film

Research date: 2026-10-16.

## How to read this report

- **Access limits.** YouTube was blocked. Direct page fetches (WebFetch and curl) were also blocked by the network proxy for every site tried (buzzyai.video, filmora.wondershare.com, aistart.ai). All facts come from web search result snippets.
- **No transcripts were found** for either video. Transcript sites (youtubetranscript, glasp, summarize.tech, NoteGPT, tactiq) returned no indexed copy.
- **Labels used:**
  - **[V]** = verified by at least one search snippet, with source cited.
  - **[Vendor]** = claim comes only from the vendor's own marketing page.
  - **[Inferred]** = my reconstruction of what the video likely shows. Not seen in the video.
  - **[Unverified]** = sources conflict or nothing confirmed it.

---

## Part 1. Video 1: "How to Use CapCut AI Tools Better than 99% of Editors"

URL: https://www.youtube.com/watch?v=lCly-zH6A78

### What is known

| Item | Finding | Status |
|---|---|---|
| Posted | About 14 days before 2026-10-16, so roughly 2026-10-02 | [V] search listing |
| Topic | Builds a complete travel vlog with CapCut AI tools, "from generating a consisten[t character]..." (description is cut off) | [V] search listing |
| Channel | Not found | [Unverified] |
| Transcript or summary | Not found on any transcript site | — |
| "99%" claim | Title framing only; no source supports it | — |

### Likely workflow (reconstructed)

This is my best reconstruction from the description, CapCut's own 2026 guides on consistent characters, and its travel-vlog page. **[Inferred]**

1. **Write the idea and script.** Use AI Writer or Script to Video to draft a travel story (places, beats, voice-over lines).
2. **Create a consistent character (the traveler).**
   - Make one "anchor" image of the character.
   - Keep a short, fixed identity description (face, hair, outfit, colors). Paste it into every prompt.
   - Change only the action, location, and camera in each new prompt.
   - Use image-to-video from the anchor still, not text-to-video, for each scene. Reviews say image-to-video is CapCut's strongest AI video mode.
   - Source: CapCut "Character Consistency in AI Video Clips" https://www.capcut.com/create/character-consistency-ai-video-clips-reference-images and "Keep Characters Consistent Across AI Video Scenes on CapCut PC" https://www.capcut.com/resource/keep-characters-consistent-ai-video-scenes-capcut-pc
3. **Generate scene clips** with the AI video generator (Seedance 2.0 inside CapCut, where the region has it), one clip per location beat.
4. **Assemble on the timeline.** Add voice-over (text-to-speech), auto captions, AI music, transitions, and keyframed zooms or pans.
5. **Polish.** Relight, background removal for "traveler in front of landmark" shots, AI effects, color filters.
6. **Reframe and export.** Auto reframe to 9:16 for Shorts, Reels, and TikTok, and keep 16:9 for YouTube.

### CapCut 2026 AI feature set

Menu paths change by version, region, and platform. Check them in the installed build. Free vs Pro reports conflict between sources; check CapCut's official plan page.

| Feature | What it does | Where (desktop / mobile / web) | Free vs Pro | Status / sources |
|---|---|---|---|---|
| **AI character / consistent character** | No single "lock character" toggle was confirmed. CapCut teaches a workflow: anchor image, fixed identity text, reference images, image-to-video. CapCut warns that references "do not guarantee an identical face, outfit, or body shape." Reviews say drift between clips is still a problem, and you cannot lock a seed. | AI video / AI design tools on desktop and web; AI Avatar on web ("Avatar video") | Generation uses credits; heavier use needs paid plan | [V] workflow; [Unverified] dedicated mobile feature. https://www.capcut.com/create/character-consistency-ai-video-clips-reference-images ; https://www.nemovideo.com/blog/capcut-ai-video-generator-review ; https://morphed.app/blog/capcut-ai-video-generator |
| **AI avatar** | Builds a digital presenter from a front-facing photo or short video; prebuilt avatars too | Web: "Avatar video"; app versions exist | [Unverified] | https://www.capcut.com/create/ai-avatar ; https://www.snaplama.com/blog/how-to-create-ai-avatar-in-capcut-complete-2025-2026-guide |
| **AI video generation (Seedance 2.0 / Sora 2)** | Text-to-video and image-to-video. Seedance 2.0 came to CapCut in March 2026, first in Brazil, Indonesia, Malaysia, Mexico, Philippines, Thailand, Vietnam. Dreamina's Seedance 2.0 takes up to 12 references (9 images, 3 videos, 3 audio). | Desktop, web, mobile (by region) | Paid users, select markets | [V] https://techcrunch.com/2026/03/26/bytedances-new-ai-video-generation-model-dreamina-seedance-2-0-comes-to-capcut/ ; [Vendor] https://dreamina.capcut.com/tools/seedance-2-0 ; "Character Lock" and "Director Mode" claims [Unverified] |
| **Script to Video** | Turns a prompt or script into a draft timeline with scenes, stock clips, music, and voice-over. One review says it assembles stock footage, so it is not fully generative. Treat output as a draft. | Desktop: Script to Video → AI Writer → type idea → Smart Generation. Web: Script to Video entry. | Limited free; more on Pro | [V] https://www.capcut.com/tools/script-to-video-maker ; https://www.frankx.ai/blog/ultimate-capcut-workflow-2026 |
| **AI Writer** | Generates a script from a prompt | Inside Script to Video and Text panel | Limited free | [V] https://www.capcut.com/resource/how-to-use-capcut-on-pc |
| **Auto captions** | Speech to subtitles; then style the text | Desktop: "Captions" in left toolbar → Auto captions → choose language → Generate (older builds: under Text, or "Caption"). Mobile: Text / Captions. | Free (one source: up to 10 min per video) | [V] https://www.capcut.com/help/how-to-recognise-subtitles ; https://typito.com/blog/capcut-auto-captions-add-subtitles-in-capcut/ |
| **Text-to-speech** | Turns a text layer into voice-over on its own audio track. 50+ voices per one review; lineup varies by region. | Desktop: Text → Default text → type script → "Text to speech" in right panel → pick voice → Generate. Mobile: select text → Text to speech. Missing in some Mac builds or regions. | Free with limits | [V] https://anyvoice.io/blog/capcut-text-to-speech ; https://www.camb.ai/blog-post/add-text-to-speech-capcut-pro-tools |
| **AI voice / voice changer / voice clone** | Voice effects and enhancement; voice cloning | Audio panel (Voice changer, Enhance voice) | Voice cloning is Pro only | [V] https://www.miracamp.com/learn/capcut/price-free-vs-capcut-pro ; https://primalvideo.com/guides/capcut-ai-tools/ |
| **Enhance voice / noise reduction** | Cleans speech, removes background noise | Select clip → Audio → Enhance voice | [Unverified] tier | [V] search summary of CapCut guides |
| **Auto Cut / Smart Cut / AutoCut** | Finds highlights and cuts best moments; Smart Cut removes silences and pauses | Desktop toolbar / mobile "AutoCut" | Limited on Free, unlimited on Pro | [V] https://www.capcut.com/resource/ai-cut ; https://fluxnote.io/guides/capcut-ai-features-free-vs-paid-2026 |
| **Background removal** | AI cutout of the person, no green screen. Hair and glasses may need brush touch-up. | Desktop: select clip → Video → Remove BG → Auto removal (also Custom removal, Chroma key). Mobile: Edit → Remove background. Separate "AI remove" (Video → Basic) erases objects. | Free with limits | [V] https://www.capcut.com/resource/how-to-remove-background-in-capcut ; https://www.skillademia.com/capcut/how-to-remove-the-background-in-capcut/ |
| **Relight** | AI changes lighting: intensity, color, radius, direction; 15+ light presets; can target face or background | Desktop (Mac, Windows); in video/image adjust panel | [Unverified] tier | [Vendor] https://www.capcut.com/tools/relight-videos-with-ai ; https://www.capcut.com/resource/relight-photo |
| **AI effects** | Prompt-based or AI style effects on clips (stylize, transform) | Effects panel | [Unverified] | No source found for 2026 details |
| **AI music** | Text-to-music: describe mood, genre, tempo; track goes to timeline. CapCut also has a large royalty-free library. | Audio panel | [Unverified]; CapCut calls it free; third parties found no AI generator on any tier | [Vendor] https://www.capcut.com/resource/top-7-ai-music-generators-for-travel-vlogs |
| **Separate audio / vocal isolation** | Splits vocals, drums, etc. into tracks | Audio panel | Vocal isolation listed as Pro | [V] https://www.miracamp.com/learn/capcut/price-free-vs-capcut-pro |
| **Auto reframe** | Tracks the subject and reframes to a new aspect ratio | Desktop: Video → Basic → Auto reframe → pick ratio | Pro or Pro-accelerated per some sources | [V] https://www.capcut.com/resource/how-to-use-capcut-on-pc ; https://fluxnote.io/guides/capcut-ai-features-free-vs-paid-2026 |
| **Keyframes** | Animate Position, Scale, Rotation, Opacity, Effect, Audio between two states | Desktop: select clip → diamond next to a property in right panel (filled = keyframe at playhead). Mobile: diamond icon near preview/timeline. | Free | [V] https://www.capcut.com/help/keyframes-in-capcut-pc ; https://www.technobezz.com/how-to-add-keyframes-in-capcut-pc |
| **Templates** | Prebuilt edits; drop in clips. Mini vlog templates exist. | Mobile Templates tab; desktop and web Templates | Many free; some Pro | [V] https://www.capcut.com/explore/mini-vlog-template/7520713674706257928 |
| **Upscale / enhance** | AI upscaling of video or image | AI tools hub | Pro for 4K | [V] https://www.capcut.com/tools/ai-tools |
| **Camera tracking, remove flickers** | Stabilize-style tracking; deflicker | Video panel | Pro | [V] search summary of pricing guides |

**Pricing.** Tiers: Free, Standard, Pro. Pro is about $19.99/month or $179.99/year on US web (local prices vary). Pro adds 4K export, full asset library, and advanced AI. AI generation uses monthly credits. Source: https://www.eesel.ai/blog/capcut-pricing ; https://vidpros.com/capcut-pro-vs-free/

### Travel-vlog advice from related sources

- A real filmed host needs no AI consistency tool. Series consistency comes from color grade, audio levels, and recurring graphics. https://eurotravelo.com/how-to-keep-your-travel-vlog-host-looking-consistent-across-ai-edited-clips/
- CapCut's travel-vlogger page and Owl Over The World cover the usual edit: trim, captions, music, transitions, color. https://www.capcut.com/create/ai-video-editing-for-travel-vloggers ; https://owlovertheworld.com/edit-travel-vlogs-with-capcut/
- Always review auto captions by hand. https://www.nemovideo.com/blog/capcut-ai-video-generator-review
- Preview upscaled output at full size against the original before export. https://www.capcut.com/resource/ai-cut

---

## Part 2. Video 2: "Buzzy AI Tutorial (2026) — Turn One Idea Into a Cinematic Film"

URL: https://www.youtube.com/watch?v=p4Uz4Q3_zV4

### What is known

- Description says it follows "one simple workflow from start to finish". It includes a discount link and coupon code, so it is sponsored or affiliate content. [V]
- Contents of the video could not be seen. Steps below are rebuilt from Buzzy's pages and third-party guides. [Inferred]
- Related tutorials on the same workflow: https://www.youtube.com/watch?v=LOJOhJLnoPM , https://www.youtube.com/watch?v=CazTVnwurvc , https://www.youtube.com/watch?v=cHYzZDe29Gg , https://www.youtube.com/watch?v=gSVhpAMoK4Q
- Do not confuse with "Buzzy" the app builder (docs.buzzy.buzz). Different product.

### What Buzzy is

- Browser-based "Director Canvas" and agentic "Buzzy Canvas" (also called "AI co-director"). [Vendor] https://www.buzzyai.video/director ; https://x.com/Buzzy_now_AI/status/2064346847838388486
- Combines 11+ video and image models in one canvas: Seedance (2.0 / 2.5), Kling, Runway (Gen-4), Veo, Sora 2, GPT image, Nano Banana, Midjourney. [Vendor] https://www.buzzyai.video/ ; https://www.buzzy.now/sora ; https://www.buzzy.now/runway-gen-4
- Domains seen: buzzyai.video, buzzy.now.
- Canvas limits claimed: 4K, up to 30 s per generation, up to 50 reference inputs. [Vendor]

### Step-by-step workflow (reconstructed)

1. **Sign up.** Browser only, no install. [V] French guide https://www.ai-operators-academy.fr/ressources/creer-videos-ia-buzzy-canvas-guide
2. **Give the agent one idea.** The Creative Agent builds a **moodboard** and a **storyline** on the canvas. [V] same guide; [Vendor] X post
3. **Create the character sheet.** "Omni Reference": one photo → full character sheet, reused in every shot. [V] French guide
4. **Generate the storyboard.** From the idea or an image. A **9-square grid** splits the project into frames before any clip renders. Each frame has its lighting and camera move set in advance. The storyboard **locks** characters, objects, and locations. [Vendor] https://www.buzzyai.video/director
5. **Direct each shot on the canvas.**
   - Drag or rotate the **camera cube** to set angle, tilt, and motion; sliders for angle, tilt, zoom.
   - **Relight:** key light, color temperature, rim light toggle, in real time.
   - Fix one area by highlighting it or by a text command, instead of regenerating the whole shot. [V] Filmora review (French) https://filmora.wondershare.fr/video-editor-review/buzzy-review.html
6. **Pick a model and render.** Seedance 2.5 for multi-shot consistency, Veo / Kling / Runway / Sora per shot need. [Vendor]
7. **Export.** Up to 4K on paid plans (vendor); one guide says 1080p. [Unverified which applies]
8. **Finish elsewhere.** Filmora's review uses Buzzy for generation, then a separate editor for trim, sound, and captions. One Buzzy page says audio needs a separate post step. [V] https://filmora.wondershare.com/video-editor-review/buzzy-review.html ; [Vendor] https://www.buzzy.now/seedance-2-5

### Prompting tactics (from Buzzy's Seedance 2.5 guides)

- **Seven-slot formula:** Subject → Action → Camera → Motion → Lighting → Style → (Reference). [Vendor] https://www.buzzy.now/blog/seedance-2-5-prompt-guide
- **Short order (product page):** subject, action, environment, lighting, camera movement. https://www.buzzy.now/seedance-2-5
- **Image-to-video order:** subject and motion first, camera second, mood and light last. https://www.buzzy.now/blog/buzzy-seedance-2-5-image-to-video
- **Shot size is separate from movement.** Sizes: close-up, medium, wide establishing, aerial.
- **Camera moves:** dolly, pan, tilt, tracking, crane, orbit, push-in, pull-out, zoom, static.
- **One camera move per shot.** Put shot size and move before light and mood. [V] Dreamina guide https://dreamina.capcut.com/seedance/seedance-2-5-prompt
- **Continuous moves work better in 2.5** (for example a slow dolly beside a walking subject).
- **Lighting keywords fall into four groups:** light-source placement, natural-light moments (golden hour, blue hour), color-grade style, film-look references.
- **Weakness:** Seedance 2.5 follows complex multi-element prompts less faithfully than Sora 2 and renders on-screen text worse. Keep prompts simple; add text in the editor. [Vendor admits] https://www.buzzy.now/blog/seedance-2-5-vs-sora
- **Multi-shot in one generation:** Higgsfield's guide shows a 30 s, five-segment sequence with four "HARD CUT" markers. https://higgsfield.ai/blog/seedance-2-5-prompting-guide

### Consistency tactics

- One clean, **front-facing reference with neutral lighting**. Dramatic light in the reference leaks into later shots.
- Give **each storyboard cell its own reference image** instead of re-prompting.
- **Repeat identical lighting and style tokens word for word** in every prompt of a sequence. https://www.buzzy.now/blog/seedance-2-5-tutorial-blog
- **Split long clips:** make a 30 s piece as three 10 s segments with the same reference; re-run any segment that drifts. https://www.buzzy.now/blog/seedance-2-5-prompt-guide
- **Lock locations and objects** in the storyboard, not only characters.
- **Storyboard before you render**, so bad references show up before you spend credits.
- **Validate 3 to 5 anchor images per character** before the full shot breakdown. (General guide, not Buzzy.) https://frankhoubre.com/blog/generer-storyboard-professionnel-complet-ia

### Storyboard and shot list conventions (reconstructed)

- **Moodboard first, then storyboard.** Moodboard fixes art direction (style, wardrobe, palette). Storyboard splits the story into shots.
- **9-panel grid** as the default sequence size (vendor). A 30 s film at 3 s per panel fits 9 to 10 panels.
- **Per panel, write:** shot number, shot size, camera angle, camera move, subject + action, location, lighting (key, temperature, rim), duration, model, reference IDs.
- **Multi-cam coverage:** for one moment, generate wide + medium + close-up from different cube angles, so the edit has cut options. [Inferred from "multi-cam storyboard" and camera cube]

### Pricing and free tier (conflicting)

| Source | Free | Paid |
|---|---|---|
| Official site (buzzyai.video), per search snippet | Starter $0: 20 generations/month, 720p | Creator $15/mo: 500 generations, 4K, 30 s clips. Studio $49/mo: unlimited |
| Filmora review | 50 free credits, 1080p cap | $19 to $199/mo |
| NemoVideo | First 2 AI videos free on sign-up; about 10 credits per second | No public price page |

The official tiers are most likely current, but none could be opened directly. [Unverified] https://www.nemovideo.com/blog/is-buzzy-ai-free-pricing-2026

---

## Part 3. General, tool-independent tactics

These are standard film and short-form practice. Both videos apply them through their tools. Most are not tool claims, so they need no source; tool mappings are listed for later skills.

### 3.1 Pre-production pipeline

| Step | Output | Rule of thumb |
|---|---|---|
| 1. Idea | One sentence | Who wants what, where |
| 2. Logline | 1 to 2 sentences | Hero + goal + obstacle + stakes |
| 3. Beat sheet | 5 to 9 beats | Hook, setup, journey beats, turn, payoff, outro/CTA |
| 4. Script / VO | Lines per beat | About 2.5 words per second of voice-over |
| 5. Moodboard | 6 to 12 images | Palette, light, wardrobe, film look |
| 6. Character sheet | Front, 3/4, side, full body, expressions | Neutral light, plain background |
| 7. Location sheet | Wide + 2 detail angles per place | Same time of day per scene |
| 8. Storyboard | One frame per shot | Approve frames before video |
| 9. Shot list | Table (below) | One move per shot |

### 3.2 Shot list template

| # | Beat | Dur (s) | Size | Angle | Move | Subject + action | Location | Light | Audio | Refs | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hook | 2 | ECU | eye level | push-in | traveler opens train window | alpine train | golden hour, warm key, rim | wind SFX | char_A, loc_train | i2v |

### 3.3 Camera language cheat sheet

- **Sizes:** ECU, CU, MCU, MS, MWS, WS, EWS / establishing, aerial, POV, over-the-shoulder, insert.
- **Angles:** eye level, low (power), high (small), dutch (unease), top-down.
- **Moves:** static, pan, tilt, dolly in/out, push-in, pull-out, tracking / follow, crane / jib, orbit, handheld, whip pan, zoom.
- **Lenses (prompt words):** wide 24mm for places, 50mm natural, 85mm portrait with shallow depth of field.
- **Coverage pattern:** establish (wide) → orient (medium) → emotion (close-up) → detail (insert) → back out.

### 3.4 Consistency rules

- One fixed **identity block** (age, face, hair, outfit, colors) pasted word for word in every prompt.
- Start every shot from an approved **reference image** (image-to-video), not plain text.
- Fix **lighting tokens** per scene (direction, time of day, color temperature) and repeat them.
- Keep **wardrobe and props** in a continuity list; check each shot against it.
- Keep **screen direction** (180-degree rule): if the traveler walks left to right, keep it until a clear turn.
- **Re-roll** drifting shots; do not try to fix drift in the edit.
- Generate in short segments (5 to 10 s); stitch in the editor.

### 3.5 Editing and pacing

- **Hook in the first 1 to 2 seconds:** strongest image, motion, or question. No logo intro.
- **Cut on action:** cut during a movement so the move hides the cut.
- **Shot length:** 1.5 to 3 s for social; 3 to 6 s for cinematic. Vary length; speed up toward the climax.
- **B-roll** over every voice-over line; change the image when the sentence changes topic.
- **J-cuts and L-cuts:** let sound lead or trail the picture.
- **Match cuts** between locations (shape, motion, color).
- **Speed ramps** and keyframed zooms add energy; use sparingly.
- **Pattern interrupt** every 5 to 8 s in shorts (new angle, text, sound hit).
- **Payoff and call to action** at the end; loop the last frame to the first for shorts.

### 3.6 Captions and text

- Burn in captions; most social viewers watch muted.
- 1 to 4 words per caption for shorts; highlight the key word; keep inside safe areas (avoid the bottom 20% and right edge on 9:16).
- Check auto captions by hand for names and places.

### 3.7 Sound design

- Layers: voice-over (loudest), music (ducked about -12 to -18 dB under voice), ambience (room tone, city, wind), spot SFX (whoosh on transitions, hits on cuts).
- Cut to the music beat.
- Loudness target about -14 LUFS for YouTube and social.
- AI video audio is often weak or missing; plan a separate audio pass.

### 3.8 Color and look

- Pick one grade per film (for example warm teal-orange travel look). Apply the same LUT or filter to every clip.
- Match AI clips to each other before styling: exposure, white balance, then look.
- Add light film grain and the same aspect ratio across clips to hide model differences.

### 3.9 Delivery

- Master in 16:9 for YouTube; reframe to 9:16 and 1:1 with subject tracking.
- Export 1080p minimum; 4K when the source supports it; upscale weak AI clips first.

### 3.10 Mapping to other tools (for skill authors)

| Tactic | Higgsfield (MCP) | ffmpeg | Remotion |
|---|---|---|---|
| Character sheet | character-sheet workflow, `generate_image`, `manage_reference_elements` | — | — |
| Shot generation, camera moves | `generate_video` with Seedance 2.5 / Kling / Veo, multi-shot "HARD CUT" prompts | — | — |
| Relight | relight_image (per server instructions) | `eq`, `curves`, `colorbalance` filters | CSS filters |
| Reframe | `reframe` | `crop`, `scale`, `pad` | composition sizes |
| Background removal | `remove_background` | `chromakey` (green screen only) | — |
| Upscale | `upscale_video` | `scale` with lanczos | — |
| Voice-over / music | `generate_audio`, `create_voice` | `amix`, `sidechaincompress` for ducking, `loudnorm` | `<Audio>` |
| Captions | — | `subtitles` filter (burn-in SRT/ASS) | caption components (word timing) |
| Cuts, pacing, transitions | — | `concat`, `xfade`, `trim`, `setpts` (speed) | `<Sequence>`, `<TransitionSeries>` |
| Keyframed zoom / pan | — | `zoompan` | `interpolate()`, `spring()` |
| Color grade | — | `lut3d`, `eq`, `noise` (grain) | CSS filters / LUT shader |
| Hook check | `virality_predictor` | — | — |

The Higgsfield tool names come from this session's tool list; check their parameters before using them.

---

## Open gaps

- Channel name of Video 1: not found.
- Actual on-screen steps of both videos: not seen.
- CapCut "AI effects" prompt feature and AI music tier for 2026: no reliable source.
- Buzzy export resolution per tier (720p / 1080p / 4K) and current prices: sources conflict.
- Seedance "Character Lock" and CapCut "Director Mode" (June 2026): competitor claims only.
