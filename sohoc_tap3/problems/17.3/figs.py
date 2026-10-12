from figlib import *

def grid(path):
    fig, ax = new(7.6, 3.0)
    x = [3, 2, 1]; y = [5, 4]           # 123, 45 (ô thấp nhất trước)
    c = 0.5; X0, Y0 = 1.0, 2.0
    kinds = ['ans', 'done', 'in', 'green']
    txt(ax, X0 - 0.45, Y0 + 0.75, 'y[j] \\ x[i]', fs=7.5, color=GRAY)
    for i in range(3):
        txt(ax, X0 + (2 - i) * c + c / 2, Y0 + 0.75, 'x[%d]=%d' % (i, x[i]), fs=7.5, color=NAVY, bold=True)
    for j in range(2):
        txt(ax, X0 - 0.4, Y0 + 0.25 - j * c, 'y[%d]=%d' % (j, y[j]), fs=7.5, color=NAVY, bold=True)
        for i in range(3):
            cell(ax, X0 + (2 - i) * c, Y0 - j * c, c - 0.05, c - 0.05, str(x[i] * y[j]), kinds[i + j], fs=9)
            txt(ax, X0 + (2 - i) * c + c - 0.11, Y0 - j * c + 0.08, 'k=%d' % (i + j), fs=5.5, color=GRAY)
    C = [15, 22, 13, 4]
    txt(ax, 3.2, 2.45, 'Cộng dồn theo cột k = i + j:', fs=8.6, ha='left', bold=True, color=NAVY)
    for k in range(4):
        cell(ax, 3.2 + (3 - k) * 0.65, 1.85, 0.6, 0.38, 'c[%d]=%d' % (k, C[k]), kinds[k], fs=8)
    txt(ax, 3.2, 1.45, 'Dồn nhớ một lượt từ c[0]:', fs=8.6, ha='left', bold=True, color=NAVY)
    steps = ['c[0] = 15 → 5, nhớ 1', 'c[1] = 22 + 1 = 23 → 3, nhớ 2', 'c[2] = 13 + 2 = 15 → 5, nhớ 1', 'c[3] = 4 + 1 = 5']
    for t, s in enumerate(steps):
        txt(ax, 3.3, 1.15 - t * 0.25, s, fs=8, ha='left')
    txt(ax, 6.6, 0.4, '5535', fs=12, bold=True, color=DRED)
    txt(ax, X0 + 0.7, 0.75, '123 × 45 trong cơ số 10', fs=8.5, color=GRAY)
    save(fig, path)

def bases(path):
    fig, ax = new(7.4, 1.9)
    rows = [('cơ số 10', '50 000 ô', '2,5 · 10⁹ phép nhân', 'quá chậm', 'pink'),
            ('cơ số 10⁴', '12 500 ô', '1,56 · 10⁸ phép nhân', 'c[k] ≤ 1,25 · 10¹²: an toàn', 'green'),
            ('cơ số 10⁹', '5 556 ô', '3,1 · 10⁷ phép nhân', 'c[k] tới 5,6 · 10²¹: tràn', 'pink')]
    ws = [1.1, 1.0, 2.0, 2.9]
    hdr = ['Cơ số', 'Số ô', 'Số phép nhân', 'Cộng dồn c[k]']
    x = 0.1
    for c, h in enumerate(hdr):
        cell(ax, x, 1.45, ws[c], 0.32, h, 'navy', fs=8.5, bold=True); x += ws[c]
    for r, row in enumerate(rows):
        x = 0.1
        for c in range(4):
            cell(ax, x, 1.1 - r * 0.34, ws[c], 0.32, row[c], row[4] if c == 3 or c == 0 else 'plain', fs=8.3, bold=c == 0); x += ws[c]
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Tách dấu; cắt |a|, |b| thành khối 4 chữ số từ cuối', 0, 0)
    f.node('b', 'proc', 'c[i + j] += x[i] · y[j]  với mọi i, j', 0, -0.6)
    f.node('c', 'proc', 'dồn nhớ: c[k+1] += c[k] / 10⁴;  c[k] %= 10⁴', 0, -1.2)
    f.node('d', 'dec', 'tích = 0 ?', 0, -1.95)
    f.node('e', 'end', 'In 0', 2.6, -1.95)
    f.node('g', 'end', 'In dấu (nếu khác dấu), ô cao nhất,\ncác ô sau bằng %04lld', 0, -2.85)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.edge('d', 'e', 'r', 'l', label='Đúng')
    f.edge('d', 'g', label='Sai', lpos=(0.25, -2.42))
    f.draw(path)

def make(F):
    grid(F('grid')); bases(F('bases')); opt_flow(F('opt'))
