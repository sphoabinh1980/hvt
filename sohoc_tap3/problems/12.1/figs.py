from figlib import *

def merge(path):
    fig, ax = new(6.8, 2.5)
    rows = [('khởi đầu', '–', '–', '0', '1'), ('x ≡ 2 (mod 3)', 't ≡ 2', 't = 2', '2', '3'), ('x ≡ 3 (mod 5)', '3t ≡ 1', 't = 2', '8', '15'),
            ('x ≡ 2 (mod 7)', '15t ≡ 1 → t ≡ 1', 't = 1', '23', '105'), ('x ≡ 0 (mod 1)', 'luôn đúng', 't = 0', '23', '105')]
    hdr = ['phương trình', 'M·t ≡ a − r (mod m)', 't', 'r', 'M']
    ws = [1.6, 1.9, 0.8, 0.8, 0.8]
    x = 0.1
    for j, h in enumerate(hdr):
        cell(ax, x, 2.05, ws[j] - 0.04, 0.3, h, 'navy', fs=7.8, bold=True); x += ws[j]
    for i, row in enumerate(rows):
        x = 0.1; y = 1.7 - i * 0.33
        for j, v in enumerate(row):
            k = 'ans' if (i == 3 and j >= 3) else ('in' if j == 0 else 'plain')
            cell(ax, x, y, ws[j] - 0.04, 0.3, v, k, fs=8, lw=1.0 if k == 'ans' else None); x += ws[j]
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc hệ;  x ← L', 0, 0)
    f.node('c', 'dec', 'x mod mᵢ = aᵢ với mọi i ?', 0, -0.8)
    f.node('i', 'proc', 'x ← x + 1', -2.8, -0.8)
    f.node('o', 'end', 'In x', 0, -1.65)
    f.edge('s', 'c'); f.edge('c', 'i', 'l', 'r', label='Sai')
    f.edge('i', 'c', 't', 't', via=[(-2.8, -0.35), (0, -0.35)]); f.edge('c', 'o', label='Đúng', lpos=(0.33, -1.25))
    f.draw(path)

def jump(path):
    fig, ax = new(6.8, 2.0)
    x0, sc = 0.4, 6.0 / 250
    def X(v): return x0 + v * sc
    line(ax, [(X(0), 0.9), (X(250), 0.9)], color=GRAY)
    for v in (23, 128, 233):
        k = 'ans' if v == 128 else 'done'
        fc, ec, _ = KIND[k]
        ax.add_patch(Circle((X(v), 0.9), 0.09, facecolor=fc, edgecolor=ec, lw=1.4, zorder=4))
        txt(ax, X(v), 0.62, str(v), fs=9, bold=v == 128, color=DRED if v == 128 else NAVY)
    ax.plot([X(100)] * 2, [0.55, 1.0], color=GREEN, ls='--', lw=1.3)
    txt(ax, X(100), 0.45, 'L = 100', fs=8.5, color=GREEN, bold=True)
    arrow(ax, (X(23), 1.05), (X(128), 1.05), rad=-0.3, color=NAVY)
    txt(ax, X(75), 1.68, '+ M = 105', fs=8.5, color=NAVY, bold=True)
    txt(ax, 3.4, 0.1, 'x = L + ((r − L) mod M) = 100 + ((23 − 100) mod 105) = 100 + 28 = 128', fs=8.5, color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'r ← 0;  M ← 1', 0, 0)
    f.node('l', 'proc', 'với mỗi (m, a):  u ← M⁻¹ mod m (Euclid mở rộng)\nt ← (a − r) · u mod m;   r ← r + M·t;   M ← M·m', 0, -0.72)
    f.node('x', 'proc', 'x ← L + ((r − L) mod M)  (số dư không âm)', 0, -1.45)
    f.node('o', 'end', 'In x', 0, -2.05)
    f.edge('s', 'l'); f.edge('l', 'x'); f.edge('x', 'o')
    f.draw(path)

def make(F):
    merge(F('merge')); naive_flow(F('naive')); jump(F('jump')); opt_flow(F('opt'))
