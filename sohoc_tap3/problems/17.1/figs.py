from figlib import *

def column(ax, x0, top, bot, res, marks, op, title, mark_lab):
    c, W = 0.36, 6
    txt(ax, x0 + W * c / 2, 2.5, title, fs=8.6, bold=True, color=NAVY)
    txt(ax, x0 - 0.35, 2.12, mark_lab, fs=7.2, color=DRED, ha='right')
    for k in marks:
        txt(ax, x0 + k * c + c / 2, 2.12, '1' if op == '+' else '−1', fs=7.8, color=DRED, bold=True)
    for y, s in ((1.7, top), (1.3, bot)):
        for k, ch in enumerate(s.rjust(W)):
            if ch != ' ': cell(ax, x0 + k * c, y, c - 0.04, c - 0.04, ch, 'done', fs=8.8)
    txt(ax, x0 - 0.2, 1.47, op.replace('-', '−'), fs=11, color=NAVY, bold=True)
    line(ax, [(x0 - 0.3, 1.22), (x0 + W * c, 1.22)], color=NAVY, lw=1.1)
    for k, ch in enumerate(res.rjust(W)):
        if ch != ' ':
            lead = op == '-' and k == 0
            cell(ax, x0 + k * c, 0.78, c - 0.04, c - 0.04, ch, 'gray' if lead else 'ans', fs=8.8, bold=not lead)

def ops(path):
    fig, ax = new(7.4, 2.7)
    column(ax, 0.9, '98765', '4789', '103554', [0, 1, 2, 3, 4], '+', 'Cùng dấu: cộng, số nhớ 0 hoặc 1', 'nhớ')
    column(ax, 4.6, '100000', '1', '099999', [0, 1, 2, 3, 4], '-', 'Khác dấu: lớn trừ nhỏ, mượn lan xa', 'mượn')
    txt(ax, 4.6 + 0.16, 0.55, 'xóa 0 thừa', fs=7.5, color=GRAY)
    save(fig, path)

def cases(path):
    f = Flow()
    f.node('a', 'start', 'Tách dấu: a = ±A, b = ±B (A, B là xâu chữ số)', 0, 0)
    f.node('b', 'dec', 'cùng dấu ?', 0, -0.8)
    f.node('c', 'proc', 'kết quả = dấu chung + add(A, B)', 3.1, -0.8)
    f.node('d', 'dec', 'cmp(A, B)', 0, -1.85)
    f.node('e', 'proc', '0', -2.6, -1.85, w=0.6)
    f.node('g', 'proc', 'dấu của a + sub(A, B)', 0.0, -2.85)
    f.node('h', 'proc', 'dấu của b + sub(B, A)', 3.1, -1.85)
    f.edge('a', 'b')
    f.edge('b', 'c', 'r', 'l', label='Đúng')
    f.edge('b', 'd', label='Sai', lpos=(0.25, -1.3))
    f.edge('d', 'e', 'l', 'r', label='A = B')
    f.edge('d', 'h', 'r', 'l', label='A < B')
    f.edge('d', 'g', label='A > B', lpos=(0.4, -2.37))
    f.draw(path)

def make(F):
    ops(F('ops')); cases(F('cases'))
