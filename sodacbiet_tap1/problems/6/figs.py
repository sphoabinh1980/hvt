from figlib import *

COL = ['ans', 'done', 'in', 'green', 'purple', 'yellow', 'pink', 'dblue', 'gray']

def chain(path):
    fig, ax = new(7.6, 1.6)
    seqs = [['987654321', '45', '9'], ['2026', '10', '1'], ['199', '19', '10', '1']]
    x0s = [0.1, 2.85, 5.35]
    for (seq, x0) in zip(seqs, x0s):
        x = x0
        for i, s in enumerate(seq):
            w = 0.18 + 0.1 * len(s)
            last = i == len(seq) - 1
            cell(ax, x, 0.8, w, 0.4, s, 'ans' if last else 'done', fs=9, bold=last)
            if not last:
                arrow(ax, (x + w + 0.03, 1.0), (x + w + 0.27, 1.0), color=GRAY)
            x += w + 0.3
    txt(ax, 3.8, 0.35, 'Mỗi mũi tên là một lần thay số bằng tổng các chữ số của nó; điểm dừng (ô vàng) là căn số.', fs=8.2, color=NAVY)
    save(fig, path)

def grid(path):
    fig, ax = new(7.6, 2.25)
    c = 0.62
    for x in range(1, 37):
        i, j = (x - 1) % 9, (x - 1) // 9
        d = 1 + (x - 1) % 9
        cell(ax, 0.6 + i * c, 1.75 - j * 0.38, c - 0.05, 0.33, str(x), COL[d - 1], fs=8.5)
    for i in range(9):
        txt(ax, 0.6 + i * c + c / 2 - 0.02, 2.2, 'căn %d' % (i + 1), fs=7.3, color=NAVY, bold=True)
    txt(ax, 6.6, 1.3, 'mỗi cột:\ncùng số dư\nkhi chia cho 9', fs=8, color=DRED, ha='left')
    save(fig, path)

def cast(path):
    fig, ax = new(7.6, 1.8)
    rows = [('2026', '2 + 0 + 2 + 6 = 10 → 1', '1'), ('× 4321', '4 + 3 + 2 + 1 = 10 → 1', '1'), ('= 8754346', '8+7+5+4+3+4+6 = 37 → 10 → 1', '1')]
    for i, (a, b, c) in enumerate(rows):
        y = 1.4 - i * 0.42
        txt(ax, 1.3, y, a, fs=10, ha='right', bold=True, family='monospace')
        txt(ax, 1.6, y, b, fs=8.6, ha='left')
        cell(ax, 4.6, y - 0.16, 0.38, 0.32, c, 'ans', fs=9.5, bold=True)
    txt(ax, 5.2, 1.2, '1 × 1 = 1 ✓', fs=9.5, ha='left', color=GREEN, bold=True)
    txt(ax, 5.2, 0.8, 'căn số của tích =', fs=8, ha='left', color=NAVY)
    txt(ax, 5.2, 0.55, 'căn số của (căn số × căn số)', fs=8, ha='left', color=NAVY)
    txt(ax, 3.8, 0.08, 'Phép thử bỏ chín: nếu hai vế khác căn số thì phép nhân chắc chắn sai (điều ngược lại không đúng).', fs=7.8, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R, d;  cnt ← 0', 0, 0)
    f.node('b', 'proc', 'với x = L..R:  y ← x;  khi y ≥ 10: y ← tổng chữ số của y\nnếu y = d thì cnt++', 0, -0.7)
    f.node('c', 'end', 'In cnt', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R, d', 0, 0)
    f.node('b', 'proc', 'dem(n) = 0 nếu n < d;  ngược lại (n − d) / 9 + 1', 0, -0.6)
    f.node('c', 'end', 'In dem(R) − dem(L − 1)', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def make(F):
    chain(F('chain')); grid(F('grid')); cast(F('cast')); naive_flow(F('naive')); opt_flow(F('opt'))
