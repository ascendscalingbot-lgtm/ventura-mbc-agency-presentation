# Shayan Samimi — "Your Growth Partner" intro reel

## Brief
- **What it's for:** a personal intro reel for Shayan Samimi (COO, Ventura Marketing): who he is and the role he plays for clients.
- **Who's watching:** founders and brand owners on Instagram who might hire Ventura Marketing. They care about growth, not job titles.
- **What they should do at the end:** remember "Shayan Samimi — Growth Partner, Ventura Marketing" and look him up / DM.
- **Length and sizes:** 11.1 s, locked to the original reel's audio. 16:9 1920×1080 master (the reference's aspect) + 9:16 1080×1920 for Reels. 60 fps.
- **Brand:** Ventura Marketing. Background navy-black `#020617` / light `#f2f3f8`, ink `#0b0b19`, mint `#a5ffd6` (on dark), deep mint `#12b886` (on light, decorative only). Type: Geist (all UI type), Newsreader italic (the Ventura wordmark, as on the deck cover).
- **Facts file:** `video/FACTS.md`. Only the name, company and roles in it appear on screen.
- **Assets:** `shayan-samimi-headshot.jpg`, cut to a silhouette (`build/assets/shayan-silhouette.png`).
- **Style reference:** `video/source/reel.mp4` (Tiago Feitosa / KORAI "Your Creative Partner" reel).
- **Audio:** the user explicitly asked for **the exact audio from the reference**. It is used untouched (stream-copied AAC). This overrides the base prompt's "never copy music" rule; everything else in the picture is rebuilt in code.

## Reference study (measured)
- 1276×720, 30 fps, 11.10 s video / 11.21 s audio. Music ≈112 BPM (beat 0.534 s).
- Hard cuts (frame-diff spikes): **0.467** (dark→light), **1.067** (Hello→head), **3.900** (Your→eye), **5.367** (eye→light titles), **9.567** (name→logo). Fade to black ≈10.8.
- Audio: onsets on every half-beat; a **dead stop 3.25–3.75 s** (−29/−33 dB) before the hit at **3.89**; big hits at 3.89, 4.95, 5.48, 9.56. Title swaps land on 5.47, 6.07, 6.60, 6.93, 7.27, 7.80.
- Key mechanisms:
  1. **Design-tool canvas:** dashed guides + live px measurements hug a growing "H" (Figma-style), letters type in with a trailing accent ghost.
  2. **Type lives inside the subject:** "I'm" sits inside the head silhouette; deleting it makes the head bow, and the name types above.
  3. **Letter becomes object:** the "o" of "Your" fills, becomes a pupil, and grows into the eye of the next scene (foreground-becomes-transition).
  4. **The eye as portal:** the camera pushes into the eye; the first title word slides out from behind the iris and the white of the eye becomes the next scene's background.
  5. **Carousel of titles:** fixed first word + swapping bold second word, a persistent icon riding the last letter, squiggle underline.
  6. **Resolve:** the title collapses into the name, which slowly shrinks, then hard cut to the brand mark.

## Storyboard (times locked to the audio)

| Time (s) | On screen | What the moment is for | How it leaves | Carried into next shot |
|---|---|---|---|---|
| 0.00–0.47 | Navy canvas, dashed guides, px labels; a mint caret births a white "H" that grows while labels count up | Hook: "something is being designed" | Hard cut on beat, H stays in place | The "H" + guides (same pixels, colours invert) |
| 0.47–1.07 | Light canvas; "Hello" types letter by letter, each with a mint ghost; dot-matrix hand fades in and waves | Greeting | Hard cut on beat | Centre text position → "I'm" |
| 1.07–1.55 | Shayan's silhouette fills the frame; white "I'm" inside his head | Who: it's a person | Caret deletes "m", head bows with motion blur | The caret |
| 1.55–2.60 | Small bowed silhouette; "Shayan **Samimi**" types above his head, caret blinks | The name | "Samimi" hops, then is deleted | The last letter "i" |
| 2.60–3.90 | "Shayan" is deleted too; the dot of the last "i" grows into the "o" as the stem drops away, then Y/u/r fly in to "Your"; the o fills mint, then ink: a pupil. On the dead stop, "r" drops; 3.73–3.87 a ring appears behind the pupil, the pupil rises and swells while the head lifts and pushes toward camera with blur | Set up the promise: "Your…" | The pupil grows into the next scene | **The o/pupil** |
| 3.90–4.40 | Navy; the eye starts as a half-dome (upper lid only) round the pupil, becoming an almond by ≈4.47; iris gets texture, pupil narrows to a slit | Attention: he's watching your brand | Eye widens, iris darts right with blur, leaving a flat accent afterimage (4.53–4.73) | The iris |
| 4.40–5.37 | Full almond eye, mint iris right of centre; "Growth" slides out from behind the iris; camera pushes in | The role, first word | White of the eye fills the frame | The word "Growth" (same pixels) |
| 5.37–5.60 | Light; "Growth" centred, slides left as **Strategist** focuses in | Role 1 (YouTube/content strategy) | Word swap on beat | "Growth" + icon |
| 5.60–6.07 | Accent dot lands on the bold word; squiggle draws under "Growth" (5.60–6.00) | Detail layer | Swap | icon |
| 6.07 / 6.60 / 6.93 | **Operator** → **Marketer** → **Architect**; one icon rides the last letter and changes meaning each swap (play ▶ Strategist, gear Operator, target Marketer, spark Architect, linked rings Partner) | Roles 2–4 (COO / Meta ads / AI systems) | Swaps on beats, speeding up | icon |
| 7.27–7.80 | **Growth Partner**; squiggle under "Growth" turns accent and unwinds 7.33–7.60 | Payoff line | Collapses into the name | Centre text |
| 7.80–9.57 | "Shayan **Samimi**" centred with a small "Growth Partner · Ventura Marketing" line under it, slow shrink | Sign-off | Hard cut on the hit | Centre point |
| 9.57–10.77 | Navy; "Ventura Marketing" wordmark (Newsreader italic, mint gradient), ≤3% push | Brand | Hard cut off | — |
| 10.77–11.21 | Empty navy while the audio rings out (video runs to the audio's 11.21 s so the track is untouched) | Ending | — | — |

## 9:16 framing
The 16:9 design stage is scaled ×0.72 and centred in 1080×1920; backgrounds, guides and the eye field are full-bleed, the silhouette extends to the bottom edge, and the widest element (the eye, ≈1050 px) fits inside the width.

## Signature moments (no effect names)
1. The "o" in "Your" turns into the pupil of the eye that looks back at you.
2. The first word of his title walks out from behind the iris.
3. His name types itself above his own bowed head.

## Deliberately not used
- **Three.js:** nothing in this story is physical or spatial; a 3D element would be decoration, so it's left out per the kit's rule.
- **Generated images/footage:** none. The only photographic asset is Shayan's real headshot, reduced to a silhouette.
- **Extra sound effects:** the reference track already carries every hit; adding whooshes on top of a track the user wants kept exactly would change it.
