from figlib import *

def window(path):
    L, R = 100, 130
    fig, ax = new(6.9, 3.3)
    cw, x0 = 0.18, 0.75
    ps = [2, 3, 5, 7, 11]
    for i, x in enumerate(range(L, R + 1)):
        if x % 5 == 0 or x == R:
            txt(ax, x0 + i * cw + cw / 2, 3.1, str(x), fs=6.5, color=NAVY)
        cell(ax, x0 + i * cw, 2.8, cw - 0.02, 0.18, '', 'navy')
    dead = set()
    for k, p in enumerate(ps):
        y = 2.45 - k * 0.32
        txt(ax, x0 - 0.08, y + 0.12, 'p=%d' % p, fs=7.5, ha='right', color=NAVY, bold=True)
        start = max(p * p, (L + p - 1) // p * p)
        for i, x in enumerate(range(L, R + 1)):
            if x >= start and (x - start) % p == 0:
                k2 = 'ans' if x == start else 'pink'
                cell(ax, x0 + i * cw, y, cw - 0.02, 0.24, '', k2, lw=1.0 if k2 == 'ans' else 0.5)
                dead.add(x)
            else:
                cell(ax, x0 + i * cw, y, cw - 0.02, 0.24, '', 'plain', lw=0.3)
    y = 2.45 - 5 * 0.32 - 0.05
    txt(ax, x0 - 0.08, y + 0.12, 'còn lại', fs=7.5, ha='right', color=DRED, bold=True)
    for i, x in enumerate(range(L, R + 1)):
        if x not in dead:
            cell(ax, x0 + i * cw, y, cw - 0.02, 0.24, '', 'done', lw=1.2)
            txt(ax, x0 + i * cw + cw / 2, y - 0.16, str(x), fs=6.5, color=BLUE, bold=True)
    txt(ax, 3.45, 0.2, 'Ô vàng: ô bắt đầu max(p², ⌈L/p⌉·p). Số nguyên tố còn lại: 101, 103, 107, 109, 113, 127 (tổng 660).', fs=8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc L, R;  c ← 0;  s ← 0', 0, 0)
    f.node('l', 'proc', 'với x = L..R:  nếu isPrime(x) (thử chia 6k ± 1) thì c++, s += x', 0, -0.62)
    f.node('o', 'end', 'In c, s', 0, -1.24)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def startfig(path):
    fig, ax = new(6.6, 1.9)
    rows = [('p = 7', '⌈100/7⌉ · 7 = 15 · 7 = 105', 'p² = 49 < 105', '105'),
            ('p = 11', '⌈100/11⌉ · 11 = 10 · 11 = 110', 'p² = 121 > 110', '121'),
            ('p = 101 (nếu L ≤ 101 ≤ R)', '⌈L/p⌉ · p có thể = p', 'p² > p', 'không gạch p')]
    for i, (a, b, c, d) in enumerate(rows):
        y = 1.45 - i * 0.48
        cell(ax, 0.1, y, 1.55, 0.38, a, 'in', fs=7.2)
        cell(ax, 1.75, y, 2.3, 0.38, b, 'plain', fs=8)
        cell(ax, 4.15, y, 1.2, 0.38, c, 'plain', fs=8)
        cell(ax, 5.45, y, 1.05, 0.38, d, 'ans', fs=8, bold=True, lw=1.0)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng thường tới 10⁶ → danh sách pr', 0, 0)
    f.node('r', 'io', 'Đọc L, R;  mark[0..R − L] ← 0', 0, -0.6)
    f.node('a', 'proc', 'với p ∈ pr, p² ≤ R:  gạch j = max(p², ⌈L/p⌉·p), j + p, ... ≤ R  (ô j − L)', 0, -1.2)
    f.node('b', 'proc', 'nếu L = 1: gạch ô 0', 0, -1.8)
    f.node('c', 'proc', 'đếm và cộng các x có mark[x − L] = 0  (long long)', 0, -2.4)
    f.node('o', 'end', 'In c, s', 0, -3.0)
    for a, b in [('s', 'r'), ('r', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    window(F('window')); naive_flow(F('naive')); startfig(F('start')); opt_flow(F('opt'))
