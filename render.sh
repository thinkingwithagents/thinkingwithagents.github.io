#!/usr/bin/env bash
# Build the full uvmecon-ai site: website + slides (HTML + PDF)
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"

echo "=== Rendering website ==="
cd "$REPO" && quarto render

echo "=== Rendering slides (HTML) ==="
cd "$REPO/slides"
quarto render session1.qmd --to revealjs
quarto render session2.qmd --to revealjs

echo "=== Rendering slides (PDF) ==="
./render_pdf.sh session1.qmd
PORT=8001 ./render_pdf.sh session2.qmd

echo "=== Done ==="
ls -lh "$REPO/docs/slides/"
