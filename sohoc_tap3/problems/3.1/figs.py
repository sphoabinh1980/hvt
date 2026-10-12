from figlib import *

def tiles(path):
    fig, ax = new(6.6, 2.7)
    a, b, g = 252, 105, 21
    sc = 4.4 / a
    x0, y0 = 0.3, 0.35
    for i in range(a // g):
        for j in range(b // g):
            ax.add_patch(Rectangle((x0 + i * g * sc, y0 + j * g * sc), g * sc, g * sc, facecolor='#DEEBF7' if (i + j) % 2 else '#BDD7EE', edgecolor=BLUE, lw=0.6))
    ax.add_patch(Rectangle((x0, y0), g * sc, g * sc, facecolor='#FFE699', edgecolor=DRED, lw=1.6, zorder=3))
    txt(ax, x0 + a * sc / 2, y0 - 0.17, '252 = 12 · 21', fs=9, color=NAVY, bold=True)
    txt(ax, x0 - 0.15, y0 + b * sc / 2, '105 = 5 · 21', fs=9, color=NAVY, bold=True, rotation=90)
    x1 = x0 + a * sc + 0.3
    txt(ax, x1, 2.25, 'Cạnh miếng vuông: s | 252 và s | 105', fs=8.5, ha='left', color=NAVY)
    txt(ax, x1, 1.95, '→ s lớn nhất = gcd(252, 105) = 21', fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, x1, 1.5, 'Số miếng = (252/21) · (105/21)', fs=8.5, ha='left')
    txt(ax, x1, 1.22, '              = 12 · 5 = 60', fs=8.5, ha='left', bold=True)
    txt(ax, x1, 0.75, 'Euclid: (252, 105) → (105, 42)', fs=8, ha='left', color=GRAY)
    txt(ax, x1, 0.5, '→ (42, 21) → (21, 0): g = 21', fs=8, ha='left', color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b;  s ← min(a, b)', 0, 0)
    f.node('c', 'dec', 's | a và s | b ?', 0, -0.78)
    f.node('d', 'proc', 's ← s − 1', -2.3, -0.78)
    f.node('o', 'end', 'In s, (a/s)·(b/s)', 0, -1.65)
    f.edge('s', 'c'); f.edge('c', 'd', 'l', 'r', label='Sai')
    f.edge('d', 'c', 't', 't', via=[(-2.3, -0.32), (0, -0.32)])
    f.edge('c', 'o', label='Đúng', lpos=(0.32, -1.25))
    f.draw(path)

def sizes(path):
    fig, ax = new(6.6, 2.15)
    rows = [('a, b', 18, 'in'), ('g, a/g, b/g', 18, 'done'), ('long long (tới ≈ 9,2·10¹⁸)', 18.96, 'green'),
            ('số miếng (a/g)·(b/g)', 36, 'pink'), ('unsigned __int128 (≈ 3,4·10³⁸)', 38.5, 'purple')]
    x0, sc = 2.55, 3.8 / 39
    for i, (lab, e, k) in enumerate(rows):
        y = 1.8 - i * 0.38
        txt(ax, x0 - 0.1, y + 0.13, lab, fs=8.2, ha='right', color=NAVY)
        cell(ax, x0, y, e * sc, 0.27, {18: '10¹⁸', 36: '10³⁶'}.get(e, ''), k, fs=8)
    txt(ax, x0 + 36 * sc + 0.1, 1.8 - 3 * 0.38 + 0.13, '← tràn long long!', fs=8, color=DRED, bold=True, ha='left')
    save(fig, path)

def euclid_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b;  (x, y) ← (a, b)', 0, 0)
    f.node('c', 'dec', 'y ≠ 0 ?', 0, -0.72)
    f.node('d', 'proc', '(x, y) ← (y, x mod y)', -2.6, -0.72)
    f.node('g', 'proc', 'g ← x', 0, -1.5)
    f.node('m', 'proc', 'cnt ← (u128)(a/g) · (b/g)', 0, -2.1)
    f.node('o', 'io', 'In g;  in cnt bằng print128', 0, -2.7)
    f.edge('s', 'c'); f.edge('c', 'd', 'l', 'r', label='Đúng')
    f.edge('d', 'c', 't', 't', via=[(-2.6, -0.3), (0, -0.3)])
    f.edge('c', 'g', label='Sai', lpos=(0.3, -1.13)); f.edge('g', 'm'); f.edge('m', 'o')
    f.draw(path)

def make(F):
    tiles(F('tiles')); naive_flow(F('naive')); sizes(F('sizes')); euclid_flow(F('opt'))
