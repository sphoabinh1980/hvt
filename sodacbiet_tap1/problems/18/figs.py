from figlib import *

def sieve(path):
    N = 12
    fig, ax = new(7.6, 3.9)
    txt(ax, 0.4, 3.7, 'x', fs=9, color=GRAY)
    for x in range(1, N + 1):
        cell(ax, 0.75 + (x - 1) * 0.55, 3.5, 0.5, 0.34, str(x), 'navy', fs=9, bold=True)
    for d in range(1, 7):
        y = 3.5 - d * 0.42
        txt(ax, 0.4, y + 0.17, 'd = %d' % d, fs=8.5, color=GRAY)
        for x in range(1, N + 1):
            hit = x % d == 0 and x >= 2 * d
            cell(ax, 0.75 + (x - 1) * 0.55, y, 0.5, 0.34, '+%d' % d if hit else '', 'pink' if hit else 'plain', fs=8.5, lw=0.5)
    s = [0] * (N + 1)
    for d in range(1, N + 1):
        for m in range(2 * d, N + 1, d): s[m] += d
    y = 3.5 - 7 * 0.42 - 0.12
    txt(ax, 0.4, y + 0.17, 's[x]', fs=9, color=NAVY, bold=True)
    for x in range(1, N + 1):
        k = 'ans' if s[x] == x else 'green' if s[x] > x else 'done'
        cell(ax, 0.75 + (x - 1) * 0.55, y, 0.5, 0.34, str(s[x]), k, fs=9, bold=True)
    y2 = y - 0.42
    cell(ax, 0.75, y2, 0.3, 0.22, '', 'ans'); txt(ax, 1.12, y2 + 0.11, 's[x] = x: hoàn hảo (6)', fs=8, ha='left')
    cell(ax, 3.2, y2, 0.3, 0.22, '', 'green'); txt(ax, 3.57, y2 + 0.11, 's[x] > x: dư (12)', fs=8, ha='left')
    cell(ax, 5.3, y2, 0.3, 0.22, '', 'done'); txt(ax, 5.67, y2 + 0.11, 's[x] < x: thiếu', fs=8, ha='left')
    save(fig, path)

def pair(path):
    fig, ax = new(7.6, 2.3)
    A = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    B = [1, 2, 4, 71, 142]
    cell(ax, 0.1, 1.55, 0.8, 0.45, '220', 'navy', fs=11, bold=True)
    for i, d in enumerate(A):
        cell(ax, 1.05 + i * 0.5, 1.6, 0.46, 0.36, str(d), 'done', fs=8.5)
    txt(ax, 6.65, 1.78, '= 284', fs=11, ha='left', color=DRED, bold=True)
    cell(ax, 0.1, 0.55, 0.8, 0.45, '284', 'navy', fs=11, bold=True)
    for i, d in enumerate(B):
        cell(ax, 1.05 + i * 0.5, 0.6, 0.46, 0.36, str(d), 'green', fs=8.5)
    txt(ax, 3.65, 0.78, '= 220', fs=11, ha='left', color=DRED, bold=True)
    txt(ax, 3.8, 0.15, 'tổng các ước thực sự của số này bằng chính số kia', fs=9, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc N', 0, 0)
    f.node('b', 'proc', 'với a = 1 .. N: b ← s(a) (thử chia tới √a)\nnếu a < b ≤ N và s(b) = a: ghi nhận cặp (a, b)', 0, -0.7)
    f.node('c', 'end', 'In số cặp và các cặp', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc N;  s[1..N] ← 0', 0, 0)
    f.node('b', 'proc', 'với d = 1 .. N/2: cộng d vào s[2d], s[3d], ...', 0, -0.62)
    f.node('c', 'proc', 'với a = 1 .. N: b ← s[a];  nếu a < b ≤ N và s[b] = a: ghi nhận (a, b)', 0, -1.24)
    f.node('d', 'end', 'In số cặp và các cặp', 0, -1.86)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    sieve(F('sieve')); pair(F('pair')); naive_flow(F('naive')); opt_flow(F('opt'))
