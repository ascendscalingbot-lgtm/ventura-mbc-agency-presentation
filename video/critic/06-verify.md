# Critic 06-verify

Evidence is in `critic/work-06-verify/`: the `sheet-*` sheets and the `z6_*` zooms.

## Items from 05-verify
- **Likeness: PARTLY.** The large profile (1.07–1.60) reads as him: the curly fringe, the moustache, the full nape. The small figure now keeps its features. The small bust still hurts the read.
- **Moustache / mouth: FIXED.** The moustache now clearly overhangs a recessed lower lip, and the spike is gone (`z6_pair.png`, left).
- **Bow / tuck: FIXED.** The tuck is about 25°. The nose, moustache and chin point down and stay legible from 1.70 to 3.90 (`z6_pair.png`, right). The throat line is short.
- **Bust shape: STILL PRESENT.** The small torso is still a tombstone in both formats. The left edge is a vertical wall with a rounded top corner, and only the right shoulder slopes. It is worst in 9:16. It still pops from the blurred sloped bust to the boxy one at 1.65→1.667 (`z6_pop_9x16.png`).
- **Seam: PARTLY.** It is down to about 1/255 and invisible at normal viewing. Contrast enhancement still shows the diagonal from the jaw to the nape, plus a short vertical line at x≈700, y 680–700 (`z6_seam2.png`).
- **Collisions / 9:16: PASS.** The pupil dot clears the head at 3.8–3.9, and the name clears the head. There are no regressions.

## New defects
1. **Jaw ledge (1.07–1.60).** The underside of the jaw ends in a flat horizontal step at about (650–695, 680) in 16x9. The front of the neck then drops straight down. In the photo the chin curves smoothly into the throat.

## Verdict: ONE MORE PASS
1. **Rebuild the small bust as a scaled copy of the large one.** It needs a sloped left shoulder and a sloped right shoulder, with no vertical wall. Crossfade or morph through 1.60–1.70 so the shape doesn't pop.
2. **Smooth the jaw-to-throat join.** Replace the ledge at about (650–695, 680) with a curve from the chin into the front of the neck, as in the photo.
3. **Remove the seam.** Merge the head and torso into one filled path, or overlap them, so neither the diagonal nor the vertical line survives enhancement.
