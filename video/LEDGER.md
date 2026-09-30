# Critic ledger and quality-bar results

Every round was reviewed by a fresh critic agent that had not seen the build. Full reports are in `critic/`.

| Round | Artifact | Critic's top findings | What changed | Measured result |
|---|---|---|---|---|
| 00 storyboard | `STORYBOARD.md` | The "i"→"o" morph was weak; roles had no visual meaning; "Engineer" read as a coding job; the ending dropped the title; missed beats (head lift at 3.73, the iris afterimage); the underline was on the wrong word; the ending didn't match the reference | The dot of the "i" grows into the "o"; one icon per role; Engineer → **Architect**; "Growth Partner · Ventura Marketing" subline; squiggle under "Growth"; hard cut off the logo | Beat map matched the reference cuts |
| 01 full film | r1 renders | 9:16 was a ×0.72 shrink; the silhouette had straight crop lines and no bow; the eye exit popped; frozen holds; tiny subline and icons | Separate 9:16 framing; shoulders extended from the headshot; eye exit rebuilt; slow camera push through the holds; icons ×1.45; name 84px, subline 32px | Frozen time 3.6 → 2.4 s (16:9), 5.3 → 2.0 s (9:16) |
| 02 verify | r2 renders | A size jump on "Growth" in 9:16; the iris clipped in 9:16; the 9:16 silhouette looked like a cone; still no bow; a 5-frame dissolve | Camera eases back to 1 before the handoff; iris target moved in 9:16; bust scaled uniformly and centred; head split at the neck and tipped forward; 9:16 subline on two lines; 1-frame dissolve | All three fixes confirmed in round 03 |
| 03 verify | r3 renders (final) | Only optional items: a 2-frame edge overrun on the 9:16 slide-in, the ghost word near the edge inside the eye, the bow reads soft | Left as is. Transitional, and below perception at speed | **SHIP** |

## Quality bar (final render)

| Check | Target | Result |
|---|---|---|
| Audio is the reference's | identical | Decoded PCM md5 `c95e6b88…` identical to `source/reel.mp4` in both renders ✅ |
| Loudness | as the source | −14.1 LUFS, LRA 1.4 LU, TP −0.8 dBFS: the source's own values, untouched ✅ |
| Cuts on the reference's hits | ±1 frame | 0.48 / 1.08 / 3.90 / 5.33–5.35 / 9.58 ✅ |
| Frozen time | ≤ reference (3.4 s) | 16:9 **2.4 s**, 9:16 **2.0 s**, all in the sign-off and wordmark holds ✅ |
| Frame one | finished composition | Navy canvas, guides and the mint caret with the "H" ✅ |
| Text contrast | ≥ 4.5:1 | Name 18.8:1, subline ≈7:1 ✅ |
| 9:16 text inside the frame | settled text ≥ 58 px margin | ✅ (the only edge touch is 2 transitional frames at 5.47) |
| On-screen facts | FACTS.md only | ✅ |
| Brand colours | tokens | Backgrounds measure #010416 and #f1f2f7 against #020617 and #f2f3f8 ✅ |

## Still needs a human
- **Listen to it.** The audio is proven bit-identical to the reference, but nobody has judged how the new picture feels against it.
- **The head bow at ~1.6 s** is an approximation: the headshot is front-on, so the head is tipped forward at the neck. The critic called it soft but acceptable.
- **Rights:** the music and the motion design are the original creator's. Check you're comfortable posting a recreation with their audio. If you post the reel, you could use Instagram's "use audio" from the original.
