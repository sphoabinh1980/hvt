import math
from figlib import *

def clocks(path):
    fig, ax = new(6.8, 3.0)
    for ci, (k, cx) in enumerate([(5, 1.5), (4, 5.2)]):
        cy, R = 1.55, 1.05
        ax.add_patch(Circle((cx, cy), R + 0.14, facecolor='#F7F7F7', edgecolor=NAVY, lw=1.2))
        seen = []
        v = 0
        while v not in seen:
            seen.append(v); v = (v + k) % 12
        P = lambda j: (cx + R * math.sin(2 * math.pi * j / 12), cy + R * math.cos(2 * math.pi * j / 12))
        for a, b in zip(seen, seen[1:] + [seen[0]]):
            arrow(ax, P(a), P(b), color=GREEN if k == 5 else DRED, lw=0.9, ms=7)
        for j in range(12):
            x, y = P(j)
            on = j in seen
            ax.add_patch(Circle((x, y), 0.13, facecolor='#FFE699' if on else 'white', edgecolor=DRED if on else GRAY, lw=1.2 if on else 0.7, zorder=4))
            txt(ax, x, y, str(j), fs=7.5, bold=on)
        txt(ax, cx, 0.12, 'k = %d: thăm %d vạch%s' % (k, len(seen), ' (gcd(4, 12) = 4)' if k == 4 else ' — đủ cả 12'), fs=8.5, color=GREEN if k == 5 else DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n;  cnt ← 0', 0, 0)
    f.node('l', 'proc', 'với k = 1..n:  nếu gcd(k, n) = 1 thì cnt ← cnt + 1', 0, -0.6)
    f.node('o', 'end', 'In cnt', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def sieve12(path):
    fig, ax = new(6.8, 2.2)
    cw = 0.45
    for k in range(1, 13):
        X = 0.9 + (k - 1) * cw
        cell(ax, X, 1.65, cw - 0.04, 0.3, str(k), 'navy', fs=8.5, bold=True)
        cell(ax, X, 1.25, cw - 0.04, 0.3, '' if k % 2 else '/2', 'gray' if k % 2 == 0 else 'plain', fs=7.5)
        cell(ax, X, 0.85, cw - 0.04, 0.3, '' if k % 3 else '/3', 'gray' if k % 3 == 0 else 'plain', fs=7.5)
        ok = math.gcd(k, 12) == 1
        cell(ax, X, 0.45, cw - 0.04, 0.3, '✓' if ok else '', 'ans' if ok else 'plain', fs=9, lw=1.0 if ok else None)
    for y, lab in [(1.8, 'k'), (1.4, 'chia hết 2'), (1.0, 'chia hết 3'), (0.6, 'gcd = 1')]:
        txt(ax, 0.82, y, lab, fs=7.5, ha='right', color=NAVY, bold=True)
    txt(ax, 0.9 + 12 * cw + 0.12, 1.2, 'loại 1/2,', fs=8.3, ha='left', color=GRAY)
    txt(ax, 0.9 + 12 * cw + 0.12, 0.95, 'rồi loại 1/3 phần còn lại', fs=8.3, ha='left', color=GRAY)
    txt(ax, 0.9 + 12 * cw + 0.12, 0.6, 'φ(12) = 12·(1−½)·(1−⅓) = 4', fs=8.6, ha='left', color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'res ← n', 0, 0)
    f.node('a', 'proc', 'nếu 2 | n:  res ← res − res/2;  chia n cho 2 tới hết', 0, -0.6)
    f.node('b', 'proc', 'p = 3, 5, 7, ... khi p² ≤ n:  nếu p | n: res ← res − res/p; chia hết p', 0, -1.2)
    f.node('c', 'proc', 'nếu n > 1 (ước nguyên tố lớn còn lại):  res ← res − res/n', 0, -1.8)
    f.node('o', 'end', 'trả về res = φ(n)', 0, -2.4)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    clocks(F('clocks')); naive_flow(F('naive')); sieve12(F('sieve12')); opt_flow(F('opt'))
