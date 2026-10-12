from figlib import *

def grid(path):
    m, n = 4, 3
    bad = {(3, 2), (1, 1)}
    f = {}
    for x in range(m + 1):
        for y in range(n + 1):
            if (x, y) in bad: f[(x, y)] = 0; continue
            if x == 0 and y == 0: f[(x, y)] = 1; continue
            f[(x, y)] = f.get((x - 1, y), 0) + f.get((x, y - 1), 0)
    fig, ax = new(6.8, 3.0)
    s, ox, oy = 0.62, 0.6, 0.45
    P = lambda x, y: (ox + x * s, oy + y * s)
    for x in range(m + 1): line(ax, [P(x, 0), P(x, n)], color='#D9D9D9', lw=1)
    for y in range(n + 1): line(ax, [P(0, y), P(m, y)], color='#D9D9D9', lw=1)
    path_ = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3)]
    line(ax, [P(*p) for p in path_], color=DRED, lw=2.5, z=2)
    for x in range(m + 1):
        for y in range(n + 1):
            k = 'gray' if (x, y) in bad else ('ans' if (x, y) == (m, n) else 'done')
            fc, ec, _ = KIND[k]
            ax.add_patch(Circle(P(x, y), 0.17, facecolor=fc, edgecolor=ec, lw=1.2, zorder=4))
            txt(ax, *P(x, y), '✕' if (x, y) in bad else str(f[(x, y)]), fs=8.5, bold=(x, y) == (m, n), color=DRED if (x, y) in bad else '#1A1A1A')
    txt(ax, *P(1, 1), '', fs=1)
    tx = ox + m * s + 0.6
    txt(ax, tx, 2.45, 'Ô cấm: B(1, 1), A(3, 2)', fs=8.5, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 2.1, 'Tất cả: C(7, 3) = 35', fs=8.5, ha='left')
    txt(ax, tx, 1.8, 'Qua B: C(2,1)·C(5,3) = 20', fs=8.5, ha='left')
    txt(ax, tx, 1.5, 'Qua A: C(5,3)·C(2,1) = 20', fs=8.5, ha='left')
    txt(ax, tx, 1.2, 'Qua cả hai (B trước A): 2·3·2 = 12', fs=8.5, ha='left')
    txt(ax, tx, 0.8, '35 − 20 − 20 + 12 = 7', fs=9.5, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'f[0][0] ← 1', 0, 0)
    f.node('l', 'proc', 'với x = 0..m, y = 0..n:  ô cấm thì f = 0;\nngược lại f[x][y] ← f[x − 1][y] + f[x][y − 1]', 0, -0.7)
    f.node('o', 'end', 'In f[m][n]', 0, -1.4)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def venn(path):
    fig, ax = new(6.8, 1.9)
    pts = [('O', 0.3), ('B', 2.0), ('A', 3.9), ('T', 5.8)]
    for lab, x in pts:
        k = 'gray' if lab in 'AB' else 'done'
        fc, ec, _ = KIND[k]
        ax.add_patch(Circle((x, 1.1), 0.2, facecolor=fc, edgecolor=ec, lw=1.3, zorder=3))
        txt(ax, x, 1.1, lab, fs=10, bold=True)
    for (a, xa), (b, xb), lab in [(pts[0], pts[1], 'paths(O, B)'), (pts[1], pts[2], 'paths(B, A)'), (pts[2], pts[3], 'paths(A, T)')]:
        arrow(ax, (xa + 0.22, 1.1), (xb - 0.22, 1.1), color=NAVY)
        txt(ax, (xa + xb) / 2, 1.35, lab, fs=8, color=NAVY)
    txt(ax, 3.4, 0.55, 'Đường qua cả hai ô phải qua ô "trước" (nằm phía dưới bên trái) trước; quy tắc nhân cho tích ba đoạn.', fs=8.2, color=NAVY)
    txt(ax, 3.4, 0.25, 'Nếu hai ô không so sánh được (như (1, 0) và (0, 1)) thì không đường nào qua cả hai: paths = 0.', fs=8.2, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Bảng giai thừa tới 2·10⁶', 0, 0)
    f.node('a', 'proc', 'ans ← paths(O, T)', 0, -0.6)
    f.node('b', 'proc', 'mỗi ô cấm X:  ans −= paths(O, X) · paths(X, T)', 0, -1.2)
    f.node('c', 'proc', 'K = 2:  ans += paths(O, A)·paths(A, B)·paths(B, T) + paths(O, B)·paths(B, A)·paths(A, T)', 0, -1.8)
    f.node('o', 'end', 'In ans mod p (không âm)', 0, -2.4)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    grid(F('grid')); naive_flow(F('naive')); venn(F('venn')); opt_flow(F('opt'))
