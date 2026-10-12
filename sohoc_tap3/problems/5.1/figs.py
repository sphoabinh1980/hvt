from figlib import *

def loang(path):
    fig, ax = new(6.6, 2.3)
    x0, cw = 0.25, 0.47
    order = {26: 1, 25: 2, 27: 3, 24: 4, 28: 5, 23: 6}
    pr = {19, 23, 29, 31}
    for i, v in enumerate(range(20, 33)):
        x = x0 + i * cw
        if v == 23: k = 'ans'
        elif v in order: k = 'gray'
        elif v in pr: k = 'done'
        else: k = 'plain'
        cell(ax, x, 1.05, cw - 0.05, 0.4, str(v), k, fs=9.5, bold=v in (23, 26))
        if v in order:
            ax.add_patch(Circle((x + cw / 2 - 0.025, 1.68), 0.12, facecolor='white', edgecolor=NAVY, lw=1))
            txt(ax, x + cw / 2 - 0.025, 1.68, str(order[v]), fs=8, bold=True, color=NAVY)
    txt(ax, x0 + 6 * cw + cw / 2, 0.78, 'n = 26', fs=8.5, color=NAVY, bold=True)
    for d in range(4):
        txt(ax, x0 + 6.5 * cw, 2.12 - 0, '', fs=1)
    txt(ax, 3.3, 2.1, 'Thứ tự kiểm tra: d = 0, 1, 2, 3; mỗi d xét n − d trước n + d.', fs=8.5, color=NAVY)
    txt(ax, 3.3, 0.45, 'Số nguyên tố đầu tiên gặp được là 23 (d = 3): cũng là số nhỏ hơn nếu có hai số cách đều.', fs=8.3, color=DRED)
    txt(ax, 3.3, 0.18, 'Ô xanh: số nguyên tố chưa cần xét (29 cũng cách 26 ba đơn vị nhưng xét sau 23).', fs=8, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n;  d ← 0', 0, 0)
    f.node('a', 'dec', 'n − d nguyên tố?', 0, -0.78)
    f.node('o1', 'io', 'In n − d', 2.7, -0.78)
    f.node('b', 'dec', 'n + d nguyên tố?', 0, -1.75)
    f.node('o2', 'io', 'In n + d', 2.7, -1.75)
    f.node('i', 'proc', 'd ← d + 1', 0, -2.55)
    f.edge('s', 'a'); f.edge('a', 'o1', 'r', 'l', label='Đúng'); f.edge('a', 'b', label='Sai', lpos=(0.3, -1.22))
    f.edge('b', 'o2', 'r', 'l', label='Đúng'); f.edge('b', 'i', label='Sai', lpos=(0.3, -2.2))
    f.edge('i', 'a', 'l', 'l', via=[(-1.9, -2.55), (-1.9, -0.78)])
    f.draw(path)

def wheel(path):
    fig, ax = new(6.6, 2.9)
    cw, ch, x0, y0 = 0.62, 0.32, 0.9, 2.3
    for j, lab in enumerate(['6k', '6k+1', '6k+2', '6k+3', '6k+4', '6k+5']):
        cell(ax, x0 + j * cw, y0, cw - 0.04, 0.3, lab, 'navy', fs=7.5, bold=True)
    pr = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41}
    for i in range(7):
        for j in range(6):
            v = 6 * i + j
            if v == 0: continue
            y = y0 - (i + 1) * ch
            if j in (1, 5): k = 'ans' if v in pr else 'done'
            else: k = 'gray'
            if v in (2, 3): k = 'ans'
            cell(ax, x0 + j * cw, y, cw - 0.04, ch - 0.03, str(v), k, fs=8.5, lw=1.0 if k == 'ans' else None)
    tx = x0 + 6 * cw + 0.15
    txt(ax, tx, 2.05, 'Cột 6k, 6k+2, 6k+4: chia hết cho 2', fs=8.2, ha='left', color=GRAY)
    txt(ax, tx, 1.78, 'Cột 6k+3: chia hết cho 3', fs=8.2, ha='left', color=GRAY)
    txt(ax, tx, 1.4, 'Mọi số nguyên tố > 3 nằm ở', fs=8.5, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 1.15, 'cột 6k − 1 (= 6k+5) hoặc 6k + 1', fs=8.5, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 0.7, '→ chỉ thử chia 2, 3 rồi các cặp', fs=8.2, ha='left', color=DRED)
    txt(ax, tx, 0.45, '   i, i + 2 với i = 5, 11, 17, ...', fs=8.2, ha='left', color=DRED)
    txt(ax, tx, 0.2, '   (1/3 số lượng phép chia)', fs=8.2, ha='left', color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'isPrime(x)', 0, 0)
    f.node('a', 'dec', 'x < 2 ?', 0, -0.72)
    f.node('f1', 'end', 'sai', 1.9, -0.72)
    f.node('b', 'dec', 'x < 4 ?', 0, -1.5)
    f.node('t1', 'end', 'đúng', 1.9, -1.5)
    f.node('c', 'dec', '2 | x hoặc 3 | x ?', 0, -2.32)
    f.node('f2', 'end', 'sai', 2.3, -2.32)
    f.node('i', 'proc', 'i ← 5', 0, -3.05)
    f.node('d', 'dec', 'i · i ≤ x ?', 0, -3.8)
    f.node('t2', 'end', 'đúng', 2.1, -3.8)
    f.node('e', 'dec', 'i | x hoặc (i+2) | x ?', 0, -4.7)
    f.node('f3', 'end', 'sai', 2.5, -4.7)
    f.node('j', 'proc', 'i ← i + 6', -2.3, -4.25)
    f.edge('s', 'a'); f.edge('a', 'f1', 'r', 'l', label='Đúng'); f.edge('a', 'b', label='Sai', lpos=(0.3, -1.12))
    f.edge('b', 't1', 'r', 'l', label='Đúng'); f.edge('b', 'c', label='Sai', lpos=(0.3, -1.92))
    f.edge('c', 'f2', 'r', 'l', label='Đúng'); f.edge('c', 'i', label='Sai', lpos=(0.3, -2.72)); f.edge('i', 'd')
    f.edge('d', 't2', 'r', 'l', label='Sai'); f.edge('d', 'e', label='Đúng', lpos=(0.32, -4.25))
    f.edge('e', 'f3', 'r', 'l', label='Đúng'); f.edge('e', 'j', 'l', 'b', via=[(-2.3, -4.7)], label='Sai', lpos=(-1.6, -4.6))
    f.edge('j', 'd', 't', 'l', via=[(-2.3, -3.8)])
    f.draw(path)

def make(F):
    loang(F('loang')); naive_flow(F('naive')); wheel(F('wheel')); opt_flow(F('opt'))
