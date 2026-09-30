# Critic round 02-verify: Shayan "Growth Partner" reel

Evidence: `critic/work-02-verify/` (sheets, 1/60s windows `d_*`, stills `n_*`).

## Measured
- **Audio:** decoded PCM md5 `c95e6b88…` and AAC packet md5 `0ee5de84…` are identical in both renders and the reference. It is the exact reference audio.
- **Frozen time:** 16:9 is 2.4s, 9:16 is 2.0s and the reference is 3.4s., down from 3.6s and 5.3s.
- **Cuts** (luma diff): 0.483, 1.083, 3.900, 5.267–5.300 (a 3-frame fill, no longer a one-frame pop), 9.583.
- **Facts:** the titles (Strategist, Operator, Marketer, Architect, Partner), the subline and the wordmark all match FACTS.md.

## Previous items
1. **9:16 rebuild: PARTLY.** The silhouette now bleeds off the bottom and the eye fills the width. Titles are an 81px line box, 910px wide, and the name a 72px line box. The subline cap height is 24px, short of the 28px target. New 9:16 issues are listed below.
2. **Silhouette asset: PARTLY.** The shoulders now slope, so the straight crop lines are gone. The bow is **still missing**: 1.55–1.75 is still a sink-and-shrink under blur.
3. **Eye exit: FIXED in 16:9.** The sclera scales and the iris fades. "Growth" crossfades to ink over 5.25–5.30 with no wedges or pop.
4. **Retime: PARTLY.** The dart now starts at 4.53, which is FIXED. The frame fills at 5.30–5.317 against the reference's 5.34–5.37, so the exit is still about 3–4 frames early.
5. **Frozen holds: FIXED.** 2.0–2.3, 3.2–3.6 and 5.6–5.9 all move now.
6. **Sign-off legibility: PARTLY.** The subline cap is 24px in both formats and holds 8.0–9.57. That is fine in 16:9 but under 28px in 9:16.
7. **Carousel icon: FIXED.** About 56px.
8. **Hello ghost: FIXED** (about 5 frames, 0.75–0.83). **Head centred under the name: FIXED.**

Layout: the 9:16 floating block and eye size are FIXED. The 9:16 iris crop is **STILL PRESENT** (N2).

## New defects
- **N1. 9:16 "Growth" handoff pop, 5.367→5.383.** In one frame the ink word shrinks about 1.29× (630px→488px wide), jumps about 180px right and picks up blur. Before that (5.25–5.30) the "G" touches x=0. 16:9 is continuous.
- **N2. 9:16 iris clipped by the right edge, 4.6–5.28**, by about 12% of its width (`v_eye.png`).
- **N3. 9:16 silhouette proportions, 1.7–3.9.** The torso is stretched into a tall tapered cone about 700px high, so it reads as a cloak or bell rather than a person (`sil_combo.png`). At 1.07–1.6 the bust is also off-centre, with the left shoulder cut by the frame edge.
- **N4. Minor:** the title→name dissolve at 7.75–7.82 is a 5-frame double exposure, where the reference has 2 frames.

16:9 has no clipped text and no glitch frames.

## Verdict: ONE MORE PASS
1. **Fix the 9:16 eye-to-carousel handoff.** Keep "Growth" at the carousel's final size and position from 5.30 on, keep it inside a ≥60px safe margin, and shift the iris dart so it stays in frame. Retime the fill to land at 5.35–5.367 (both formats).
2. **Re-proportion the 9:16 silhouette.** Scale the bust uniformly so its natural shoulders reach the bottom edge, not a vertically stretched torso, and centre it at 1.07–1.6.
3. **Add the bow at 1.55–1.75.** Tilt the head forward about 20–25° (a chin-down rotation plus a slight forward lean) instead of the blur-shrink. Raise the 9:16 subline to ≥28px.
