from figlib import *
from matplotlib.patches import Polygon as Pg

T3 = [(1, 1), (13, 9), (13, 2)]

def cr(a, b, p): return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

def tri(path):
    fig, ax = new(7.6, 3.0)
    s = 0.26; X0, Y0 = 0.3, 0.3
    T = lambda p: (X0 + p[0] * s, Y0 + p[1] * s)
    ax.add_patch(Pg([T(p) for p in T3], closed=True, facecolor='#F3F6FA', edgecolor=NAVY, lw=1.5, zorder=1))
    ni = nb = 0
    for x in range(0, 15):
        for y in range(0, 10):
            p = (x, y)
            c = [cr(T3[0], T3[1], p), cr(T3[1], T3[2], p), cr(T3[2], T3[0], p)]
            onb = any(c[i] == 0 and min(T3[i][0], T3[(i + 1) % 3][0]) <= x <= max(T3[i][0], T3[(i + 1) % 3][0])
                      and min(T3[i][1], T3[(i + 1) % 3][1]) <= y <= max(T3[i][1], T3[(i + 1) % 3][1]) for i in range(3))
            if onb:
                ax.plot(*T(p), 'o', ms=6.5, color='#FFC000', markeredgecolor=DRED, zorder=5); nb += 1
            elif all(v > 0 for v in c) or all(v < 0 for v in c):
                ax.plot(*T(p), 'o', ms=5, color=BLUE, zorder=5); ni += 1
            else:
                ax.plot(*T(p), '.', ms=2.5, color='#C0C0C0', zorder=2)
    assert (ni, nb) == (37, 12), (ni, nb)
    tx = 4.3
    txt(ax, tx, 2.7, 'u = (12, 8),  v = (12, 1)', fs=8.6, ha='left')
    txt(ax, tx, 2.4, '2S = |12 · 1 − 12 · 8| = 84', fs=8.6, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 2.0, 'B = gcd(12, 8) + gcd(12, 1) + gcd(0, 7)', fs=8.6, ha='left')
    txt(ax, tx, 1.72, '   = 4 + 1 + 7 = 12  (vàng)', fs=8.6, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 1.25, 'I = (84 − 12 + 2) / 2 = 37  (xanh)', fs=9.2, ha='left', bold=True, color=DRED)
    save(fig, path)

def sizes(path):
    fig, ax = new(7.4, 2.3)
    rows = [('tọa độ', '10¹⁸', 'long long', 'green'),
            ('hiệu ux, uy, vx, vy', '2 · 10¹⁸', 'long long (tới 9,2 · 10¹⁸)', 'green'),
            ('tích ux · vy', '4 · 10³⁶', '__int128 (tới 1,7 · 10³⁸)', 'pink'),
            ('2S', '8 · 10³⁶', '__int128', 'pink'),
            ('B (ba gcd)', '6 · 10¹⁸', 'vừa long long, cộng vào __int128', 'yellow'),
            ('I', '4 · 10³⁶', '__int128 + hàm in tự viết', 'pink')]
    ws = [1.9, 1.2, 3.6]
    x = 0.1
    for c, h in enumerate(['Đại lượng', 'Tới khoảng', 'Kiểu dữ liệu']):
        cell(ax, x, 1.95, ws[c], 0.3, h, 'navy', fs=8.3, bold=True); x += ws[c]
    for r, row in enumerate(rows):
        x = 0.1
        for c in range(3):
            cell(ax, x, 1.62 - r * 0.31, ws[c], 0.29, row[c], row[3] if c == 2 else 'plain', fs=8.2, bold=c == 0); x += ws[c]
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc ba đỉnh', 0, 0)
    f.node('b', 'proc', 'u, v ← hiệu tọa độ (long long)', 0, -0.6)
    f.node('c', 'proc', '2S ← |(__int128)ux · vy − (__int128)vx · uy|', 0, -1.2)
    f.node('d', 'proc', 'B ← tổng gcd ba cạnh', 0, -1.8)
    f.node('e', 'end', 'In (2S − B + 2)/2 bằng hàm in __int128', 0, -2.4)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.draw(path)

def make(F):
    tri(F('tri')); sizes(F('sizes')); opt_flow(F('opt'))
