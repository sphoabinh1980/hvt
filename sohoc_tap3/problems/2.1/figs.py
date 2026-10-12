from figlib import *

def grids(path):
    fig, ax = new(6.6, 2.35)
    x = 0.2
    for r, c in [(2, 6), (3, 4), (4, 3), (6, 2)]:
        best = (r, c) == (3, 4)
        s = 0.22
        w, h = c * s, r * s
        y0 = 0.55 + (6 - r) * s / 2
        if best:
            ax.add_patch(Rectangle((x - 0.08, y0 - 0.08), w + 0.16, h + 0.16, facecolor='#FFF2CC', edgecolor=DRED, lw=1.6, zorder=1))
        for i in range(r):
            for j in range(c):
                ax.add_patch(Circle((x + j * s + s / 2, y0 + i * s + s / 2), 0.075, facecolor='#9DC3E6', edgecolor=BLUE, lw=0.8, zorder=3))
        txt(ax, x + w / 2, 0.3, '%d hàng × %d bạn' % (r, c), fs=8.5, color=DRED if best else NAVY, bold=best)
        if best:
            txt(ax, x + w / 2, 0.08, 'cân đối nhất', fs=8, color=DRED, italic=True)
        x += w + 0.55
    txt(ax, x + 0.1, 1.35, 'loại:\n1 × 12\n12 × 1', fs=8.5, color=GRAY, ha='left')
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n;  k ← 0;  d ← 1', 0, 0)
    f.node('c', 'dec', 'd ≤ n ?', 0, -0.72)
    f.node('m', 'dec', 'n mod d = 0 ?', 0, -1.6)
    f.node('u', 'proc', 'nếu 2 ≤ d ≤ n/2: k ← k + 1\nnếu d·d ≤ n: r ← d', 2.6, -1.6)
    f.node('i', 'proc', 'd ← d + 1', 0, -2.45)
    f.node('o', 'end', 'In k, r, n/r (hoặc 0)', 2.6, -0.72)
    f.edge('s', 'c'); f.edge('c', 'm', label='Đúng', lpos=(0.32, -1.1)); f.edge('m', 'u', 'r', 'l', label='Đúng')
    f.edge('m', 'i', label='Sai', lpos=(0.3, -2.1)); f.edge('u', 'i', 'b', 'r', via=[(2.6, -2.45)])
    f.edge('i', 'c', 'l', 'l', via=[(-1.6, -2.45), (-1.6, -0.72)])
    f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def pairs(path):
    fig, ax = new(6.6, 2.4)
    ds = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    x0, cw = 0.5, 0.62
    for i, d in enumerate(ds):
        kind = 'ans' if d == 6 else ('done' if d < 6 else 'in')
        cell(ax, x0 + i * cw, 0.85, cw - 0.08, 0.36, str(d), kind, fs=10, bold=d == 6)
    for i in range(4):
        a = x0 + i * cw + (cw - 0.08) / 2
        b = x0 + (8 - i) * cw + (cw - 0.08) / 2
        ax.add_patch(matplotlib.patches.Arc(((a + b) / 2, 1.21), b - a, 0.35 + 0.25 * (4 - i), theta1=0, theta2=180, color=NAVY, lw=1.1))
    txt(ax, x0 + 4 * cw + (cw - 0.08) / 2, 0.62, '6 · 6 = 36:\ntự bắt cặp', fs=7.5, color=DRED, bold=True)
    txt(ax, x0 + 1.5 * cw + 0.2, 0.62, 'd < √36: tăng dần', fs=8.5, color=BLUE)
    txt(ax, x0 + 6.5 * cw + 0.25, 0.62, 'n / d > √36: giảm dần', fs=8.5, color=ORANGE)
    txt(ax, 3.3, 0.18, '36 có 9 ước = 4 cặp + 1 ước tự bắt cặp; cách xếp cân đối nhất: r = 6 (ước cuối cùng gặp khi d ≤ √n)', fs=8.3, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n;  cnt ← 0;  d ← 1', 0, 0)
    f.node('c', 'dec', 'd · d ≤ n ?', 0, -0.74)
    f.node('m', 'dec', 'n mod d = 0 ?', 0, -1.62)
    f.node('u', 'proc', 'cnt ← cnt + (d·d = n ? 1 : 2)\nr ← d', 2.7, -1.62)
    f.node('i', 'proc', 'd ← d + 1', 0, -2.45)
    f.node('q', 'dec', 'cnt − 2 ≤ 0 ?', 3.0, -0.74)
    f.node('o1', 'io', 'In 0', 4.85, -0.74)
    f.node('o2', 'io', 'In cnt − 2, r, n / r', 3.0, 0.15)
    f.edge('s', 'c'); f.edge('c', 'm', label='Đúng', lpos=(0.32, -1.12)); f.edge('m', 'u', 'r', 'l', label='Đúng')
    f.edge('m', 'i', label='Sai', lpos=(0.3, -2.12)); f.edge('u', 'i', 'b', 'r', via=[(2.7, -2.45)])
    f.edge('i', 'c', 'l', 'l', via=[(-1.6, -2.45), (-1.6, -0.74)])
    f.edge('c', 'q', 'r', 'l', label='Sai')
    f.edge('q', 'o1', 'r', 'l', label='Đúng'); f.edge('q', 'o2', 't', 'b', label='Sai', lpos=(3.22, -0.25))
    f.draw(path)

import matplotlib
def make(F):
    grids(F('grids')); naive_flow(F('naive')); pairs(F('pairs')); opt_flow(F('opt'))
