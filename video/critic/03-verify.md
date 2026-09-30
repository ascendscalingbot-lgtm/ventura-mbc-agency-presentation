# Critic round 03-verify: Shayan "Growth Partner" reel

Evidence: `critic/work-03-verify/`. It holds 0.2s sheets (`sheet_*`), 1/60s windows (`d_<fmt>_<start>.png`, labels relative to the window start), `bow_*`, `n_9x16_whip.png`, `n_signoff_*` and `raw/`.

## Measured
- **Audio:** the decoded PCM md5 is `c95e6b88…` and the ADTS stream-copy md5 is `5ead25f3…`. Both are identical in both renders and the reference, so it is the exact reference audio.
- **Frozen time:** 16:9 is 2.4s, 9:16 is 2.0s and the reference is 3.4s. All of it is in the sign-off and wordmark holds.
- **Facts:** the five titles, "Shayan Samimi", "GROWTH PARTNER / VENTURA MARKETING" and "Ventura Marketing" all match FACTS.md.
- **9:16 text bounds:** I scanned every light-background frame. Titles span x 106–1022 (the Operator icon is the widest point, a 58px margin). The name is at x 261–817. Both subline lines are 28px tall, at x 319–783. The only text that touches an edge is the 5.47–5.48 slide-in (N5).

## 02-verify items
1. **9:16 rebuild: FIXED.** The subline is now two lines with a 28px cap.
2. **Silhouette bow: PARTLY.** At 1.62–1.68 the head tips and sinks into the shoulders, so the neck compresses (`bow_16x9.png`, `bow_9x16.png`). It is still carried mostly by blur plus a shrink over about 4 frames, not a clear chin-down pitch. It is acceptable.
3. **Eye exit (16:9): FIXED.** It still holds.
4. **Retime: FIXED** to within one frame. The frame is light at 5.333 in 16:9, and 0.94 light at 5.333 and full at 5.35 in 9:16. The reference fills at 5.34–5.37.
5. **Frozen holds: FIXED.**
6. **Sign-off legibility: FIXED.** The 9:16 subline is 28px; 16:9 is 24px, which is fine at that width.
7. **Carousel icon: FIXED.**
8. **Hello ghost and head centring: FIXED.** At 1.07–1.4 the 9:16 head centre is x≈538.

- **N1 (9:16 "Growth" handoff pop): FIXED.** Ink "Growth" keeps its size (481px wide and 110px tall before and after), with no blur. It whips right x 65→209→296 over 5.317–5.367, then holds. 16:9 behaves the same (556→717). **Residual:** at 5.15–5.28 the white ghost "Growth" inside the eye starts at x≈20px in 9:16, which is inside the 60px margin.
- **N2 (9:16 iris clip): FIXED.** The iris stays inside x 296–1010 through 5.25. It only reaches the edge (x 1074) at 5.30–5.317, while it is fading and scaling out.
- **N3 (9:16 proportions): FIXED.** At 2.5–3.9 the bust is uniformly scaled with natural shoulders and centred at x≈524. At 1.07–1.4 the bust fills and bleeds off the bottom. The left shoulder touches x=0 while the right leaves a 10–14px gap, which is a slight asymmetry and not a defect.
- **N4 (title→name dissolve): FIXED.** It is now a single double-exposed frame at 7.783, in both formats.

The three 02 fixes: fix 1 FIXED apart from the ghost-margin residual, fix 2 FIXED, fix 3 PARTLY (the bow is soft; the subline is FIXED).

## New defects
- **N5. Minor, 9:16 only, 5.467–5.483.** "Strategist" slides in from the right and runs past the frame edge for 2 frames (the ink bbox reaches x=1079), while "Growth" shrinks from 110px to 88px tall. It reads as an entrance and settles by 5.50 at x 130–970. 16:9 stays inside (max x 1597).
- **N6. Cosmetic.** At the 3.90 cut, the first eye frame is an oversized dome that snaps smaller on the next frame. The reference has the same transitional frame, so this is not a defect.

I found no glitch frames, broken overlaps or clipped settled text in either render. The 9.583 cut to the wordmark is clean.

## Verdict: SHIP
The remaining items (a soft bow, a 2-frame edge overrun on the 9:16 slide-in, the ghost word near the edge inside the eye) are transitional and sub-perceptual at speed. If one more pass is wanted anyway, these are optional:
1. Start the 9:16 "Strategist" slide-in with its right edge at x≤1020.
2. Inset the 9:16 in-eye ghost "Growth" to x≥60 at 5.15–5.30.
3. Add a real chin-down pitch of 15–20° to the head at 1.60–1.70.
