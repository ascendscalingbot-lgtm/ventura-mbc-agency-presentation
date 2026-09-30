# Enhanced prompt: Shayan Samimi "Your Growth Partner" reel

This is Shayan's base prompt, tailored to this project. It's what the build in this folder follows.
Reference reel: `video/source/reel.mp4` (Instagram reel Dd2E7NWp198)
Kit: https://github.com/echris6/motion-video-kit (copied into `video/kit/`)
Frame capture: https://github.com/bradautomates/claude-video (`/watch`, run by `video/watch-reel.sh`)

---

<role>
you design and build motion videos entirely in code, with gsap for the animation and three.js for any 3d. every decision is judged against the reference reel frame for frame, and the video isn't finished until it holds up next to it.
</role>

<brief>
- what the video is for: a personal intro reel for **Shayan Samimi**, COO of **Ventura Marketing**, that tells people who he is and what he does for clients.
- who's watching: founders and brand owners scrolling Instagram who might hire Ventura. They care about growth: attention, content and ads that convert. They don't care about job titles.
- what they should do at the end: remember "Shayan Samimi, Growth Partner, Ventura Marketing", then look him up or DM him.
- length and sizes: **11.2 s, locked to the reference reel's audio.** 16:9 1920×1080 master (the reference's aspect ratio) and 9:16 1080×1920 for Reels, both at 60 fps.
- brand: Ventura Marketing. Navy `#020617`, light `#f2f3f8`, ink `#0b0b19`, mint `#a5ffd6` on dark, deep mint `#12b886` for accents on light. Geist for all type; Newsreader italic for the "Ventura Marketing" wordmark (as on the deck cover). Photo: `shayan-samimi-headshot.jpg`.
- facts file: `video/FACTS.md`. It's the only source for any name, title or claim on screen. No numbers, clients, results or testimonials appear.
- assets: Shayan's headshot, cut into a silhouette in code. Nothing is generated.
- style reference: `video/source/reel.mp4` ("Hello / I'm Tiago Feitosa / Your Creative Producer…Partner / KORAI").
- text swaps:
  - "Tiago Feitosa" → **Shayan Samimi**
  - "Creative" → **Growth**
  - Producer / Director / Designer / Editor / Partner → **Strategist** (YouTube & content), **Operator** (COO), **Marketer** (Meta ads), **Architect** (AI systems), **Partner** (always last)
  - "KORAI" → **Ventura Marketing**
- audio: **use the exact audio from the reference, untouched** (stream-copied, verified by md5). This overrides the "never copy music" rule below. It's the client's explicit request.

i'm away and won't answer questions. make the calls yourself and keep going until the video passes every check below.
</brief>

<kit>
before anything else, clone and read github.com/echris6/motion-video-kit. read business-motion-film/SKILL.md first, then every reference file it points to at the step where it says to read it. its rules, critic prompts, quality bar, 3d patterns, audio tools and scripts override your defaults.
</kit>

<setup>
- build every scene as an html page animated on a single gsap timeline, with three.js for any 3d, all as pinned local files (gsap and fonts are vendored in `video/build/`)
- render the timeline to video frame by frame: seek, screenshot in headless chromium, pipe to ffmpeg (`video/build/render.mjs`)
- use ffmpeg for frames, contact sheets and audio measurement
- keep every api key in environment variables. never write a key into any file
- render a 5 second test first and confirm it works before building the real video
</setup>

<study_the_references>
- capture every frame of the reference with the watch skill and ffmpeg (`video/ref/`)
- run a fast numeric pass over every frame: how much changed from the last frame, brightness and edge detail, to find every cut and every fast moment
- measured cuts: 0.467, 1.067, 3.900, 5.367, 9.567 s. music ≈112 bpm. a silent pause at 3.25–3.75 before the hit at 3.89. title swaps at 5.47, 6.07, 6.60, 6.93, 7.27, 7.80.
- make one overview contact sheet and a dense sheet of every second at 15 frames a second (`video/ref/sheets/`)
- write down the mechanisms: the design-canvas "H", type inside the head, the "o" becoming a pupil, the eye as a portal, the title carousel, the collapse into the name
- borrow mechanisms and timing only. the name, titles, silhouette, colours and wordmark are all Shayan's
</study_the_references>

<motion_principles>
1. the thing in the front of the shot becomes the transition: the "o" of "Your" becomes the pupil; the white of the eye becomes the next background
2. one object carries the story across shots: caret → name → the dot of the last "i" → "o" → pupil → iris → "Growth"
3. one main movement leads, with smaller ones layered under it, all overlapping. the frame never stops and starts all at once
4. the speed always changes. things land slowly enough to read, leave fast, and the next thing slows as it arrives. no linear motion
5. cuts only where the reference cuts, on its hits
6. every action produces a visible result: typing makes the name, deleting makes the head bow, the swap makes a new role and a new icon
7. type is motion too
8. vary the scale from full-frame silhouette, to small figure under type, to macro eye, to the type carousel
</motion_principles>

<storyboard>
see `video/STORYBOARD.md`. it was reviewed by a fresh critic before building (`video/critic/00-storyboard.md`).
</storyboard>

<build>
- every animated value is a function of timeline time only. no timers, no real-time animation, no unseeded randomness
- shared pieces first: colours, fonts, the silhouette, and the exact pixel positions of every handoff
- carried objects land on exactly the same pixels on both sides of a cut
- don't stop to ask for approval between steps
</build>

<3d>
not used. nothing in this story is physical or spatial, so 3d would only be decoration.
</3d>

<audio>
the reference track, bit-identical. no added effects, because the track already carries every hit. the music-only version is the track itself.
</audio>

<critic_loop>
the builder never judges its own work. each full render goes to a fresh critic with the brief and the reference, and never with the builder's reasoning. the critic pulls its own frames and measures for itself, and the next critic checks every earlier item as fixed, partly fixed or still there. keep a ledger (`video/LEDGER.md`).
</critic_loop>

<quality_bar>
- frozen time no worse than the reference (3.4 s), and no still stretch longer than about half a second outside the end card
- frame one is a finished composition
- all settled text meets 4.5:1 contrast, and nothing collides with or leaves the frame
- the audio's md5 matches the reference
- a first-time viewer, with the sound off, understands "Shayan Samimi, Growth Partner, Ventura Marketing"
- a critic would put it next to the reference without it looking weaker
</quality_bar>

<honesty>
- only names and titles from FACTS.md go on screen
- in reports, separate what was measured from what still needs a human to watch or listen
</honesty>

<deliverables>
- `video/out/shayan-growth-partner-16x9.mp4` and `video/out/shayan-growth-partner-9x16.mp4`, 60 fps
- `video/out/music-only.m4a`
- `video/out/contact-sheet-16x9.jpg`, `video/out/contact-sheet-9x16.jpg`, `video/out/poster-16x9.jpg`
- `video/LEDGER.md` (critic ledger and quality-bar results)
</deliverables>
