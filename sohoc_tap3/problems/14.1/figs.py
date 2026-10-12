from figlib import *
from matplotlib.patches import Circle as Ci

def grid(path):
    fig, ax = new(6.8, 2.2)
    cw = 0.6
    for x in range(1, 31):
        i, j = (x - 1) % 10, (x - 1) // 10
        ab = x % 2 == 0 or x % 3 == 0
        c = x % 5 == 0
        k = ('gray' if c else 'ans') if ab else 'plain'
        cell(ax, 0.3 + i * cw, 1.6 - j * 0.48, cw - 0.06, 0.42, str(x), k, fs=9, bold=k == 'ans', lw=1.0 if k == 'ans' else None)
    txt(ax, 3.4, 0.1, 'Ô vàng: chia hết cho 2 hoặc 3 và không chia hết cho 5 (16 số). Ô xám: 10, 15, 20, 30 bị loại vì chia hết cho 5.', fs=8, color=NAVY)
    save(fig, path)

def venn(path):
    fig, ax = new(6.8, 2.9)
    for (x, y) in [(1.3, 1.75), (2.4, 1.75)]:
        ax.add_patch(Ci((x, y), 0.8, facecolor='#FFE699', edgecolor='none', zorder=1))
    ax.add_patch(Ci((1.85, 0.95), 0.8, facecolor='#E0E0E0', edgecolor='none', zorder=2))
    for (x, y, col) in [(1.3, 1.75, BLUE), (2.4, 1.75, ORANGE), (1.85, 0.95, GRAY)]:
        ax.add_patch(Ci((x, y), 0.8, fill=False, edgecolor=col, lw=1.5, zorder=3))
    txt(ax, 0.75, 2.4, 'A', fs=11, bold=True, color=BLUE); txt(ax, 2.95, 2.4, 'B', fs=11, bold=True, color=ORANGE); txt(ax, 1.85, 0.3, 'C', fs=11, bold=True, color=GRAY)
    txt(ax, 1.85, 2.15, 'vùng vàng: cần đếm', fs=8.5, bold=True, color=DRED)
    txt(ax, 1.85, 0.75, 'bị loại', fs=8.5, color=GRAY)
    tx = 3.95
    txt(ax, tx, 2.45, 'Cần: |(A ∪ B) \\ C| = |A ∪ B| − |(A ∪ B) ∩ C|', fs=9, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 2.05, '|A ∪ B| = ⌊N/a⌋ + ⌊N/b⌋ − ⌊N/lcm(a,b)⌋', fs=8.6, ha='left')
    txt(ax, tx, 1.65, '(A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C):', fs=8.6, ha='left')
    txt(ax, tx, 1.35, '  ⌊N/lcm(a,c)⌋ + ⌊N/lcm(b,c)⌋ − ⌊N/lcm(a,b,c)⌋', fs=8.6, ha='left')
    txt(ax, tx, 0.85, 'Đếm trên [L, R] = f(R) − f(L − 1)', fs=9, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc L, R, a, b, c;  cnt ← 0', 0, 0)
    f.node('l', 'proc', 'với x = L..R:  nếu (a | x hoặc b | x) và c ∤ x thì cnt++', 0, -0.6)
    f.node('o', 'end', 'In cnt', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Tính AB, AC, BC, ABC bằng lcm có chặn (> 10¹⁸ → INF)', 0, 0)
    f.node('a', 'proc', 'f(N) = N/a + N/b − N/AB − (N/AC + N/BC − N/ABC)', 0, -0.6)
    f.node('o', 'end', 'In f(R) − f(L − 1)', 0, -1.2)
    f.edge('s', 'a'); f.edge('a', 'o')
    f.draw(path)

def make(F):
    grid(F('grid')); naive_flow(F('naive')); venn(F('venn')); opt_flow(F('opt'))
