from figlib import *

def place(path):
    fig, ax = new(7.4, 1.9)
    ds = '2026'; labs = ['nghìn\n10³', 'trăm\n10²', 'chục\n10¹', 'đơn vị\n10⁰']
    for i, (d, l) in enumerate(zip(ds, labs)):
        x = 0.5 + i * 0.9
        cell(ax, x, 0.95, 0.75, 0.55, d, 'in', fs=15, bold=True)
        txt(ax, x + 0.375, 0.55, l, fs=7.8, color=GRAY)
    txt(ax, 4.3, 1.35, '2026 = 2 · 10³ + 0 · 10² + 2 · 10¹ + 6 · 10⁰', fs=10, ha='left', bold=True, color=NAVY)
    txt(ax, 4.3, 0.95, 'chữ số hàng đơn vị = 2026 mod 10 = 6', fs=9, ha='left')
    txt(ax, 4.3, 0.65, 'bỏ chữ số hàng đơn vị: ⌊2026 / 10⌋ = 202', fs=9, ha='left')
    save(fig, path)

def tach(path):
    fig, ax = new(7.6, 1.75)
    ys = [2026, 202, 20, 2, 0]
    for i, y in enumerate(ys):
        x = 0.2 + i * 1.55
        cell(ax, x, 0.95, 0.95, 0.45, str(y), 'done' if y else 'gray', fs=11, bold=True)
        if i < 4:
            arrow(ax, (x + 0.98, 1.17), (x + 1.52, 1.17), color=GRAY)
            txt(ax, x + 1.25, 1.36, '/ 10', fs=7.5, color=GRAY)
            cell(ax, x + 0.25, 0.25, 0.45, 0.4, str(y % 10), 'ans', fs=11, bold=True)
            arrow(ax, (x + 0.475, 0.93), (x + 0.475, 0.68), color=DRED)
            txt(ax, x + 0.8, 0.8, '% 10', fs=7.5, color=DRED)
    txt(ax, 6.4, 0.45, 'các chữ số lấy ra:\n6, 2, 0, 2\n(từ phải sang trái)', fs=8, color=DRED, ha='left')
    save(fig, path)

def cot(path):
    fig, ax = new(7.6, 3.3)
    c, h = 0.3, 0.24
    for blk in range(3):
        X0 = 0.35 + blk * 2.5
        for r in range(10):
            x = blk * 10 + r
            y = 3.0 - (r + 1) * h
            s = '%02d' % x
            cell(ax, X0, y, c, h - 0.02, s[0], 'in' if s[0] != '0' else 'gray', fs=8)
            cell(ax, X0 + c, y, c, h - 0.02, s[1], 'done', fs=8)
            txt(ax, X0 + 2 * c + 0.12, y + h / 2, str(x), fs=7, color=GRAY, ha='left')
    txt(ax, 0.35, 3.1, 'chục  đơn vị', fs=7.5, color=NAVY, ha='left')
    txt(ax, 3.8, 0.3, 'Cột đơn vị: 0, 1, ..., 9 lặp lại mỗi 10 số.   Cột chục: 10 số 0, 10 số 1, 10 số 2, ... lặp lại mỗi 100 số.', fs=8.2, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc n;  S ← 0', 0, 0)
    f.node('b', 'proc', 'với x = 1, 2, ..., n:\ny ← x;  khi y > 0:  S += y mod 10;  y ← y / 10', 0, -0.7)
    f.node('c', 'end', 'In S', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc n;  S ← 0;  p ← 1', 0, 0)
    f.node('b', 'dec', 'p ≤ n ?', 0, -0.75)
    f.node('c', 'proc', 'high ← n / (10p);  cur ← (n / p) mod 10;  low ← n mod p\nS += 45 · high · p + p · cur(cur − 1)/2 + cur · (low + 1)\np ← 10p', 0, -1.75)
    f.node('d', 'end', 'In S', 2.6, -0.75)
    f.edge('a', 'b')
    f.edge('b', 'c', label='Đúng', lpos=(0.3, -1.2))
    f.edge('c', 'b', 'l', 'l', via=[(-3.25, -1.75), (-3.25, -0.75)])
    f.edge('b', 'd', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    place(F('place')); tach(F('tach')); cot(F('cot')); naive_flow(F('naive')); opt_flow(F('opt'))
