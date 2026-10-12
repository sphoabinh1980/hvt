from figlib import *
from itertools import permutations

def perms(path):
    fig, ax = new(7.4, 2.2)
    ps = [p for p in permutations(range(1, 5)) if sum(p[i] == i + 1 for i in range(4)) == 1]
    cw, ch = 0.36, 0.3
    for t, p in enumerate(ps):
        X = 0.15 + (t % 4) * 1.8; Y = 1.45 - (t // 4) * 0.95
        for j in range(4):
            if t < 4: txt(ax, X + j * cw + cw / 2, Y + ch + 0.12, 'ng.%d' % (j + 1), fs=6.5, color=GRAY)
            cell(ax, X + j * cw, Y, cw - 0.03, ch, str(p[j]), 'ans' if p[j] == j + 1 else 'done', fs=8.5, bold=p[j] == j + 1)
    txt(ax, 3.7, 0.08, 'Người may mắn (ô vàng) có 4 cách chọn; ba người còn lại hoán đổi vòng quanh: 2 cách. Tổng 4 · 2 = 8.', fs=8, color=NAVY)
    save(fig, path)

def rec(path):
    fig, ax = new(7.6, 3.0)
    def row(y, items, lab):
        for i, (s, k) in enumerate(items):
            cell(ax, 0.2 + i * 0.5, y, 0.45, 0.34, s, k, fs=8.5)
        txt(ax, 0.2 + len(items) * 0.5 + 0.12, y + 0.17, lab, fs=8.4, ha='left')
    txt(ax, 0.2, 2.8, 'Người k nhận quà của người j (j ≠ k): có k − 1 cách chọn j. Xét người j nhận quà của ai:', fs=8.6, ha='left', color=NAVY, bold=True)
    row(2.05, [('1', 'gray'), ('...', 'gray'), ('j', 'pink'), ('...', 'gray'), ('k', 'pink')], 'Trường hợp 1: j nhận quà của k (đổi chéo j ↔ k).')
    txt(ax, 2.92, 1.88, 'Bỏ j, k đi: k − 2 người còn lại tự xếp lệch nhau  →  D(k − 2) cách.', fs=8.2, ha='left', color=GRAY)
    row(1.0, [('1', 'gray'), ('...', 'gray'), ('j', 'in'), ('...', 'gray'), ('k', 'pink')], 'Trường hợp 2: j không nhận quà của k.')
    txt(ax, 2.92, 0.83, 'Coi quà của k như "quà của j bị cấm": k − 1 người xếp lệch  →  D(k − 1) cách.', fs=8.2, ha='left', color=GRAY)
    cell(ax, 0.2, 0.08, 6.9, 0.38, 'D(k) = (k − 1) · (D(k − 1) + D(k − 2)),   D(0) = 1,  D(1) = 0', 'ans', fs=9.5, bold=True)
    save(fig, path)

def dtable(path):
    fig, ax = new(7.2, 0.75)
    D = [1, 0]
    for i in range(2, 11): D.append((i - 1) * (D[-1] + D[-2]))
    cell(ax, 0, 0.38, 0.6, 0.32, 'k', 'navy', fs=8.5, bold=True); cell(ax, 0, 0.06, 0.6, 0.32, 'D(k)', 'navy', fs=8.5, bold=True)
    w = [0.42] * 7 + [0.6, 0.72, 0.85, 0.95]
    x = 0.6
    for k in range(11):
        cell(ax, x, 0.38, w[k], 0.32, str(k), 'done', fs=8.5)
        cell(ax, x, 0.06, w[k], 0.32, format(D[k], ',').replace(',', ' '), 'ans' if k in (3, 10) else 'plain', fs=8)
        x += w[k]
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'a = (0, 1, ..., n − 1);  cnt ← 0', 0, 0)
    f.node('l', 'proc', 'với mỗi hoán vị a (next_permutation):\nđếm số i có a[i] = i; nếu bằng m thì cnt++', 0, -0.68)
    f.node('o', 'end', 'In cnt', 0, -1.36)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc n, m;  k ← n − m', 0, 0)
    f.node('b', 'proc', 'num ← Π (n − i) mod p, i = 0..k − 1  (lấy dư từng thừa số)\nkf ← k! mod p', 0, -0.68)
    f.node('c', 'proc', 'C ← num · kf^(p − 2) mod p', 0, -1.36)
    f.node('d', 'proc', 'D(k) bằng truy hồi, chỉ giữ hai giá trị cuối', 0, -1.98)
    f.node('e', 'end', 'In C · D(k) mod p', 0, -2.6)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.draw(path)

def make(F):
    perms(F('perms')); rec(F('rec')); dtable(F('dtab')); naive_flow(F('naive')); opt_flow(F('opt'))
