from figlib import *

G = [(1, [1, 10, 100]), (2, [2, 20]), (3, [3, 12, 21, 30]), (4, [4, 40]), (5, [5, 50]), (6, [6, 24, 42, 60]), (7, [7, 70]), (8, [8, 80]),
     (9, [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]), (12, [48, 84])]

def groups(path):
    fig, ax = new(7.4, 3.9)
    txt(ax, 0.35, 3.75, 'tổng s', fs=8.5, color=GRAY); txt(ax, 0.85, 3.75, 'các số Harshad ≤ 100 có tổng chữ số s', fs=8.5, color=GRAY, ha='left')
    txt(ax, 6.95, 3.75, 'số lượng', fs=8.5, color=GRAY)
    for i, (s, xs) in enumerate(G):
        y = 3.35 - i * 0.36
        cell(ax, 0.1, y, 0.5, 0.3, str(s), 'navy', fs=9, bold=True)
        for j, x in enumerate(xs):
            cell(ax, 0.85 + j * 0.56, y, 0.52, 0.3, str(x), 'ans' if s == 12 else 'done', fs=8.5)
        cell(ax, 6.7, y, 0.5, 0.3, str(len(xs)), 'green', fs=9, bold=True)
    txt(ax, 7.2, -0.05, 'Tổng: 33 số. Các tổng 10, 11, 13..18 không có số nào ≤ 100.', fs=8.5, ha='right', color=DRED)
    save(fig, path)

def trans(path):
    fig, ax = new(7.4, 1.9)
    rbox(ax, 0.1, 0.45, 2.1, 1.1, 'tiền tố 4\nt = 4\nr = 4 mod 9 = 4', 'done', fs=9)
    rbox(ax, 2.9, 0.75, 1.1, 0.5, 'thêm x = 5', 'in', fs=9)
    rbox(ax, 4.7, 0.45, 2.6, 1.1, 'tiền tố 45\nt = 4 + 5 = 9\nr = (4·10 + 5) mod 9 = 0', 'ans', fs=9)
    arrow(ax, (2.2, 1.0), (2.9, 1.0)); arrow(ax, (4.0, 1.0), (4.7, 1.0))
    txt(ax, 3.7, 0.1, 'Với s = 9: hết chữ số, t = s và r = 0 → 45 là số Harshad (45 = 9 · 5)', fs=8.8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc N;  cnt ← 0', 0, 0)
    f.node('b', 'proc', 'với x = 1 .. N: s ← tổng chữ số của x;  nếu x mod s = 0 thì cnt++', 0, -0.65)
    f.node('c', 'end', 'In cnt', 0, -1.3)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc N (L chữ số);  ans ← 0', 0, 0)
    f.node('b', 'proc', 'với s = 1 .. 9L:', 0, -0.6)
    f.node('c', 'sub', 'quy hoạch động qua L vị trí, trạng thái (t, r):\nt = tổng chữ số đã điền (≤ s), r = tiền tố mod s;\nnhánh "rời khỏi N" thêm vào khi đặt chữ số nhỏ hơn N', 0, -1.45)
    f.node('d', 'proc', 'ans += số trạng thái (s, 0);  nếu N có tổng s và chia hết cho s: ans++', 0, -2.3)
    f.node('e', 'end', 'In ans', 0, -2.9)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.edge('d', 'b', 'r', 'r', via=[(3.3, -2.3), (3.3, -0.6)], label='s tiếp theo', lpos=(3.75, -1.45))
    f.draw(path)

def make(F):
    groups(F('groups')); trans(F('trans')); naive_flow(F('naive')); opt_flow(F('opt'))
