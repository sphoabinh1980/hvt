import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from figlib import *

TILES = [
    ('153', '1³ + 5³ + 3³', 'số tự luân', 'ans'), ('6174', '7641 − 1467', 'hằng số Kaprekar', 'done'),
    ('142857', '× 2 = 285714', 'số vòng', 'in'), ('12321', 'đọc xuôi = đọc ngược', 'số đối xứng', 'green'),
    ('28', '1 + 2 + 4 + 7 + 14', 'số hoàn hảo', 'purple'), ('76', '76² = 5776', 'số tự đồng cấu', 'yellow'),
    ('145', '1! + 4! + 5!', 'factorion', 'pink'), ('1729', '1³ + 12³ = 9³ + 10³', 'số taxi', 'dblue'),
    ('220 · 284', 'σ(220) − 220 = 284', 'cặp thân thiết', 'green'), ('7 → 1', '7 → 49 → 97 → 130 → 10 → 1', 'số hạnh phúc', 'ans'),
    ('2026', '2 + 0 + 2 + 6 = 10', 'tổng chữ số', 'in'), ('1111111', '239 × 4649', 'repunit', 'done'),
]

def make(path):
    fig, ax = new(7.6, 3.55)
    w, h, gx, gy = 1.75, 1.0, 0.13, 0.15
    for k, (big, f, cap, kind) in enumerate(TILES):
        r, c = divmod(k, 4)
        x = 0.1 + c * (w + gx); y = 2.45 - r * (h + gy)
        rbox(ax, x, y, w, h, '', kind, r=0.1, lw=1.4)
        txt(ax, x + w / 2, y + 0.66, big, fs=15 if len(big) < 8 else 12.5, bold=True, color=NAVY)
        txt(ax, x + w / 2, y + 0.36, f, fs=7.4, color='#333333')
        txt(ax, x + w / 2, y + 0.13, cap, fs=7.4, color=DRED, bold=True)
    save(fig, path)

if __name__ == '__main__':
    make(sys.argv[1])
