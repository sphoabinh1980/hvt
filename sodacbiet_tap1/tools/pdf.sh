#!/bin/bash
# chuyển docx sang pdf và ảnh trang: pdf.sh <docx> <firstpage> <lastpage> [dpi]
cd "$(dirname "$1")"
f=$(basename "$1" .docx)
timeout 600 python3 /root/.claude/skills/synced/8783fe73-3e48-469a-a14b-77adf6a9c171_4272d704-7a29-4b0f-b9b1-870c36f688e4/docx/scripts/office/soffice.py --headless --convert-to pdf "$f.docx" >/dev/null 2>&1
pdfinfo "$f.pdf" | grep Pages
rm -f pg-*.jpg
pdftoppm -jpeg -r ${4:-70} -f ${2:-1} -l ${3:-999} "$f.pdf" pg
