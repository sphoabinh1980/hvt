from figlib import *
from matplotlib.patches import Rectangle

COLS = ['#FFE699', '#DEEBF7', '#FBE5D6', '#E2F0D9', '#EDE5F5', '#F8DEDD', '#FFF2CC', '#D9E1F2']

def bars(path):
    fig, ax = new(7.6, 2.9)
    n, k = 20, 24; w = 0.29; hs = 0.1
    i = 1; b = 0; col = {}
    while i <= n:
        q = n // i; j = n // q
        for x in range(i, j + 1): col[x] = (COLS[b % 8], q)
        b += 1; i = j + 1
    for x in range(1, k + 1):
        r = n % x
        fc, q = col.get(x, ('#EDEDED', 0))
        X = 0.3 + (x - 1) * w
        ax.add_patch(Rectangle((X, 0.5), w - 0.03, max(r, 0.04) * hs, facecolor=fc, edgecolor='#7F7F7F', lw=0.6, zorder=2))
        txt(ax, X + w / 2, 0.5 + r * hs + 0.1, str(r), fs=6.8, color=NAVY)
        txt(ax, X + w / 2, 0.38, str(x), fs=6.8, color=GRAY)
        txt(ax, X + w / 2, 0.2, str(q), fs=6.8, color=DRED)
    txt(ax, 0.12, 0.38, 'i', fs=7.5, color=GRAY); txt(ax, 0.1, 0.2, 'q', fs=7.5, color=DRED)
    line(ax, [(0.3 + 20 * w - 0.015, 0.4), (0.3 + 20 * w - 0.015, 2.75)], color=RED, lw=1.0, ls='--')
    txt(ax, 0.3 + 24 * w + 0.1, 1.6, 'i > n:\nn mod i = n', fs=7.8, color=RED, bold=True, ha='left')
    txt(ax, 3.2, 2.6, 'khối [7, 10], q = 2: số dư 6, 4, 2, 0 giảm đều 2', fs=8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'S ← 0', 0, 0)
    f.node('b', 'proc', 'với i = 1..k:  S ← (S + n mod i) mod p', 0, -0.6)
    f.node('c', 'end', 'In S', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'S ← n · k mod p;  lim ← min(n, k);  i ← 1', 0, 0)
    f.node('b', 'dec', 'i ≤ lim ?', 0, -0.75)
    f.node('c', 'proc', 'q ← ⌊n/i⌋;  j ← min(⌊n/q⌋, lim)\nS ← S − q · (i + ... + j)  (mod p)\ni ← j + 1', 3.2, -0.75)
    f.node('d', 'end', 'In S', 0, -1.6)
    f.edge('a', 'b')
    f.edge('b', 'c', 'r', 'l', label='Đúng')
    f.edge('c', 'b', 't', 't', via=[(3.2, -0.22), (0, -0.22)])
    f.edge('b', 'd', label='Sai', lpos=(0.25, -1.28))
    f.draw(path)

def make(F):
    bars(F('bars')); naive_flow(F('naive')); opt_flow(F('opt'))
