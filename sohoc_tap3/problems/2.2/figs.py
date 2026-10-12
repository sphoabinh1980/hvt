from figlib import *

def merge(path):
    fig, ax = new(6.6, 2.7)
    cw = 0.5
    txt(ax, 0.15, 2.38, 'ước nhỏ (d ≤ √36), theo thứ tự gặp:', fs=8.5, ha='left', color=BLUE, bold=True)
    for i, d in enumerate([1, 2, 3, 4, 6]):
        cell(ax, 0.2 + i * cw, 1.85, cw - 0.05, 0.36, str(d), 'done', fs=10)
    txt(ax, 3.55, 2.38, 'ước lớn (36 / d), theo thứ tự gặp:', fs=8.5, ha='left', color=ORANGE, bold=True)
    for i, d in enumerate([36, 18, 12, 9]):
        cell(ax, 3.6 + i * cw, 1.85, cw - 0.05, 0.36, str(d), 'in', fs=10)
    txt(ax, 5.75, 2.03, 'giảm dần', fs=8, color=ORANGE, italic=True, ha='left')
    for i, d in enumerate([9, 12, 18, 36]):
        arrow(ax, (3.6 + (3 - i) * cw + 0.22, 1.83), (0.2 + (5 + i) * cw + 0.22, 0.82), color='#BFBFBF', lw=0.8, ms=7)
    txt(ax, 0.15, 1.1, 'nối tiếp, đảo ngược dãy ước lớn:', fs=8.5, ha='left', color=NAVY, bold=True)
    for i, d in enumerate([1, 2, 3, 4, 6, 9, 12, 18, 36]):
        cell(ax, 0.2 + i * cw, 0.45, cw - 0.05, 0.36, str(d), 'done' if i < 5 else 'in', fs=10)
    txt(ax, 0.2 + 9 * cw + 0.1, 0.63, '← tăng dần, không cần sắp xếp', fs=8.5, color=DRED, ha='left')
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, Q', 0, 0)
    f.node('a', 'proc', 'thử d = 1..n: d | n thì thêm vào ds', 0, -0.6)
    f.node('o', 'io', 'In |ds| và dãy ds', 0, -1.2)
    f.node('c', 'dec', 'còn khách?', 0, -1.92)
    f.node('x', 'io', 'Đọc x', 0, -2.7)
    f.node('l', 'proc', 'duyệt ds từ đầu tới phần tử đầu tiên ≥ x', 0, -3.3)
    f.node('p', 'io', 'In phần tử đó (hoặc −1)', 0, -3.9)
    f.node('e', 'end', 'Kết thúc', 2.3, -1.92)
    for a, b in [('s', 'a'), ('a', 'o'), ('o', 'c'), ('x', 'l'), ('l', 'p')]: f.edge(a, b)
    f.edge('c', 'x', label='Đúng', lpos=(0.32, -2.42)); f.edge('c', 'e', 'r', 'l', label='Sai')
    f.edge('p', 'c', 'l', 'l', via=[(-2.4, -3.9), (-2.4, -1.92)])
    f.draw(path)

def bsearch(path):
    fig, ax = new(6.6, 2.75)
    ds = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    cw = 0.52
    steps = [(0, 9, 4), (5, 9, 7), (5, 7, 6), (6, 6, None)]
    for k, (lo, hi, mid) in enumerate(steps):
        y = 2.25 - k * 0.55
        txt(ax, 0.1, y + 0.18, 'bước %d' % (k + 1) if mid is not None else 'kết quả', fs=8, ha='left', color=NAVY, bold=True)
        for i, d in enumerate(ds):
            if mid is None:
                kind = 'ans' if i == lo else 'gray'
            elif i == mid:
                kind = 'yellow'
            elif lo <= i < hi:
                kind = 'done'
            else:
                kind = 'gray'
            cell(ax, 0.85 + i * cw, y, cw - 0.05, 0.34, str(d), kind, fs=9.5, bold=kind == 'ans')
        if mid is not None:
            ok = ds[mid] >= 10
            txt(ax, 0.85 + 9 * cw + 0.1, y + 0.17, 'giữa = %d %s 10 → %s' % (ds[mid], '≥' if ok else '<', 'giữ nửa trái' if ok else 'bỏ nửa trái'), fs=8, ha='left')
        else:
            txt(ax, 0.85 + 9 * cw + 0.1, y + 0.17, 'ước nhỏ nhất ≥ 10 là 12', fs=8.5, ha='left', color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, Q', 0, 0)
    f.node('a', 'proc', 'd = 1..√n: d | n thì small ← d, big ← n/d', 0, -0.6)
    f.node('b', 'proc', 'ds ← small nối big đảo ngược', 0, -1.2)
    f.node('o', 'io', 'In |ds| và dãy ds', 0, -1.8)
    f.node('c', 'dec', 'còn khách?', 0, -2.52)
    f.node('x', 'io', 'Đọc x', 0, -3.3)
    f.node('l', 'proc', 'it ← lower_bound(ds, x)', 0, -3.9)
    f.node('p', 'io', 'In *it (hoặc −1 nếu hết dãy)', 0, -4.5)
    f.node('e', 'end', 'Kết thúc', 2.3, -2.52)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'o'), ('o', 'c'), ('x', 'l'), ('l', 'p')]: f.edge(a, b)
    f.edge('c', 'x', label='Đúng', lpos=(0.32, -3.02)); f.edge('c', 'e', 'r', 'l', label='Sai')
    f.edge('p', 'c', 'l', 'l', via=[(-2.4, -4.5), (-2.4, -2.52)])
    f.draw(path)

def make(F):
    merge(F('merge')); naive_flow(F('naive')); bsearch(F('bsearch')); opt_flow(F('opt'))
