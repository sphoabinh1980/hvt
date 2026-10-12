from figlib import *
from matplotlib.patches import Rectangle

COLS = ['#FFE699', '#DEEBF7', '#FBE5D6', '#E2F0D9', '#EDE5F5', '#F8DEDD']

def blocks(n, L):
    out = []; i = 1
    while i <= L:
        q = n // i; j = min(n // q, L); out.append((i, j, q)); i = j + 1
    return out

def rowblocks(ax, y, B, lab, w, x0, ec=GRAY, lw=0.8):
    txt(ax, x0 - 0.1, y + 0.17, lab, fs=8.2, ha='right', bold=True, color=NAVY)
    for k, (i, j, q) in enumerate(B):
        X = x0 + (i - 1) * w
        ax.add_patch(Rectangle((X, y), (j - i + 1) * w - 0.04, 0.34, facecolor=COLS[k % 6], edgecolor=ec, lw=lw, zorder=2))
        txt(ax, X + (j - i + 1) * w / 2 - 0.02, y + 0.17, str(q) if q else '', fs=8.5, bold=True)

def common(path):
    fig, ax = new(7.6, 3.1)
    n, m, L = 10, 7, 7
    w, x0 = 0.62, 1.7
    for i in range(1, L + 1):
        txt(ax, x0 + (i - 0.5) * w - 0.02, 2.9, 'i = %d' % i, fs=7.8, color=GRAY)
    rowblocks(ax, 2.35, blocks(n, L), '⌊10/i⌋', w, x0)
    rowblocks(ax, 1.85, blocks(m, L), '⌊7/i⌋', w, x0)
    C = []; i = 1
    while i <= L:
        a, b = n // i, m // i; j = min(n // a, m // b, L); C.append((i, j, 0)); i = j + 1
    txt(ax, x0 - 0.1, 1.52, 'khối chung', fs=8.2, ha='right', bold=True, color=DRED)
    for (i, j, _) in C:
        X = x0 + (i - 1) * w
        ax.add_patch(Rectangle((X, 1.35), (j - i + 1) * w - 0.04, 0.34, facecolor='white', edgecolor=DRED, lw=1.6, zorder=2))
        txt(ax, X + (j - i + 1) * w / 2 - 0.02, 1.52, '[%d, %d]' % (i, j) if i != j else str(i), fs=8, color=DRED, bold=True)
    for r, (lab, f) in enumerate([('10 mod i', lambda i: n % i), ('7 mod i', lambda i: m % i), ('tích', lambda i: (n % i) * (m % i))]):
        y = 0.9 - r * 0.33
        txt(ax, x0 - 0.1, y + 0.13, lab, fs=8, ha='right', color=NAVY if r < 2 else DRED, bold=r == 2)
        for i in range(1, L + 1):
            v = f(i)
            cell(ax, x0 + (i - 1) * w, y, w - 0.04, 0.28, str(v), ('ans' if v else 'gray') if r == 2 else 'plain', fs=8, bold=r == 2 and v > 0)
    txt(ax, x0 + L * w + 0.15, 0.37, 'S = 1 + 6 + 4 = 11', fs=9, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'S ← 0', 0, 0)
    f.node('b', 'proc', 'với i = 1..min(n, m):  S += (n mod i)(m mod i)', 0, -0.6)
    f.node('c', 'end', 'In S mod p', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'L ← min(n, m);  i ← 1;  S ← 0', 0, 0)
    f.node('b', 'dec', 'i ≤ L ?', 0, -0.8)
    f.node('c', 'proc', 'a ← ⌊n/i⌋;  b ← ⌊m/i⌋\nj ← min(⌊n/a⌋, ⌊m/b⌋)\nS += nm·cnt − (nb + ma)·Σi + ab·Σi²\ni ← j + 1', 3.3, -0.8)
    f.node('d', 'end', 'In S', 0, -1.65)
    f.edge('a', 'b')
    f.edge('b', 'c', 'r', 'l', label='Đúng')
    f.edge('c', 'b', 't', 't', via=[(3.3, -0.28), (0, -0.28)])
    f.edge('b', 'd', label='Sai', lpos=(0.25, -1.33))
    f.draw(path)

def make(F):
    common(F('common')); naive_flow(F('naive')); opt_flow(F('opt'))
