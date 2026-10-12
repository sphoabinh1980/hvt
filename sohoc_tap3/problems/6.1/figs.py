from figlib import *

def isp(x):
    return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))

def arrays(path):
    N = 20
    fig, ax = new(6.8, 2.6)
    cw, x0 = 0.29, 0.95
    c = 0; cs = []
    for x in range(1, N + 1):
        c += isp(x); cs.append(c)
    rows = [('x', [str(x) for x in range(1, N + 1)], lambda x: 'navy'),
            ('', ['' for x in range(1, N + 1)], lambda x: 'done' if isp(x) else 'gray'),
            ('c[x]', [str(v) for v in cs], lambda x: 'ans' if x == 20 else 'plain')]
    for j, (lab, vals, kf) in enumerate(rows):
        y = 2.1 - j * 0.38
        txt(ax, x0 - 0.1, y + 0.15, lab if j != 1 else 'nguyên tố?', fs=8, ha='right', color=NAVY, bold=True)
        for i, v in enumerate(vals):
            x = i + 1
            k = kf(x)
            t = v if j != 1 else ('✓' if isp(x) else '')
            cell(ax, x0 + i * cw, y, cw - 0.02, 0.32, t, k, fs=7.5 if j == 0 else 8, lw=1.0 if k == 'ans' else None)
    ps = [x for x in range(2, N + 1) if isp(x)]
    txt(ax, x0 - 0.1, 0.72, 'pr[k−1]', fs=8, ha='right', color=NAVY, bold=True)
    for i, p in enumerate(ps):
        cell(ax, x0 + i * 0.45, 0.55, 0.42, 0.32, str(p), 'ans' if i == 6 else 'done', fs=8.5, lw=1.0 if i == 6 else None)
        txt(ax, x0 + i * 0.45 + 0.21, 0.42, 'k=%d' % (i + 1), fs=6.5, color=GRAY)
    txt(ax, x0 + 8 * 0.45 + 0.2, 0.71, '← "2 7" đọc pr[6] = 17', fs=8, ha='left', color=DRED, bold=True)
    txt(ax, x0 + N * cw + 0.08, 2.1 - 2 * 0.38 + 0.15, '← "1 20" đọc c[20] = 8', fs=8, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc truy vấn (t, x)', 0, 0)
    f.node('c', 'dec', 't = 1 ?', 0, -0.72)
    f.node('a', 'proc', 'đếm v = 2..x mà isPrime(v)', -2.0, -1.55)
    f.node('b', 'proc', 'tăng v tới khi gặp số nguyên tố thứ x', 2.0, -1.55)
    f.node('o', 'io', 'In kết quả', 0, -2.35)
    f.edge('s', 'c'); f.edge('c', 'a', 'l', 't', via=[(-2.0, -0.72)], label='Đúng', lpos=(-1.2, -0.62))
    f.edge('c', 'b', 'r', 't', via=[(2.0, -0.72)], label='Sai', lpos=(1.2, -0.62))
    f.edge('a', 'o', 'b', 'l', via=[(-2.0, -2.35)]); f.edge('b', 'o', 'b', 'r', via=[(2.0, -2.35)])
    f.draw(path)

def sieve(path):
    N = 30
    fig, ax = new(6.8, 2.5)
    cw, x0 = 0.61, 0.3
    killer = {}
    for p in (2, 3, 5):
        for j in range(p * p, N + 1, p):
            killer.setdefault(j, p)
    for x in range(1, N + 1):
        i, j = (x - 1) % 10, (x - 1) // 10
        y = 1.85 - j * 0.5
        if x == 1: k = 'gray'
        elif x in killer: k = {2: 'gray', 3: 'pink', 5: 'purple'}[killer[x]]
        else: k = 'done'
        cell(ax, x0 + i * cw, y, cw - 0.05, 0.42, str(x), k, fs=9, bold=k == 'done')
        if x in killer:
            txt(ax, x0 + i * cw + cw - 0.13, y + 0.32, '/%d' % killer[x], fs=6, color=GRAY)
    txt(ax, 3.3, 0.18, 'p = 2 gạch từ 4, p = 3 gạch từ 9, p = 5 gạch từ 25 (mỗi p bắt đầu ở p², vì bội nhỏ hơn đã bị gạch). 7² > 30: dừng.', fs=7.8, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Bắt đầu', 0, 0)
    f.node('a', 'proc', 'sàng Eratosthenes tới 10⁷', 0, -0.6)
    f.node('b', 'proc', 'x = 1..10⁷:  c[x] ← c[x − 1] + [x nguyên tố];  nguyên tố thì đẩy vào pr', 0, -1.2)
    f.node('c', 'dec', 'còn truy vấn (t, x)?', 0, -1.98)
    f.node('o', 'io', 'In  t = 1 ? c[x] : pr[x − 1]', 0, -2.8)
    f.node('e', 'end', 'Kết thúc', 2.8, -1.98)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'o', label='Đúng', lpos=(0.33, -2.45))
    f.edge('o', 'c', 'l', 'l', via=[(-2.4, -2.8), (-2.4, -1.98)]); f.edge('c', 'e', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    arrays(F('arrays')); naive_flow(F('naive')); sieve(F('sieve')); opt_flow(F('opt'))
