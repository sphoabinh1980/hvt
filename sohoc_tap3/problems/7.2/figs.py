from figlib import *

def dots(path):
    fig, ax = new(6.8, 2.6)
    cw = 0.5
    def e(n, p):
        c = 0
        while n % p == 0: n //= p; c += 1
        return c
    for i, k in enumerate(range(1, 11)):
        x = 0.9 + i * cw
        cell(ax, x, 2.05, cw - 0.05, 0.3, str(k), 'navy', fs=8.5, bold=True)
        for j in range(e(k, 2)):
            ax.add_patch(Circle((x + 0.22, 1.85 - j * 0.17), 0.065, facecolor='#F4B183', edgecolor=ORANGE, lw=0.8))
        for j in range(e(k, 3)):
            ax.add_patch(Circle((x + 0.22, 1.1 - j * 0.17), 0.065, facecolor='#9DC3E6', edgecolor=BLUE, lw=0.8))
    txt(ax, 0.75, 1.68, 'thừa số 2', fs=8, ha='right', color=ORANGE, bold=True)
    txt(ax, 0.75, 1.02, 'thừa số 3', fs=8, ha='right', color=BLUE, bold=True)
    tx = 0.9 + 10 * cw + 0.2
    txt(ax, tx, 1.75, '8 chấm cam: 2⁸', fs=8.5, ha='left', color=ORANGE, bold=True)
    txt(ax, tx, 1.1, '4 chấm xanh: 3⁴', fs=8.5, ha='left', color=BLUE, bold=True)
    txt(ax, 3.4, 0.45, '12 = 2² · 3: mỗi chữ số 0 "tiêu" 2 chấm cam và 1 chấm xanh.  min(⌊8/2⌋, ⌊4/1⌋) = 4.', fs=8.5, color=DRED, bold=True)
    txt(ax, 3.4, 0.15, '10! = 2⁸ · 3⁴ · 5² · 7  viết trong hệ cơ số 12 có 4 chữ số 0 tận cùng.', fs=8.3, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, b', 0, 0)
    f.node('a', 'proc', 'f ← n!  (nhân 2 · 3 · ... · n)', 0, -0.6)
    f.node('b', 'proc', 'cnt ← 0;  trong khi b | f:  f ← f / b,  cnt ← cnt + 1', 0, -1.2)
    f.node('o', 'end', 'In cnt', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def legendre(path):
    fig, ax = new(6.8, 2.1)
    n, p = 2026, 3
    terms = []
    m = n
    while m: m //= p; terms.append(m)
    terms = terms[:-1]
    x = 0.2
    for i, t in enumerate(terms):
        cell(ax, x, 1.15, 0.85, 0.42, '⌊n/3%s⌋' % ('¹²³⁴⁵⁶⁷'[i]), 'navy', fs=8, bold=True)
        cell(ax, x, 0.7, 0.85, 0.42, str(t), 'done', fs=9.5)
        if i < len(terms) - 1: txt(ax, x + 0.92, 0.91, '+', fs=10, color=NAVY)
        x += 0.98
    cell(ax, x + 0.05, 0.7, 0.85, 0.42, '= %d' % sum(terms), 'ans', fs=9.5, bold=True)
    txt(ax, 3.4, 1.85, 'Số mũ của 3 trong 2026!: mỗi bội của 3 góp 1, mỗi bội của 9 góp thêm 1, ...', fs=8.5, color=NAVY)
    txt(ax, 3.4, 0.3, 'Cài đặt: while (n) { n /= p; s += n; }  — không bao giờ tính lũy thừa pᵏ (tránh tràn số).', fs=8.3, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, b;  ans ← ∞', 0, 0)
    f.node('a', 'proc', 'thử chia b cho p = 2, 3, ... khi p² ≤ b', 0, -0.6)
    f.node('c', 'dec', 'p | b ?', 0, -1.35)
    f.node('d', 'proc', 'k ← số mũ của p trong b\nans ← min(ans, ⌊e_p(n!) / k⌋)', 2.9, -1.35)
    f.node('e', 'proc', 'phần còn lại b > 1:  ans ← min(ans, e_b(n!))', 0, -2.2)
    f.node('o', 'end', 'In ans', 0, -2.8)
    f.edge('s', 'a'); f.edge('a', 'c'); f.edge('c', 'd', 'r', 'l', label='Đúng')
    f.edge('c', 'e', label='hết p', lpos=(0.45, -1.8), lcolor=NAVY); f.edge('e', 'o')
    f.draw(path)

def make(F):
    dots(F('dots')); naive_flow(F('naive')); legendre(F('legendre')); opt_flow(F('opt'))
