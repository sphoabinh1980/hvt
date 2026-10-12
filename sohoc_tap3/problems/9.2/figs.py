from figlib import *

def horner(path):
    a, m, b = 2, 1000, '12345'
    fig, ax = new(6.8, 2.55)
    cw, x0 = 1.05, 1.35
    labs = ['chữ số d', 'phần đầu x', 'r = aˣ mod m', 'tính từ']
    for k, lab in enumerate(labs):
        txt(ax, x0 - 0.1, 2.12 - k * 0.45 + 0.16, lab, fs=8, ha='right', color=NAVY, bold=True)
    r = 1
    for i, c in enumerate(b):
        X = x0 + i * cw
        d = int(c)
        prev = r
        r = pow(r, 10, m) * pow(a, d, m) % m
        cell(ax, X, 2.12, cw - 0.06, 0.32, c, 'in', fs=10, bold=True)
        cell(ax, X, 1.67, cw - 0.06, 0.32, b[:i + 1], 'plain', fs=9)
        cell(ax, X, 1.22, cw - 0.06, 0.32, str(r), 'ans' if i == 4 else 'done', fs=9.5, bold=i == 4, lw=1.0 if i == 4 else None)
        cell(ax, X, 0.77, cw - 0.06, 0.32, '%d¹⁰ · 2%s' % (prev, '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]), 'plain', fs=7.5)
    txt(ax, 3.4, 0.3, 'a = 2, m = 1000, b = 12345:  a^(10x + d) = (aˣ)¹⁰ · aᵈ.  Đáp số 832.', fs=8.5, color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b, m  (b kiểu long long)', 0, 0)
    f.node('a', 'proc', 'r ← power(a, b, m)', 0, -0.6)
    f.node('o', 'end', 'In r', 0, -1.2)
    f.edge('s', 'a'); f.edge('a', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, xâu b, m;  a ← a mod m', 0, 0)
    f.node('p', 'proc', 'pw[d] ← aᵈ mod m  (d = 0..9);   r ← 1 mod m', 0, -0.6)
    f.node('c', 'dec', 'còn chữ số d ?', 0, -1.35)
    f.node('u', 'proc', 'r ← r¹⁰ · pw[d] mod m', 0, -2.15)
    f.node('o', 'end', 'In r', 2.5, -1.35)
    f.edge('s', 'p'); f.edge('p', 'c'); f.edge('c', 'u', label='Đúng', lpos=(0.32, -1.8))
    f.edge('u', 'c', 'l', 'l', via=[(-2.1, -2.15), (-2.1, -1.35)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    horner(F('horner')); naive_flow(F('naive')); opt_flow(F('opt'))
