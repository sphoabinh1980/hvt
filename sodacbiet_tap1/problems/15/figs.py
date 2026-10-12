from figlib import *

W = [[1] + [0] * 11, [1] * 10 + [0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8], [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 63, 69]]

def table(path):
    fig, ax = new(7.4, 2.5)
    txt(ax, 0.35, 2.2, 'k \\ t', fs=9, color=GRAY)
    for t in range(12):
        cell(ax, 0.75 + t * 0.55, 1.98, 0.53, 0.38, str(t), 'navy', fs=9, bold=True)
    for k in range(4):
        y = 1.55 - k * 0.43
        cell(ax, 0.15, y, 0.5, 0.38, str(k), 'navy', fs=9, bold=True)
        for t in range(12):
            v = W[k][t]
            kind = 'ans' if (k, t) in ((3, 10), (3, 9)) else 'pink' if (k == 2 and 1 <= t <= 10) else 'gray' if v == 0 else 'done'
            cell(ax, 0.75 + t * 0.55, y, 0.53, 0.38, str(v), kind, fs=9, bold=kind == 'ans')
    txt(ax, 7.35, 0.02, 'ways(3, 10) = 63 = tổng 10 ô tô hồng ở hàng k = 2 (t = 1..10)', fs=8.5, color=DRED, ha='right')
    save(fig, path)

def tree(path):
    fig, ax = new(7.6, 3.3)
    rows = [('2 0 2 6', 'Bám sát N = 2026, cần tổng S = 10', None, 'navy'),
            ('0 _ _ _', 'chữ số đầu 0 < 2, 3 chữ số tự do, cần tổng 10', 'ways(3, 10) = 63', 'done'),
            ('1 _ _ _', 'chữ số đầu 1 < 2, 3 chữ số tự do, cần tổng 9', 'ways(3, 9) = 55', 'done'),
            ('2 0 _ _', 'chữ số thứ hai bằng 0: không có d < 0', '0', 'gray'),
            ('2 0 0 _', 'chữ số thứ ba 0 < 2, cần tổng 8 trong 1 chữ số', 'ways(1, 8) = 1', 'done'),
            ('2 0 1 _', 'chữ số thứ ba 1 < 2, cần tổng 7 trong 1 chữ số', 'ways(1, 7) = 1', 'done'),
            ('2 0 2 d', 'd < 6, cần tổng 6 trong 0 chữ số: không có', '0', 'gray'),
            ('2 0 2 6', 'chính N, tổng đúng 10', '1', 'green')]
    for r, (pat, lab, val, kind) in enumerate(rows):
        y = 3.0 - r * 0.4
        for j, ch in enumerate(pat.split()):
            cell(ax, 0.1 + j * 0.34, y - 0.16, 0.32, 0.32, ch, 'navy' if kind == 'navy' else 'in' if ch != '_' else 'plain', fs=9, bold=ch != '_')
        txt(ax, 1.6, y, lab, fs=8.6, ha='left', color=NAVY if kind != 'gray' else GRAY)
        if val:
            cell(ax, 5.75, y - 0.16, 1.6, 0.32, val, 'gray' if kind == 'gray' else 'green' if kind == 'green' else 'done', fs=8.6)
    txt(ax, 7.35, 0.0, 'Tổng: 63 + 55 + 1 + 1 + 1 = 121', fs=9.5, ha='right', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R, S;  cnt ← 0', 0, 0)
    f.node('b', 'proc', 'với x = L .. R: tính tổng chữ số của x;  nếu bằng S thì cnt++', 0, -0.65)
    f.node('c', 'end', 'In cnt', 0, -1.3)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R, S', 0, 0)
    f.node('b', 'sub', 'f(N): duyệt các chữ số c của N từ trái sang;\nvới mỗi d < c: cnt += ways(số chữ số còn lại, need − d)\nneed −= c', 0, -0.85)
    f.node('c', 'proc', 'nếu need = 0 thì cnt++ (chính N)', 0, -1.7)
    f.node('d', 'end', 'In f(R) − f(L − 1)', 0, -2.3)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    table(F('table')); tree(F('tree')); naive_flow(F('naive')); opt_flow(F('opt'))
