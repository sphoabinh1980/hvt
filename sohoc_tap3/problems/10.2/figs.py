from figlib import *

def table(path):
    p = 11
    inv = [0, 1]
    for i in range(2, 11): inv.append((p - p // i) * inv[p % i] % p)
    fig, ax = new(6.9, 2.75)
    cw, x0 = 0.52, 1.35
    labs = ['i', '⌊p/i⌋', 'p mod i', 'inv[p mod i]', 'inv[i]']
    for k, lab in enumerate(labs):
        txt(ax, x0 - 0.1, 2.3 - k * 0.42 + 0.15, lab, fs=8, ha='right', color=NAVY, bold=True)
    for i in range(1, 11):
        X = x0 + (i - 1) * cw
        cell(ax, X, 2.3, cw - 0.04, 0.3, str(i), 'navy', fs=8.5, bold=True)
        if i == 1:
            for k in range(1, 4): cell(ax, X, 2.3 - k * 0.42, cw - 0.04, 0.3, '–', 'gray', fs=8)
        else:
            cell(ax, X, 1.88, cw - 0.04, 0.3, str(p // i), 'plain', fs=8.5)
            cell(ax, X, 1.46, cw - 0.04, 0.3, str(p % i), 'in', fs=8.5)
            cell(ax, X, 1.04, cw - 0.04, 0.3, str(inv[p % i]), 'done', fs=8.5)
        cell(ax, X, 0.62, cw - 0.04, 0.3, str(inv[i]), 'ans', fs=9, bold=True, lw=1.0)
    txt(ax, 3.45, 0.2, 'inv[i] = (p − ⌊p/i⌋) · inv[p mod i] mod p.  Ví dụ i = 7: (11 − 1) · inv[4] = 10 · 3 = 30 ≡ 8;  7 · 8 = 56 ≡ 1.', fs=7.8, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc n, p', 0, 0)
    f.node('l', 'proc', 'với i = 1..n:  thử x = 1, 2, ... tới khi i · x mod p = 1', 0, -0.6)
    f.node('h', 'proc', 'H ← (H + x) mod p;   X ← X xor x', 0, -1.2)
    f.node('o', 'end', 'In H, X', 0, -1.8)
    f.edge('s', 'l'); f.edge('l', 'h'); f.edge('h', 'o')
    f.draw(path)

def derive(path):
    fig, ax = new(6.9, 2.2)
    steps = ['p = q·i + r\n0 < r < i', 'q·i + r ≡ 0\n(mod p)', 'nhân hai vế\nvới i⁻¹·r⁻¹', 'q·r⁻¹ + i⁻¹ ≡ 0', 'i⁻¹ ≡ −q·r⁻¹\n≡ (p − q)·r⁻¹']
    x = 0.1
    for k, s in enumerate(steps):
        w = 1.25
        cell(ax, x, 1.2, w, 0.55, s, 'ans' if k == 4 else ('in' if k == 0 else 'done'), fs=8.2, bold=k == 4, lw=1.0 if k == 4 else None)
        if k < 4: arrow(ax, (x + w + 0.01, 1.47), (x + w + 0.12, 1.47))
        x += w + 0.14
    txt(ax, 3.45, 0.75, 'r = p mod i < i: nghịch đảo của r đã tính xong khi xét i theo thứ tự tăng dần.', fs=8.5, color=NAVY)
    txt(ax, 3.45, 0.45, 'r > 0 vì p nguyên tố và 1 < i < p nên i không chia hết p.', fs=8.5, color=GRAY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'inv[1] ← 1;  H ← 1;  X ← 1', 0, 0)
    f.node('l', 'proc', 'với i = 2..n:  inv[i] ← (p − ⌊p/i⌋) · inv[p mod i] mod p', 0, -0.6)
    f.node('h', 'proc', 'H ← H + inv[i] (trừ p nếu ≥ p);   X ← X xor inv[i]', 0, -1.2)
    f.node('o', 'end', 'In H, X', 0, -1.8)
    f.edge('s', 'l'); f.edge('l', 'h'); f.edge('h', 'o')
    f.draw(path)

def make(F):
    table(F('table')); naive_flow(F('naive')); derive(F('derive')); opt_flow(F('opt'))
