from figlib import *
from math import comb

def lucas(path):
    fig, ax = new(7.6, 2.7)
    n, k, p = 1000, 500, 7
    def digs(x):
        d = []
        while x: d.append(x % p); x //= p
        return d[::-1]
    dn, dk = digs(n), digs(k)
    cw, x0 = 0.55, 1.5
    txt(ax, 0.1, 2.4, 'Bước 1 (Lucas, p = 7): viết n, k trong cơ số 7', fs=8.8, ha='left', bold=True, color=NAVY)
    for row, (lab, ds) in enumerate([('1000 =', dn), ('500 =', dk)]):
        y = 1.95 - row * 0.42
        txt(ax, x0 - 0.1, y + 0.16, lab, fs=8.5, ha='right', color=NAVY)
        for i, d in enumerate(ds):
            cell(ax, x0 + i * cw, y, cw - 0.04, 0.34, str(d), 'in' if row == 0 else 'done', fs=10, bold=True)
    y = 1.05
    for i, (a, b) in enumerate(zip(dn, dk)):
        cell(ax, x0 + i * cw - 0.05, y, cw + 0.06, 0.34, 'C(%d,%d)' % (a, b), 'plain', fs=7)
        txt(ax, x0 + i * cw + cw / 2 - 0.02, y - 0.17, '= %d' % comb(a, b), fs=7.5, color=GRAY)
    txt(ax, x0 + 4 * cw + 0.15, y + 0.17, '⇒ 2·20·2·20 = 1600 ≡ 4 (mod 7)', fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, 0.1, 0.62, 'Bước 2 (Trung Hoa): m = 30 = 2·3·5', fs=8.8, ha='left', bold=True, color=NAVY)
    for i, (p, r) in enumerate([(2, 0), (3, 0), (5, 2)]):
        cell(ax, 0.2 + i * 1.75, -0.05, 1.65, 0.32, 'C(10,5) ≡ %d (mod %d)' % (r, p), 'done', fs=8)
    txt(ax, 5.55, 0.11, '⇒ C(10, 5) ≡ 12 (mod 30)', fs=8.8, ha='left', color=DRED, bold=True)
    txt(ax, 5.55, -0.17, '(252 = 30·8 + 12)', fs=8, ha='left', color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc Q, m', 0, 0)
    f.node('a', 'proc', 'C[a][b] ← (C[a − 1][b − 1] + C[a − 1][b]) mod m,  a ≤ 2000', 0, -0.6)
    f.node('o', 'end', 'Mỗi truy vấn: in C[n][k] (0 nếu k > n)', 0, -1.2)
    f.edge('s', 'a'); f.edge('a', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Phân tích m = p₁·p₂···p_r (thử chia)', 0, 0)
    f.node('a', 'proc', 'mỗi pᵢ: bảng giai thừa và nghịch đảo giai thừa 0..pᵢ − 1', 0, -0.6)
    f.node('b', 'proc', 'eᵢ ← (m/pᵢ) · (m/pᵢ)⁻¹ mod pᵢ   (eᵢ ≡ 1 mod pᵢ, ≡ 0 mod pⱼ)', 0, -1.2)
    f.node('c', 'proc', 'mỗi truy vấn: rᵢ ← Lucas(n, k, pᵢ);   x ← Σ rᵢ · eᵢ  mod m', 0, -1.8)
    f.node('o', 'end', 'In x', 0, -2.4)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    lucas(F('lucas')); naive_flow(F('naive')); opt_flow(F('opt'))
