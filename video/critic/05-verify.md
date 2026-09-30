# Critic 05-verify

Evidence is in `critic/work-05-verify/`: the `sheet_*` sheets, the 1/60s windows `d_a_*` (1.5–1.9) and `d_b_*` (3.7–3.95), and the `z_*` zooms.

## Items from 04-verify
- **Likeness: PARTLY.** The large profile (1.07–1.60) reads as him. From 1.70 to 3.90 the face is tucked so deep that only the fringe and the nose tip read (`z_head_2.5_16x9`).
- **Moustache: PARTLY.** The upper-lip bump is small. A sharp lower-lip spike juts past it, so at 1.07–1.60 the mouth reads as open or pouting (`z_mouth`).
- **Hair feather: FIXED.** The hair edge ramp now matches the jacket (about 7px on both).
- **Nape notch: FIXED.** The nape is now a smooth curve.
- **Arms and fists: FIXED.** None are visible from 1.60 to 3.90 in either format.
- **Bow: PARTLY.** The chin-down pitch with motion blur at 1.617–1.70 is right. After that it over-tucks: the nose points into the chest, the chin vanishes and there is no throat line. The reference keeps its features legible.
- **Collisions / 9:16: PASS.** In 9:16 the pupil dot gets closest to the blurred head at 3.83–3.88 without touching it. The name clears the head.

## New defects
1. **Tombstone bust (1.68–3.90).** The small torso is a tall block with vertical sides and rounded top corners, and it has lost the sloped shoulder. It reads square-on or from behind, worst in 9:16. The shape pops from sloped to boxy at 1.667–1.70.
2. **Faint seam (1.07–1.60).** A line about 2/255 darker runs diagonally from the jaw at about (700,690) to the nape at about (1000,640) in 16x9 (`seam_1.2_16x9`).

## Regressions
None. The diff against r4 at 0–1, 3.9–5.4 and 7.6–10.8 has a mean absolute difference of 0.16 or less.

## Verdict: ONE MORE PASS
1. **Reduce the tuck to about 25°.** Pivot at the neck so the nose, moustache and chin stay visible, pointing down with a throat line, from 1.70 to 3.90.
2. **Make the small bust a scaled copy of the large one.** It should keep the sloped shoulder, with no shape pop.
3. **Fix the mouth and the seam.** Give the moustache a clear overhang past the lower lip, round the lower-lip spike and remove the seam.
