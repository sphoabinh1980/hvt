from figlib import *

def line_fig(path):
    fig, ax = new(6.6, 3.0)
    ox, oy, sc = 1.3, 0.75, 0.165
    def P(x, y): return (ox + x * sc, oy + y * sc)
    for x in range(-6, 17):
        for y in range(-4, 11):
            ax.plot(*P(x, y), 'o', ms=1.2, color='#BFBFBF', zorder=1)
    ax.add_patch(Rectangle(P(0, 0), 16 * sc, 10 * sc, facecolor='#E2F0D9', edgecolor='none', alpha=0.6, zorder=0))
    line(ax, [P(-6, -4), P(16, -4)], color=GRAY, lw=0.6); 
    line(ax, [P(-6, 0), P(16.5, 0)], color=NAVY, lw=1.0); line(ax, [P(0, -4), P(0, 10.5)], color=NAVY, lw=1.0)
    txt(ax, *P(16.8, 0), 'x', fs=9, color=NAVY); txt(ax, *P(0, 11), 'y', fs=9, color=NAVY)
    line(ax, [P(-6, 48 / 5), P(16, -18 / 5)], color=BLUE, lw=1.3)
    for x, y in [(-5, 9), (0, 6), (5, 3), (10, 0), (15, -3)]:
        ok = x >= 0 and y >= 0
        px, py = P(x, y)
        ax.add_patch(Circle((px, py), 0.08, facecolor='#FFE699' if ok else '#EDEDED', edgecolor=DRED if ok else '#A6A6A6', lw=1.4 if ok else 1, zorder=4))
        txt(ax, px + 0.1, py + 0.17, '(%d, %d)' % (x, y), fs=7.5, color=DRED if ok else GRAY, ha='left', bold=ok)
    txt(ax, 4.9, 2.6, '3x + 5y = 30', fs=9, color=BLUE, bold=True)
    txt(ax, 4.9, 2.25, 'nghiệm cách đều: x tăng 5,', fs=8, color=NAVY)
    txt(ax, 4.9, 2.0, 'y giảm 3', fs=8, color=NAVY)
    txt(ax, 4.9, 1.55, '3 nghiệm trong góc', fs=8, color=GREEN, bold=True)
    txt(ax, 4.9, 1.3, 'x ≥ 0, y ≥ 0', fs=8, color=GREEN, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b, c;  cnt ← 0;  x ← 0', 0, 0)
    f.node('c', 'dec', 'a · x ≤ c ?', 0, -0.74)
    f.node('m', 'dec', '(c − a·x) mod b = 0 ?', 0, -1.62)
    f.node('u', 'proc', 'cnt ← cnt + 1', 2.6, -1.62)
    f.node('i', 'proc', 'x ← x + 1', 0, -2.45)
    f.node('o', 'end', 'In cnt', 2.3, -0.74)
    f.edge('s', 'c'); f.edge('c', 'm', label='Đúng', lpos=(0.32, -1.12)); f.edge('m', 'u', 'r', 'l', label='Đúng')
    f.edge('m', 'i', label='Sai', lpos=(0.3, -2.12)); f.edge('u', 'i', 'b', 'r', via=[(2.6, -2.45)])
    f.edge('i', 'c', 'l', 'l', via=[(-2.1, -2.45), (-2.1, -0.74)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def xaxis(path):
    fig, ax = new(6.6, 1.9)
    x0, sc = 0.4, 5.8 / 26
    def X(v): return x0 + (v + 5) * sc
    line(ax, [(X(-5), 0.95), (X(21), 0.95)], color=GRAY)
    for v in range(-5, 21):
        ax.plot([X(v)] * 2, [0.9, 1.0], color=GRAY, lw=0.7)
    for v in [-5, 0, 5, 10, 15, 20]:
        inside = 0 <= v <= 10
        kind = 'ans' if v == 0 else ('done' if inside else 'gray')
        fc, ec, _ = KIND[kind]
        ax.add_patch(Circle((X(v), 0.95), 0.09, facecolor=fc, edgecolor=ec, lw=1.4, zorder=4))
        txt(ax, X(v), 0.66, str(v), fs=8, color=NAVY if inside else GRAY, bold=inside)
    ax.plot([X(10)] * 2, [0.55, 1.4], color=DRED, ls='--', lw=1.2)
    txt(ax, X(10), 1.55, 'C/A = 10 (y = 0)', fs=8, color=DRED, bold=True)
    ax.plot([X(0)] * 2, [0.55, 1.4], color=GREEN, ls='--', lw=1.2)
    txt(ax, X(0), 1.55, 'x_min = x₀ mod B', fs=8, color=GREEN, bold=True)
    txt(ax, 3.3, 0.25, 'Số nghiệm = số bước nhảy B từ x_min mà vẫn ≤ C/A, cộng 1:  ⌊(C − A·x_min) / (A·B)⌋ + 1 = ⌊30/15⌋ + 1 = 3', fs=8.2, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b, c', 0, 0)
    f.node('e', 'proc', 'g ← extgcd(a, b, u, v)   (a·u + b·v = g)', 0, -0.6)
    f.node('d', 'dec', 'g | c ?', 0, -1.35)
    f.node('z', 'io', 'In 0', 2.2, -1.35)
    f.node('r', 'proc', 'A, B, C ← a/g, b/g, c/g;  x ← (C mod B)·(u mod B) mod B', 0, -2.12)
    f.node('k', 'dec', 'A · x ≤ C ?', 0, -2.92)
    f.node('o', 'io', 'In (C − A·x) / (A·B) + 1', 0, -3.72)
    f.node('z2', 'io', 'In 0', 2.6, -2.92)
    f.edge('s', 'e'); f.edge('e', 'd'); f.edge('d', 'z', 'r', 'l', label='Sai')
    f.edge('d', 'r', label='Đúng', lpos=(0.32, -1.8)); f.edge('r', 'k'); f.edge('k', 'o', label='Đúng', lpos=(0.32, -3.4))
    f.edge('k', 'z2', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    line_fig(F('line')); naive_flow(F('naive')); xaxis(F('xaxis')); opt_flow(F('opt'))
