import math
from figlib import *

def grid(path):
    N = 8
    fig, ax = new(6.8, 3.1)
    cw, ch, x0, y0 = 0.42, 0.31, 0.9, 2.65
    txt(ax, x0 - 0.1, y0 + 0.15, 'b \\ a', fs=8, ha='right', color=NAVY, bold=True)
    for a in range(1, N):
        cell(ax, x0 + (a - 1) * cw, y0, cw - 0.03, 0.28, str(a), 'navy', fs=8, bold=True)
    for b in range(2, N + 1):
        y = y0 - (b - 1) * ch
        cell(ax, x0 - 0.45, y, 0.38, ch - 0.03, str(b), 'in', fs=8.5, bold=True)
        cnt = 0
        for a in range(1, N):
            if a < b:
                ok = math.gcd(a, b) == 1
                cnt += ok
                cell(ax, x0 + (a - 1) * cw, y, cw - 0.03, ch - 0.03, '%d/%d' % (a, b), 'done' if ok else 'gray', fs=6.5)
        txt(ax, x0 + (N - 1) * cw + 0.15, y + ch / 2, 'φ(%d) = %d' % (b, cnt), fs=8, ha='left', color=DRED, bold=True)
    txt(ax, x0 + (N - 1) * cw + 1.3, 1.6, 'Hàng mẫu b có đúng φ(b)', fs=8.5, ha='left', color=NAVY)
    txt(ax, x0 + (N - 1) * cw + 1.3, 1.35, 'phân số tối giản (ô xanh).', fs=8.5, ha='left', color=NAVY)
    txt(ax, x0 + (N - 1) * cw + 1.3, 0.95, 'Tổng mẫu 2..8: 1+2+2+4+2+6+4 = 21', fs=8.5, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc L, R;  cnt ← 0', 0, 0)
    f.node('l', 'proc', 'với b = L..R, a = 1..b − 1:  nếu gcd(a, b) = 1 thì cnt++', 0, -0.6)
    f.node('o', 'end', 'In cnt', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def phisieve(path):
    N = 12
    fig, ax = new(6.8, 2.5)
    cw, x0 = 0.42, 0.95
    phi = list(range(N + 1))
    rows = [('ban đầu', list(phi))]
    for p in (2, 3, 5, 7, 11):
        for j in range(p, N + 1, p): phi[j] -= phi[j] // p
        rows.append(('p = %d' % p, list(phi)))
    rows = rows[:4] + [('p = 7, 11', list(phi))]
    for k, (lab, vals) in enumerate(rows):
        y = 2.1 - k * 0.4
        txt(ax, x0 - 0.08, y + 0.14, lab, fs=7.5, ha='right', color=NAVY, bold=True)
        for i in range(1, N + 1):
            prev = rows[k - 1][1][i] if k else vals[i]
            kind = 'navy' if k == 0 else ('ans' if k == len(rows) - 1 else ('pink' if vals[i] != prev else 'plain'))
            cell(ax, x0 + (i - 1) * cw, y, cw - 0.03, 0.3, str(vals[i]), kind, fs=8, lw=1.0 if kind == 'ans' else None)
    txt(ax, 3.45, 0.1, 'Mỗi số nguyên tố p (nhận ra vì phi[p] vẫn bằng p) sửa mọi bội j: phi[j] ← phi[j] − phi[j]/p. Ô hồng: vừa thay đổi.', fs=7.8, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc mọi câu hỏi; N ← max R', 0, 0)
    f.node('a', 'proc', 'phi[i] ← i;  với p = 2..N mà phi[p] = p:  phi[j] −= phi[j]/p  (j bội của p)', 0, -0.6)
    f.node('b', 'proc', 'S[b] ← S[b − 1] + phi[b]  (b ≥ 2), S[1] = 0', 0, -1.2)
    f.node('o', 'end', 'Mỗi câu hỏi: in S[R] − S[L − 1]', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def make(F):
    grid(F('grid')); naive_flow(F('naive')); phisieve(F('phisieve')); opt_flow(F('opt'))
