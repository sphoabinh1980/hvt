from figlib import *

def pairs(path):
    fig, ax = new(7.6, 2.2)
    fac = {1: [], 2: ['2'], 3: ['3'], 4: ['2', '2'], 5: ['5'], 6: ['2', '3'], 7: ['7'], 8: ['2', '2', '2'], 9: ['3', '3'], 10: ['2', '5']}
    x = 0.15
    for i in range(1, 11):
        cell(ax, x, 1.55, 0.6, 0.35, str(i), 'done', fs=9, bold=True)
        for j, f in enumerate(fac[i]):
            k = 'ans' if f == '5' else ('in' if f == '2' else 'gray')
            cell(ax, x + 0.12, 1.15 - j * 0.3, 0.36, 0.26, f, k, fs=8)
        x += 0.72
    txt(ax, 3.8, 0.12, '10! có 8 thừa số 2 (cam) nhưng chỉ 2 thừa số 5 (vàng): ghép được 2 cặp 2 · 5 = 10, nên 10! = 3628800 có 2 chữ số 0 tận cùng.', fs=8, color=NAVY)
    save(fig, path)

def legendre(path):
    fig, ax = new(7.6, 1.9)
    for k in range(1, 13):
        v = 5 * k; x = 0.2 + (k - 1) * 0.6
        kind = 'ans' if v % 25 == 0 else 'done'
        cell(ax, x, 1.1, 0.52, 0.38, str(v), kind, fs=9, bold=kind == 'ans')
        ax.plot([x + 0.26], [0.95], 'o', ms=5, color=BLUE)
        if v % 25 == 0: ax.plot([x + 0.26], [0.78], 'o', ms=5, color=DRED)
    txt(ax, 0.05, 0.95, '', fs=7)
    txt(ax, 3.8, 0.4, 'n = 60: mỗi bội của 5 góp một thừa số 5 (chấm xanh): ⌊60/5⌋ = 12;  mỗi bội của 25 góp thêm một (chấm đỏ): ⌊60/25⌋ = 2.', fs=8, color=NAVY)
    txt(ax, 3.8, 0.12, '60! có 12 + 2 = 14 chữ số 0 tận cùng.', fs=8.6, color=DRED, bold=True)
    save(fig, path)

def trap(path):
    fig, ax = new(7.6, 1.75)
    txt(ax, 0.1, 1.55, 'Đúng:', fs=9, ha='left', bold=True, color=GREEN)
    txt(ax, 0.9, 1.55, '14! = 871782912|00   →  × 15  →  15! = 1307674368|000', fs=9.2, ha='left', family='monospace')
    txt(ax, 0.1, 1.0, 'Sai:', fs=9, ha='left', bold=True, color=RED)
    txt(ax, 0.9, 1.0, 'chỉ giữ  2         →  2 × 15 = 30  →  bỏ 0  →  3', fs=9.2, ha='left', family='monospace')
    txt(ax, 0.9, 0.55, 'giữ   912         →  912 × 15 = 13680  →  1368  →  8', fs=9.2, ha='left', family='monospace', color=GREEN)
    txt(ax, 3.8, 0.1, 'Nhân với 5 tạo ra số 0 mới và "kéo" các chữ số bên trái xuống hàng đơn vị: chữ số đã vứt đi quay lại quyết định kết quả.', fs=7.8, color=GRAY)
    save(fig, path)

def chain(path):
    fig, ax = new(7.6, 2.2)
    rows = [(2026, 405, 1, 2), (405, 81, 0, 6), (81, 16, 1, 8), (16, 3, 1, 8), (3, None, None, 6)]
    for i, (n, k, r, d) in enumerate(rows):
        x = 0.15 + i * 1.5
        cell(ax, x, 1.35, 1.2, 0.42, 'D(%d)' % n, 'ans' if i == 0 else 'done', fs=9.5, bold=True)
        cell(ax, x, 0.85, 1.2, 0.42, '= %d' % d, 'ans' if i == 0 else 'plain', fs=10, bold=True)
        if k is not None:
            arrow(ax, (x + 1.22, 1.56), (x + 1.48, 1.56), color=GRAY)
            p2 = [6, 2, 4, 8][k % 4]
            txt(ax, x + 0.6, 0.55, 'k = %d, r = %d' % (k, r), fs=7.2, color=GRAY)
            txt(ax, x + 0.6, 0.3, '2ᵏ → %d' % p2, fs=7.2, color=GRAY)
        else:
            txt(ax, x + 0.6, 0.45, '3! = 6', fs=7.5, color=GRAY)
    txt(ax, 3.8, 2.05, 'D(n) = 2ᵏ · D(k) · D(r) mod 10,   k = ⌊n/5⌋, r = n mod 5 (tính ngược từ phải sang trái)', fs=8.6, color=NAVY, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'c2 ← 0;  c5 ← 0;  rest ← 1', 0, 0)
    f.node('b', 'proc', 'với i = 2..n:  x ← i;  tách hết thừa số 2, 5 khỏi x (đếm c2, c5)\nrest ← rest · x mod 10', 0, -0.7)
    f.node('c', 'proc', 'd ← rest · 2^(c2 − c5) mod 10', 0, -1.4)
    f.node('e', 'end', 'In c5 (số chữ số 0) và d', 0, -2.0)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'e')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'D(n)', 0, 0)
    f.node('b', 'dec', 'n < 5 ?', 0, -0.75)
    f.node('c', 'end', 'trả về 1, 1, 2, 6, 4', 2.6, -0.75)
    f.node('d', 'proc', 'k ← n / 5;  r ← n mod 5', 0, -1.6)
    f.node('e', 'end', 'trả về (2ᵏ mod 10) · D(k) · D(r) mod 10', 0, -2.25)
    f.edge('a', 'b'); f.edge('b', 'c', 'r', 'l', label='Đúng'); f.edge('b', 'd', label='Sai', lpos=(0.25, -1.27)); f.edge('d', 'e')
    f.draw(path)

def make(F):
    pairs(F('pairs')); legendre(F('legendre')); trap(F('trap')); chain(F('chain')); naive_flow(F('naive')); opt_flow(F('opt'))
