import sys, glob, os
from PIL import Image
# sheet.py out.jpg pid...  : ghép các hình của các bài để xem nhanh
out = sys.argv[1]
fs = []
for pid in sys.argv[2:]:
    fs += sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'problems', pid, 'fig', '*.png')))
ims = []
for f in fs:
    im = Image.open(f).convert('RGB')
    s = 520 / max(im.size)
    ims.append(im.resize((int(im.size[0] * s), int(im.size[1] * s))))
cols = 4
rows = (len(ims) + cols - 1) // cols
W = 540 * cols; H = 540 * rows
c = Image.new('RGB', (W, H), 'white')
for k, im in enumerate(ims):
    c.paste(im, ((k % cols) * 540, (k // cols) * 540))
c.save(out, quality=85)
print(len(ims), 'figs')
