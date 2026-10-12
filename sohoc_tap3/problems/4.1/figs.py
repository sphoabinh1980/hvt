from figlib import *

def jumps(path):
    fig, ax = new(6.6, 2.4)
    x0, sc = 0.3, 6.0 / 16
    def X(v): return x0 + v * sc
    line(ax, [(X(0), 0.9), (X(16), 0.9)], color=GRAY)
    for v in range(0, 17):
        ok = v % 2 == 0
        ax.add_patch(Circle((X(v), 0.9), 0.08, facecolor='#9DC3E6' if ok else '#EDEDED', edgecolor=BLUE if ok else '#A6A6A6', lw=0.8, zorder=3))
        txt(ax, X(v), 0.66, str(v), fs=7.5, color=NAVY if ok else GRAY)
    ax.add_patch(Circle((X(7), 0.9), 0.1, facecolor='#EDEDED', edgecolor=DRED, lw=1.5, zorder=4))
    txt(ax, X(7) + 0.3, 0.42, '7: không tới được', fs=7.5, color=DRED, bold=True)
    arrow(ax, (X(0), 1.05), (X(6), 1.05), color=GREEN, rad=-0.45, lw=1.3)
    txt(ax, X(3), 1.65, '+6', fs=8.5, color=GREEN, bold=True)
    arrow(ax, (X(6), 1.05), (X(2), 1.05), color=DRED, rad=-0.45, lw=1.3)
    txt(ax, X(4), 0.42, '−4', fs=8.5, color=DRED, bold=True)
    arrow(ax, (X(6), 1.05), (X(10), 1.05), color=GREEN, rad=-0.45, lw=1.3)
    txt(ax, X(8), 1.48, '+4', fs=8.5, color=GREEN, bold=True)
    txt(ax, 3.3, 2.15, 'Can 6 lít và 4 lít: mỗi thao tác là một bước ±6 hoặc ±4.', fs=8.8, color=NAVY)
    txt(ax, 3.3, 0.12, 'Mọi bước đều chẵn ⇒ chỉ tới được các bội của gcd(6, 4) = 2, và tới được tất cả.', fs=8.8, color=NAVY)
    save(fig, path)

def bfs_flow(path):
    f = Flow()
    f.node('s', 'start', 'seen[0] ← đúng;  hàng đợi ← {0}', 0, 0)
    f.node('c', 'dec', 'hàng đợi rỗng?', 0, -0.75)
    f.node('v', 'proc', 'lấy v;  với mỗi can x: w = v ± x\nnếu 0 ≤ w ≤ 4000 và chưa thăm: đánh dấu, đẩy w', 0, -1.65)
    f.node('o', 'end', 'g ← lượng dương nhỏ nhất đã thăm;\nmỗi c: CO nếu seen[c]', 3.4, -0.75)
    f.edge('s', 'c'); f.edge('c', 'v', label='Sai', lpos=(0.3, -1.2))
    f.edge('v', 'c', 'l', 'l', via=[(-2.9, -1.65), (-2.9, -0.75)])
    f.edge('c', 'o', 'r', 'l', label='Đúng')
    f.draw(path)

def chain(path):
    fig, ax = new(6.6, 2.1)
    def box(x, y, t, k='in', w=0.9):
        cell(ax, x, y, w, 0.42, t, k, fs=10, bold=True)
    box(0.2, 1.4, '6'); box(0.2, 0.5, '10'); box(2.3, 0.95, 'g = 2', 'done', 1.1)
    arrow(ax, (1.1, 1.61), (2.3, 1.25)); arrow(ax, (1.1, 0.71), (2.3, 1.05))
    box(2.4, 0.05, '15'); box(4.4, 0.5, 'g = 1', 'ans', 1.1)
    arrow(ax, (3.4, 1.16), (4.4, 0.81)); arrow(ax, (3.3, 0.26), (4.4, 0.62))
    txt(ax, 1.75, 1.75, '2 = 6 − 4 = 6·2 − 10', fs=8, color=GRAY)
    txt(ax, 4.2, 1.6, '1 = 2·8 − 15 = 6·16 − 10·8 − 15', fs=8, color=GRAY)
    txt(ax, 5.6, 0.71, '← nhỏ nhất', fs=8.5, color=DRED, bold=True, ha='left')
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'g ← 0', 0, 0)
    f.node('a', 'proc', 'với mỗi can a[i]:  g ← gcd(g, a[i])', 0, -0.6)
    f.node('o', 'io', 'In g', 0, -1.2)
    f.node('c', 'proc', 'với mỗi c:  in CO nếu c mod g = 0, ngược lại KHONG', 0, -1.8)
    for a, b in [('s', 'a'), ('a', 'o'), ('o', 'c')]: f.edge(a, b)
    f.draw(path)

def make(F):
    jumps(F('jumps')); bfs_flow(F('naive')); chain(F('chain')); opt_flow(F('opt'))
