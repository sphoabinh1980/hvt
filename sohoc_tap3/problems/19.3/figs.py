from figlib import *

def reduce(path):
    fig, ax = new(7.6, 2.9)
    A = [[1, 2, 3], [4, 5, 6]]
    c = 0.45
    txt(ax, 0.9, 2.7, 'Lưới (k = 3)', fs=8.6, bold=True, color=NAVY)
    for i in range(2):
        for j in range(3):
            cell(ax, 0.3 + j * c, 2.1 - i * c, c - 0.04, c - 0.04, str(A[i][j]), 'in', fs=9.5)
    txt(ax, 0.2, 2.1 - 0.5 * c + c / 2, '', fs=8)
    line(ax, [(0.25, 2.1 + c), (0.25, 2.1 - c)], color=DRED, lw=2)
    txt(ax, 0.9, 1.05, 'cố định hàng 1..2', fs=8, color=DRED)
    arrow(ax, (1.75, 2.0), (2.25, 2.0), color=GRAY)
    txt(ax, 3.1, 2.7, 'b = tổng cột', fs=8.6, bold=True, color=NAVY)
    for j, v in enumerate([5, 7, 9]):
        cell(ax, 2.4 + j * c, 1.85, c - 0.04, c - 0.04, str(v), 'done', fs=9.5)
        txt(ax, 2.4 + j * c + c / 2 - 0.02, 1.62, 'dư %d' % (v % 3), fs=7.5, color=GRAY)
    arrow(ax, (3.85, 2.0), (4.35, 2.0), color=GRAY)
    txt(ax, 5.6, 2.7, 'tiền tố của b (mod 3)', fs=8.6, bold=True, color=NAVY)
    for j, v in enumerate([0, 2, 0, 0]):
        cell(ax, 4.5 + j * c, 1.85, c - 0.04, c - 0.04, str(v), 'ans' if v == 0 else 'gray', fs=9.5, bold=v == 0)
        txt(ax, 4.5 + j * c + c / 2 - 0.02, 2.4, 'P%s' % '₀₁₂₃'[j], fs=7.5, color=GRAY)
    txt(ax, 5.4, 1.45, 'ba tiền tố dư 0 → C(3, 2) = 3 đoạn:', fs=8, color=DRED)
    txt(ax, 5.4, 1.2, '[5, 7], [5, 7, 9], [9]', fs=8, color=DRED, bold=True)
    txt(ax, 3.8, 0.6, 'Mỗi cặp hàng (i₁, i₂) cho một dãy b; mỗi hình chữ nhật giữa hai hàng là một đoạn con của b.', fs=8.2, color=NAVY)
    txt(ax, 3.8, 0.3, 'Ba cặp hàng (1,1), (2,2), (1,2), mỗi cặp 3 đoạn: tổng 9.', fs=8.2, color=GRAY)
    save(fig, path)

def clear(path):
    fig, ax = new(7.4, 1.7)
    txt(ax, 0.05, 1.5, 'Mỗi cặp hàng chỉ ghi vào tối đa n + 1 = 401 ô của mảng cnt[0..k − 1]:', fs=8.6, ha='left', bold=True, color=NAVY)
    W = 6.9
    cell(ax, 0.1, 0.85, W, 0.36, '', 'plain')
    import random
    r = random.Random(5)
    for _ in range(28):
        x = 0.1 + r.random() * (W - 0.08)
        cell(ax, x, 0.85, 0.06, 0.36, '', 'ans', lw=0.5)
    txt(ax, 0.1 + W / 2, 0.6, 'xóa cả mảng: k = 10⁶ thao tác × 80 200 cặp = 8 · 10¹⁰  (quá chậm)', fs=8.2, color=RED)
    txt(ax, 0.1 + W / 2, 0.3, 'đi lại dãy tiền tố, gán cnt[Pⱼ] = 0: n + 1 thao tác  (ô vàng)', fs=8.2, color=GREEN, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'a[i][j] ← số dư không âm khi đọc', 0, 0)
    f.node('b', 'proc', 'với i₁ = 1..m:  b ← 0;  với i₂ = i₁..m:', 0, -0.6)
    f.node('c', 'proc', 'b[j] ← (b[j] + a[i₂][j]) mod k   (mọi j)', 0, -1.2)
    f.node('d', 'proc', 'P₀ = 0, cnt[0] = 1;  với j = 1..n:\nPⱼ ← (Pⱼ₋₁ + b[j]) mod k;  ans += cnt[Pⱼ];  cnt[Pⱼ]++', 0, -1.9)
    f.node('e', 'proc', 'xóa cnt[Pⱼ], j = 0..n', 0, -2.6)
    f.node('g', 'end', 'In ans', 0, -3.2)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e'); f.edge('e', 'g')
    f.edge('e', 'c', 'r', 'r', via=[(3.6, -2.6), (3.6, -1.2)], label='i₂ tiếp', lpos=(4.0, -1.9))
    f.draw(path)

def make(F):
    reduce(F('reduce')); clear(F('clear')); opt_flow(F('opt'))
