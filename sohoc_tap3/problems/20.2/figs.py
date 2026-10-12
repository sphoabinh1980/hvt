from figlib import *
from matplotlib.patches import Polygon as Pg

P = [(0, 0), (6, 0), (6, 4), (2, 6), (0, 3)]

def onseg(p, a, b):
    cr = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    return cr == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def inside(p):
    c = False
    for i in range(5):
        a, b = P[i], P[(i + 1) % 5]
        if (a[1] > p[1]) != (b[1] > p[1]):
            x = a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
            if p[0] < x: c = not c
    return c

def pick(path):
    fig, ax = new(7.6, 3.4)
    s = 0.45; X0, Y0 = 0.4, 0.35
    T = lambda p: (X0 + p[0] * s, Y0 + p[1] * s)
    ax.add_patch(Pg([T(p) for p in P], closed=True, facecolor='#F3F6FA', edgecolor=NAVY, lw=1.6, zorder=1))
    nb = ni = 0
    for x in range(-1, 8):
        for y in range(-1, 8):
            p = (x, y)
            if any(onseg(p, P[i], P[(i + 1) % 5]) for i in range(5)):
                ax.plot(*T(p), 'o', ms=8, color='#FFC000', markeredgecolor=DRED, zorder=5); nb += 1
            elif inside(p):
                ax.plot(*T(p), 'o', ms=7, color=BLUE, zorder=5); ni += 1
            else:
                ax.plot(*T(p), '.', ms=3, color='#C0C0C0', zorder=2)
    for p, d in zip(P, [(-0.3, -0.18), (0.35, -0.18), (0.4, 0.05), (0, 0.25), (-0.4, 0.05)]):
        txt(ax, T(p)[0] + d[0], T(p)[1] + d[1], '(%d,%d)' % p, fs=7.5, color=NAVY, bold=True)
    tx = 4.3
    txt(ax, tx, 3.1, '2S = |Σ (xᵢ yᵢ₊₁ − xᵢ₊₁ yᵢ)|', fs=8.8, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 2.8, '= 0 + 24 + 28 + 6 + 0 = 58', fs=8.6, ha='left')
    txt(ax, tx, 2.35, 'B = Σ gcd(|dx|, |dy|)', fs=8.8, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 2.05, '= 6 + 4 + 2 + 1 + 3 = 16  (vàng)', fs=8.6, ha='left')
    txt(ax, tx, 1.6, 'Pick:  S = I + B/2 − 1', fs=8.8, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 1.3, 'I = (2S − B + 2)/2 = (58 − 16 + 2)/2', fs=8.6, ha='left')
    txt(ax, tx, 1.0, '= 22  (xanh)', fs=9.5, ha='left', bold=True, color=DRED)
    assert (ni, nb) == (22, 16)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'S2 ← 0;  B ← 0', 0, 0)
    f.node('b', 'proc', 'với mỗi cạnh Pᵢ → Pᵢ₊₁ (kể cả Pₙ → P₁):\nS2 += xᵢ yᵢ₊₁ − xᵢ₊₁ yᵢ;   B += gcd(|dx|, |dy|)', 0, -0.68)
    f.node('c', 'proc', 'S2 ← |S2|;  I ← (S2 − B + 2) / 2', 0, -1.36)
    f.node('d', 'end', 'In I, B', 0, -1.96)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    pick(F('pick')); opt_flow(F('opt'))
