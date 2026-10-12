import math
from figlib import *

def clock(path):
    fig, ax = new(6.8, 3.0)
    cx, cy, R = 1.3, 1.5, 1.05
    ax.add_patch(Circle((cx, cy), R + 0.12, facecolor='#F7F7F7', edgecolor=NAVY, lw=1.4))
    for k in range(12):
        an = math.pi / 2 - 2 * math.pi * k / 12
        x, y = cx + R * math.cos(an), cy + R * math.sin(an)
        hl = k in (5,)
        ax.add_patch(Circle((x, y), 0.13, facecolor='#FFE699' if hl else 'white', edgecolor=DRED if hl else GRAY, lw=1.3 if hl else 0.7, zorder=3))
        txt(ax, x, y, str(k), fs=7.5, bold=hl)
    for k, col, lab in [(0, BLUE, 'A'), (3, ORANGE, 'B')]:
        an = math.pi / 2 - 2 * math.pi * k / 12
        arrow(ax, (cx, cy), (cx + 0.75 * math.cos(an), cy + 0.75 * math.sin(an)), color=col, lw=2)
        txt(ax, cx + 0.45 * math.cos(an) + 0.12, cy + 0.45 * math.sin(an) + 0.05, lab, fs=9, color=col, bold=True)
    txt(ax, cx, 0.12, 'giây 0: A ở nấc 0, B ở nấc 3', fs=8, color=NAVY)
    x0, cw = 2.9, 0.36
    A = [(0 + 5 * t) % 12 for t in range(11)]
    B = [(3 + 2 * t) % 12 for t in range(11)]
    for j, (lab, vals, kind) in enumerate([('t', list(range(11)), 'navy'), ('A', A, 'done'), ('B', B, 'in')]):
        y = 2.3 - j * 0.4
        txt(ax, x0 - 0.12, y + 0.15, lab, fs=9, bold=True, ha='right', color=NAVY)
        for i, v in enumerate(vals):
            k = kind
            if j > 0 and A[i] == B[i]: k = 'ans'
            cell(ax, x0 + i * cw, y, cw - 0.03, 0.3, str(v), k, fs=8.5, lw=1.0 if k == 'ans' else None)
    txt(ax, x0, 0.95, 'Trùng nhau ở giây 1, 5, 9 (cách nhau m/g = 12/gcd(3, 12) = 4).', fs=8.3, ha='left', color=DRED, bold=True)
    txt(ax, x0, 0.62, 'A: p + 5t,  B: q + 2t  (mod 12).  Trùng ⇔ 3t ≡ 3 (mod 12).', fs=8.3, ha='left', color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'A ← p;  B ← q;  t ← 0', 0, 0)
    f.node('c', 'dec', 't < max(T + 1, m) ?', 0, -0.76)
    f.node('h', 'proc', 'nếu A = B: ghi giây đầu tiên;\nnếu thêm t ≤ T: đếm', 0, -1.6)
    f.node('m', 'proc', 'A ← (A + a) mod m;  B ← (B + b) mod m;  t ← t + 1', 0, -2.3)
    f.node('o', 'end', 'In first, cnt', 2.9, -0.76)
    f.edge('s', 'c'); f.edge('c', 'h', label='Đúng', lpos=(0.32, -1.22)); f.edge('h', 'm')
    f.edge('m', 'c', 'l', 'l', via=[(-2.95, -2.3), (-2.95, -0.76)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def reduce_fig(path):
    fig, ax = new(6.8, 1.6)
    steps = [('p + a·t ≡ q + b·t', 'in'), ('(a − b)·t ≡ q − p', 'done'), ('d·t ≡ e (mod m)', 'done'), ('t ≡ t₀ (mod m/g)', 'ans')]
    x = 0.1
    for i, (s, k) in enumerate(steps):
        w = 1.45
        cell(ax, x, 0.7, w, 0.45, s, k, fs=8.5, bold=k == 'ans')
        if i < 3:
            arrow(ax, (x + w + 0.02, 0.92), (x + w + 0.2, 0.92))
        x += w + 0.22
    txt(ax, 0.1 + 1.67 * 1.5 + 0.72, 0.42, 'd = (a − b) mod m,  e = (q − p) mod m', fs=8, color=NAVY)
    txt(ax, 0.1 + 1.67 * 3 + 0.72, 0.42, 'chỉ khi g = gcd(d, m) | e', fs=8, color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc m, p, a, q, b, T', 0, 0)
    f.node('d', 'proc', 'd ← (a − b) mod m;  e ← (q − p) mod m  (không âm)', 0, -0.6)
    f.node('g', 'proc', 'g ← extgcd(d, m, u, v)', 0, -1.2)
    f.node('c', 'dec', 'g | e ?', 0, -1.95)
    f.node('n', 'io', 'In −1 0', 2.2, -1.95)
    f.node('t', 'proc', 'M ← m/g;  t₀ ← (e/g mod M) · (u mod M) mod M   [__int128]', 0, -2.72)
    f.node('o', 'io', 'In t₀ và (t₀ > T ? 0 : (T − t₀)/M + 1)', 0, -3.32)
    f.edge('s', 'd'); f.edge('d', 'g'); f.edge('g', 'c'); f.edge('c', 'n', 'r', 'l', label='Sai')
    f.edge('c', 't', label='Đúng', lpos=(0.32, -2.4)); f.edge('t', 'o')
    f.draw(path)

def make(F):
    clock(F('clock')); naive_flow(F('naive')); reduce_fig(F('reduce')); opt_flow(F('opt'))
