#!/usr/bin/env bash
# Build uvmecon-ai safely:
# - website pages render to docs/
# - slides render to docs/slides as revealjs HTML
# - slide PDFs are generated from HTML via Chrome headless
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
SLIDES_DIR="$REPO/slides"
DOCS_SLIDES="$REPO/docs/slides"

SLIDES=(
  demo-title.qmd
  demo-columns.qmd
  demo-table.qmd
  demo-seminar.qmd
  s1-emily.qmd
  s1-erkmen.qmd
  s2-part1.qmd
  s2-part2.qmd
)

usage() {
  cat <<'EOF'
Usage: ./render.sh [site|slides-html|slides-pdf|all]

  site        Render the main website only
  slides-html Render revealjs slide HTML only
  slides-pdf  Render slide PDFs from already-built HTML
  all         Render website + slide HTML + slide PDFs

Default: site
EOF
}

render_site() {
  echo "=== Rendering website ==="
  cd "$REPO"
  quarto render --output-dir docs
}

render_slides_html() {
  echo "=== Rendering slides (HTML) ==="
  cd "$SLIDES_DIR"
  for f in "${SLIDES[@]}"; do
    quarto render "$f" --to revealjs
  done
}

render_slides_pdf() {
  echo "=== Rendering slides (PDF) ==="
  cd "$SLIDES_DIR"

  local port=8000
  for f in "${SLIDES[@]}"; do
    PORT="$port" ./render_pdf.sh "$f"
    port=$((port + 1))
  done
}

MODE="${1:-site}"

case "$MODE" in
  site)
    render_site
    ;;
  slides-html)
    render_slides_html
    ;;
  slides-pdf)
    render_slides_pdf
    ;;
  all)
    render_site
    render_slides_html
    render_slides_pdf
    ;;
  -h|--help|help)
    usage
    exit 0
    ;;
  *)
    usage
    exit 1
    ;;
esac

echo "=== Done ==="
if [ -d "$DOCS_SLIDES" ]; then
  ls -lh "$DOCS_SLIDES"
fi
