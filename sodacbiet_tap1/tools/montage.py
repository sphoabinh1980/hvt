#!/usr/bin/env python3
"""montage.py out.jpg first last [cols]: ghép các ảnh trang out/pg-*.jpg thành một ảnh."""
import sys, glob, os, re
from PIL import Image
out, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 4
fs = {int(re.search(r'pg-0*(\d+)\.jpg', f).group(1)): f for f in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out', 'pg-*.jpg'))}
ims = [Image.open(fs[k]) for k in range(a, b + 1) if k in fs]
w, h = ims[0].size
rows = (len(ims) + cols - 1) // cols
s = Image.new('RGB', (w * cols, h * rows), 'white')
for k, im in enumerate(ims): s.paste(im, ((k % cols) * w, (k // cols) * h))
s.save(out)
