from figlib import *

def bits(ax, x, y, s, kinds, c=0.34):
    for i, ch in enumerate(s):
        cell(ax, x + i * c, y, c - 0.03, c - 0.03, ch, kinds[i], fs=9, bold=ch in '01' and kinds[i] == 'ans')

def count(path):
    fig, ax = new(7.6, 2.7)
    txt(ax, 0.1, 2.5, 'Đếm x ≤ 12 = (1100)₂ có đúng k = 2 bit 1', fs=9, ha='left', bold=True, color=NAVY)
    rows = [('n =', '1100', ['done'] * 4, '', ''),
            ('nhóm bit 3:', '0***', ['ans', 'gray', 'gray', 'gray'], 'C(3, 2) = 3', '3, 5, 6'),
            ('nhóm bit 2:', '10**', ['done', 'ans', 'gray', 'gray'], 'C(2, 1) = 2', '9, 10'),
            ('chính n:', '1100', ['done'] * 4, 't = k = 2 → 1', '12')]
    for r, (lab, s, k, f, ex) in enumerate(rows):
        y = 1.9 - r * 0.48
        txt(ax, 1.5, y + 0.15, lab, fs=8.5, ha='right', color=NAVY)
        bits(ax, 1.65, y, s, k)
        txt(ax, 3.2, y + 0.15, f, fs=8.6, ha='left', bold=r > 0, color=DRED if r > 0 else '#1A1A1A')
        txt(ax, 4.9, y + 0.15, ex, fs=8.4, ha='left', color=GRAY)
    txt(ax, 6.6, 0.55, 'g(12) = 6', fs=10, bold=True, color=DRED)
    txt(ax, 3.9, 0.12, 'Ô vàng: bit 1 của n được đổi thành 0; dấu * : chọn tùy ý (cần đủ k − t bit 1).', fs=7.8, color=GRAY)
    save(fig, path)

def kth(path):
    fig, ax = new(7.6, 2.5)
    txt(ax, 0.1, 2.3, 'Số thứ m = 4 có k = 2 bit 1 (xét 4 bit thấp)', fs=9, ha='left', bold=True, color=NAVY)
    hdr = ['bit i', 'cần k\'', 'C(i, k\') = số cách nếu bit i = 0', 'm', 'quyết định']
    rows = [['3', '2', 'C(3, 2) = 3', '4 > 3', 'bit 3 = 1;  m ← 1, k\' ← 1'],
            ['2', '1', 'C(2, 1) = 2', '1 ≤ 2', 'bit 2 = 0'],
            ['1', '1', 'C(1, 1) = 1', '1 ≤ 1', 'bit 1 = 0'],
            ['0', '1', 'C(0, 1) = 0', '1 > 0', 'bit 0 = 1;  m ← 1, k\' ← 0']]
    ws = [0.6, 0.65, 2.45, 0.8, 2.4]
    x = 0.2
    for c, h in enumerate(hdr):
        cell(ax, x, 1.75, ws[c], 0.3, h, 'navy', fs=8, bold=True); x += ws[c]
    for r, row in enumerate(rows):
        x = 0.2
        for c, v in enumerate(row):
            k = ('ans' if row[4].startswith('bit %s = 1' % row[0]) else 'plain') if c == 4 else 'plain'
            cell(ax, x, 1.43 - r * 0.32, ws[c], 0.3, v, k, fs=8, bold=c == 4 and k == 'ans'); x += ws[c]
    txt(ax, 3.8, 0.1, 'x = (1001)₂ = 9', fs=10, bold=True, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Dựng C[i][j] bằng tam giác Pascal (i ≤ 61)', 0, 0)
    f.node('b', 'dec', 'loại câu hỏi', 0, -0.8)
    f.node('c', 'proc', 'g(n): duyệt bit i từ 60 xuống;\nbit 1 → s += C(i, k − t), t++;\ncuối cùng nếu t = k thì s++', -2.6, -1.9)
    f.node('d', 'proc', 'dựng x từ bit 59 xuống:\nnếu m > C(i, k\') thì bật bit i,\nm −= C(i, k\'), k\'−−', 2.6, -1.9)
    f.node('e', 'end', 'In g(R) − g(L − 1)', -2.6, -2.85)
    f.node('g', 'end', 'In x', 2.6, -2.85)
    f.edge('a', 'b')
    f.edge('b', 'c', 'l', 't', via=[(-2.6, -0.8)], label='loại 1', lpos=(-1.6, -0.68))
    f.edge('b', 'd', 'r', 't', via=[(2.6, -0.8)], label='loại 2', lpos=(1.6, -0.68))
    f.edge('c', 'e'); f.edge('d', 'g')
    f.draw(path)

def make(F):
    count(F('count')); kth(F('kth')); opt_flow(F('opt'))
