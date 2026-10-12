from figlib import *

def shift(path):
    fig, ax = new(6.6, 2.6)
    cw = 0.27
    def row(y, parts, label, kinds):
        txt(ax, 0.1, y + 0.16, label, fs=8.5, ha='left', color=NAVY, bold=True)
        x = 1.35
        for part, k in zip(parts, kinds):
            for ch in part:
                cell(ax, x, y, cw, 0.32, ch, k, fs=10)
                x += cw
            x += 0.04
        return x
    row(1.95, ['123456789'], 'đã viết (r):', ['done'])
    x = row(1.3, ['123456789', '00'], 'r · 10²:', ['done', 'gray'])
    txt(ax, x + 0.1, 1.46, '← dịch trái 2 chữ số', fs=8, color=GRAY, ha='left')
    x = row(0.65, ['123456789', '10'], 'r · 10² + 10:', ['done', 'ans'])
    txt(ax, x + 0.1, 0.81, '← "dán" số i = 10 vào', fs=8, color=DRED, ha='left')
    txt(ax, 3.3, 0.2, 'Viết thêm số i có k chữ số:  r ← r · 10ᵏ + i   (mọi phép tính lấy dư cho m)', fs=9, color=NAVY, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, m;  x ← 0;  i ← 1', 0, 0)
    f.node('c', 'dec', 'i ≤ n ?', 0, -0.72)
    f.node('p', 'proc', 'p ← 10^(số chữ số của i)', 0, -1.5)
    f.node('x', 'proc', 'x ← x · p + i;  i ← i + 1', 0, -2.1)
    f.node('o', 'end', 'In x mod m', 2.1, -0.72)
    f.edge('s', 'c'); f.edge('c', 'p', label='Đúng', lpos=(0.32, -1.18)); f.edge('p', 'x')
    f.edge('x', 'c', 'l', 'l', via=[(-1.75, -2.1), (-1.75, -0.72)])
    f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def memory(path):
    fig, ax = new(6.6, 2.5)
    groups = [('1–9', 9), ('10–99', 180), ('100–999', 2700), ('10³–10⁴−1', 36000), ('10⁴–10⁵−1', 450000),
              ('10⁵–10⁶−1', 5400000), ('10⁶–10⁷−1', 63000000), ('10⁷', 8)]
    tot = 0
    x0, sc = 0.25, 5.9 / 72e6
    y = 1.3
    for i, (lab, c) in enumerate(groups):
        w = c * sc
        if w > 0.004:
            cell(ax, x0 + tot * sc, y, w, 0.45, '', 'dblue' if i % 2 else 'done', lw=0.6)
        tot += c
    ax.plot([x0 + 64e6 * sc] * 2, [0.95, 2.05], color=DRED, lw=2, ls='--')
    txt(ax, x0 + 64e6 * sc, 2.2, 'giới hạn 64 MB', fs=8.5, color=DRED, bold=True)
    txt(ax, x0 + 57e6 * sc / 2 + 0.2, y + 0.22, '7 chữ số: 9 · 10⁶ số × 7 = 63 000 000 kí tự', fs=8, color=NAVY)
    txt(ax, x0, 1.08, 'tổng cộng: 68 888 897 kí tự', fs=8.5, color=NAVY, bold=True, ha='left')
    txt(ax, 3.3, 0.45, 'Xâu "1234...10⁷" dài 68 888 897 kí tự ≈ 69 MB > 64 MB: chưa kịp tính đã hết bộ nhớ.', fs=8.8, color='#1A1A1A')
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, m', 0, 0)
    f.node('i', 'proc', 'r ← 0;  p ← 10 mod m;  next ← 10;  i ← 1', 0, -0.6)
    f.node('c', 'dec', 'i ≤ n ?', 0, -1.32)
    f.node('d', 'dec', 'i = next ?', 0, -2.2)
    f.node('u', 'proc', 'p ← p · 10 mod m\nnext ← next · 10', 2.25, -2.2)
    f.node('x', 'proc', 'r ← (r · p + i) mod m;  i ← i + 1', 0, -3.05)
    f.node('o', 'end', 'In r', 2.25, -1.32)
    f.edge('s', 'i'); f.edge('i', 'c'); f.edge('c', 'd', label='Đúng', lpos=(0.32, -1.78))
    f.edge('d', 'u', 'r', 'l', label='Đúng'); f.edge('d', 'x', label='Sai', lpos=(0.3, -2.68))
    f.edge('u', 'x', 'b', 'r', via=[(2.25, -3.05)])
    f.edge('x', 'c', 'l', 'l', via=[(-2.1, -3.05), (-2.1, -1.32)])
    f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    shift(F('shift')); naive_flow(F('naive')); memory(F('memory')); opt_flow(F('opt'))
