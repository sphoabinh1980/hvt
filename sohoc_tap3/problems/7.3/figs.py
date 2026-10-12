from figlib import *

def table(path):
    a = [4, 6, 9, 10, 4]
    ps = [2, 3, 5]
    def e(x, p):
        c = 0
        while x % p == 0: x //= p; c += 1
        return c
    M = {p: max(e(x, p) for x in a) for p in ps}
    C = {p: sum(1 for x in a if e(x, p) == M[p]) for p in ps}
    fig, ax = new(6.6, 3.0)
    cw, ch, x0, y0 = 0.7, 0.34, 1.4, 2.45
    for j, p in enumerate(ps):
        cell(ax, x0 + j * cw, y0, cw - 0.04, 0.3, 'p = %d' % p, 'navy', fs=8.5, bold=True)
    for i, x in enumerate(a):
        y = y0 - (i + 1) * ch
        need = any(e(x, p) == M[p] and C[p] == 1 and M[p] > 0 for p in ps)
        cell(ax, x0 - 0.75, y, 0.68, ch - 0.04, 'a%s = %d' % ('₁₂₃₄₅'[i], x), 'ans' if need else 'in', fs=8.5, lw=1.0 if need else None)
        for j, p in enumerate(ps):
            v = e(x, p)
            k = 'yellow' if v == M[p] and v > 0 else 'plain'
            cell(ax, x0 + j * cw, y, cw - 0.04, ch - 0.04, str(v), k, fs=9, bold=k == 'yellow')
        if need:
            txt(ax, x0 + 3 * cw + 0.08, y + ch / 2 - 0.02, 'cần thiết', fs=8, ha='left', color=DRED, bold=True)
    y = y0 - 6 * ch - 0.05
    txt(ax, x0 - 0.1, y + 0.15, 'M(p)', fs=8.5, ha='right', bold=True, color=NAVY)
    txt(ax, x0 - 0.1, y - 0.2, 'đạt M', fs=8.5, ha='right', bold=True, color=NAVY)
    for j, p in enumerate(ps):
        cell(ax, x0 + j * cw, y, cw - 0.04, 0.3, str(M[p]), 'done', fs=9, bold=True)
        cell(ax, x0 + j * cw, y - 0.35, cw - 0.04, 0.3, str(C[p]), 'gray' if C[p] > 1 else 'green', fs=9, bold=True)
    tx = x0 + 3 * cw + 1.0
    txt(ax, tx, 2.2, 'L = 2² · 3² · 5 = 180', fs=9.5, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 1.85, 'Cột 2: hai số 4 cùng đạt 2² → xóa một số', fs=8, ha='left')
    txt(ax, tx, 1.62, 'vẫn còn số kia: không ai "độc quyền".', fs=8, ha='left')
    txt(ax, tx, 1.3, 'Cột 3: chỉ 9 đạt 3² → 9 cần thiết.', fs=8, ha='left')
    txt(ax, tx, 1.0, 'Cột 5: chỉ 10 đạt 5¹ → 10 cần thiết.', fs=8, ha='left')
    txt(ax, tx, 0.6, 'Số 6 = 2 · 3 không đạt max ở cột nào.', fs=8, ha='left', color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc dãy a', 0, 0)
    f.node('a', 'proc', 'L ← lcm(a₁, ..., aₙ) chính xác (__int128)', 0, -0.6)
    f.node('b', 'proc', 'với mỗi i: tính lại lcm khi bỏ aᵢ, so sánh với L', 0, -1.2)
    f.node('o', 'end', 'In L mod (10⁹ + 7) và số phần tử cần thiết', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def residue(path):
    fig, ax = new(6.6, 1.65)
    cell(ax, 0.2, 0.9, 2.9, 0.5, 'gcd(a, b) theo số thật', 'done', fs=9, bold=True)
    cell(ax, 3.5, 0.9, 2.9, 0.5, 'gcd(a mod m, b mod m)', 'pink', fs=9, bold=True)
    txt(ax, 3.3, 1.15, '≠', fs=16, color=DRED, bold=True)
    txt(ax, 1.65, 0.6, 'gcd(10⁹ + 8, 2) = 2', fs=8.5, color=NAVY)
    txt(ax, 4.95, 0.6, 'gcd(1, 2) = 1  (m = 10⁹ + 7)', fs=8.5, color=DRED)
    txt(ax, 3.3, 0.18, 'Phép lấy dư "đi qua" +, −, × nhưng KHÔNG đi qua gcd, lcm hay so sánh lớn nhỏ.', fs=8.5, color=NAVY, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc dãy a;  sàng spf tới max(a)', 0, 0)
    f.node('a', 'proc', 'Lượt 1: phân tích mọi aᵢ; với mỗi (p, e):\ne > M[p] → M[p] ← e, cnt[p] ← 1;   e = M[p] → cnt[p]++', 0, -0.72)
    f.node('b', 'proc', 'L ← Π p^M[p]  (mod 10⁹ + 7)', 0, -1.45)
    f.node('c', 'proc', 'Lượt 2: aᵢ cần thiết ⇔ có p với e = M[p] và cnt[p] = 1', 0, -2.05)
    f.node('o', 'end', 'In L và số phần tử cần thiết', 0, -2.65)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'o')
    f.draw(path)

def make(F):
    table(F('table')); naive_flow(F('naive')); residue(F('residue')); opt_flow(F('opt'))
