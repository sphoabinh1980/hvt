from figlib import *

def stack(path):
    fig, ax = new(5.4, 3.2)
    steps = [('1', '1', [], 3), ('4', '14', [], 3), ('3', '13', ['4'], 2), ('2', '12', ['3'], 1), ('2', '122', [], 1), ('1', '121', ['2'], 0), ('9', '1219', [], 0)]
    txt(ax, 0.15, 3.0, 'đọc', fs=9, color=GRAY); txt(ax, 0.85, 3.0, 'ngăn xếp', fs=9, color=GRAY, ha='left'); txt(ax, 2.55, 3.0, 'bị xóa', fs=9, color=GRAY, ha='left'); txt(ax, 3.45, 3.0, 'k còn', fs=9, color=GRAY, ha='left')
    for r, (c, st, pops, k) in enumerate(steps):
        y = 2.6 - r * 0.38
        cell(ax, 0.05, y - 0.15, 0.32, 0.3, c, 'in', fs=9, bold=True)
        for j, ch in enumerate(st):
            cell(ax, 0.85 + j * 0.34, y - 0.15, 0.32, 0.3, ch, 'ans' if r == len(steps) - 1 else 'done', fs=9, bold=r == len(steps) - 1)
        txt(ax, 2.75, y, ', '.join(pops) if pops else '–', fs=9, ha='left', color=RED if pops else GRAY, bold=bool(pops))
        txt(ax, 3.6, y, str(k), fs=9, ha='left', color=NAVY)
    txt(ax, 4.1, 1.5, 'n = 1432219\nk = 3\nđáp số 1219', fs=9, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc s, k', 0, 0)
    f.node('b', 'proc', 'lặp k lần: tìm i đầu tiên có s[i] > s[i + 1]\n(không có thì i là vị trí cuối);  xóa s[i]', 0, -0.7)
    f.node('c', 'end', 'Bỏ chữ số 0 ở đầu, in (rỗng thì in 0)', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc s, k;  ngăn xếp st rỗng', 0, 0)
    f.node('b', 'proc', 'với mỗi chữ số c của s:\nkhi k > 0 và đỉnh st > c: bỏ đỉnh, k−−\nđẩy c vào st', 0, -0.8)
    f.node('c', 'proc', 'bỏ k phần tử cuối của st (nếu còn lượt xóa)', 0, -1.6)
    f.node('d', 'end', 'Bỏ chữ số 0 ở đầu, in (rỗng thì in 0)', 0, -2.2)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    stack(F('stack')); naive_flow(F('naive')); opt_flow(F('opt'))
