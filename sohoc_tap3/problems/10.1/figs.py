from figlib import *

def bags(path):
    fig, ax = new(6.8, 2.7)
    def bag(x0, red, blue, title):
        ax.add_patch(FancyBboxPatch((x0, 0.9), 1.3, 1.25, boxstyle='round,pad=0,rounding_size=0.25', facecolor='#F7F7F7', edgecolor=NAVY, lw=1.3))
        txt(ax, x0 + 0.65, 2.32, title, fs=9, bold=True, color=NAVY)
        k = 0
        for c, n in (('#E06666', red), ('#6FA8DC', blue)):
            for _ in range(n):
                ax.add_patch(Circle((x0 + 0.3 + (k % 3) * 0.35, 1.85 - (k // 3) * 0.35), 0.13, facecolor=c, edgecolor='#555555', lw=0.8))
                k += 1
        txt(ax, x0 + 0.65, 0.65, 'P(đỏ) = %d/%d' % (red, red + blue), fs=8.5, color=DRED)
    bag(0.2, 1, 1, 'Túi 1'); bag(1.8, 1, 2, 'Túi 2')
    tx = 3.55
    txt(ax, tx, 2.2, 'P₁ = cả hai đỏ = 1/2 · 1/3 = 1/6', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, tx, 1.85, 'cả hai xanh = 1/2 · 2/3 = 1/3', fs=9, ha='left', color=BLUE)
    txt(ax, tx, 1.5, 'P₂ = ít nhất một đỏ = 1 − 1/3 = 2/3', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, tx, 1.0, 'Các túi độc lập: xác suất "cùng xảy ra"', fs=8.3, ha='left', color=NAVY)
    txt(ax, tx, 0.75, 'là tích; "ít nhất một" dùng phần bù.', fs=8.3, ha='left', color=NAVY)
    save(fig, path)

def modfrac(path):
    fig, ax = new(6.8, 1.9)
    rows = [('1/6', '6 · R ≡ 1', 'R = 166 666 668', '6 · 166 666 668 = 1 000 000 008 ≡ 1'),
            ('2/3', '3 · R ≡ 2', 'R = 666 666 672', '3 · 666 666 672 = 2 000 000 016 ≡ 2')]
    for i, (a, b, c, d) in enumerate(rows):
        y = 1.3 - i * 0.55
        cell(ax, 0.1, y, 0.7, 0.4, a, 'in', fs=10, bold=True)
        txt(ax, 0.95, y + 0.2, '→', fs=12, color=NAVY)
        cell(ax, 1.15, y, 1.2, 0.4, b, 'plain', fs=8.5)
        cell(ax, 2.45, y, 1.5, 0.4, c, 'ans', fs=8.5, bold=True, lw=1.0)
        txt(ax, 4.05, y + 0.2, d, fs=7.8, ha='left', color=GRAY)
    txt(ax, 3.4, 0.15, 'P/Q theo mô-đun p là số R ∈ [0, p) với Q · R ≡ P:  R = P · Qᵖ⁻² mod p (Fermat).', fs=8.3, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'X, Y, Z ← 1 (giá trị thật)', 0, 0)
    f.node('a', 'proc', 'mỗi túi: X ← X·x;  Y ← Y·y;  Z ← Z·(x + y)', 0, -0.6)
    f.node('b', 'proc', 'rút gọn X/Z và (Z − Y)/Z bằng gcd, rồi đổi sang mô-đun', 0, -1.2)
    f.node('o', 'end', 'In P₁, P₂', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'X, Y, Z ← 1', 0, 0)
    f.node('a', 'proc', 'mỗi túi: X ← X·x mod p;  Y ← Y·y mod p;  Z ← Z·(x + y) mod p', 0, -0.6)
    f.node('b', 'proc', 'inv ← Zᵖ⁻² mod p', 0, -1.2)
    f.node('c', 'proc', 'P₁ ← X · inv;   P₂ ← (1 − Y · inv + p) mod p', 0, -1.8)
    f.node('o', 'end', 'In P₁, P₂', 0, -2.4)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    bags(F('bags')); naive_flow(F('naive')); modfrac(F('modfrac')); opt_flow(F('opt'))
