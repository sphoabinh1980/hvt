from figlib import *
from matplotlib.patches import Rectangle

COLS = ['#FFE699', '#DEEBF7', '#FBE5D6', '#E2F0D9', '#EDE5F5', '#F8DEDD', '#FFF2CC', '#D9E1F2']

def blocks(n):
    out = []; i = 1
    while i <= n:
        q = n // i; j = n // q; out.append((i, j, q)); i = j + 1
    return out

def stair(path):
    fig, ax = new(7.6, 3.3)
    n = 20; w = 0.3; hs = 0.12
    B = blocks(n)
    for k, (i, j, q) in enumerate(B):
        for x in range(i, j + 1):
            ax.add_patch(Rectangle((0.3 + (x - 1) * w, 0.45), w - 0.02, q * hs, facecolor=COLS[k], edgecolor='#7F7F7F', lw=0.6, zorder=2))
            txt(ax, 0.3 + (x - 0.5) * w, 0.32, str(x), fs=6.8, color=GRAY)
        txt(ax, 0.3 + ((i + j) / 2 - 0.5) * w, 0.45 + q * hs + 0.1, 'q=%d' % q, fs=7.2, bold=True, color=NAVY)
    txt(ax, 3.3, 0.1, 'i', fs=8.5, color=GRAY)
    X = 6.55
    rows = [['khối', 'q', 'q · Σi']] + [['[%d, %d]' % (i, j) if i != j else '%d' % i, str(q), '%d · %d = %d' % (q, (i + j) * (j - i + 1) // 2, q * (i + j) * (j - i + 1) // 2)] for i, j, q in B]
    ws = [0.75, 0.35, 1.15]
    for r, row in enumerate(rows):
        x = X
        for c, v in enumerate(row):
            if r == 0: cell(ax, x, 3.0 - r * 0.29, ws[c], 0.27, v, 'navy', fs=7.5, bold=True)
            else:
                ax.add_patch(Rectangle((x, 3.0 - r * 0.29), ws[c], 0.27, facecolor=COLS[r - 1], edgecolor='#A6A6A6', lw=0.6, zorder=2))
                txt(ax, x + ws[c] / 2, 3.0 - r * 0.29 + 0.135, v, fs=7.5)
            x += ws[c]
    cell(ax, X, 3.0 - 9 * 0.29 - 0.04, sum(ws), 0.29, 'Tổng = 339', 'ans', fs=8.5, bold=True)
    save(fig, path)

def double(path):
    fig, ax = new(7.4, 2.5)
    n = 8; c = 0.3
    X0, Y0 = 0.9, 2.1
    txt(ax, X0 - 0.45, Y0 + 0.2, 'x \\ i', fs=7.5, color=GRAY)
    for i in range(1, n + 1):
        txt(ax, X0 + (i - 0.5) * c, Y0 + 0.2, str(i), fs=8, bold=True, color=NAVY)
    for x in range(1, n + 1):
        y = Y0 - x * c * 0.75
        txt(ax, X0 - 0.3, y + 0.11, str(x), fs=8, bold=True, color=NAVY)
        for i in range(1, n + 1):
            if x % i == 0:
                cell(ax, X0 + (i - 1) * c + 0.02, y, c - 0.04, c * 0.7, str(i), 'ans', fs=7)
        txt(ax, X0 + n * c + 0.35, y + 0.11, 'σ = %d' % sum(i for i in range(1, x + 1) if x % i == 0), fs=7.5, color=GRAY, ha='left')
    for i in range(1, n + 1):
        txt(ax, X0 + (i - 0.5) * c, Y0 - (n + 1) * c * 0.75 + 0.1, str(n // i), fs=8, bold=True, color=DRED)
    txt(ax, X0 - 0.4, Y0 - (n + 1) * c * 0.75 + 0.1, '⌊8/i⌋', fs=7.5, color=DRED, ha='center')
    tx = 4.3
    txt(ax, tx, 2.0, 'Cộng theo hàng (từng x):', fs=8.6, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 1.72, 'σ(1) + σ(2) + ... + σ(8) = 56', fs=8.6, ha='left')
    txt(ax, tx, 1.3, 'Cộng theo cột (từng ước i):', fs=8.6, ha='left', bold=True, color=NAVY)
    txt(ax, tx, 1.02, 'cột i có ⌊8/i⌋ ô, mỗi ô ghi i', fs=8.6, ha='left')
    txt(ax, tx, 0.74, 'Σ i · ⌊8/i⌋ = 8+8+6+8+5+6+7+8 = 56', fs=8.6, ha='left')
    txt(ax, tx, 0.36, 'Cùng một bảng, hai cách cộng: kết quả bằng nhau.', fs=8.4, ha='left', color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'ans ← 0', 0, 0)
    f.node('b', 'proc', 'với x = 1..n:  σ(x) bằng duyệt d ≤ √x;  ans += σ(x)', 0, -0.6)
    f.node('c', 'end', 'In ans', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'i ← 1;  ans ← 0', 0, 0)
    f.node('b', 'dec', 'i ≤ n ?', 0, -0.72)
    f.node('c', 'proc', 'q ← ⌊n/i⌋;  j ← ⌊n/q⌋\ns ← (i + j)(j − i + 1)/2  (__int128)\nans += q · s;  i ← j + 1', 3.0, -0.72)
    f.node('d', 'end', 'In ans', 0, -1.55)
    f.edge('a', 'b')
    f.edge('b', 'c', 'r', 'l', label='Đúng')
    f.edge('c', 'b', 't', 't', via=[(3.0, -0.2), (0, -0.2)][:1] + [(0, -0.2)])
    f.edge('b', 'd', label='Sai', lpos=(0.25, -1.25))
    f.draw(path)

def make(F):
    stair(F('stair')); double(F('double')); naive_flow(F('naive')); opt_flow(F('opt'))
