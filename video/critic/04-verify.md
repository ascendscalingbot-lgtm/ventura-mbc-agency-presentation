# Critic round 04-verify: photo-based silhouette

Evidence is in `critic/work-04-verify/`: the sheets `sheet_*`, the 1/60s windows `d_*`, the reference bow `d_ref_1.5.png`, the zooms `z_*`, `n9_keys.png` and `neck_1.617-1.70.png`.

## 1. Likeness: PARTLY
In the large profile (1.07–1.60) he is recognisably Shayan: the curly top and fringe, straight nose, full chin and thick neck all read. The **moustache doesn't register**, because the lip bump is a few px. After the 1.70 pull-back, the silhouette includes the photo's **raised arm and fists at the bow tie**. It reads as a hunched man with a fist at his chin, not as him (`z_bowed_2.50.png`, `n9_keys.png`). That pose holds for about 2.2s, so it is the dominant read.

## 2. Edges: minor issues
- There are no holes, background fragments or jaggies.
- The hair has a 3–4px grey feather that is softer than the crisp jacket (`z_head_1.20.png`).
- At the nape there is a flat, crisp horizontal notch of about 50px through 1.617–1.70. It reads as a small cut-line.
- There are no neck gaps or overlaps during the bow.

## 3. Bow: NOT comparable
In the reference the profile pitches down about 30°, and the nose and chin stay visible over a clean bust. Here the head tips at 1.60–1.68, but the face then sinks into the shoulder and fist mass, so no chin-down profile is readable afterwards. It reads as head-turned-away plus a raised arm.

## 4. Collisions and 9:16: PASS
- The name clears the head in both formats.
- In 9:16 the pupil dot and "You" come within about 30px of the blurred head only at 3.80–3.87. This is transitional and matches r3.
- The 9:16 bust is centred.
- The arm lump adds weight on the left.

## 5. Regressions: NONE
A 10fps diff against r3 shows that only 1.1–3.8 changed. 0–1, 3.9–5.4 and 7.6–10.8 are identical (mean abs diff <1).

## Verdict: ONE MORE PASS
1. **Mask out the forearms and fists.** Give the small or bowed bust a clean, smooth jacket shoulder line, like the reference.
2. **Pitch the head 25–30° chin-down about the neck pivot.** Keep the nose and chin visible, pointing down, through 1.70–3.90.
3. **Clean the details.** Add a few px of moustache relief, smooth the nape notch, and replace the grey hair feather with a 1px antialias.
