from figlib import *
import math
from matplotlib.patches import Circle

def node(ax, x, y, s, kind='done', r=0.27):
    fc, ec, _ = KIND[kind]
    ax.add_patch(Circle((x, y), r, facecolor=fc, edgecolor=ec, lw=1.3, zorder=4))
    txt(ax, x, y, s, fs=8.5 if len(s) < 4 else 7.5, bold=True)

def rho(path):
    fig, ax = new(7.6, 3.2)
    tail = ['2025', '33', '18', '65', '61']
    cyc = ['37', '58', '89', '145', '42', '20', '4', '16']
    for i, s in enumerate(tail):
        x = 0.45 + i * 0.85
        node(ax, x, 1.6, s, 'in')
        if i < 4: arrow(ax, (x + 0.28, 1.6), (x + 0.57, 1.6), color=NAVY)
    cx, cy, R = 5.75, 1.6, 1.25
    pos = []
    for k in range(8):
        a = math.pi - k * 2 * math.pi / 8
        pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    arrow(ax, (0.45 + 4 * 0.85 + 0.28, 1.6), (pos[0][0] - 0.28, pos[0][1]), color=NAVY)
    for k, s in enumerate(cyc):
        node(ax, pos[k][0], pos[k][1], s, 'ans' if s == '145' else 'done')
        x1, y1 = pos[k]; x2, y2 = pos[(k + 1) % 8]
        L = math.hypot(x2 - x1, y2 - y1)
        arrow(ax, (x1 + (x2 - x1) * 0.29 / L, y1 + (y2 - y1) * 0.29 / L), (x2 - (x2 - x1) * 0.29 / L, y2 - (y2 - y1) * 0.29 / L), color=NAVY, rad=-0.2)
    txt(ax, 2.15, 0.95, 'đuôi: μ = 5 phần tử', fs=8.5, color=ORANGE, bold=True)
    txt(ax, cx, cy, 'chu trình\nλ = 8', fs=8.5, color=BLUE, bold=True)
    txt(ax, 3.8, -0.35, 'Với K ≥ μ:  xₖ = x(μ + (K − μ) mod λ).   K = 10¹⁸: (10¹⁸ − 5) mod 8 = 3  →  xₖ = 145', fs=8.6, color=DRED, bold=True)
    save(fig, path)

def happy(path):
    fig, ax = new(7.6, 1.3)
    seq = ['7', '49', '97', '130', '10', '1']
    for i, s in enumerate(seq):
        x = 0.4 + i * 1.05
        node(ax, x, 0.75, s, 'ans' if s == '1' else 'done')
        if i < 5: arrow(ax, (x + 0.29, 0.75), (x + 0.76, 0.75), color=NAVY)
    arrow(ax, (0.4 + 5 * 1.05 + 0.2, 0.95), (0.4 + 5 * 1.05 + 0.2, 0.55), color=DRED, rad=-2.2)
    txt(ax, 6.65, 0.75, '1² = 1', fs=8.5, color=DRED, ha='left')
    txt(ax, 3.4, 0.15, '7 là số hạnh phúc: dãy rơi vào điểm dừng 1.', fs=8.2, color=NAVY)
    save(fig, path)

def kaprekar(path):
    fig, ax = new(7.6, 1.6)
    seq = [2026, 5994, 5355, 1998, 8082, 8532, 6174]
    for i, v in enumerate(seq):
        x = 0.15 + i * 1.07
        cell(ax, x, 0.85, 0.8, 0.42, str(v), 'ans' if v == 6174 else 'done', fs=9.5, bold=v == 6174)
        if i < 6: arrow(ax, (x + 0.82, 1.06), (x + 1.05, 1.06), color=GRAY)
    txt(ax, 3.8, 0.45, 'Mỗi bước: (chữ số xếp giảm dần) − (chữ số xếp tăng dần), giữ đủ 4 chữ số:  2026 → 6220 − 0226 = 5994.', fs=7.8, color=GRAY)
    txt(ax, 3.8, 0.15, '6174 → 7641 − 1467 = 6174: điểm dừng.', fs=8.4, color=DRED, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc x, K', 0, 0)
    f.node('b', 'proc', 'lặp K lần:  x ← tổng bình phương các chữ số của x', 0, -0.6)
    f.node('c', 'end', 'In x', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'x ← f(x);  K ← K − 1  (giờ x ≤ 1539)', 0, 0)
    f.node('b', 'proc', 'đi tiếp, ghi first[x] = chỉ số, lưu dãy seq\ncho tới khi gặp lại một giá trị (hoặc đủ K bước)', 0, -0.7)
    f.node('c', 'proc', 'μ ← first[x];  λ ← |seq| − μ', 0, -1.4)
    f.node('d', 'end', 'In seq[K] nếu K < |seq|, ngược lại seq[μ + (K − μ) mod λ]', 0, -2.0)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    rho(F('rho')); happy(F('happy')); kaprekar(F('kaprekar')); naive_flow(F('naive')); opt_flow(F('opt'))
