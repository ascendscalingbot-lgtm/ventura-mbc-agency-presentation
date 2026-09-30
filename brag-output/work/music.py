# Original 120 BPM score in A minor, synthesized. Downbeats land on odd seconds (1,3,5...) so
# scene cuts at 3, 7, 17 hit bar starts and 12 hits beat 3.
import numpy as np, wave
SR = 48000; DUR = 22.0; N = int(SR * DUR)
t_all = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
def midi(m): return 440.0 * 2 ** ((m - 69) / 12)
def env(n, a, d, s=0.0, r=None):
    e = np.ones(n); ai = max(1, int(a * SR)); e[:ai] = np.linspace(0, 1, ai)
    rest = n - ai
    if rest > 0: e[ai:] = s + (1 - s) * np.exp(-np.arange(rest) / (d * SR))
    return e
def add(buf, start, sig, gain=1.0):
    i = int(start * SR); j = min(N, i + len(sig))
    if i < N and j > i: buf[i:j] += sig[: j - i] * gain
def addst(start, sig, g=1.0, pan=0.0):
    add(L, start, sig, g * np.sqrt((1 - pan) / 2) * 1.414); add(R, start, sig, g * np.sqrt((1 + pan) / 2) * 1.414)
def lp(x, fc):  # one-pole lowpass
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); z = 0.0
    for i in range(len(x)): z = (1 - a) * x[i] + a * z; y[i] = z
    return y
def lp_fast(x, fc, order=2):
    # FFT brickwall-ish smooth lowpass (fast)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / fc) ** (2 * order)); return np.fft.irfft(X, len(x))
def hp_fast(x, fc, order=2):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR) + 1e-9
    X *= 1 / np.sqrt(1 + (fc / f) ** (2 * order)); return np.fft.irfft(X, len(x))

BEAT = 0.5
# chords per bar (bar k starts at 1 + 2k); pickup bar at -1..1 uses Am
CH = {'Am': [57, 60, 64, 67, 71], 'F': [53, 57, 60, 64, 67], 'C': [48, 55, 60, 64, 67], 'G': [55, 59, 62, 67, 69], 'Am9': [45, 57, 60, 64, 67, 71]}
BARS = [(-1, 'Am'), (1, 'Am'), (3, 'F'), (5, 'C'), (7, 'G'), (9, 'Am'), (11, 'F'), (13, 'C'), (15, 'G'), (17, 'Am'), (19, 'Am9')]
ROOT = {'Am': 45, 'F': 41, 'C': 48, 'G': 43, 'Am9': 45}

# --- pad: detuned saws, soft attack, lowpassed; opens up at the 3s reveal
pad = np.zeros((2, N))
for (bs, ch) in BARS:
    s0 = max(0, bs); e0 = min(DUR, bs + (3.0 if ch == 'Am9' else 2.0) + 0.6)
    n = int((e0 - s0) * SR); tt = np.arange(n) / SR
    for k, m in enumerate(CH[ch]):
        for side, det in ((0, -0.08), (1, 0.08)):
            f = midi(m + det)
            ph = 2 * np.pi * f * tt + k
            sig = sum(np.sin(ph * h) / h for h in range(1, 7))
            e = np.minimum(1, tt / 0.35) * np.minimum(1, (e0 - s0 - tt) / 0.6)
            i = int(s0 * SR); pad[side, i:i + n] += sig * e * 0.05
for side in range(2):
    lo = lp_fast(pad[side], 700); hi = lp_fast(pad[side], 2600)
    x = np.clip((t_all - 2.4) / 0.8, 0, 1)  # filter opens into the drop
    pad[side] = lo * (1 - x) + hi * x
fade_end = np.clip((DUR - t_all) / 1.6, 0, 1)
L += pad[0] * 0.9 * fade_end ** 0.5; R += pad[1] * 0.9 * fade_end ** 0.5

# --- pluck arp (16ths) across the chord, whole piece, softer under the drums
def pluck(f, dur=0.35, bright=1.0):
    n = int(dur * SR); tt = np.arange(n) / SR
    sig = np.sin(2 * np.pi * f * tt) + 0.35 * bright * np.sin(4 * np.pi * f * tt) * np.exp(-tt * 18) + 0.15 * np.sin(6 * np.pi * f * tt) * np.exp(-tt * 30)
    return sig * env(n, 0.003, 0.12)
for (bs, ch) in BARS:
    notes = [m + 12 for m in CH[ch][1:5]]
    pat = [0, 1, 2, 3, 2, 1, 2, 3]
    for s in range(16):
        st = bs + s * 0.125
        if st < 0.0 or st >= DUR - 1.0: continue
        m = notes[pat[s % 8]] + (12 if s in (7, 15) else 0)
        g = 0.07 if st < 3 else 0.05
        addst(st, pluck(midi(m)), g, pan=(-0.35 if s % 2 else 0.35))

# --- drums from the 3s drop to 19s, final hit at 19
def kick():
    n = int(0.35 * SR); tt = np.arange(n) / SR
    f = 45 + 90 * np.exp(-tt * 38); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-tt * 9) + 0.15 * rng.standard_normal(n) * np.exp(-tt * 200)
def hat(open_=False):
    n = int((0.18 if open_ else 0.05) * SR); tt = np.arange(n) / SR
    return hp_fast(rng.standard_normal(n), 7000) * np.exp(-tt * (18 if open_ else 70))
def clap():
    n = int(0.25 * SR); tt = np.arange(n) / SR
    x = lp_fast(hp_fast(rng.standard_normal(n), 1200), 5000)
    e = np.exp(-tt * 22) + 0.6 * np.exp(-np.maximum(0, tt - 0.012) * 40) * (tt > 0.012)
    return x * e
K = kick(); H = hat(); HO = hat(True); C = clap()
b = 3.0
while b < 19.0 - 1e-6:
    addst(b, K, 0.55)
    addst(b + 0.25, HO if int((b - 1) / 0.5) % 4 == 3 else H, 0.10, pan=0.2)
    addst(b + 0.125, H, 0.035, pan=-0.3); addst(b + 0.375, H, 0.035, pan=-0.3)
    if int(round((b - 1) / 0.5)) % 2 == 1: addst(b, C, 0.12, pan=0.05)
    b += 0.5
addst(19.0, K, 0.55)

# --- bass: root 8ths with sidechain feel
def bassnote(f, dur):
    n = int(dur * SR); tt = np.arange(n) / SR
    sig = np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt) + 0.12 * np.sin(6 * np.pi * f * tt)
    duck = 1 - 0.7 * np.exp(-((tt + 0) % 0.5) * 14)
    return sig * env(n, 0.005, 0.25, 0.55) * np.minimum(1, (dur - tt) / 0.02)
for (bs, ch) in BARS:
    if bs < 3 or bs >= 19: continue
    for s in range(4):
        st = bs + s * 0.5 + 0.25
        addst(st, bassnote(midi(ROOT[ch] - 12 + (12 if s == 3 else 0)), 0.22), 0.22)
        addst(bs + s * 0.5, bassnote(midi(ROOT[ch] - 12), 0.18), 0.12)
# final low A under Am9
addst(19.0, bassnote(midi(33), 2.8), 0.25)

# --- SFX, tuned to the key
def chime(root_m, dur=2.2):
    n = int(dur * SR); tt = np.arange(n) / SR; sig = np.zeros(n)
    for m, g in ((root_m, 1), (root_m + 7, .5), (root_m + 12, .35), (root_m + 19, .15)):
        f = midi(m); sig += g * np.sin(2 * np.pi * f * tt) * np.exp(-tt * (2.2 + m / 40))
        sig += g * 0.2 * np.sin(2 * np.pi * f * 2.76 * tt) * np.exp(-tt * 9)
    return sig * np.minimum(1, tt / 0.004)
def whoosh(dur=0.55, up=True):
    n = int(dur * SR); tt = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # sweep via several bandpassed slices crossfaded
    out = np.zeros(n); seg = 6
    for k in range(seg):
        fc = 400 * (2 ** (k * 0.9 if up else (seg - k) * 0.9))
        band = lp_fast(hp_fast(noise, fc * 0.7), fc * 1.6)
        w = np.exp(-((tt / dur - (k + 0.5) / seg) ** 2) / 0.02)
        out += band * w
    e = np.sin(np.pi * np.clip(tt / dur, 0, 1)) ** 2
    return out * e
def blip(m):
    n = int(0.4 * SR); tt = np.arange(n) / SR; f = midi(m)
    return (np.sin(2 * np.pi * f * tt) + 0.2 * np.sin(4 * np.pi * f * tt)) * env(n, 0.002, 0.07)

addst(1.0, chime(76, 1.8), 0.10, pan=0.1)                 # strike-through (E)
addst(1.62, whoosh(0.4, True), 0.05)                        # flip to "A growth partner."
addst(2.25, whoosh(0.75, True), 0.06)                       # riser into the drop
addst(3.0, chime(69, 2.5), 0.07)                            # reveal (A)
for tc in (6.6, 11.6, 16.6): addst(tc, whoosh(0.45, True), 0.05)
for i, tc in enumerate([7.75, 8.0, 8.25, 8.5, 8.75]): addst(tc, blip([81, 84, 86, 88, 91][i]), 0.05, pan=-0.4 + 0.2 * i)
# pulse travelling the engine: soft rising tone 9.5-11
n = int(1.5 * SR); tt = np.arange(n) / SR
f = midi(81) * 2 ** (tt / 1.5); sw = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / 1.5) ** 2
addst(9.5, sw, 0.025)
for tc in (12.15, 13.65, 15.15): addst(tc, whoosh(0.35, False), 0.035)
addst(19.0, chime(81, 3.0), 0.11)                           # CTA (A)

# --- space: short stereo reverb (noise IR) on everything, then gentle bus glue
def reverb(x, seed):
    r = np.random.default_rng(seed); n = int(1.6 * SR); tt = np.arange(n) / SR
    ir = r.standard_normal(n) * np.exp(-tt * 3.2); ir = lp_fast(ir, 6000); ir /= np.sqrt(np.sum(ir ** 2))
    m = len(x) + n; F = 1 << (m - 1).bit_length()
    return np.fft.irfft(np.fft.rfft(x, F) * np.fft.rfft(ir, F), F)[: len(x)]
Lw = reverb(L, 1); Rw = reverb(R, 2)
L = L + 0.22 * Lw; R = R + 0.22 * Rw
L = hp_fast(L, 30); R = hp_fast(R, 30)
# soft limiter
peak = max(np.abs(L).max(), np.abs(R).max())
L /= peak / 1.3; R /= peak / 1.3
L = np.tanh(L) ; R = np.tanh(R)
peak = max(np.abs(L).max(), np.abs(R).max())
L *= 0.89 / peak; R *= 0.89 / peak
# tail fade in last 0.25s to avoid a click
fe = np.clip((DUR - t_all) / 0.25, 0, 1); L *= fe; R *= fe
st = np.stack([L, R], 1)
with wave.open('music.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype('<i2').tobytes())
print('ok', np.sqrt(np.mean(st ** 2)))
