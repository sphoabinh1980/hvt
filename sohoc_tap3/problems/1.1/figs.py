import math
from figlib import *

def vong(path):
    fig, ax = new(6.5, 3.3)
    cx, cy, R = 2.0, 1.6, 1.15
    names = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ nhật']
    for d in range(7):
        a = math.pi / 2 - 2 * math.pi * d / 7
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        kind = 'ans' if d == 6 else ('in' if d == 0 else 'done')
        ax.add_patch(Circle((x, y), 0.25, facecolor=KIND[kind][0], edgecolor=KIND[kind][1], lw=1.6 if d in (0, 6) else 1.0, zorder=3))
        txt(ax, x, y + 0.05, str(d + 2) if d < 6 else '8', fs=11, bold=True)
        txt(ax, x, y - 0.12, 'd=%d' % d, fs=6.5, color=GRAY)
        lx, ly = cx + (R + 0.52) * math.cos(a), cy + (R + 0.42) * math.sin(a)
        txt(ax, lx, ly, names[d], fs=8, color=NAVY)
    for d in range(6):
        a1 = math.pi / 2 - 2 * math.pi * d / 7 - 0.3
        a2 = math.pi / 2 - 2 * math.pi * (d + 1) / 7 + 0.3
        arrow(ax, (cx + 0.82 * math.cos(a1), cy + 0.82 * math.sin(a1)), (cx + 0.82 * math.cos(a2), cy + 0.82 * math.sin(a2)), color=GREEN, rad=-0.25, lw=1.0, ms=8)
    txt(ax, cx, cy + 0.1, 'đi k bước', fs=8.5, color=GREEN, bold=True)
    txt(ax, cx, cy - 0.15, 'thuận chiều kim', fs=7.5, color=GREEN)
    x0 = 4.05
    txt(ax, x0, 2.95, 'Đổi tên ngày thành số dư', fs=9.5, bold=True, color=NAVY, ha='left')
    rows = [('thứ t', '→', 'd = t − 2  (0..6)'), ('sau k ngày', '→', 'd\' = (d + k) mod 7'), ('in ra', '→', 'd\' + 2')]
    for i, (a, b, c) in enumerate(rows):
        y = 2.55 - 0.42 * i
        cell(ax, x0, y - 0.16, 0.95, 0.32, a, 'in', fs=8.5)
        txt(ax, x0 + 1.08, y, b, fs=10, color=NAVY)
        cell(ax, x0 + 1.22, y - 0.16, 1.2, 0.32, c, 'done', fs=8.5)
    txt(ax, x0, 1.05, 'Ví dụ: thứ Hai (d = 0), k = 1000', fs=8.5, ha='left')
    txt(ax, x0, 0.78, '1000 mod 7 = 6  →  d\' = 6  →  in 8', fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, x0, 0.45, 'Chỉ có 7 kết quả có thể xảy ra!', fs=8.5, ha='left', color=NAVY, italic=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc t, k;  d ← t − 2', 0, 0)
    f.node('c', 'dec', 'k ≥ 0 ?', 0, -0.7)
    f.node('a', 'proc', 'lặp k lần:\nd ← d + 1 (về 0 nếu = 7)', -1.55, -1.55)
    f.node('b', 'proc', 'lặp |k| lần:\nd ← d − 1 (về 6 nếu < 0)', 1.55, -1.55)
    f.node('e', 'end', 'in d + 2', 0, -2.35)
    f.edge('s', 'c')
    f.edge('c', 'a', 'l', 't', via=[(-1.55, -0.7)], label='Đúng', lpos=(-0.95, -0.6))
    f.edge('c', 'b', 'r', 't', via=[(1.55, -0.7)], label='Sai', lpos=(0.95, -0.6))
    f.edge('a', 'e', 'b', 'l', via=[(-1.55, -2.35)])
    f.edge('b', 'e', 'b', 'r', via=[(1.55, -2.35)])
    f.draw(path)

def numline(path):
    fig, ax = new(6.4, 2.35)
    x0, sc = 0.3, 5.8 / 14.0       # trục từ -107 tới -93
    def X(v): return x0 + (v + 107) * sc
    line(ax, [(X(-107), 1.2), (X(-93), 1.2)], color=GRAY, lw=1.2)
    for v in range(-107, -92):
        big = v in (-105, -98)
        ax.plot([X(v), X(v)], [1.2 - (0.09 if big else 0.05), 1.2 + (0.09 if big else 0.05)], color=NAVY if big else GRAY, lw=1.4 if big else 0.8)
        if big or v == -100:
            txt(ax, X(v), 0.98, str(v), fs=8, color=NAVY if big else DRED, bold=True)
    for v, lab in ((-105, '7·(−15)'), (-98, '7·(−14)')):
        txt(ax, X(v), 0.78, lab, fs=7.5, color=NAVY)
    ax.add_patch(Circle((X(-100), 1.2), 0.07, facecolor='#FFE699', edgecolor=DRED, lw=1.5, zorder=5))
    arrow(ax, (X(-105), 1.5), (X(-100), 1.5), color=GREEN, lw=1.6)
    txt(ax, (X(-105) + X(-100)) / 2, 1.68, 'đúng: dư +5', fs=8.5, color=GREEN, bold=True)
    arrow(ax, (X(-98), 1.5), (X(-100), 1.5), color=DRED, lw=1.6)
    txt(ax, (X(-98) + X(-100)) / 2, 1.68, 'C++: −2', fs=8.5, color=DRED, bold=True)
    txt(ax, 3.2, 2.12, 'x = −100: thương làm tròn xuống (−15) cho số dư 5 ∈ [0, 7)', fs=8.5, color=NAVY)
    txt(ax, 3.2, 0.42, 'C++ làm tròn thương về 0 (−14) nên −100 % 7 = −2;  sửa:  ((−2) + 7) % 7 = 5', fs=8.5, color='#1A1A1A')
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Bắt đầu', 0, 0)
    f.node('r', 'io', 'Đọc Q', 0, -0.6)
    f.node('c', 'dec', 'còn câu hỏi?', 0, -1.3)
    f.node('i', 'io', 'Đọc t, k', 0, -2.05)
    f.node('x', 'proc', 'x ← t − 2 + k', 0, -2.65)
    f.node('d', 'proc', 'd ← (x % 7 + 7) % 7', 0, -3.25)
    f.node('o', 'io', 'In d + 2', 0, -3.85)
    f.node('e', 'end', 'Kết thúc', 2.2, -1.3)
    for a, b in [('s', 'r'), ('r', 'c'), ('i', 'x'), ('x', 'd'), ('d', 'o')]:
        f.edge(a, b)
    f.edge('c', 'i', label='Đúng', lpos=(0.28, -1.82))
    f.edge('c', 'e', 'r', 'l', label='Sai')
    f.edge('o', 'c', 'l', 'l', via=[(-1.5, -3.85), (-1.5, -1.3)])
    f.draw(path)

def make(F):
    vong(F('vong')); naive_flow(F('naive')); numline(F('numline')); opt_flow(F('opt'))
