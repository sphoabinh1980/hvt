from figlib import *

def seq(path):
    fig, ax = new(6.8, 2.3)
    cw, x0 = 0.5, 0.9
    for e in range(12):
        X = x0 + e * cw
        cell(ax, X, 1.6, cw - 0.04, 0.3, str(e), 'navy', fs=8.5, bold=True)
        v = pow(2, e, 12)
        kind = 'gray' if e < 2 else ('ans' if e in (2, 3) else 'done')
        cell(ax, X, 1.2, cw - 0.04, 0.34, str(v), kind, fs=9.5, lw=1.0 if kind == 'ans' else None)
    txt(ax, x0 - 0.08, 1.75, 'e', fs=8.5, ha='right', bold=True, color=NAVY)
    txt(ax, x0 - 0.08, 1.37, '2ᵉ mod 12', fs=8, ha='right', bold=True, color=NAVY)
    txt(ax, x0 + cw, 0.95, 'chưa tuần hoàn', fs=8, color=GRAY)
    txt(ax, x0 + 7 * cw, 0.95, 'chu kì 2 (là ước của φ(12) = 4)', fs=8, color=BLUE)
    txt(ax, 3.45, 0.55, 'Rút gọn "e mod φ(12)" sai ở e = 4k (cho 2⁰ = 1); đúng là dùng (e mod 4) + 4 khi e ≥ 4.', fs=8.3, color=DRED, bold=True)
    txt(ax, 3.45, 0.25, '2^(10¹⁸) mod 12: 10¹⁸ mod 4 = 0 → 2⁰⁺⁴ = 16 ≡ 4.', fs=8.3, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'v ← a_k', 0, 0)
    f.node('l', 'proc', 'i = k − 1 .. 1:  v ← a_i ^ v  (giá trị thật; 0⁰ = 1)', 0, -0.6)
    f.node('o', 'end', 'In v mod m', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def chain(path):
    fig, ax = new(7.4, 2.6)
    levels = [('a₁ = 2', 'mod 12'), ('a₂ = 10', 'mod φ(12) = 4'), ('a₃ = 18', 'mod φ(4) = 2')]
    for i, (a, m) in enumerate(levels):
        y = 2.0 - i * 0.65
        cell(ax, 0.3 + i * 0.4, y, 1.0, 0.42, a, 'in', fs=9.5, bold=True)
        cell(ax, 1.45 + i * 0.4, y, 1.45, 0.42, m, 'done', fs=8.5)
        if i < 2:
            arrow(ax, (0.8 + i * 0.4, y), (0.8 + (i + 1) * 0.4, y - 0.23), color=NAVY)
    tx = 4.0
    txt(ax, tx, 2.2, 'Tầng 3: E₃ = 18;  cần 10¹⁸ mod 4', fs=8.3, ha='left', color=NAVY)
    txt(ax, tx, 1.9, '  chặn thật của 18 ≥ φ(4) = 2 → dùng (18 mod 2) + 2 = 2', fs=8.3, ha='left')
    txt(ax, tx, 1.6, '  10² mod 4 = 0', fs=8.3, ha='left')
    txt(ax, tx, 1.25, 'Tầng 2: E₂ = 10¹⁸ (chặn: ≥ φ(12) = 4)', fs=8.3, ha='left', color=NAVY)
    txt(ax, tx, 0.95, '  → mũ dùng = (E₂ mod 4) + 4 = 0 + 4', fs=8.3, ha='left')
    txt(ax, tx, 0.55, 'Tầng 1: 2⁴ mod 12 = 4', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, 0.3, 0.2, 'Dãy mô-đun 12 → 4 → 2 → 1 về 1 rất nhanh.', fs=8.3, ha='left', color=GRAY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'solve(i, m): tháp aᵢ..a_k mod m', 0, 0)
    f.node('a', 'dec', 'm = 1 ?', 0, -0.72)
    f.node('a1', 'end', '0', 2.0, -0.72)
    f.node('b', 'dec', 'i = k ?', 0, -1.5)
    f.node('b1', 'end', 'a_k mod m', 2.1, -1.5)
    f.node('c', 'dec', 'E = cap[i + 1] < φ(m) ?', 0, -2.4)
    f.node('c1', 'end', 'aᵢ^E mod m', 2.9, -2.4)
    f.node('d', 'end', 'aᵢ ^ (solve(i + 1, φ(m)) + φ(m)) mod m', 0, -3.3)
    f.edge('s', 'a'); f.edge('a', 'a1', 'r', 'l', label='Đúng'); f.edge('a', 'b', label='Sai', lpos=(0.3, -1.12))
    f.edge('b', 'b1', 'r', 'l', label='Đúng'); f.edge('b', 'c', label='Sai', lpos=(0.3, -1.9))
    f.edge('c', 'c1', 'r', 'l', label='Đúng'); f.edge('c', 'd', label='Sai', lpos=(0.3, -2.95))
    f.draw(path)

def make(F):
    seq(F('seq')); naive_flow(F('naive')); chain(F('chain')); opt_flow(F('opt'))
