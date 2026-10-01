# Instagram post

## Caption

Comment "PROMPT" and I'll send you the exact setup Claude Opus 5.5 used to make this video.

I gave it a reel I liked and a side profile photo of me, and it rebuilt the whole thing in code. It kept the original song and the timing and swapped in my name.

I'm Shayan, COO at Ventura Marketing. Most of my week goes into YouTube and Meta ads for the brands we work with. Lately I've been building a lot of AI workflows like this one. If you want help growing your brand, my DMs are open.

#claudeai #aivideo

## DM reply

Here you go! You'll need Claude Code and two GitHub repos.

This one lets Claude watch a video frame by frame: https://github.com/bradautomates/claude-video

This one has the motion design rules it followed: https://github.com/echris6/motion-video-kit

Upload the reel you want to recreate and a photo of yourself (side profile works best), fill in the brackets below, and paste it in. Expect to go back and forth a couple of times. Mine took a few rounds before the silhouette looked like me.

```
<role>
You design and build motion videos entirely in code, with GSAP for the animation.
Every decision is judged against the reference reel frame by frame, and the video
isn't finished until it holds up next to it.
</role>

<brief>
- What it's for: a personal intro reel for [YOUR NAME], [YOUR ROLE] at [COMPANY].
- Who's watching: [WHO YOUR AUDIENCE IS AND WHAT THEY CARE ABOUT].
- What they should do at the end: remember "[YOUR NAME], [FINAL TITLE]".
- Length and sizes: locked to the reference reel's audio. 9:16 1080x1920 and 16:9 1920x1080, 60fps.
- Brand: [COLOURS AS HEX], [FONTS], [LOGO OR WORDMARK].
- Assets: [PATH TO YOUR PHOTO] (cut it into a silhouette in code).
- Reference reel: [PATH TO THE REEL].
- Text swaps: the name in the reel → [YOUR NAME]. The rotating titles →
  [TITLE 1], [TITLE 2], [TITLE 3], [TITLE 4], and the last one is always [FINAL TITLE].
- Audio: use the reference reel's audio, untouched.
I'm away and won't answer questions. Make the calls yourself and keep going
until the video passes every check below.
</brief>

<kit>
Clone and read github.com/echris6/motion-video-kit. Read business-motion-film/SKILL.md
first, then each reference file at the step it points to. Its rules, critic prompts
and quality bar override your defaults.
</kit>

<study_the_reference>
- Use github.com/bradautomates/claude-video to extract every frame of the reference.
- Find every cut and beat with a frame-difference pass and an audio onset pass.
- Make contact sheets (one per second at 15fps) and write down how each moment works.
- Borrow the mechanisms and timing only. The name, titles, silhouette, colours and logo are mine.
</study_the_reference>

<build>
- One HTML page, one GSAP timeline. Every animated value is a function of timeline time only.
- Render frame by frame with headless Chromium into ffmpeg.
- Render a 5-second test first.
- Carried objects land on the same pixels on both sides of a cut.
</build>

<critic_loop>
Never judge your own work. Send each full render to a fresh critic agent with only
the brief and the reference. It pulls its own frames, measures frozen time, and
returns a ranked list ending in SHIP or ONE MORE PASS. Fix the biggest problem first,
re-render, and send it to a new critic that checks every earlier item.
</critic_loop>

<quality_bar>
- No more frozen screen than the reference, and frame one is a finished picture.
- All text readable (4.5:1 contrast) and inside the frame in both sizes.
- Cuts land on the reference's beats to within one frame.
- A first-time viewer understands who I am with the sound off.
</quality_bar>

<deliverables>
The MP4 in both sizes, a contact sheet, and a short note on what a human should still check.
</deliverables>
```

Tag me if you post yours.
