#!/usr/bin/env bash
# Render revealjs HTML slides to PDF using Chrome headless
# Usage: ./render_pdf.sh session1.qmd [output.pdf]
# Requires: Google Chrome, quarto render already done (HTML must exist)
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <slides.qmd> [output.pdf]"
  exit 1
fi

QMD="$1"
OUT="${2:-}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCS_SLIDES="$SCRIPT_DIR/../docs/slides"
BASE_NAME="$(basename "$QMD" .qmd)"

HTML_FILE="$DOCS_SLIDES/${BASE_NAME}.html"

if [ -z "$OUT" ]; then
  OUT="$DOCS_SLIDES/${BASE_NAME}.pdf"
fi

resolve_chrome() {
  if [ -n "${CHROME:-}" ] && [ -x "${CHROME}" ]; then
    echo "${CHROME}"
    return 0
  fi

  local candidates=(
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    "$(command -v google-chrome 2>/dev/null || true)"
    "$(command -v google-chrome-stable 2>/dev/null || true)"
    "$(command -v chromium 2>/dev/null || true)"
    "$(command -v chromium-browser 2>/dev/null || true)"
  )

  local candidate
  for candidate in "${candidates[@]}"; do
    if [ -n "$candidate" ] && [ -x "$candidate" ]; then
      echo "$candidate"
      return 0
    fi
  done

  return 1
}

CHROME_BIN="$(resolve_chrome || true)"
if [ -z "$CHROME_BIN" ]; then
  echo "Chrome or Chromium not found."
  echo "Set CHROME=/path/to/browser or install Google Chrome / Chromium."
  exit 1
fi

if [ ! -f "$HTML_FILE" ]; then
  echo "HTML not found: $HTML_FILE"
  echo "Run: quarto render slides/$QMD --to revealjs"
  exit 1
fi

PORT="${PORT:-8000}"
python3 -m http.server "$PORT" --directory "$DOCS_SLIDES" >/tmp/reveal_pdf_server.log 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" >/dev/null 2>&1 || true' EXIT

# Give reveal + print CSS a little longer to settle before headless export.
sleep 2

URL="http://localhost:$PORT/${BASE_NAME}.html?print-pdf"

echo "Printing to PDF with $CHROME_BIN: $OUT"
"$CHROME_BIN" \
  --headless \
  --disable-gpu \
  --disable-dev-shm-usage \
  --no-sandbox \
  --disable-software-rasterizer \
  --disable-features=VizDisplayCompositor \
  --print-to-pdf-no-header \
  --print-to-pdf="$OUT" \
  --virtual-time-budget=60000 \
  --run-all-compositor-stages-before-draw \
  "$URL"

echo "Done: $OUT"
