from figlib import *

def tree(path):
    a, m = 2, 1000
    def S(k):
        if k == 0: return 0, 1
        if k % 2:
            s, p = S(k - 1); return (1 + a * s) % m, p * a % m
        s, p = S(k // 2); return s * (1 + p) % m, p * p % m
    chain = [10, 5, 4, 2, 1, 0]
    fig, ax = new(6.9, 2.6)
    cw = 1.08
    for i, k in enumerate(chain):
        s, p = S(k)
        X = 0.15 + i * cw
        cell(ax, X, 1.7, cw - 0.2, 0.42, 'S(%d)' % k, 'ans' if k == 10 else 'done', fs=10, bold=True, lw=1.0 if k == 10 else None)
        txt(ax, X + (cw - 0.2) / 2, 1.45, '= %d' % s, fs=9, color=DRED if k == 10 else NAVY, bold=True)
        txt(ax, X + (cw - 0.2) / 2, 1.2, 'aᵏ = %d' % p, fs=8, color=GRAY)
        if i < len(chain) - 1:
            arrow(ax, (X + cw - 0.18, 1.91), (X + cw - 0.02, 1.91))
            txt(ax, X + cw - 0.1, 2.15, 'chẵn' if k % 2 == 0 else 'lẻ', fs=7.5, color=GREEN if k % 2 == 0 else ORANGE, bold=True)
    txt(ax, 3.45, 0.75, 'chẵn: S(2h) = S(h) · (1 + aʰ),  a²ʰ = (aʰ)²;     lẻ: S(k) = 1 + a · S(k − 1),  aᵏ = a · aᵏ⁻¹', fs=8.5, color=NAVY)
    txt(ax, 3.45, 0.42, 'a = 2, m = 1000:  1 + 2 + ... + 2⁹ = S(10) = 1023 ≡ 23', fs=8.5, color=DRED, bold=True)
    save(fig, path)

def split(path):
    fig, ax = new(6.9, 1.6)
    cw = 0.62
    terms = ['1', 'a', 'a²', 'a³', 'a⁴', 'a⁵', 'a⁶', 'a⁷']
    for i, t in enumerate(terms):
        cell(ax, 0.2 + i * cw, 0.95, cw - 0.05, 0.38, t, 'done' if i < 4 else 'in', fs=10)
    txt(ax, 0.2 + 2 * cw, 0.7, 'S(4)', fs=9, color=BLUE, bold=True)
    txt(ax, 0.2 + 6 * cw, 0.7, 'a⁴ · S(4)', fs=9, color=ORANGE, bold=True)
    txt(ax, 0.2 + 8 * cw + 0.2, 1.14, '⇒  S(8) = S(4) · (1 + a⁴)', fs=10, ha='left', color=DRED, bold=True)
    txt(ax, 3.45, 0.2, 'Nửa sau bằng nửa đầu nhân aʰ: không cần phép chia nào, nên đúng với MỌI mô-đun.', fs=8.5, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, n, m;  s ← 0;  p ← 1 mod m', 0, 0)
    f.node('l', 'proc', 'lặp n + 1 lần:  s ← (s + p) mod m;  p ← p · a mod m', 0, -0.6)
    f.node('o', 'end', 'In s', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'S(k): trả về (S(k), aᵏ)', 0, 0)
    f.node('z', 'dec', 'k = 0 ?', 0, -0.72)
    f.node('z1', 'end', '(0, 1 mod m)', 2.3, -0.72)
    f.node('o', 'dec', 'k lẻ ?', 0, -1.6)
    f.node('o1', 'proc', '(s, q) ← S(k − 1)\ntrả về (1 + a·s, q·a)', 2.6, -1.6)
    f.node('e', 'proc', '(s, q) ← S(k / 2);   trả về (s · (1 + q), q · q)', 0, -2.45)
    f.edge('s', 'z'); f.edge('z', 'z1', 'r', 'l', label='Đúng'); f.edge('z', 'o', label='Sai', lpos=(0.3, -1.12))
    f.edge('o', 'o1', 'r', 'l', label='Đúng'); f.edge('o', 'e', label='Sai', lpos=(0.3, -2.0))
    f.draw(path)

def make(F):
    tree(F('tree')); naive_flow(F('naive')); split(F('split')); opt_flow(F('opt'))
