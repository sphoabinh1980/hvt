from figlib import *

def convert(path):
    fig, ax = new(7.6, 2.9)
    txt(ax, 0.1, 2.7, '① Horner: (7EA)₁₆ → giá trị', fs=9, ha='left', bold=True, color=NAVY)
    hs = [('7', '0 · 16 + 7 = 7'), ('E', '7 · 16 + 14 = 126'), ('A', '126 · 16 + 10 = 2026')]
    for i, (ch, s) in enumerate(hs):
        y = 2.2 - i * 0.48
        cell(ax, 0.15, y, 0.38, 0.38, ch, 'in', fs=10, bold=True)
        arrow(ax, (0.6, y + 0.19), (0.9, y + 0.19), color=GRAY)
        cell(ax, 0.95, y, 2.25, 0.38, 'v = ' + s, 'ans' if i == 2 else 'done', fs=8.6, bold=i == 2)
    txt(ax, 4.0, 2.7, '② Chia liên tiếp cho 8, đọc ngược số dư', fs=9, ha='left', bold=True, color=NAVY)
    ds = [(2026, 253, 2), (253, 31, 5), (31, 3, 7), (3, 0, 3)]
    for i, (v, q, r) in enumerate(ds):
        y = 2.2 - i * 0.48
        cell(ax, 4.0, y, 2.2, 0.38, '%d = 8 · %d + ' % (v, q), 'done', fs=8.6)
        cell(ax, 6.2, y, 0.42, 0.38, str(r), 'ans', fs=10, bold=True)
    arrow(ax, (6.85, 0.8), (6.85, 2.45), color=DRED, lw=1.5)
    txt(ax, 7.0, 1.6, 'đọc\nngược', fs=8, color=DRED, ha='left', bold=True)
    txt(ax, 5.3, 0.2, '(7EA)₁₆ = (3752)₈', fs=10, bold=True, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc a, b, S', 0, 0)
    f.node('b', 'proc', 'v ← 0;  với mỗi kí tự c của S:  v ← v · a + giá trị(c)', 0, -0.6)
    f.node('c', 'proc', 'ghi DIG[v mod b];  v ← v div b', 0, -1.3)
    f.node('d', 'dec', 'v > 0 ?', 0, -2.05)
    f.node('e', 'end', 'In các chữ số theo thứ tự ngược', 0, -2.85)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.edge('d', 'c', 'r', 'r', via=[(2.0, -2.05), (2.0, -1.3)], label='Đúng', lpos=(1.2, -1.93))
    f.edge('d', 'e', label='Sai', lpos=(0.25, -2.52))
    f.draw(path)

def make(F):
    convert(F('conv')); opt_flow(F('opt'))
