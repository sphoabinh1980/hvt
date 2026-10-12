from figlib import *
from math import gcd

def prefix(path):
    a = [12, 18, 7, 24, 30]
    n = len(a)
    L = [0] * (n + 2); R = [0] * (n + 2)
    for i in range(1, n + 1): L[i] = gcd(L[i - 1], a[i - 1])
    for i in range(n, 0, -1): R[i] = gcd(R[i + 1], a[i - 1])
    fig, ax = new(6.6, 3.1)
    cw, x0 = 0.62, 1.1
    def row(y, lab, vals, kinds, idx=range(0, n + 2)):
        txt(ax, x0 - 0.12, y + 0.17, lab, fs=8.5, ha='right', color=NAVY, bold=True)
        for j, (v, k) in enumerate(zip(vals, kinds)):
            cell(ax, x0 + j * cw, y, cw - 0.05, 0.34, v, k, fs=9.5)
    row(2.55, 'i', [str(i) for i in range(0, n + 2)], ['navy'] * (n + 2))
    row(2.15, 'a[i]', [''] + [str(x) for x in a] + [''], ['plain'] + ['in'] * n + ['plain'])
    row(1.7, 'L[i]', [str(x) for x in L[:n + 1]] + [''], ['gray'] + ['done'] * n + ['plain'])
    row(1.25, 'R[i]', [''] + [str(x) for x in R[1:]], ['plain'] + ['done'] * n + ['gray'])
    res = [''] + [str(gcd(L[i - 1], R[i + 1])) for i in range(1, n + 1)] + ['']
    kinds = ['plain'] + ['ans' if i == 3 else 'green' for i in range(1, n + 1)] + ['plain']
    row(0.75, 'bỏ a[i]', res, kinds)
    for (xa, ya) in [(2, 1.7), (4, 1.25)]:
        ax.add_patch(Rectangle((x0 + xa * cw - 0.03, ya - 0.03), cw + 0.01, 0.4, fill=False, edgecolor=DRED, lw=1.5, ls='--', zorder=6))
    txt(ax, x0 + (n + 2) * cw + 0.1, 0.92, 'bỏ a[3] = 7:\ngcd(L[2], R[4])\n= gcd(6, 6) = 6', fs=8, ha='left', color=DRED, bold=True)
    txt(ax, 3.3, 0.25, 'L[0] = R[n + 1] = 0 và gcd(0, x) = x: hai đầu dãy không cần xét riêng.', fs=8.5, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc dãy;  best ← −1;  i ← 1', 0, 0)
    f.node('c', 'dec', 'i ≤ n ?', 0, -0.72)
    f.node('g', 'proc', 'g ← gcd mọi a[j] với j ≠ i   (n − 1 lần gcd)', 0, -1.5)
    f.node('u', 'proc', 'nếu g > best: best ← g, idx ← i;   i ← i + 1', 0, -2.1)
    f.node('o', 'end', 'In best, idx', 2.5, -0.72)
    f.edge('s', 'c'); f.edge('c', 'g', label='Đúng', lpos=(0.32, -1.15)); f.edge('g', 'u')
    f.edge('u', 'c', 'l', 'l', via=[(-2.9, -2.1), (-2.9, -0.72)])
    f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc dãy a[1..n]', 0, 0)
    f.node('l', 'proc', 'L[0] ← 0;  L[i] ← gcd(L[i − 1], a[i]), i = 1..n', 0, -0.6)
    f.node('r', 'proc', 'R[n + 1] ← 0;  R[i] ← gcd(R[i + 1], a[i]), i = n..1', 0, -1.2)
    f.node('g', 'proc', 'với i = 1..n:  g ← gcd(L[i − 1], R[i + 1]);  giữ g lớn nhất (i nhỏ nhất)', 0, -1.8)
    f.node('o', 'end', 'In best, idx', 0, -2.4)
    for a, b in [('s', 'l'), ('l', 'r'), ('r', 'g'), ('g', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    prefix(F('prefix')); naive_flow(F('naive')); opt_flow(F('opt'))
