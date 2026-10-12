from figlib import *

def stars(path):
    fig, ax = new(6.8, 2.6)
    # phát trước mỗi bạn 1 cái
    txt(ax, 0.1, 2.35, 'Bước 1: phát trước mỗi bạn t = 1 cái', fs=8.8, ha='left', bold=True, color=NAVY)
    for i, c in enumerate(['#E06666', '#6FA8DC', '#93C47D']):
        ax.add_patch(Circle((0.45 + i * 0.75, 1.95), 0.14, facecolor=c, edgecolor='#555555'))
        txt(ax, 0.45 + i * 0.75, 1.68, 'bạn %d' % (i + 1), fs=7.5, color=GRAY)
    txt(ax, 2.7, 1.95, 'còn 10 − 3 = 7 cái, chia tùy ý', fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, 0.1, 1.3, 'Bước 2: xếp 7 kẹo và 2 vạch ngăn vào 9 ô; mỗi cách chọn vị trí 2 vạch là một cách chia', fs=8.8, ha='left', bold=True, color=NAVY)
    seq = 'ooo|o|ooo'
    for i, ch in enumerate(seq):
        x = 0.4 + i * 0.5
        cell(ax, x, 0.55, 0.46, 0.46, '', 'plain', lw=0.6)
        if ch == 'o':
            ax.add_patch(Circle((x + 0.23, 0.78), 0.13, facecolor='#F4B183', edgecolor=ORANGE, lw=0.9, zorder=4))
        else:
            ax.plot([x + 0.23] * 2, [0.58, 0.98], color=DRED, lw=3, zorder=4)
    txt(ax, 0.4 + 9 * 0.5 + 0.15, 0.78, '→ (3, 1, 3) + 1 mỗi bạn = (4, 2, 4)', fs=8.5, ha='left', color=NAVY)
    txt(ax, 3.4, 0.2, 'Số cách = C(9, 2) = 36', fs=9.5, color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'go(i, left): số cách chia left kẹo cho các bạn i..k−1', 0, 0)
    f.node('c', 'dec', 'i = k ?', 0, -0.75)
    f.node('o', 'end', '1 nếu left = 0, ngược lại 0', 2.7, -0.75)
    f.node('l', 'proc', 'tổng go(i + 1, left − x) với x = t, t + 1, ..., left', 0, -1.55)
    f.edge('s', 'c'); f.edge('c', 'o', 'r', 'l', label='Đúng'); f.edge('c', 'l', label='Sai', lpos=(0.3, -1.15))
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'fact[0..2·10⁶];  ifact[N] ← fact[N]ᵖ⁻²;  ifact[i−1] ← ifact[i]·i', 0, 0)
    f.node('c', 'dec', 'k · t > n ?  (long long)', 0, -0.8)
    f.node('z', 'io', 'In 0', 2.6, -0.8)
    f.node('o', 'io', 'm ← n − k·t;   in C(m + k − 1, k − 1)', 0, -1.6)
    f.edge('s', 'c'); f.edge('c', 'z', 'r', 'l', label='Đúng'); f.edge('c', 'o', label='Sai', lpos=(0.3, -1.22))
    f.draw(path)

def make(F):
    stars(F('stars')); naive_flow(F('naive')); opt_flow(F('opt'))
