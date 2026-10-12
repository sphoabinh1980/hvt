from figlib import *
import math

def cycle7(path):
    fig, ax = new(7.6, 2.9)
    rs = [1, 3, 2, 6, 4, 5]; ds = [1, 4, 2, 8, 5, 7]
    cx, cy, R = 1.6, 1.45, 1.05
    for i, r in enumerate(rs):
        a = math.pi / 2 - i * 2 * math.pi / 6
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        from matplotlib.patches import Circle
        ax.add_patch(Circle((x, y), 0.22, facecolor='#DEEBF7' if i else '#FFE699', edgecolor=BLUE if i else DRED, lw=1.4, zorder=4))
        txt(ax, x, y, str(r), fs=10, bold=True)
        a2 = math.pi / 2 - (i + 1) * 2 * math.pi / 6
        x2, y2 = cx + R * math.cos(a2), cy + R * math.sin(a2)
        mx, my = (x + x2) / 2, (y + y2) / 2
        arrow(ax, (x + (x2 - x) * 0.25, y + (y2 - y) * 0.25), (x + (x2 - x) * 0.75, y + (y2 - y) * 0.75), color=NAVY, rad=-0.15)
        txt(ax, cx + (mx - cx) * 1.35, cy + (my - cy) * 1.35, str(ds[i]), fs=9.5, color=DRED, bold=True)
    txt(ax, cx, cy, 'số dư\nmod 7', fs=8, color=GRAY)
    tx = 3.4
    txt(ax, tx, 2.6, 'Chia 1 cho 7 kiểu "chia tay":', fs=9, ha='left', bold=True, color=NAVY)
    rows = ['10 = 7 · 1 + 3', '30 = 7 · 4 + 2', '20 = 7 · 2 + 6', '60 = 7 · 8 + 4', '40 = 7 · 5 + 5', '50 = 7 · 7 + 1  ← số dư 1 lặp lại']
    for i, s in enumerate(rows):
        txt(ax, tx + 0.1, 2.25 - i * 0.28, s, fs=8.5, ha='left', family='monospace', color=DRED if i == 5 else '#1A1A1A')
    txt(ax, tx, 0.38, '1/7 = 0,(142857): chữ số đỏ là thương, số trong vòng tròn là số dư', fs=8.6, ha='left', color=DRED, bold=True)
    save(fig, path)

def rho(path):
    fig, ax = new(7.6, 2.0)
    pts = ['1', '10', '4']
    for i, s in enumerate(pts):
        x = 0.3 + i * 1.1
        cell(ax, x, 0.95, 0.7, 0.42, s, 'gray' if i < 2 else 'ans', fs=10, bold=i == 2)
        if i < 2: arrow(ax, (x + 0.72, 1.16), (x + 1.08, 1.16), color=NAVY)
        txt(ax, x + 0.35, 0.75, ['chữ số 0', 'chữ số 8', 'chữ số 3'][i], fs=7.5, color=GRAY)
    arrow(ax, (2.55, 1.38), (2.85, 1.38), color=DRED, rad=-2.5)
    txt(ax, 2.95, 1.7, '4 → 4', fs=8.5, color=DRED, ha='left')
    txt(ax, 4.1, 1.35, '1/12 = 0,08(3)', fs=11, ha='left', bold=True, color=NAVY)
    txt(ax, 4.1, 1.0, 'phần không tuần hoàn: 2 chữ số (08)', fs=8.6, ha='left')
    txt(ax, 4.1, 0.72, 'chu kì: 1 chữ số (3)', fs=8.6, ha='left')
    txt(ax, 4.1, 0.38, '12 = 2² · 3:  max(2, 0) = 2;  cấp của 10 mod 3 là 1', fs=8.3, ha='left', color=DRED)
    save(fig, path)

def cyclic(path):
    fig, ax = new(7.6, 2.3)
    base = '142857'
    for k in range(1, 7):
        v = str(int(base) * k); y = 2.0 - (k - 1) * 0.33
        txt(ax, 0.4, y, '142857 × %d =' % k, fs=9, ha='left', family='monospace')
        sh = (base + base).index(v)
        for j, ch in enumerate(v):
            cell(ax, 2.6 + j * 0.34, y - 0.14, 0.32, 0.28, ch, 'ans' if ch == '1' else 'done', fs=9, bold=ch == '1')
    txt(ax, 5.0, 1.5, 'Sáu tích là sáu vòng quay', fs=8.8, ha='left', color=NAVY, bold=True)
    txt(ax, 5.0, 1.22, 'của cùng một dãy chữ số.', fs=8.8, ha='left', color=NAVY, bold=True)
    txt(ax, 5.0, 0.8, '142857 × 7 = 999999', fs=8.6, ha='left', color=DRED, bold=True)
    txt(ax, 5.0, 0.52, '142857 = (10⁶ − 1) / 7', fs=8.6, ha='left', color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'r ← 1 mod n;  i ← 0;  pos ← rỗng', 0, 0)
    f.node('b', 'dec', 'r = 0 hoặc\nr đã có trong pos ?', 0, -0.95)
    f.node('c', 'proc', 'pos[r] ← i;  i++;  r ← 10r mod n', 3.3, -0.95)
    f.node('d', 'end', 'r = 0: in "i 0";  ngược lại in "pos[r]  i − pos[r]"', 0, -1.95)
    f.edge('a', 'b'); f.edge('b', 'c', 'r', 'l', label='Sai'); f.edge('c', 'b', 't', 't', via=[(3.3, -0.45), (0, -0.45)])
    f.edge('b', 'd', label='Đúng', lpos=(0.35, -1.6))
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'n = 2ᵃ · 5ᵇ · m  (gcd(m, 10) = 1)', 0, 0)
    f.node('b', 'proc', 'pre ← max(a, b)', 0, -0.6)
    f.node('c', 'proc', 'phi ← φ(m) (phân tích m bằng các số nguyên tố ≤ 10⁶)', 0, -1.2)
    f.node('d', 'proc', 'ord ← phi;  với mỗi ước nguyên tố p của phi:\nkhi p | ord và 10^(ord/p) ≡ 1 (mod m): ord ← ord / p', 0, -1.9)
    f.node('e', 'end', 'In pre và ord (ord = 0 nếu m = 1)', 0, -2.6)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.draw(path)

def make(F):
    cycle7(F('cycle7')); rho(F('rho')); cyclic(F('cyclic')); naive_flow(F('naive')); opt_flow(F('opt'))
