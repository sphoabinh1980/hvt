from figlib import *

def stairs(path):
    fig, ax = new(7.4, 2.7)
    f = [1, 1, 0, 2, 0, 2, 4]
    bad = {2, 4}
    w, h = 0.85, 0.3
    for x in range(7):
        X = 0.3 + x * w; Y = 0.35 + x * h
        cell(ax, X, 0.35, w, Y - 0.35 + h, '', 'gray' if x in bad else ('ans' if x == 6 else 'done'), lw=1.0)
        txt(ax, X + w / 2, Y + h / 2, 'bậc %d' % x if x else 'đất', fs=7.5, color=GRAY if x in bad else '#1A1A1A')
        txt(ax, X + w / 2, 0.2, 'f = %d' % f[x], fs=8.5, bold=True, color=DRED if x == 6 else NAVY)
        if x in bad: txt(ax, X + w / 2, Y - 0.12, 'hỏng', fs=7.5, color=RED, bold=True)
    for (a, b, rad) in [(0, 1, -0.5), (1, 3, -0.4), (0, 3, -0.35), (3, 5, -0.4), (3, 6, -0.3), (5, 6, -0.5)]:
        arrow(ax, (0.3 + a * w + w / 2, 0.35 + a * h + h + 0.05), (0.3 + b * w + w / 2, 0.35 + b * h + h + 0.05), color=ORANGE, lw=1.0, rad=rad, ms=8)
    txt(ax, 6.7, 1.9, 'f[x] = f[x−1] + f[x−2] + f[x−3]', fs=8.6, ha='left', color=NAVY)
    txt(ax, 6.7, 1.6, 'nếu x hỏng thì f[x] = 0', fs=8.6, ha='left', color=RED)
    txt(ax, 6.7, 1.3, 'f[6] = 2 + 0 + 2 = 4', fs=8.6, ha='left', color=DRED, bold=True)
    save(fig, path)

def matrix(path):
    fig, ax = new(7.0, 1.5)
    def vec(x, items, k):
        for i, s in enumerate(items):
            cell(ax, x, 1.0 - i * 0.32, 1.0, 0.3, s, k, fs=8.5)
    vec(0.1, ['f[x+1]', 'f[x]', 'f[x−1]'], 'ans')
    txt(ax, 1.35, 0.68, '=', fs=13)
    M = [['1', '1', '1'], ['1', '0', '0'], ['0', '1', '0']]
    for i in range(3):
        for j in range(3):
            cell(ax, 1.6 + j * 0.4, 1.0 - i * 0.32, 0.38, 0.3, M[i][j], 'in', fs=9, bold=True)
    txt(ax, 2.95, 0.68, '·', fs=14)
    vec(3.15, ['f[x]', 'f[x−1]', 'f[x−2]'], 'done')
    txt(ax, 4.45, 1.1, 'Hàng 1: tổng ba số hạng.', fs=8.4, ha='left')
    txt(ax, 4.45, 0.8, 'Hàng 2, 3: dịch xuống một ô.', fs=8.4, ha='left')
    txt(ax, 4.45, 0.45, 'Đi e bậc liền không hỏng:  v ← Tᵉ · v', fs=8.6, ha='left', bold=True, color=DRED)
    txt(ax, 2.18, 1.45, 'T', fs=10, bold=True, color=ORANGE)
    save(fig, path)

def segments(path):
    fig, ax = new(7.4, 1.7)
    xs = [0.3, 2.3, 4.2, 6.9]
    labs = ['0', 'b₁', 'b₂', 'n']
    line(ax, [(0.2, 0.8), (7.1, 0.8)], color=GRAY, lw=1.5)
    for x, l in zip(xs, labs):
        ax.plot([x], [0.8], 'o', color=RED if l.startswith('b') else NAVY, ms=7, zorder=5)
        txt(ax, x, 0.55, l, fs=9.5, bold=True, color=RED if l.startswith('b') else NAVY)
    for (a, b, s) in [(0, 1, 'v ← T^(b₁ − 0) v'), (1, 2, 'v ← T^(b₂ − b₁) v'), (2, 3, 'v ← T^(n − b₂) v')]:
        arrow(ax, (xs[a] + 0.05, 1.0), (xs[b] - 0.05, 1.0), color=BLUE, rad=-0.25)
        txt(ax, (xs[a] + xs[b]) / 2, 1.42, s, fs=8.3, color=BLUE)
    for x in xs[1:3]:
        txt(ax, x, 0.25, 'v[0] ← 0', fs=8.3, color=RED, bold=True)
    txt(ax, 0.3, 0.25, 'v = (1, 0, 0)', fs=8.3, color=NAVY)
    txt(ax, 6.9, 0.25, 'đáp số v[0]', fs=8.3, color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đánh dấu bad[b];  f[0] ← 1', 0, 0)
    f.node('b', 'proc', 'với x = 1..n:  f[x] ← 0 nếu bad[x],\nngược lại f[x−1] + f[x−2] + f[x−3]', 0, -0.68)
    f.node('c', 'end', 'In f[n]', 0, -1.36)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc n, K, các bậc hỏng; sắp xếp tăng dần', 0, 0)
    f.node('b', 'proc', 'v ← (1, 0, 0);  cur ← 0', 0, -0.6)
    f.node('c', 'dec', 'còn bậc hỏng x ?', 0, -1.35)
    f.node('d', 'proc', 'v ← T^(x − cur) · v\nv[0] ← 0;  cur ← x', 3.0, -1.35)
    f.node('e', 'proc', 'v ← T^(n − cur) · v', 0, -2.15)
    f.node('g', 'end', 'In v[0]', 0, -2.75)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.edge('c', 'd', 'r', 'l', label='Đúng')
    f.edge('d', 'c', 't', 't', via=[(3.0, -0.95), (0, -0.95)])
    f.edge('c', 'e', label='Sai', lpos=(0.25, -1.88))
    f.edge('e', 'g')
    f.draw(path)

def make(F):
    stairs(F('stairs')); matrix(F('matrix')); segments(F('seg')); naive_flow(F('naive')); opt_flow(F('opt'))
