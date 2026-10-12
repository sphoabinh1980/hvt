from figlib import *
import math

def circle(path):
    fig, ax = new(7.4, 3.6)
    R = math.sqrt(325); s = 3.3 / R; ox, oy = 0.4, 0.15
    for i in range(0, 19):
        line(ax, [(ox + i * s, oy), (ox + i * s, oy + 18.2 * s)], color='#E0E0E0', lw=0.5)
        line(ax, [(ox, oy + i * s), (ox + 18.2 * s, oy + i * s)], color='#E0E0E0', lw=0.5)
    th = [k * math.pi / 2 / 100 for k in range(101)]
    line(ax, [(ox + R * math.cos(t) * s, oy + R * math.sin(t) * s) for t in th], color=NAVY, lw=1.5)
    line(ax, [(ox, oy), (ox + 18.3 * s, oy)], color=GRAY); line(ax, [(ox, oy), (ox, oy + 18.3 * s)], color=GRAY)
    line(ax, [(ox, oy), (ox + 13 * s, oy + 13 * s)], color=GRAY, ls='--', lw=0.8)
    pts = [(a, b) for a in range(19) for b in range(19) if a * a + b * b == 325]
    for a, b in pts:
        k = 'ans' if a <= b else 'gray'
        ax.add_patch(Circle((ox + a * s, oy + b * s), 0.07, facecolor='#FFE699' if a <= b else '#D9D9D9', edgecolor=DRED if a <= b else GRAY, lw=1.2, zorder=6))
        if a <= b:
            txt(ax, ox + a * s + 0.12, oy + b * s + 0.1, '(%d, %d)' % (a, b), fs=8.5, ha='left', color=DRED, bold=True)
    txt(ax, ox + 13.5 * s, oy + 12.5 * s, 'a = b', fs=8, color=GRAY, ha='left')
    txt(ax, 4.4, 3.0, 'x² + y² = 325 = 5² · 13', fs=10, ha='left', color=NAVY, bold=True)
    txt(ax, 4.4, 2.55, 'B = (2 + 1)(1 + 1) = 6 điểm trên cung', fs=9, ha='left')
    txt(ax, 4.4, 2.2, '0 ≤ x, 0 < y (kể cả hai phía đường chéo)', fs=9, ha='left')
    txt(ax, 4.4, 1.75, 'Lấy nửa a ≤ b: 3 cách', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, 4.4, 1.35, '1² + 18²,  6² + 17²,  10² + 15²', fs=9, ha='left', color=DRED)
    save(fig, path)

def grid(path):
    fig, ax = new(7.6, 2.75)
    S = {a * a + b * b for a in range(10) for b in range(10)}
    def isp(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
    for n in range(1, 51):
        r, c = (n - 1) // 10, (n - 1) % 10
        k = 'green' if n in S else 'plain'
        if isp(n) and n > 2: k = 'ans' if n % 4 == 1 else 'pink'
        cell(ax, 0.2 + c * 0.72, 2.2 - r * 0.42, 0.66, 0.36, str(n), k, fs=9, bold=isp(n) and n > 2)
    y = 0.0
    cell(ax, 0.2, y, 0.3, 0.22, '', 'ans'); txt(ax, 0.57, y + 0.11, 'nguyên tố 4k + 1: luôn được', fs=8, ha='left')
    cell(ax, 2.75, y, 0.3, 0.22, '', 'pink'); txt(ax, 3.12, y + 0.11, 'nguyên tố 4k + 3: không bao giờ', fs=8, ha='left')
    cell(ax, 5.45, y, 0.3, 0.22, '', 'green'); txt(ax, 5.82, y + 0.11, 'số khác viết được', fs=8, ha='left')
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc Q;  với mỗi truy vấn đọc n', 0, 0)
    f.node('b', 'proc', 'cnt ← 0;  với a = 0, 1, ... khi 2a² ≤ n:\nb ← ⌊√(n − a²)⌋;  nếu b² = n − a² thì cnt++', 0, -0.7)
    f.node('c', 'end', 'In cnt', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'proc', 'Sàng spf[] tới 10⁷', 0, 0)
    f.node('b', 'io', 'Với mỗi truy vấn đọc n', 0, -0.6)
    f.node('c', 'proc', 'phân tích n bằng spf: B ← Π (e + 1) với p ≡ 1 (mod 4)\nghi nhận nếu có p ≡ 3 (mod 4) với số mũ lẻ', 0, -1.3)
    f.node('d', 'dec', 'có p ≡ 3 mũ lẻ ?', 0, -2.15)
    f.node('e', 'end', 'In 0', 2.8, -2.15)
    f.node('g', 'end', 'In (B + [n chính phương] + [n = 2h²]) / 2', 0, -3.0)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e', 'r', 'l', label='Đúng'); f.edge('d', 'g', label='Sai', lpos=(0.3, -2.62))
    f.draw(path)

def make(F):
    circle(F('circle')); grid(F('grid')); naive_flow(F('naive')); opt_flow(F('opt'))
