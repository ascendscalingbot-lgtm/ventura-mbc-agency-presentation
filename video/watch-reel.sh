#!/usr/bin/env bash
# Capture every frame of the reference reel with the claude-video /watch skill.
# Usage: ./watch-reel.sh            (downloads from Instagram — needs instagram.com allowed)
#        ./watch-reel.sh local      (uses video/source/reel.mp4 if you upload the file)
set -euo pipefail
cd "$(dirname "$0")"
[ -d claude-video ] || git clone --depth 1 https://github.com/bradautomates/claude-video.git
SRC="https://www.instagram.com/reel/Dd2E7NWp198/"
[ "${1:-}" = "local" ] && SRC="source/reel.mp4"
python3 claude-video/skills/watch/scripts/watch.py "$SRC" \
  --engine local --detail token-burner --resolution 1024 --no-dedup --no-whisper \
  --out-dir watch-run
