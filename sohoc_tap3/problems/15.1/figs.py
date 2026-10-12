from figlib import *

def tilings(n):
    if n == 0: return [[]]
    if n < 0: return []
    return [t + ['V'] for t in tilings(n - 1)] + [t + ['H'] for t in tilings(n - 2)]

def draw_tiling(ax, x0, y0, t, u=0.28, last=False):
    x = x0
    for i, b in enumerate(t):
        hl = last and i == len(t) - 1
        if b == 'V':
            cell(ax, x, y0, u, 2 * u, '', 'ans' if hl else 'done', lw=1.2); x += u
        else:
            cell(ax, x, y0 + u, 2 * u, u, '', 'ans' if hl else 'in', lw=1.2)
            cell(ax, x, y0, 2 * u, u, '', 'ans' if hl else 'in', lw=1.2); x += 2 * u

def gallery(path):
    fig, ax = new(7.6, 3.1)
    u = 0.24
    y = 2.45
    for n in range(1, 5):
        ts = tilings(n)
        txt(ax, 0.05, y + u, 'n = %d' % n, fs=9, ha='left', bold=True, color=NAVY)
        for k, t in enumerate(ts):
            draw_tiling(ax, 0.75 + k * (n * u + 0.3), y, t, u)
        txt(ax, 0.75 + len(ts) * (n * u + 0.3) + 0.05, y + u, '%d cách' % len(ts), fs=9, ha='left', color=DRED, bold=True)
        y -= 0.8
    save(fig, path)

def lastcol(path):
    fig, ax = new(7.4, 1.9)
    u = 0.3
    for k in range(4):
        cell(ax, 0.2 + k * u, 1.0, u, 2 * u, '', 'gray', lw=0.6)
    draw_tiling(ax, 0.2 + 4 * u, 1.0, ['V'], u, last=True)
    txt(ax, 0.2 + 2 * u, 1.0 + u, 'T(n − 1)', fs=9, bold=True)
    txt(ax, 0.95, 0.75, 'cột cuối là một viên dọc', fs=8.2, color=GRAY)
    X = 3.0
    for k in range(3):
        cell(ax, X + k * u, 1.0, u, 2 * u, '', 'gray', lw=0.6)
    draw_tiling(ax, X + 3 * u, 1.0, ['H'], u, last=True)
    txt(ax, X + 1.5 * u, 1.0 + u, 'T(n − 2)', fs=9, bold=True)
    txt(ax, X + 0.75, 0.75, 'hai viên ngang chồng nhau', fs=8.2, color=GRAY)
    txt(ax, 5.15, 1.45, 'T(n) = T(n − 1) + T(n − 2)', fs=10, ha='left', bold=True, color=DRED)
    txt(ax, 5.15, 1.1, 'T(1) = 1,  T(2) = 2', fs=9, ha='left')
    txt(ax, 5.15, 0.8, '⇒  T(n) = F(n + 1)', fs=9.5, ha='left', bold=True, color=NAVY)
    txt(ax, 3.7, 0.3, 'Một viên ngang đơn lẻ ở cột cuối để lại một ô trống bên trên/dưới, ô đó chỉ có thể là một viên ngang nữa.', fs=8, color=GRAY)
    save(fig, path)

def tree(path):
    fig, ax = new(7.4, 2.2)
    def node(x, y, n, d):
        rbox(ax, x - 0.22, y - 0.14, 0.44, 0.28, 'T(%d)' % n, 'in' if n in (3, 2) and d > 1 else 'done', fs=7.5)
        if n <= 1 or d == 3: return
        w = 1.75 / 2 ** d
        for c, dx in ((n - 1, -w), (n - 2, w)):
            line(ax, [(x, y - 0.14), (x + dx, y - 0.46)], color=GRAY, lw=0.8)
            node(x + dx, y - 0.6, c, d + 1)
    node(3.5, 2.2, 6, 0)
    txt(ax, 3.5, -0.02, 'Chỉ vẽ bốn tầng đầu. T(6) gọi T(4) hai lần, T(3) ba lần...: số lời gọi tăng như F(n), khoảng 1,6ⁿ.', fs=8.2, color=NAVY)
    save(fig, path)

def powsteps(path):
    fig, ax = new(7.4, 1.6)
    txt(ax, 0.05, 1.4, 'n = 10 = 1010₂:  R ← I, nhân dần theo bit từ thấp tới cao', fs=9, ha='left', bold=True, color=NAVY)
    items = [('bit 0 = 0', 'Q¹', 'R = I', 'plain'), ('bit 1 = 1', 'Q²', 'R = Q²', 'ans'), ('bit 2 = 0', 'Q⁴', 'R = Q²', 'plain'), ('bit 3 = 1', 'Q⁸', 'R = Q¹⁰', 'ans')]
    for i, (b, q, r, k) in enumerate(items):
        x = 0.1 + i * 1.8
        cell(ax, x, 0.75, 1.6, 0.32, b + ':  b = ' + q, 'done', fs=8.5)
        cell(ax, x, 0.4, 1.6, 0.32, r, k, fs=8.5, bold=k == 'ans')
    txt(ax, 3.7, 0.12, 'Q¹⁰ = [[89, 55], [55, 34]]  ⇒  T(10) = F(11) = 89', fs=9, color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc n', 0, 0)
    f.node('b', 'proc', 'R ← I;  B ← Q = [[1, 1], [1, 0]];  e ← n', 0, -0.6)
    f.node('c', 'dec', 'e > 0 ?', 0, -1.3)
    f.node('d', 'proc', 'nếu e lẻ: R ← R · B\nB ← B · B;  e ← e / 2', 2.6, -1.3)
    f.node('e', 'end', 'In R[0][0] = F(n + 1)', 0, -2.05)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.edge('c', 'd', 'r', 'l', label='Đúng')
    f.edge('d', 'c', 't', 't', via=[(2.6, -0.95), (0, -0.95)][:1] + [(0.0, -0.95)])
    f.edge('c', 'e', label='Sai', lpos=(0.25, -1.75))
    f.draw(path)

def make(F):
    gallery(F('gallery')); lastcol(F('lastcol')); tree(F('tree')); powsteps(F('pow')); opt_flow(F('opt'))
