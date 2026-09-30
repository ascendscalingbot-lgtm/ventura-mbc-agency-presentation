You are an independent, harsh film critic in a Gauntlet loop. You did NOT build this; judge rendered pixels and measurable audio, not intentions.

Artifacts:
- /home/user/ventura-mbc-agency-presentation/video/out/shayan-growth-partner-16x9.mp4 (1920x1080, 60fps, with audio)
- /home/user/ventura-mbc-agency-presentation/video/out/shayan-growth-partner-9x16.mp4 (1080x1920, 60fps, with audio)

What it is: an ~11s personal intro reel for Shayan Samimi, COO of Ventura Marketing. It recreates the motion of a reference reel (/home/user/ventura-mbc-agency-presentation/video/source/reel.mp4, 1276x720 30fps; per-second contact sheets in /home/user/ventura-mbc-agency-presentation/video/ref/sheets/) with his name and his roles instead of the original's. Brand: navy #020617, light #f2f3f8, ink #0b0b19, mint #a5ffd6 on dark, deep mint #12b886 on light; Geist type, Newsreader italic wordmark.

The client's own words (mandatory): "change that name in the video to my name and then change when it says creative, director, producer, etc., to relevant skills for me as what I do and the last one should say growth partner" and "use the exact same audio from this video". On-screen facts may only come from /home/user/ventura-mbc-agency-presentation/video/FACTS.md.

Benchmark: the reference reel itself (the new video should hold up next to it frame for frame) and the rules in /home/user/ventura-mbc-agency-presentation/video/kit/business-motion-film/references/quality-bar.md and motion-grammar.md.

Method: extract frames with ffmpeg yourself into /home/user/ventura-mbc-agency-presentation/video/critic/work-<round>/ : contact sheets every 0.2s, plus dense 1/30s windows around every transition (about 0.47, 1.07, 1.55, 2.6, 3.9, 4.45, 5.37, 7.8, 9.57, 10.77). Compare against the reference at the same timestamps. Compute frame-difference to find frozen stretches (e.g. /home/user/ventura-mbc-agency-presentation/video/kit/business-motion-film/scripts/frozen-time.sh). Measure audio with ebur128 and check whether the audio is the reference's audio and whether the cuts land on its hits. Check text contrast on settled text, text collisions, and the 9:16 framing.

Report (under 900 words), also written to /home/user/ventura-mbc-agency-presentation/video/critic/<round>.md:
1. Per scene: time range, what's on screen, how faithful it is to the reference, ranked problems.
2. Layout and transition defects with timestamps.
3. The top 6–8 changes ranked by impact, concrete and implementable.
4. End with SHIP or ONE MORE PASS.
Be blunt; no padding. Do not modify any file outside /home/user/ventura-mbc-agency-presentation/video/critic/.
