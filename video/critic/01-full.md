# Critic round 01-full — Shayan "Growth Partner" reel

Evidence: `critic/work-01-full/` (sheets, dense pairs ref-over-ours, 9:16 strips, `diff.py`).

## Measured
- **Audio:** same decoded PCM md5 as the reference (`c95e6b88…`) and the same AAC packet md5 in both outputs. Exact reference audio. −14.1 LUFS, LRA 1.4, TP −0.8, identical to source.
- **Cuts vs hits** (frame-diff ours / ref / audio onset): dark→light 0.483 / 0.467 / –; Hello→head 1.083 / 1.067 / 1.06; Your→eye 3.90 / 3.90 / 3.88; eye→titles **5.23–5.30 / 5.34–5.37** / 5.48 hit; name→logo 9.567 / 9.567 / 9.56. Every cut lands except eye→titles (≈4–5 frames early). The iris dart is also ~0.07s early (4.48 vs 4.55).
- **Frozen time** (frozen-time.sh): 16:9 3.6s, 9:16 5.3s, reference 3.4s. The frozen stretches the reference *doesn't* have are 2.0–2.3, **3.2–3.6** (the reference keeps "r" dropping and hair moving; we're at 0.05 diff) and **5.6–5.9** (the reference's squiggle/push runs at about 1.0 diff; ours reads 0.08). In 9:16 the 7.9–9.5 name shrink falls below the threshold too.
- **Contrast:** settled text passes. The name is 18.8:1 and the subline #50505a is about 7:1. Brand backgrounds measure #010416 and #f1f2f7, which is on token.

## 1. Per scene
**0.00–0.47 H on canvas.** Faithful.

**0.47–1.07 "Hello" + hand.** Faithful; the letter ghost is 1 frame (reference: 3–4). Minor.

**1.07–1.55 silhouette + "I'm".** Weakest scene. (1) The headshot cutout is a frontal bust whose **shoulders end in straight vertical crop lines**, so the silhouette's right side is a ruler-straight edge at x≈1234 in 16:9 (`combo2.png`). It reads as a default-avatar icon. (2) Being frontal, it can't *bow*. At 1.55–1.70 it just sinks and shrinks under blur, so the reference's key gesture (head drops, name types above it) is lost.

**1.55–2.60 name types above head.** The type is faithful. The head is ~40px right of the name's centre (`h_2.2`, `v_2.2`). The 2.0–2.3 hold is dead.

**2.60–3.90 i→o→"Your"→pupil.** Faithful; 3.2–3.6 frozen.

**3.90–5.37 eye.** Very close to the reference: half-dome, almond, slit, dart, afterimage, "Growth" from behind the iris. The white "Growth" over the white sclera is invisible for 4.9–5.2 (the reference does the same). **Exit is broken:** at 5.23–5.30 the *iris* scales about 3.5× over a light field with navy wedge corners showing (`combo1.png`, `h_5.27`). It then vanishes in one frame, and "Growth" flickers white→grey→ink. The reference pushes the *sclera* to fill the frame instead. Ours pops (one-frame diff 82).

**5.37–7.80 title carousel.** Faithful mechanics, and the swaps land on beats. The icon riding the last letter is 10–15px, which is unreadable at phone size and changes meaning invisibly. 5.6–5.9 is frozen.

**7.80–9.57 name sign-off.** The collapse is fine. The subline "GROWTH PARTNER · VENTURA MARKETING" is 17px cap-height in 16:9 and **12px in 9:16**, so it's illegible on a phone.

**9.57–10.77 wordmark.** Clean, and the cut is on the hit.

## 2. Layout / transition defects
- **9:16 silhouette 1.07–3.9: floating block.** The torso ends in a hard flat bottom at y≈1627, 290px above the frame edge, with near-vertical extruded sides, and 45% of the frame above it is empty (`v_2.2.png`). At 1.6–1.7 it becomes a blurred trapezoid.
- **9:16 eye 3.9–5.3:** the eye is about 20% of frame height with ~60% navy below and above. The almond corners clip the left and right edges. At **5.27 the iris is cropped by the right edge** (`combo1.png`, `dense_v_5.37`).
- **9:16 overall:** the ×0.72 downscale of the 16:9 stage leaves title and name text tiny (title about 30px, name 38px, subline 12px on 1920 height). None of it is "readable at phone size".
- 5.23–5.34 iris pop, navy wedges, "Growth" colour flicker (both formats).

## 3. Top changes, ranked
1. **Rebuild the 9:16 layout, not a ×0.72 shrink.** Anchor the silhouette so it bleeds off the bottom edge: extend the torso, or scale it up so its crop sits below the frame. Scale the eye ~1.4× with deliberate corner bleed. Set type at ≥1.6× its current 9:16 size: name ≥64px, titles ≥56px, subline ≥28px.
2. **Fix the silhouette asset.** Re-cut the headshot with full shoulders, feathered to a natural edge or extended to frame bottom, so there are no straight vertical crop lines. Make the bow at 1.55 a real forward rotation (~25° about the neck), not a sink-and-shrink.
3. **Redo the eye exit at 5.23–5.37.** Scale the sclera/almond, not the iris, until the white fills the frame. Fade or slide the iris out, keep "Growth" in ink from the moment it sits on white, and retime so the frame fills at 5.367, as in the reference.
4. **Retime the early moves:** iris dart +0.07s (to start at 4.55), eye exit +0.07s.
5. **Kill the frozen holds.** At 2.0–2.3 and 3.2–3.6, add a slow 2–3% push on head and text, a caret blink, and the "r" drop. At 5.6–5.9, draw the squiggle over that window as the storyboard says, plus a 2% push.
6. **Sign-off legibility:** subline to ≥24px in 16:9 and ≥28px in 9:16, with the name about 1.5× larger. Hold it readable for ≥1.5s.
7. **Carousel icon:** ≥28px in 16:9 so the play/gear/target/spark/rings meanings actually read.
8. Make the Hello ghost trail 3–4 frames long so it registers. Centre the silhouette head under the typed name.

## Verdict
**ONE MORE PASS.** Audio, cut timing and most 16:9 motion are faithful. The 9:16 framing, the cropped avatar silhouette with no bow, and the eye-exit pop each fail next to the reference.
