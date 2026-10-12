from figlib import *

def grid72(path):
    fig, ax = new(6.6, 2.8)
    cw, ch, x0, y0 = 0.75, 0.38, 1.0, 1.9
    for j, c in enumerate(['3⁰ = 1', '3¹ = 3', '3² = 9']):
        cell(ax, x0 + j * cw, y0 + 0.02, cw - 0.04, 0.32, c, 'navy', fs=8, bold=True)
    for i in range(4):
        cell(ax, x0 - 0.78, y0 - (i + 1) * ch, 0.72, ch - 0.04, '2%s = %d' % ('⁰¹²³'[i], 2 ** i), 'navy', fs=8, bold=True)
        for j in range(3):
            v = 2 ** i * 3 ** j
            cell(ax, x0 + j * cw, y0 - (i + 1) * ch, cw - 0.04, ch - 0.04, str(v), 'ans' if v == 72 else 'done', fs=9.5, lw=1.0 if v == 72 else None)
        cell(ax, x0 + 3 * cw + 0.1, y0 - (i + 1) * ch, 0.8, ch - 0.04, '%d · 13' % 2 ** i, 'in', fs=8)
    txt(ax, x0 + 3 * cw + 0.5, y0 + 0.18, 'tổng hàng', fs=8, color=ORANGE, bold=True)
    tx = x0 + 3 * cw + 1.15
    txt(ax, tx, 1.75, '72 = 2³ · 3²', fs=9.5, ha='left', color=NAVY, bold=True)
    txt(ax, tx, 1.45, 'số ước = 4 · 3 = 12', fs=9, ha='left')
    txt(ax, tx, 1.15, 'σ = (1 + 2 + 4 + 8)(1 + 3 + 9)', fs=9, ha='left')
    txt(ax, tx, 0.88, '   = 15 · 13 = 195', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, 3.3, 0.1, 'Mỗi ước chọn số mũ của 2 (4 cách) và của 3 (3 cách) độc lập.', fs=8.3, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n;  d ← 0;  s ← 0', 0, 0)
    f.node('l', 'proc', 'với k = 1..n:  nếu k | n thì d ← d + 1, s ← s + k', 0, -0.62)
    f.node('o', 'end', 'In d, s', 0, -1.24)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def spf(path):
    N = 24
    sp = [0] * (N + 1)
    for p in range(2, N + 1):
        if sp[p] == 0:
            for j in range(p, N + 1, p):
                if sp[j] == 0: sp[j] = p
    fig, ax = new(6.8, 2.7)
    cw, x0 = 0.25, 1.0
    for i in range(2, N + 1):
        cell(ax, x0 + (i - 2) * cw, 2.2, cw - 0.02, 0.28, str(i), 'navy', fs=7)
        k = 'ans' if sp[i] == i else {2: 'done', 3: 'in', 5: 'green', 7: 'purple'}.get(sp[i], 'plain')
        cell(ax, x0 + (i - 2) * cw, 1.9, cw - 0.02, 0.28, str(sp[i]), k, fs=7.5, lw=1.0 if k == 'ans' else None)
    txt(ax, x0 - 0.1, 2.34, 'n', fs=8, ha='right', bold=True, color=NAVY)
    txt(ax, x0 - 0.1, 2.04, 'spf[n]', fs=8, ha='right', bold=True, color=NAVY)
    chain = [360, 180, 90, 45, 15, 5, 1]
    divs = [2, 2, 2, 3, 3, 5]
    x = 0.3
    for i, v in enumerate(chain):
        cell(ax, x, 0.85, 0.6, 0.38, str(v), 'ans' if v == 1 else 'done', fs=9, bold=True)
        if i < len(divs):
            arrow(ax, (x + 0.62, 1.04), (x + 0.86, 1.04))
            txt(ax, x + 0.74, 1.22, '÷%d' % divs[i], fs=7.5, color=DRED, bold=True)
        x += 0.88
    txt(ax, 3.3, 0.45, '360 = 2³ · 3² · 5¹: mỗi bước chia cho spf hiện tại; gom các lần chia cùng p để có số mũ.', fs=8.2, color=NAVY)
    txt(ax, 3.3, 0.18, 'd = (3 + 1)(2 + 1)(1 + 1) = 24,   σ = 15 · 13 · 6 = 1170', fs=8.5, color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng spf tới 10⁷ (một lần)', 0, 0)
    f.node('r', 'io', 'Đọc n;  d ← 1;  s ← 1', 0, -0.6)
    f.node('c', 'dec', 'n > 1 ?', 0, -1.32)
    f.node('a', 'proc', 'p ← spf[n];  chia n cho p tới hết, đếm e, cộng dồn 1 + p + ... + pᵉ', 0, -2.1)
    f.node('b', 'proc', 'd ← d · (e + 1);  s ← s · (1 + p + ... + pᵉ)', 0, -2.7)
    f.node('o', 'io', 'In d, s', 2.3, -1.32)
    f.edge('s', 'r'); f.edge('r', 'c'); f.edge('c', 'a', label='Đúng', lpos=(0.32, -1.72)); f.edge('a', 'b')
    f.edge('b', 'c', 'l', 'l', via=[(-3.4, -2.7), (-3.4, -1.32)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    grid72(F('grid72')); naive_flow(F('naive')); spf(F('spf')); opt_flow(F('opt'))
