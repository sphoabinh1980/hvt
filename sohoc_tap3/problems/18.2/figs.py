from figlib import *

def table(path):
    fig, ax = new(7.6, 3.6)
    c, h = 0.42, 0.24
    X0, Y0 = 0.9, 3.25
    for k in range(4):
        txt(ax, X0 + (3 - k) * c + c / 2, Y0 + 0.17, 'bit %d' % k, fs=7.5, color=NAVY, bold=True)
    for x in range(13):
        y = Y0 - (x + 1) * h
        txt(ax, X0 - 0.3, y + h / 2, str(x), fs=8, color=NAVY, bold=True)
        for k in range(4):
            b = x >> k & 1
            kind = ('ans' if 5 <= x <= 7 else 'done') if b else ('plain' if 5 <= x <= 7 or x > 4 else 'plain')
            cell(ax, X0 + (3 - k) * c, y, c - 0.03, h - 0.03, str(b), kind if b else 'plain', fs=7.5, bold=bool(b) and 5 <= x <= 7, lw=0.6 if not b else None)
        txt(ax, X0 + 4 * c + 0.25, y + h / 2, str(bin(x).count('1')), fs=7.5, color=GRAY)
    txt(ax, X0 + 4 * c + 0.25, Y0 + 0.17, 'pc', fs=7.5, color=GRAY)
    tx = 3.35
    txt(ax, tx, 3.2, 'Cột bit k lặp lại chu kì 2ᵏ⁺¹:', fs=8.8, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 2.92, '2ᵏ số 0 rồi 2ᵏ số 1 (cột bit 1: 0 0 1 1 0 0 1 1 ...)', fs=8.2, ha='left')
    txt(ax, tx, 2.5, 'Trên 0..n (n + 1 số), chia n + 1 cho 2ᵏ⁺¹:', fs=8.6, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 2.22, 'thương q, dư r  →  số bit 1 ở cột k là', fs=8.2, ha='left')
    txt(ax, tx + 0.2, 1.92, 'q · 2ᵏ + max(0, r − 2ᵏ)', fs=9.5, ha='left', bold=True, color=DRED)
    txt(ax, tx, 1.45, 'n = 12, cột 2: n + 1 = 13 = 1 · 8 + 5', fs=8.2, ha='left')
    txt(ax, tx + 0.2, 1.17, '→ 1 · 4 + (5 − 4) = 5 bit 1 (các số 4, 5, 6, 7, 12)', fs=8.2, ha='left')
    txt(ax, tx, 0.7, 'f(12) = 6 + 6 + 5 + 5 = 22 (bốn cột);  f(4) = 5', fs=8.6, ha='left', color=NAVY)
    txt(ax, tx, 0.4, 'Đoạn [5, 7] (ô vàng): f(7) − f(4) = 12 − 5 = 7', fs=8.8, ha='left', bold=True, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R', 0, 0)
    f.node('b', 'proc', 'f(n): với k = 0..60:  q, r ← (n + 1) chia 2ᵏ⁺¹\ns += q · 2ᵏ + max(0, r − 2ᵏ)   (unsigned __int128)', 0, -0.7)
    f.node('c', 'end', 'In f(R) − f(L − 1) bằng hàm in tự viết', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def make(F):
    table(F('table')); opt_flow(F('opt'))
