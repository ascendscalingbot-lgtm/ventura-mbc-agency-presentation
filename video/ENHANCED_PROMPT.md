# Enhanced prompt — Shayan Samimi reel recreation

> Reference reel: https://www.instagram.com/reel/Dd2E7NWp198/
> Frame-capture tool: https://github.com/bradautomates/claude-video (`/watch` skill, cloned in `video/claude-video`)
>
> Status: the frame capture has **not run yet**. This environment's network policy blocks
> `www.instagram.com`. Sections marked **[FILL FROM FRAMES]** need to be completed once the frames are
> captured (see `video/watch-reel.sh`).

---

## The prompt

**Role:** You are a senior motion designer and front-end engineer. Recreate a short-form Instagram
reel as closely as possible, frame for frame, then swap in a new person's name and titles. Match the
original's timing, layout and motion exactly. The only things that change are the text and the
colour styling described below.

### Step 1 — Study the reference before building anything

1. Run the watch skill on the reference with the maximum frame budget:
   ```bash
   python3 video/claude-video/skills/watch/scripts/watch.py "https://www.instagram.com/reel/Dd2E7NWp198/" \
     --detail token-burner --resolution 1024 --no-dedup --out-dir video/watch-run
   ```
   If Instagram is unreachable, use a local copy of the reel: `video/source/reel.mp4`.
2. Look at **every** frame in the report. Then save a numbered storyboard to `video/frames/`
   (`frame_001_0.00s.jpg` …) with a one-line note per frame covering what is on screen, where it sits,
   and what moves.
3. Write down these values from the frames. Don't guess them.
   - Canvas: aspect ratio (expected 9:16, 1080×1920), background colour or texture, and any grain,
     vignette or blur.
   - Typography: font family (or the closest Google Font), weight, case, tracking and size relative
     to the canvas width. Note any serif/sans pairing.
   - Name treatment: how the name appears (typewriter, mask reveal, per-letter stagger, scale-in),
     where it sits, and how long it holds.
   - Title sequence: how each title ("Creative", "Director", "Producer", …) enters and exits
     (slide, flip, blur-swap, cut on the beat). Record each title's in and out timestamps.
   - Final beat: how the last title lands and holds, and whether there's an end card, logo or CTA.
   - Audio: whether cuts land on beats. Record the beat timestamps so the new version keeps the same
     rhythm.
   - **[FILL FROM FRAMES]** Paste the measured timeline table here.

### Step 2 — Text swaps (the only content changes)

| Original | Replace with |
|---|---|
| The creator's name | **Shayan Samimi** |
| Title 1 ("Creative") | **Operator** |
| Title 2 ("Director") | **YouTube Strategist** |
| Title 3 ("Producer") | **Meta Ads Strategist** |
| Title 4 (if present) | **AI Systems Builder** |
| Title 5 (if present) | **Content Engine Architect** |
| **Last title (always)** | **Growth Partner** |

Rules for the titles:
- Keep the **same number of titles** as the original. If it has fewer slots than the list above, drop
  titles from the middle of the list first. **Growth Partner is always last.** If it has more slots,
  add from this backup list, in this order: *COO*, *Creative Strategist*, *Performance Marketer*.
- Every title swap happens at the original's timestamp. The longer titles must not change the rhythm.
  Scale the type down or allow two lines instead of speeding anything up.
- **Growth Partner** should land slightly heavier than the other titles: hold it about 20% longer, or
  give it the original's emphasis treatment. It's the payoff line.
- Use "Shayan Samimi" exactly as written, including capitalisation. Don't add a middle initial,
  handle or emoji.

### Step 3 — Brand styling (Ventura Marketing)

Only apply these where the original uses a neutral or white accent. Keep the original's structure.
- Background `#000000`, with a subtle radial glow `rgba(52,211,153,0.18)` at the top-left.
- Primary text `#f8fafc`, muted text `#a1a1aa`, accent `#a5ffd6` (with `#7cf0c0` for a gradient).
- Fonts: **Newsreader italic** for the name (same as the deck's speaker cards) and **Geist** for the
  titles.
- Optional end card: headshot `shayan-samimi-headshot.jpg` in a round frame with a mint glow, next to
  "Shayan Samimi / Growth Partner · Ventura Marketing".

### Step 4 — Build and export

- Build it as one self-contained `video/index.html` (HTML/CSS/GSAP from cdnjs) at 1080×1920, driven
  by a single master timeline so every timestamp is set in one place.
- Render it to `video/shayan-reel.mp4` by capturing frames with Playwright (Chromium at
  `/opt/pw-browsers`) and encoding with `ffmpeg -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18`. If the
  original's audio is available and licensed for reuse, mux it back in. Otherwise leave the render
  silent so music can be added in CapCut/Instagram.
- **Check the result against the reference:** extract frames from the render at the same timestamps
  as the storyboard and put each pair side by side in `video/compare/`. Fix any beat that is off by
  more than 2 frames, or any layout that's off by more than about 2% of the canvas.

### Definition of done
- [ ] Timing matches the original to within ±2 frames at every title swap.
- [ ] The name reads **Shayan Samimi** and the titles follow the table, ending on **Growth Partner**.
- [ ] Nothing overflows the 9:16 safe area (keep text clear of the top 250px and bottom 350px, where
      the Instagram UI sits).
- [ ] `video/shayan-reel.mp4` plays at 1080×1920, 30fps, and a side-by-side comparison sheet exists.
