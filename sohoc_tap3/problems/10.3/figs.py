from figlib import *

def line_fig(path):
    fig, ax = new(6.8, 1.9)
    x0, sc = 0.3, 6.2 / 30
    def X(v): return x0 + (v + 5) * sc
    line(ax, [(X(-5), 0.9), (X(25), 0.9)], color=GRAY)
    for v in range(-5, 26):
        ax.plot([X(v)] * 2, [0.85, 0.95], color=GRAY, lw=0.6)
    ax.add_patch(Rectangle((X(0), 0.78), X(20) - X(0), 0.24, facecolor='#E2F0D9', edgecolor=GREEN, lw=1, zorder=1))
    for v in [-6, -1, 4, 9, 14, 19, 24]:
        if v < -5: continue
        inside = 0 <= v <= 20
        kind = 'ans' if v == 4 else ('done' if inside else 'gray')
        fc, ec, _ = KIND[kind]
        ax.add_patch(Circle((X(v), 0.9), 0.09, facecolor=fc, edgecolor=ec, lw=1.4, zorder=4))
        txt(ax, X(v), 0.6, str(v), fs=8.5, color=NAVY if inside else GRAY, bold=inside)
    txt(ax, X(0), 1.15, 'L = 0', fs=8, color=GREEN, bold=True); txt(ax, X(20), 1.15, 'R = 20', fs=8, color=GREEN, bold=True)
    txt(ax, 3.4, 1.6, '6x ≡ 4 (mod 10)  ⇔  x ≡ 4 (mod 5): các nghiệm cách đều 5 đơn vị', fs=8.8, color=NAVY, bold=True)
    txt(ax, 3.4, 0.25, '4 nghiệm trong đoạn, nhỏ nhất là 4 (ô vàng)', fs=8.5, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, c, m, L, R', 0, 0)
    f.node('l', 'proc', 'với x = L..R:  nếu (a·x − c) mod m = 0: đếm, nhớ x đầu tiên', 0, -0.6)
    f.node('o', 'end', 'In số nghiệm và nghiệm đầu (hoặc 0)', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def chain(path):
    fig, ax = new(6.9, 1.8)
    steps = [('a·x ≡ c (mod m)', 'in'), ('g = gcd(a, m)\ng ∤ c ⇒ vô nghiệm', 'done'), ('a\'·x ≡ c\' (mod M)\nM = m/g', 'done'), ('x ≡ x₀ (mod M)\nx₀ = c\'·a\'⁻¹', 'done'), ('đầu tiên ≥ L\nđếm tới R', 'ans')]
    x = 0.05
    for k, (s, kd) in enumerate(steps):
        w = 1.25
        cell(ax, x, 0.75, w, 0.62, s, kd, fs=8, bold=kd == 'ans', lw=1.0 if kd == 'ans' else None)
        if k < 4: arrow(ax, (x + w + 0.01, 1.06), (x + w + 0.12, 1.06))
        x += w + 0.14
    txt(ax, 3.45, 0.35, 'Trước hết đưa a, c về [0, m): a % m của C++ có thể âm.', fs=8.3, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'a ← a mod m;  c ← c mod m  (không âm)', 0, 0)
    f.node('g', 'proc', 'g ← extgcd(a, m, u, v)', 0, -0.6)
    f.node('c', 'dec', 'g | c ?', 0, -1.35)
    f.node('z', 'io', 'In 0', 2.1, -1.35)
    f.node('x', 'proc', 'M ← m/g;  x₀ ← (c/g mod M)·(u mod M) mod M  [__int128]', 0, -2.12)
    f.node('f', 'proc', 'first ← L + ((x₀ − L) mod M)', 0, -2.72)
    f.node('d', 'dec', 'first ≤ R ?', 0, -3.47)
    f.node('o', 'io', 'In (R − first)/M + 1, first', 0, -4.27)
    f.node('z2', 'io', 'In 0', 2.2, -3.47)
    f.edge('s', 'g'); f.edge('g', 'c'); f.edge('c', 'z', 'r', 'l', label='Sai'); f.edge('c', 'x', label='Đúng', lpos=(0.33, -1.8))
    f.edge('x', 'f'); f.edge('f', 'd'); f.edge('d', 'o', label='Đúng', lpos=(0.33, -3.92)); f.edge('d', 'z2', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    line_fig(F('line')); naive_flow(F('naive')); chain(F('chain')); opt_flow(F('opt'))
