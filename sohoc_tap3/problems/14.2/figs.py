from figlib import *
from math import gcd

def grid(path):
    fig, ax = new(7.4, 3.6)
    cw, ch = 0.36, 0.33
    for x in range(1, 101):
        i, j = (x - 1) % 10, (x - 1) // 10
        k = 'ans' if gcd(x, 30) == 1 else 'gray'
        cell(ax, 0.1 + i * cw, 3.3 - j * ch, cw - 0.04, ch - 0.04, str(x), k, fs=7, bold=k == 'ans', lw=0.9 if k == 'ans' else 0.6)
    X = 3.95
    rows = [('tập con', 'd', 'dấu', '⌊100/d⌋'), ('∅', '1', '+', '100'), ('{2}', '2', '−', '50'), ('{3}', '3', '−', '33'), ('{5}', '5', '−', '20'),
            ('{2,3}', '6', '+', '16'), ('{2,5}', '10', '+', '10'), ('{3,5}', '15', '+', '6'), ('{2,3,5}', '30', '−', '3')]
    ws = [0.95, 0.6, 0.55, 0.85]
    for r, row in enumerate(rows):
        x = X
        for c, v in enumerate(row):
            kind = 'navy' if r == 0 else ('pink' if row[2] == '−' else 'green')
            cell(ax, x, 3.3 - r * ch, ws[c], ch - 0.02, v, kind, fs=8, bold=r == 0)
            x += ws[c]
    cell(ax, X, 3.3 - 9 * ch - 0.05, sum(ws), ch, 'Tổng: 100 − 103 + 32 − 3 = 26', 'ans', fs=8.5, bold=True)
    txt(ax, 1.9, -0.05, 'Ô vàng: 26 số nguyên tố cùng nhau với 30', fs=8, color=DRED, bold=True)
    save(fig, path)

def trial(path):
    fig, ax = new(7.0, 2.3)
    txt(ax, 0.05, 2.1, 'Thử chia n = 999 999 999 989 (số nguyên tố) cho mọi d với d² ≤ n:', fs=8.8, ha='left', color=NAVY, bold=True)
    cell(ax, 0.05, 1.45, 6.6, 0.4, 'mọi d = 2, 3, 4, ..., 999 999:  ≈ 10⁶ phép chia × 1000 câu hỏi = 10⁹', 'pink', fs=8.6)
    cell(ax, 0.05, 0.85, 6.6 * 78498 / 1e6, 0.4, '', 'green')
    txt(ax, 0.65, 1.05, 'chỉ các số nguyên tố p ≤ 10⁶:  78 498 phép chia × 1000 ≈ 7,8 · 10⁷', fs=8.6, ha='left')
    txt(ax, 0.05, 0.45, 'Hợp số d (như 4, 6, 9) không bao giờ chia hết phần còn lại của n: các ước nguyên tố của d đã bị chia hết trước đó.', fs=8, ha='left', color=GRAY)
    txt(ax, 0.05, 0.15, 'Sàng sẵn một lần O(10⁶ log log 10⁶), rồi mỗi câu hỏi chỉ duyệt danh sách số nguyên tố.', fs=8, ha='left', color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, N;  cnt ← 0', 0, 0)
    f.node('l', 'proc', 'với x = 1..N:  nếu gcd(x, n) = 1 thì cnt++', 0, -0.6)
    f.node('o', 'end', 'In cnt', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Sàng các số nguyên tố ≤ 10⁶ (một lần)', 0, 0)
    f.node('b', 'io', 'Đọc n, N', 0, -0.6)
    f.node('c', 'proc', 'Thử chia n cho các p nguyên tố, p² ≤ n:\nlưu p vào ps, chia hết p khỏi n', 0, -1.25)
    f.node('d', 'dec', 'n > 1 ?', 0, -2.0)
    f.node('e', 'proc', 'ps.push(n)', 2.0, -2.0)
    f.node('g', 'proc', 'ans = Σ theo mặt nạ S ⊆ ps:  ± ⌊N / d_S⌋\n(dấu + khi |S| chẵn, − khi |S| lẻ)', 0, -2.8)
    f.node('h', 'end', 'In ans', 0, -3.4)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.edge('d', 'e', 'r', 'l', label='Đúng')
    f.edge('e', 'g', 'b', 'r', via=[(2.0, -2.8)])
    f.edge('d', 'g', label='Sai', lpos=(0.25, -2.48))
    f.edge('g', 'h')
    f.draw(path)

def make(F):
    grid(F('grid')); trial(F('trial')); naive_flow(F('naive')); opt_flow(F('opt'))
