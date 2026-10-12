from figlib import *

def steps(path):
    fig, ax = new(7.6, 2.9)
    rows = [('534976', 'Bước 1: đuôi không tăng dài nhất là 976; i chỉ vào chữ số 4 ngay trước đuôi', {2: 'ans', 3: 'gray', 4: 'gray', 5: 'gray'}),
            ('534976', 'Bước 2: trong đuôi, chữ số nhỏ nhất lớn hơn 4 là 6 (vị trí j)', {2: 'ans', 5: 'pink'}),
            ('536974', 'Bước 3: đổi chỗ s[i] và s[j]', {2: 'pink', 5: 'ans'}),
            ('536479', 'Bước 4: đảo đuôi thành tăng dần: 974 → 479', {3: 'green', 4: 'green', 5: 'green'})]
    for r, (s, lab, kinds) in enumerate(rows):
        y = 2.45 - r * 0.68
        for j, ch in enumerate(s):
            cell(ax, 0.2 + j * 0.42, y, 0.38, 0.4, ch, kinds.get(j, 'done'), fs=11, bold=j in kinds)
        txt(ax, 2.9, y + 0.2, lab, fs=8.4, ha='left', color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc n;  key ← các chữ số của n đã sắp xếp', 0, 0)
    f.node('b', 'proc', 'với x = n + 1, n + 2, ... (cùng số chữ số):\nnếu các chữ số của x sắp xếp = key: in x, dừng', 0, -0.7)
    f.node('c', 'end', 'Không tìm được: in −1', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc xâu s', 0, 0)
    f.node('b', 'proc', 'i ← vị trí lớn nhất có s[i] < s[i + 1]', 0, -0.6)
    f.node('c', 'dec', 'có i ?', 0, -1.3)
    f.node('d', 'end', 'In −1', 2.4, -1.3)
    f.node('e', 'proc', 'j ← vị trí lớn nhất có s[j] > s[i];  đổi chỗ s[i], s[j]\nđảo ngược đoạn s[i + 1 ..]', 0, -2.15)
    f.node('g', 'end', 'In s', 0, -2.85)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd', 'r', 'l', label='Sai'); f.edge('c', 'e', label='Đúng', lpos=(0.35, -1.72)); f.edge('e', 'g')
    f.draw(path)

def make(F):
    steps(F('steps')); naive_flow(F('naive')); opt_flow(F('opt'))
