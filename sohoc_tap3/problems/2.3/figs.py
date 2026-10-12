from figlib import *

def amicable(path):
    fig, ax = new(6.6, 2.3)
    d220 = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    d284 = [1, 2, 4, 71, 142]
    cw = 0.42
    txt(ax, 0.1, 1.95, 'Ước thực sự của 220:', fs=8.5, ha='left', bold=True, color=NAVY)
    for i, d in enumerate(d220):
        cell(ax, 0.1 + i * cw, 1.45, cw - 0.04, 0.32, str(d), 'done', fs=8.5)
    txt(ax, 0.1 + 11 * cw + 0.1, 1.61, 'tổng = 284', fs=9, ha='left', bold=True, color=DRED)
    txt(ax, 0.1, 1.05, 'Ước thực sự của 284:', fs=8.5, ha='left', bold=True, color=NAVY)
    for i, d in enumerate(d284):
        cell(ax, 0.1 + i * cw, 0.55, cw - 0.04, 0.32, str(d), 'in', fs=8.5)
    txt(ax, 0.1 + 5 * cw + 0.1, 0.71, 'tổng = 220', fs=9, ha='left', bold=True, color=DRED)
    txt(ax, 3.3, 0.18, 'Bậc k: s(a) = b + k và s(b) = a + k.  Với mỗi a chỉ có đúng một ứng viên b = s(a) − k.', fs=8.5, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc N, k;  a ← 1', 0, 0)
    f.node('c', 'dec', 'a ≤ N ?', 0, -0.72)
    f.node('b', 'proc', 'b ← s(a) − k   (s tính bằng thử ước)', 0, -1.5)
    f.node('t', 'dec', 'a < b ≤ N và s(b) = a + k ?', 0, -2.35)
    f.node('g', 'proc', 'ghi nhận cặp (a, b)', 3.3, -2.35)
    f.node('i', 'proc', 'a ← a + 1', 0, -3.2)
    f.node('o', 'end', 'In các cặp', 2.4, -0.72)
    f.edge('s', 'c'); f.edge('c', 'b', label='Đúng', lpos=(0.32, -1.15)); f.edge('b', 't')
    f.edge('t', 'g', 'r', 'l', label='Đúng'); f.edge('t', 'i', label='Sai', lpos=(0.3, -2.92))
    f.edge('g', 'i', 'b', 'r', via=[(3.3, -3.2)])
    f.edge('i', 'c', 'l', 'l', via=[(-2.6, -3.2), (-2.6, -0.72)])
    f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def sieve(path):
    N = 12
    fig, ax = new(6.6, 3.2)
    cw, ch, x0, y0 = 0.42, 0.27, 0.95, 2.75
    for m in range(1, N + 1):
        cell(ax, x0 + (m - 1) * cw, y0, cw, ch, str(m), 'navy', fs=8.5, bold=True)
    txt(ax, 0.45, y0 + ch / 2, 'm', fs=9, bold=True, color=NAVY)
    s = [0] * (N + 1)
    for d in range(1, N // 2 + 1):
        y = y0 - d * ch
        cell(ax, 0.3, y, 0.42, ch, 'd=%d' % d, 'in', fs=8)
        for m in range(1, N + 1):
            if m % d == 0 and m > d:
                cell(ax, x0 + (m - 1) * cw, y, cw, ch, '+%d' % d, 'done', fs=8)
                s[m] += d
            else:
                cell(ax, x0 + (m - 1) * cw, y, cw, ch, '', 'plain', lw=0.4)
    y = y0 - (N // 2 + 1) * ch - 0.05
    cell(ax, 0.3, y, 0.42, ch, 's(m)', 'ans', fs=7.5, bold=True, lw=1.0)
    for m in range(1, N + 1):
        cell(ax, x0 + (m - 1) * cw, y, cw, ch, str(s[m]), 'ans', fs=8.5, bold=True, lw=1.0)
    txt(ax, x0 + N * cw + 0.12, y0 - 2 * ch, 'mỗi d chỉ\n"ghé" các bội\n2d, 3d, ...', fs=8, ha='left', color=BLUE)
    txt(ax, x0 + N * cw + 0.12, y + ch / 2, 's(12) = 16', fs=8.5, ha='left', color=DRED, bold=True)
    save(fig, path)

def memory(path):
    fig, ax = new(6.6, 1.9)
    x0, sc = 2.15, 4.2 / 85
    for i, (lab, mb, k) in enumerate([('mảng int', 40, 'done'), ('mảng long long', 80, 'pink')]):
        y = 1.15 - i * 0.55
        txt(ax, 0.1, y + 0.17, lab + ' (10⁷ phần tử)', fs=8.5, ha='left', color=NAVY)
        cell(ax, x0, y, mb * sc, 0.34, '%d MB' % mb, k, fs=9, bold=True)
    ax.plot([x0 + 64 * sc] * 2, [0.45, 1.65], color=DRED, lw=2, ls='--')
    txt(ax, x0 + 64 * sc, 1.78, 'giới hạn 64 MB', fs=8.5, color=DRED, bold=True)
    txt(ax, 3.3, 0.2, 's(n) < σ(n) ≤ 45 732 192 < 2³¹ − 1: kiểu int là đủ.', fs=8.5, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc N, k;  s[1..N] ← 0', 0, 0)
    f.node('a', 'proc', 'với mỗi d = 1..N/2:  s[j] += d  với j = 2d, 3d, ... ≤ N', 0, -0.62)
    f.node('b', 'proc', 'với mỗi a = 1..N:  b ← s[a] − k', 0, -1.24)
    f.node('t', 'dec', 'a < b ≤ N và s[b] = a + k ?', 0, -2.05)
    f.node('g', 'proc', 'ghi nhận (a, b)', 3.3, -2.05)
    f.node('o', 'end', 'In các cặp', 0, -2.9)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 't')
    f.edge('t', 'g', 'r', 'l', label='Đúng')
    f.edge('t', 'o', label='hết a', lpos=(0.45, -2.55), lcolor=NAVY)
    f.draw(path)

def make(F):
    amicable(F('amicable')); naive_flow(F('naive')); sieve(F('sieve')); memory(F('memory')); opt_flow(F('opt'))
