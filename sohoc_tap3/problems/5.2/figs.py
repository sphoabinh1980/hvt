from figlib import *

def isp(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True

def tries(path):
    n = 98
    ps = [p for p in range(2, 20) if isp(p)]
    fig, ax = new(6.6, 2.2)
    cw = 0.78
    for i, p in enumerate(ps):
        q = n - p
        ok = isp(q)
        x = 0.15 + i * cw
        cell(ax, x, 1.4, cw - 0.06, 0.36, 'p = %d' % p, 'in', fs=8.5)
        f = next(d for d in range(2, q) if q % d == 0) if not ok else None
        cell(ax, x, 0.85, cw - 0.06, 0.45, '%d' % q + ('' if ok else '\n= %d·%d' % (f, q // f)), 'ans' if ok else 'gray', fs=8, bold=ok)
    txt(ax, 0.15, 1.95, 'n = 98: thử p nguyên tố tăng dần, kiểm tra q = n − p', fs=8.8, ha='left', color=NAVY, bold=True)
    txt(ax, 3.3, 0.45, 'Hầu hết q bị loại ngay bởi một ước nhỏ (2, 3, 5, 7...). Lần đầu q nguyên tố: p = 19.', fs=8, color=NAVY)
    txt(ax, 3.3, 0.18, 'Thứ tự p ≤ q tăng dần đảm bảo cặp tìm được có p nhỏ nhất.', fs=8, color=DRED)
    save(fig, path)

def parity(path):
    fig, ax = new(6.6, 2.0)
    rows = [('chẵn + chẵn', 'chẵn', 'chỉ có 2 + 2 = 4'), ('lẻ + lẻ', 'chẵn', 'mọi số nguyên tố > 2'), ('chẵn + lẻ', 'lẻ', 'p = 2 bắt buộc!')]
    for i, (a, b, c) in enumerate(rows):
        y = 1.45 - i * 0.48
        cell(ax, 0.2, y, 1.6, 0.38, 'p + q: ' + a, 'in', fs=8.5)
        txt(ax, 2.0, y + 0.19, '→', fs=11, color=NAVY)
        cell(ax, 2.2, y, 1.0, 0.38, b, 'done', fs=8.5, bold=True)
        cell(ax, 3.4, y, 3.0, 0.38, c, 'ans' if i == 2 else 'plain', fs=8.5, bold=i == 2, lw=1.0 if i == 2 else None)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n', 0, 0)
    f.node('c', 'dec', 'n lẻ ?', 0, -0.72)
    f.node('o', 'dec', 'n − 2 nguyên tố ?', 2.7, -0.72)
    f.node('o1', 'io', 'In 2, n − 2', 2.7, -1.6)
    f.node('o2', 'io', 'In −1', 4.6, -0.72)
    f.node('l', 'proc', 'p ← 2, 3, 4, ... ≤ n/2', 0, -1.55)
    f.node('t', 'dec', 'p nguyên tố  &&  n − p nguyên tố ?', 0, -2.4)
    f.node('o3', 'io', 'In p, n − p', 0, -3.25)
    f.edge('s', 'c'); f.edge('c', 'o', 'r', 'l', label='Đúng'); f.edge('o', 'o1', label='Đúng', lpos=(3.02, -1.2))
    f.edge('o', 'o2', 'r', 'l', label='Sai'); f.edge('c', 'l', label='Sai', lpos=(0.3, -1.15)); f.edge('l', 't')
    f.edge('t', 'o3', label='Đúng', lpos=(0.33, -2.88))
    f.edge('t', 'l', 'l', 'l', via=[(-2.3, -2.4), (-2.3, -1.55)], label='Sai', lpos=(-2.05, -2.25))
    f.draw(path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n', 0, 0)
    f.node('a', 'proc', 'sàng Eratosthenes trên [0, n]  (mảng n + 1 phần tử)', 0, -0.6)
    f.node('b', 'proc', 'p ← 2, 3, ..., n/2:  nếu p và n − p chưa bị gạch: in, dừng', 0, -1.2)
    f.node('o', 'end', 'không tìm thấy: in −1', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def make(F):
    tries(F('tries')); naive_flow(F('naive')); parity(F('parity')); opt_flow(F('opt'))
