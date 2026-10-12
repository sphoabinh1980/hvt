from figlib import *

def groups(path):
    fig, ax = new(7.6, 2.5)
    segs = [('1..9', '9 số × 1', 9, 'in'), ('10..99', '90 số × 2', 180, 'done'), ('100..999', '900 số × 3', 2700, 'green'), ('1000..9999', '9000 số × 4', 36000, 'purple')]
    widths = [0.7, 1.4, 2.6, 2.6]
    x = 0.1
    for (lab, sub, n, k), w in zip(segs, widths):
        cell(ax, x, 1.2, w - 0.04, 0.5, '%s chữ số' % format(n, ',').replace(',', ' '), k, fs=8.5, bold=True)
        txt(ax, x + w / 2, 1.88, lab, fs=8.5, color=NAVY, bold=True)
        txt(ax, x + w / 2, 0.98, sub, fs=7.5, color=GRAY)
        x += w
    txt(ax, x + 0.05, 1.45, '...', fs=12, ha='left')
    # vị trí k = 2026: 9 + 180 + 1837 với 1837/2700 của nhóm 3
    xk = 0.1 + 0.7 + 1.4 + 2.6 * 1837 / 2700
    arrow(ax, (xk, 0.55), (xk, 1.17), color=DRED, lw=1.6)
    txt(ax, xk, 0.38, 'k = 2026 = 9 + 180 + 1837', fs=8.5, color=DRED, bold=True)
    txt(ax, xk, 0.13, 'chữ số thứ 1837 của nhóm ba chữ số', fs=7.8, color=DRED)
    save(fig, path)

def inside(path):
    fig, ax = new(7.6, 1.9)
    txt(ax, 0.1, 1.72, 'Trong nhóm 3 chữ số: vị trí k = 1837 (đánh số từ 1)', fs=9, ha='left', bold=True, color=NAVY)
    nums = ['100', '101', '...', '711', '712', '713']
    x = 0.2
    for s in nums:
        if s == '...':
            txt(ax, x + 0.35, 1.08, '...', fs=12); x += 0.75; continue
        for j, ch in enumerate(s):
            hl = s == '712' and j == 0
            cell(ax, x + j * 0.3, 0.9, 0.28, 0.36, ch, 'ans' if hl else ('done' if s == '712' else 'plain'), fs=9, bold=hl)
        txt(ax, x + 0.45, 0.72, s, fs=7, color=GRAY)
        x += 1.05
    txt(ax, 3.9, 0.35, 'số thứ ⌊(1837 − 1)/3⌋ = 612 của nhóm (tính từ 0): 100 + 612 = 712;  vị trí (1837 − 1) mod 3 = 0: chữ số đầu của 712, là 7', fs=8, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc k;  x ← 1', 0, 0)
    f.node('b', 'dec', 'k ≤ len(x) ?', 0, -0.8)
    f.node('c', 'proc', 'k ← k − len(x);  x ← x + 1', 2.9, -0.8)
    f.node('d', 'end', 'In chữ số thứ k của x', 0, -1.7)
    f.edge('a', 'b'); f.edge('b', 'c', 'r', 'l', label='Sai'); f.edge('c', 'b', 't', 't', via=[(2.9, -0.35), (0, -0.35)])
    f.edge('b', 'd', label='Đúng', lpos=(0.3, -1.3))
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc k;  len ← 1;  cnt ← 9;  start ← 1', 0, 0)
    f.node('b', 'dec', 'k > len · cnt ?', 0, -0.85)
    f.node('c', 'proc', 'k ← k − len · cnt\nlen++;  cnt ← 10 cnt;  start ← 10 start', 3.3, -0.85)
    f.node('d', 'proc', 'num ← start + (k − 1) / len', 0, -1.8)
    f.node('e', 'end', 'In chữ số thứ (k − 1) mod len của num', 0, -2.4)
    f.edge('a', 'b'); f.edge('b', 'c', 'r', 'l', label='Đúng'); f.edge('c', 'b', 't', 't', via=[(3.3, -0.4), (0, -0.4)])
    f.edge('b', 'd', label='Sai', lpos=(0.25, -1.4)); f.edge('d', 'e')
    f.draw(path)

def make(F):
    groups(F('groups')); inside(F('inside')); naive_flow(F('naive')); opt_flow(F('opt'))
