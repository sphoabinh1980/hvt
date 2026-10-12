from figlib import *

def arcs(path):
    fig, ax = new(7.6, 2.4)
    S = [0, 2, -5, 0, 4, 1, 2]; d = [s % 3 for s in S]
    K = {0: 'ans', 1: 'done', 2: 'in'}
    X0, w = 0.9, 0.85
    txt(ax, 0.45, 0.95, 'i', fs=8, color=GRAY); txt(ax, 0.45, 0.62, 'Sᵢ', fs=8, color=GRAY); txt(ax, 0.45, 0.3, 'Sᵢ mod 3', fs=7.5, color=GRAY)
    for i in range(7):
        x = X0 + i * w
        txt(ax, x + 0.3, 0.95, str(i), fs=8.5, bold=True, color=NAVY)
        cell(ax, x, 0.48, 0.6, 0.28, str(S[i]), 'plain', fs=8.5)
        cell(ax, x, 0.16, 0.6, 0.28, str(d[i]), K[d[i]], fs=8.5, bold=True)
    for (a, b, col, lab) in [(0, 3, DRED, 'dư 0: [1, 3], dài 3'), (1, 6, ORANGE, 'dư 2: [2, 6], dài 5'), (2, 5, BLUE, 'dư 1: [3, 5], dài 3')]:
        arrow(ax, (X0 + a * w + 0.3, 1.1), (X0 + b * w + 0.3, 1.1), color=col, rad=-0.35 if b - a < 4 else -0.3, lw=1.3)
    txt(ax, X0 + 1.5 * w + 0.3, 1.62, 'dư 0: [1, 3], dài 3', fs=7.8, color=DRED, bold=True)
    txt(ax, X0 + 3.5 * w + 0.3, 2.02, 'dư 2: [2, 6], dài 5', fs=7.8, color=ORANGE, bold=True)
    txt(ax, X0 + 4.1 * w + 0.3, 1.32, 'dư 1: [3, 5]', fs=7.8, color=BLUE, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'first[·] ← −1;  first[0] ← 0;  s ← 0', 0, 0)
    f.node('b', 'proc', 'đọc a_r;  s ← ((s + a_r) mod k + k) mod k', 0, -0.6)
    f.node('c', 'dec', 'first[s] = −1 ?', 0, -1.35)
    f.node('d', 'proc', 'first[s] ← r', 2.9, -1.35)
    f.node('e', 'proc', 'nếu r − first[s] > bestLen:\ncập nhật bestLen, bestL ← first[s] + 1', 0, -2.25)
    f.node('g', 'end', 'Sau r = n: in 0 hoặc "bestLen bestL"', 0, -3.0)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.edge('c', 'd', 'r', 'l', label='Đúng')
    f.edge('c', 'e', label='Sai', lpos=(0.25, -1.85))
    f.edge('e', 'g')
    f.draw(path)

def make(F):
    arcs(F('arcs')); opt_flow(F('opt'))
