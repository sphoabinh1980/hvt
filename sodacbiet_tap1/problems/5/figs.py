from figlib import *

def powtab(path):
    fig, ax = new(7.6, 2.75)
    ms = [3, 9, 11, 7, 13, 37]
    per = {3: 1, 9: 1, 11: 2, 7: 6, 13: 6, 37: 3}
    cw, ch = 0.58, 0.3
    X0, Y0 = 1.2, 2.3
    txt(ax, X0 - 0.55, Y0 + 0.17, 'm \\ k', fs=8, color=GRAY)
    for k in range(9):
        cell(ax, X0 + k * cw, Y0, cw - 0.03, ch, str(k), 'navy', fs=8.5, bold=True)
    for i, m in enumerate(ms):
        y = Y0 - (i + 1) * (ch + 0.04)
        txt(ax, X0 - 0.4, y + ch / 2, 'm = %d' % m, fs=8.5, bold=True, color=NAVY)
        for k in range(9):
            v = pow(10, k, m)
            kind = 'ans' if k < per[m] else 'done'
            cell(ax, X0 + k * cw, y, cw - 0.03, ch, str(v), kind, fs=8.5, bold=k < per[m])
        txt(ax, X0 + 9 * cw + 0.1, y + ch / 2, 'chu kì %d' % per[m], fs=8, ha='left', color=DRED)
    txt(ax, 3.8, 0.05, 'Bảng 10ᵏ mod m: ô vàng là một chu kì; sau đó các giá trị lặp lại mãi.', fs=8.2, color=NAVY)
    save(fig, path)

def prefix(path):
    fig, ax = new(7.6, 2.3)
    S = '2026202620'
    P = [0, 2, 6, 6, 3, 4, 5, 3, 1, 5, 1]
    cw = 0.56; X0 = 1.0
    txt(ax, 0.45, 1.85, 'i', fs=8.5, color=GRAY); txt(ax, 0.45, 1.45, 'S[i]', fs=8.5, color=GRAY); txt(ax, 0.45, 0.95, 'P[i]', fs=8.5, color=GRAY)
    for i in range(11):
        x = X0 + i * cw
        txt(ax, x + cw / 2, 1.85, str(i), fs=8, color=GRAY)
        if i > 0:
            cell(ax, x, 1.28, cw - 0.04, 0.34, S[i - 1], 'ans' if 2 <= i <= 5 else 'in', fs=9.5, bold=2 <= i <= 5)
        cell(ax, x, 0.78, cw - 0.04, 0.34, str(P[i]), 'ans' if i in (1, 5) else 'done', fs=9.5, bold=i in (1, 5))
    txt(ax, X0 + 11 * cw + 0.05, 1.45, '', fs=8)
    txt(ax, 3.8, 0.38, 'Đoạn [2, 5] = "0262":  (P[5] − P[1] · 10⁴) mod 7 = (4 − 2 · 4) mod 7 = −4 mod 7 = 3', fs=8.8, color=DRED, bold=True)
    txt(ax, 3.8, 0.1, 'Kiểm tra: 262 = 7 · 37 + 3.', fs=8.2, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc S, m, các truy vấn', 0, 0)
    f.node('b', 'proc', 'với mỗi truy vấn (l, r):  res ← 0\nvới i = l..r:  res ← (10 · res + S[i]) mod m', 0, -0.7)
    f.node('c', 'end', 'In res', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc S, m', 0, 0)
    f.node('b', 'proc', 'P[i] ← (10 · P[i − 1] + S[i]) mod m;   pw[i] ← 10 · pw[i − 1] mod m', 0, -0.6)
    f.node('c', 'io', 'Đọc truy vấn (l, r)', 0, -1.2)
    f.node('d', 'proc', 'res ← (P[r] − P[l − 1] · pw[r − l + 1]) mod m  (đưa về không âm)', 0, -1.8)
    f.node('e', 'end', 'In res', 0, -2.4)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.edge('e', 'c', 'r', 'r', via=[(3.55, -2.4), (3.55, -1.2)], label='truy vấn tiếp', lpos=(4.25, -1.8))
    f.draw(path)

def make(F):
    powtab(F('pow')); prefix(F('prefix')); naive_flow(F('naive')); opt_flow(F('opt'))
