from figlib import *
from sympy import factorint

SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')

def table(path):
    xs = list(range(999999999990, 999999999996))
    fig, ax = new(6.9, 2.75)
    cw, x0 = 0.98, 1.0
    labs = ['x', 'p ≤ 10⁶ ghé qua', 'd tạm', 'phần còn lại', 'd(x)']
    for k, lab in enumerate(labs):
        txt(ax, x0 - 0.08, 2.35 - k * 0.45 + 0.17, lab, fs=7.5, ha='right', color=NAVY, bold=True)
    for i, x in enumerate(xs):
        f = factorint(x)
        small = [(p, e) for p, e in sorted(f.items()) if p <= 10**6]
        rest = 1
        for p, e in f.items():
            if p > 10**6: rest *= p ** e
        dt = 1
        for p, e in small: dt *= e + 1
        dfin = dt * (2 if rest > 1 else 1)
        X = x0 + i * cw
        cell(ax, X, 2.35, cw - 0.04, 0.34, '...%d' % (x % 1000), 'navy', fs=8, bold=True)
        parts = [('%d%s' % (p, str(e).translate(SUP) if e > 1 else '')) for p, e in small]
        s = ' · '.join(parts[:3]) + ('\n· ' + ' · '.join(parts[3:]) if len(parts) > 3 else '')
        cell(ax, X, 1.86, cw - 0.04, 0.42, s, 'in', fs=6.3)
        cell(ax, X, 1.45, cw - 0.04, 0.34, str(dt), 'done', fs=8.5)
        cell(ax, X, 1.0, cw - 0.04, 0.34, str(rest) if rest > 1 else '1', 'ans' if rest > 1 else 'gray', fs=7, lw=1.0 if rest > 1 else None)
        cell(ax, X, 0.55, cw - 0.04, 0.34, str(dfin), 'green', fs=8.5, bold=True)
    txt(ax, 3.45, 0.2, 'Ô vàng: phần còn lại > 1 không có ước ≤ 10⁶ nên là số nguyên tố (> 10⁶): nhân d với 2.', fs=8, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc L, R', 0, 0)
    f.node('l', 'proc', 'với x = L..R:  c ← số ước của x (duyệt k ≤ √x);  cộng dồn, giữ c lớn nhất', 0, -0.62)
    f.node('o', 'end', 'In tổng; in x có nhiều ước nhất', 0, -1.24)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng nhỏ tới 10⁶;  rest[i] ← L + i;  d[i] ← 1', 0, 0)
    f.node('a', 'proc', 'với p ∈ pr, p² ≤ R:  với mọi bội j của p trong [L, R]:\nchia rest[j − L] cho p tới hết (số mũ e);  d[j − L] ← d[j − L] · (e + 1)', 0, -0.72)
    f.node('b', 'proc', 'với mọi i: nếu rest[i] > 1 thì d[i] ← 2 · d[i]', 0, -1.45)
    f.node('o', 'end', 'In Σ d[i];  in x có d lớn nhất (x nhỏ nhất khi hòa)', 0, -2.05)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def make(F):
    table(F('table')); naive_flow(F('naive')); opt_flow(F('opt'))
