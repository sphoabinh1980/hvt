from figlib import *
from math import gcd

def path_fig(path):
    fig, ax = new(7.8, 3.2)
    s = 0.24; X0, Y0 = 0.3, 0.35
    for x in range(0, 15):
        for y in range(0, 11):
            ax.plot([X0 + x * s], [Y0 + y * s], '.', color='#B0B0B0', ms=4, zorder=1)
    P = [(1, 1), (13, 9), (13, 2)]
    line(ax, [(X0 + x * s, Y0 + y * s) for x, y in P], color=BLUE, lw=1.6)
    for i in range(2):
        (x1, y1), (x2, y2) = P[i], P[i + 1]
        g = gcd(abs(x2 - x1), abs(y2 - y1))
        for t in range(g + 1):
            x = x1 + (x2 - x1) // g * t; y = y1 + (y2 - y1) // g * t
            shared = (x, y) == (13, 9)
            ax.plot([X0 + x * s], [Y0 + y * s], 'o', ms=11 if shared else 8, color=DRED if shared else GREEN, zorder=5,
                    markeredgecolor='white' if not shared else DRED)
    for (x, y), lab, dx in [((1, 1), 'P₁(1, 1)', -0.1), ((13, 9), 'P₂(13, 9)', 0.15), ((13, 2), 'P₃(13, 2)', 0.15)]:
        txt(ax, X0 + x * s + dx, Y0 + y * s + 0.2, lab, fs=8, color=NAVY, bold=True, ha='left' if dx > 0 else 'right')
    tx = 4.75
    txt(ax, tx, 2.7, 'P₁P₂: gcd(12, 8) = 4 bước (3, 2)', fs=8.6, ha='left')
    txt(ax, tx, 2.42, '→ 5 điểm', fs=8.6, ha='left', color=GREEN, bold=True)
    txt(ax, tx, 2.0, 'P₂P₃: gcd(0, 7) = 7 bước (0, −1)', fs=8.6, ha='left')
    txt(ax, tx, 1.72, '→ 8 điểm', fs=8.6, ha='left', color=GREEN, bold=True)
    txt(ax, tx, 1.3, 'P₂ chung (đỏ): 5 + 8 − 1 = 12', fs=8.8, ha='left', color=DRED, bold=True)
    txt(ax, tx, 0.85, 'Gọn hơn: 1 (cho P₁) + 4 + 7 = 12', fs=8.8, ha='left', color=NAVY, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc P₁;  ans ← 1', 0, 0)
    f.node('b', 'proc', 'với i = 2..n:  ans += gcd(|xᵢ − xᵢ₋₁|, |yᵢ − yᵢ₋₁|)', 0, -0.6)
    f.node('c', 'end', 'In ans', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def make(F):
    path_fig(F('path')); opt_flow(F('opt'))
