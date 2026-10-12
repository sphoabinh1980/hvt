from figlib import *
from math import gcd

def blink(path):
    fig, ax = new(6.6, 2.9)
    x0, sc = 1.0, 5.2 / 13
    for k, p in enumerate([2, 3, 4]):
        y = 2.3 - k * 0.5
        txt(ax, 0.1, y, 'đèn %d (t = %d)' % (k + 1, p), fs=8.5, ha='left', color=NAVY)
        ax.plot([x0, x0 + 13 * sc], [y, y], color='#D9D9D9', lw=1)
        for s in range(p, 14, p):
            hit = s == 12
            ax.add_patch(Circle((x0 + s * sc, y), 0.1 if hit else 0.075, facecolor='#FFE699' if hit else '#9DC3E6', edgecolor=DRED if hit else BLUE, lw=1.5 if hit else 0.8, zorder=3))
    for s in range(0, 14):
        txt(ax, x0 + s * sc, 0.95, str(s), fs=7.5, color=GRAY)
    ax.plot([x0 + 12 * sc] * 2, [1.1, 2.5], color=DRED, ls='--', lw=1.2)
    txt(ax, x0 + 12 * sc, 2.68, 'giây 12 = lcm(2, 3, 4)', fs=8.5, color=DRED, bold=True)
    txt(ax, 3.3, 0.55, 'Các đèn l..r cùng nháy lần đầu ở giây lcm(t[l], ..., t[r]).', fs=8.8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc dãy t và Q kịch bản', 0, 0)
    f.node('c', 'dec', 'còn kịch bản?', 0, -0.72)
    f.node('a', 'proc', 'v ← 1;  với i = l..r: v ← lcm(v, t[i]) (chặn ở INF)', 0, -1.55)
    f.node('o', 'io', 'In v (hoặc −1 nếu v = INF)', 0, -2.15)
    f.node('e', 'end', 'Kết thúc', 2.6, -0.72)
    f.edge('s', 'c'); f.edge('c', 'a', label='Đúng', lpos=(0.32, -1.18)); f.edge('a', 'o')
    f.edge('o', 'c', 'l', 'l', via=[(-3.0, -2.15), (-3.0, -0.72)])
    f.edge('c', 'e', 'r', 'l', label='Sai')
    f.draw(path)

def segs(path):
    t = [6, 4, 3, 10, 2, 9, 5, 8]
    n = len(t)
    fig, ax = new(6.6, 3.3)
    cw, x0 = 0.55, 1.15
    txt(ax, x0 - 0.12, 2.95 + 0.15, 'l', fs=9, ha='right', bold=True, color=NAVY)
    for i in range(n):
        cell(ax, x0 + i * cw, 2.95, cw - 0.04, 0.3, str(i + 1), 'navy', fs=8.5)
    txt(ax, x0 - 0.12, 2.55 + 0.15, 't[l]', fs=8.5, ha='right', bold=True, color=NAVY)
    for i in range(n):
        cell(ax, x0 + i * cw, 2.55, cw - 0.04, 0.3, str(t[i]), 'in', fs=9)
    pal = ['done', 'green', 'yellow', 'purple', 'pink', 'dblue']
    for rr, y in [(5, 1.95), (6, 1.45), (8, 0.95)]:
        txt(ax, x0 - 0.12, y + 0.15, 'r = %d' % rr, fs=8.5, ha='right', bold=True, color=NAVY)
        vals = []
        for l in range(1, rr + 1):
            v = 1
            for x in t[l - 1:rr]: v = v * x // gcd(v, x)
            vals.append(v)
        distinct = []
        for l in range(rr, 0, -1):
            if not distinct or vals[l - 1] != distinct[-1]: distinct.append(vals[l - 1])
        for l in range(1, rr + 1):
            k = distinct.index(vals[l - 1])
            cell(ax, x0 + (l - 1) * cw, y, cw - 0.04, 0.3, str(vals[l - 1]), pal[k % len(pal)], fs=8)
        txt(ax, x0 + n * cw + 0.08, y + 0.15, '%d giá trị' % len(distinct), fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, 3.3, 0.5, 'Mỗi ô: lcm(t[l..r]). Với r cố định, l giảm thì BCNN chỉ tăng, và mỗi lần đổi giá trị thì tăng ít nhất gấp đôi.', fs=8.2, color=NAVY)
    txt(ax, 3.3, 0.2, 'Cùng màu = cùng giá trị: lưu cả khối bằng một cặp (giá trị, l nhỏ nhất của khối).', fs=8.2, color=NAVY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc t; gom kịch bản theo r', 0, 0)
    f.node('c', 'dec', 'r = 1..n', 0, -0.72)
    f.node('a', 'proc', 'nseg ← [(t[r], r)];  với (v, lo) trong seg:\nv\' ← lcm(v, t[r]); trùng giá trị cuối thì gộp, khác thì thêm', 0, -1.62)
    f.node('b', 'proc', 'seg ← nseg', 0, -2.37)
    f.node('q', 'proc', 'với kịch bản (l, r): cặp đầu tiên có lo ≤ l cho đáp số', 0, -2.97)
    f.node('e', 'end', 'In đáp số theo thứ tự', 2.9, -0.72)
    f.edge('s', 'c'); f.edge('c', 'a', label='tiếp', lpos=(0.3, -1.08), lcolor=GREEN); f.edge('a', 'b'); f.edge('b', 'q')
    f.edge('q', 'c', 'l', 'l', via=[(-3.4, -2.97), (-3.4, -0.72)])
    f.edge('c', 'e', 'r', 'l', label='hết', lcolor=RED)
    f.draw(path)

def make(F):
    blink(F('blink')); naive_flow(F('naive')); segs(F('segs')); opt_flow(F('opt'))
