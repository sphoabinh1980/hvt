from figlib import *

def lights(path):
    fig, ax = new(6.8, 2.9)
    x0, sc = 0.9, 5.6 / 34
    def X(v): return x0 + v * sc
    for blk, (a1, p1, a2, p2, ans, title, y0) in enumerate([(2, 3, 3, 5, 8, 'Câu 1: đèn 1 (2, 3), đèn 2 (3, 5)', 2.25), (10, 4, 0, 6, 18, 'Câu 3: đèn 1 (10, 4), đèn 2 (0, 6)', 0.95)]):
        txt(ax, 0.1, y0 + 0.42, title, fs=8.5, ha='left', color=NAVY, bold=True)
        for j, (a, p) in enumerate([(a1, p1), (a2, p2)]):
            y = y0 - j * 0.32
            txt(ax, x0 - 0.1, y, 'đèn %d' % (j + 1), fs=7.5, ha='right', color=GRAY)
            line(ax, [(X(0), y), (X(34), y)], color='#D9D9D9', lw=0.8)
            for t in range(a, 35, p):
                hit = t == ans
                ax.add_patch(Circle((X(t), y), 0.085 if hit else 0.06, facecolor='#FFE699' if hit else '#9DC3E6', edgecolor=DRED if hit else BLUE, lw=1.4 if hit else 0.7, zorder=3))
        if blk == 1:
            ax.add_patch(Circle((X(6), y0 - 0.16), 0.2, fill=False, edgecolor=GRAY, ls='--', lw=1.2))
            txt(ax, X(6), y0 - 0.55, '6: đèn 1 chưa bật', fs=7.5, color=GRAY)
        txt(ax, X(ans) + 0.15, y0 + 0.17, '→ %d' % ans, fs=8.5, ha='left', color=DRED, bold=True)
    for t in range(0, 35, 2):
        txt(ax, X(t), 0.1, str(t), fs=6.5, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 't₁ ← a₁;  t₂ ← a₂', 0, 0)
    f.node('c', 'dec', 't₁ = t₂ ?', 0, -0.75)
    f.node('o', 'end', 'In t₁', 2.2, -0.75)
    f.node('d', 'proc', 'tăng thời điểm nhỏ hơn: t₁ += p₁ hoặc t₂ += p₂\n(dừng, in −1 nếu vượt max(a₁, a₂) + p₁p₂)', 0, -1.6)
    f.edge('s', 'c'); f.edge('c', 'o', 'r', 'l', label='Đúng'); f.edge('c', 'd', label='Sai', lpos=(0.3, -1.15))
    f.edge('d', 'c', 'l', 'l', via=[(-3.0, -1.6), (-3.0, -0.75)])
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'r₁ ← a₁ mod p₁;  r₂ ← a₂ mod p₂;  g ← gcd(p₁, p₂)', 0, 0)
    f.node('c', 'dec', 'g | (r₂ − r₁) ?', 0, -0.78)
    f.node('n', 'io', 'In −1', 2.4, -0.78)
    f.node('t', 'proc', 's ← (r₂ − r₁)/g · (p₁/g)⁻¹ mod (p₂/g);   r ← r₁ + p₁·s;   L ← lcm', 0, -1.55)
    f.node('o', 'io', 'A ← max(a₁, a₂);   in A + ((r − A) mod L)', 0, -2.15)
    f.edge('s', 'c'); f.edge('c', 'n', 'r', 'l', label='Sai'); f.edge('c', 't', label='Đúng', lpos=(0.33, -1.2)); f.edge('t', 'o')
    f.draw(path)

def make(F):
    lights(F('lights')); naive_flow(F('naive')); opt_flow(F('opt'))
