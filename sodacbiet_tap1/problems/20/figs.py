from figlib import *
from matplotlib.patches import Circle

def ptr(path):
    h = [1]; i = [0, 0, 0]; P = [2, 3, 5]; rows = []
    for k in range(1, 12):
        c = [h[i[j]] * P[j] for j in range(3)]; m = min(c); h.append(m)
        adv = [j for j in range(3) if c[j] == m]
        rows.append((k, c, m, adv))
        for j in adv: i[j] += 1
    fig, ax = new(7.4, 5.0)
    heads = ['k', '2 · h[i2]', '3 · h[i3]', '5 · h[i5]', 'h[k] = min', 'con trỏ tăng']
    xs = [0.1, 0.65, 1.75, 2.85, 3.95, 5.15]; ws = [0.5, 1.05, 1.05, 1.05, 1.15, 2.1]
    for x, w, t in zip(xs, ws, heads):
        cell(ax, x, 4.6, w, 0.34, t, 'navy', fs=8.5, bold=True)
    for r, (k, c, m, adv) in enumerate(rows):
        y = 4.18 - r * 0.38
        cell(ax, xs[0], y, ws[0], 0.34, str(k), 'plain', fs=9)
        for j in range(3):
            cell(ax, xs[1 + j], y, ws[1 + j], 0.34, str(c[j]), 'ans' if j in adv else 'done', fs=9, bold=j in adv)
        cell(ax, xs[4], y, ws[4], 0.34, str(m), 'green', fs=9, bold=True)
        cell(ax, xs[5], y, ws[5], 0.34, ', '.join(['i2', 'i3', 'i5'][j] for j in adv), 'pink' if len(adv) > 1 else 'plain', fs=9)
    txt(ax, 3.7, -0.05, 'Ô hồng: hai con trỏ cùng tăng, nhờ vậy 6, 10, 12, 15 không bị sinh hai lần.', fs=8.5, color=DRED)
    save(fig, path)

def dots(path):
    fig, ax = new(7.6, 1.75)
    x0 = 0.15
    for n in range(1, 6):
        for r in range(n):
            for c in range(r + 1):
                ax.add_patch(Circle((x0 + c * 0.2 + (n - 1 - r) * 0.1, 0.45 + (n - 1 - r) * 0.18 * 1.0), 0.07, facecolor='#9DC3E6', edgecolor=NAVY, lw=0.8, zorder=3))
        txt(ax, x0 + (n - 1) * 0.1 + 0.0, 0.15, 'T%s = %d' % ('₁₂₃₄₅'[n - 1], n * (n + 1) // 2), fs=8.5, color=NAVY, ha='left')
        x0 += n * 0.2 + 0.3
    x0 += 0.25
    for n in range(1, 4):
        for r in range(n):
            for c in range(n):
                ax.add_patch(Circle((x0 + c * 0.2, 0.45 + r * 0.2), 0.07, facecolor='#FFE699', edgecolor=DRED, lw=0.8, zorder=3))
        txt(ax, x0, 0.15, '%d² = %d' % (n, n * n), fs=8.5, color=DRED, ha='left')
        x0 += n * 0.2 + 0.4
    txt(ax, 3.8, 1.6, 'Số tam giác Tₙ = 1 + 2 + ... + n = n(n + 1)/2        Số chính phương n² = Tₙ + Tₙ₋₁', fs=9, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc n;  x ← 0;  k ← 0', 0, 0)
    f.node('b', 'proc', 'khi k < n: x++;  chia x cho 2, 3, 5 tới hết;\nnếu còn lại 1 thì k++', 0, -0.7)
    f.node('c', 'end', 'In x', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc n;  h[0] ← 1;  i2 = i3 = i5 = 0', 0, 0)
    f.node('b', 'proc', 'với k = 1 .. n − 1:\nh[k] ← min(2·h[i2], 3·h[i3], 5·h[i5])\ntăng mọi con trỏ cho giá trị bằng h[k]', 0, -0.85)
    f.node('c', 'end', 'In h[n − 1]', 0, -1.65)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def make(F):
    ptr(F('ptr')); dots(F('dots')); naive_flow(F('naive')); opt_flow(F('opt'))
