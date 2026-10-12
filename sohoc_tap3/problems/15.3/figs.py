from figlib import *
from matplotlib.patches import Circle as Ci

POS = {1: (0.4, 1.0), 2: (1.2, 1.75), 3: (1.2, 0.25), 4: (2.2, 0.25)}
EDG = [(1, 2), (1, 3), (2, 3), (3, 4)]

def small_graph(ax, ox, oy, s, walk=None, r=0.17):
    P = {k: (ox + x * s, oy + y * s) for k, (x, y) in POS.items()}
    for a, b in EDG:
        line(ax, [P[a], P[b]], color='#BFBFBF', lw=1.2, z=1)
    if walk:
        for i in range(len(walk) - 1):
            a, b = P[walk[i]], P[walk[i + 1]]
            L = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
            ux, uy = (b[0] - a[0]) / L * r * 1.1, (b[1] - a[1]) / L * r * 1.1
            arrow(ax, (a[0] + ux, a[1] + uy), (b[0] - ux, b[1] - uy), color=DRED, lw=1.3, rad=0.35, ms=8)
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            dx, dy = b[0] - a[0], b[1] - a[1]
            ax.text(mx + dy * 0.32, my - dx * 0.32, str(i + 1), fontsize=7, color=DRED, fontweight='bold', ha='center', va='center', zorder=8,
                    bbox=dict(boxstyle='circle,pad=0.12', fc='white', ec=DRED, lw=0.6))
    for k, (x, y) in P.items():
        hl = walk and k in (walk[0], walk[-1])
        ax.add_patch(Ci((x, y), r, facecolor='#FFE699' if hl else '#DEEBF7', edgecolor=DRED if hl else BLUE, lw=1.2, zorder=6))
        ax.text(x, y, str(k), ha='center', va='center', fontsize=8.5, fontweight='bold', zorder=7)

def walks(path):
    fig, ax = new(7.6, 3.2)
    small_graph(ax, 0.05, 0.9, 0.85, r=0.15)
    txt(ax, 1.05, 0.55, 'Mỗi cạnh = hai tuyến ngược chiều', fs=7.8, color=GRAY)
    W = [[1, 2, 1, 3], [1, 3, 1, 3], [1, 3, 2, 3], [1, 3, 4, 3]]
    for i, w in enumerate(W):
        ox = 2.45 + (i % 2) * 2.65; oy = 1.75 - (i // 2) * 1.5
        small_graph(ax, ox, oy, 0.62, walk=w, r=0.12)
        txt(ax, ox + 0.8, oy - 0.2, ' → '.join(map(str, w)), fs=8.3, color=DRED, bold=True)
    save(fig, path)

def cost(path):
    fig, ax = new(7.2, 1.85)
    txt(ax, 0.05, 1.65, 'Một bước của lũy thừa nhanh (n = 50):', fs=9, ha='left', bold=True, color=NAVY)
    cell(ax, 0.05, 1.0, 6.0, 0.4, 'ma trận × ma trận:  50³ = 125 000 phép nhân', 'pink', fs=8.6)
    cell(ax, 0.05, 0.45, 6.0 * 2500 / 125000 + 0.04, 0.4, '', 'green')
    txt(ax, 0.3, 0.65, 'vectơ × ma trận:  50² = 2 500 phép nhân  (ít hơn 50 lần)', fs=8.6, ha='left')
    txt(ax, 0.05, 0.15, 'Chỉ cần hàng s của A^K, tức e_s · A^K: nhân dần vectơ hàng với các lũy thừa tính sẵn.', fs=8.2, ha='left', color=GRAY)
    save(fig, path)

def query(path):
    fig, ax = new(7.6, 1.7)
    txt(ax, 0.05, 1.5, 'K = 13 = 1101₂ = 8 + 4 + 1', fs=9, ha='left', bold=True, color=NAVY)
    items = [('v = e_s', 'ans'), ('× A¹', 'done'), ('× A⁴', 'done'), ('× A⁸', 'done'), ('= e_s · A¹³', 'ans')]
    x = 0.05
    for s, k in items:
        w = 1.15 if k == 'done' else 1.45
        cell(ax, x, 0.75, w, 0.42, s, k, fs=9, bold=k == 'ans')
        x += w + 0.25
    txt(ax, 3.7, 0.4, 'A¹, A², A⁴, ..., A^(2⁵⁹) tính sẵn một lần (59 phép nhân ma trận), dùng chung cho mọi câu hỏi.', fs=8.2, color=GRAY)
    txt(ax, 3.7, 0.12, 'Mỗi câu hỏi: ≤ 60 phép nhân vectơ × ma trận; đáp số là phần tử thứ t của v.', fs=8.2, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'cnt ← e_s  (cnt[s] = 1)', 0, 0)
    f.node('b', 'proc', 'lặp K lần:  nxt[v] = Σ cnt[u] với mọi tuyến u → v', 0, -0.6)
    f.node('c', 'end', 'In cnt[t]', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc đồ thị;  P[0] ← A', 0, 0)
    f.node('b', 'proc', 'P[i] ← P[i − 1] · P[i − 1],  i = 1..59', 0, -0.6)
    f.node('c', 'io', 'Đọc câu hỏi s, t, K', 0, -1.2)
    f.node('d', 'proc', 'v ← e_s;  với mỗi bit i của K bằng 1:  v ← v · P[i]', 0, -1.8)
    f.node('e', 'end', 'In v[t]', 0, -2.4)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.edge('e', 'c', 'r', 'r', via=[(2.9, -2.4), (2.9, -1.2)], label='câu hỏi tiếp', lpos=(3.45, -1.8))
    f.draw(path)

def make(F):
    walks(F('walks')); cost(F('cost')); query(F('query')); naive_flow(F('naive')); opt_flow(F('opt'))
