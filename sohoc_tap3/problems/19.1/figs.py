from figlib import *

def plot(path):
    fig, ax = new(7.6, 2.9)
    S = [0, 2, -5, 0, 4, 1, 2]
    X0, Y0, dx, dy = 0.6, 1.45, 0.62, 0.22
    line(ax, [(X0 - 0.2, Y0), (X0 + 6 * dx + 0.2, Y0)], color='#BFBFBF', lw=0.8)
    pts = [(X0 + i * dx, Y0 + s * dy) for i, s in enumerate(S)]
    line(ax, pts, color=BLUE, lw=1.4)
    for (i, j, col) in [(0, 3, DRED), (1, 6, ORANGE)]:
        line(ax, [pts[i], pts[j]], color=col, lw=1.4, ls='--')
    for i, (x, y) in enumerate(pts):
        hl = i in (0, 3, 1, 6)
        ax.plot([x], [y], 'o', ms=7, color=DRED if i in (0, 3) else (ORANGE if i in (1, 6) else BLUE), zorder=6)
        txt(ax, x, y + (0.2 if S[i] >= 0 and i != 5 else -0.2), 'S%s=%d' % ('₀₁₂₃₄₅₆'[i], S[i]), fs=7.8, color=NAVY)
    tx = 5.0
    txt(ax, tx, 2.5, 'S₀ = S₃ = 0  →  đoạn [1, 3]', fs=8.6, ha='left', color=DRED, bold=True)
    txt(ax, tx, 2.2, 'S₁ = S₆ = 2  →  đoạn [2, 6]', fs=8.6, ha='left', color=ORANGE, bold=True)
    txt(ax, tx, 1.7, 'Đoạn [l, r] có tổng 0', fs=8.4, ha='left')
    txt(ax, tx, 1.45, '⇔  Sᵣ = Sₗ₋₁:', fs=8.4, ha='left')
    txt(ax, tx, 1.2, 'hai điểm cùng độ cao.', fs=8.4, ha='left')
    save(fig, path)

def groups(path):
    fig, ax = new(7.4, 1.6)
    S = sorted([0, 1, 0, 1, 0, 1])
    txt(ax, 0.05, 1.4, 'Ví dụ 3: các tổng tiền tố 0, 1, 0, 1, 0, 1 sau khi sắp xếp', fs=8.8, ha='left', bold=True, color=NAVY)
    for i, s in enumerate(S):
        cell(ax, 0.2 + i * 0.62, 0.7, 0.56, 0.4, str(s), 'ans' if s == 0 else 'done', fs=10, bold=True)
    txt(ax, 0.2 + 1.5 * 0.62 - 0.03, 0.45, 'nhóm 3 số 0: C(3, 2) = 3', fs=8, color=DRED)
    txt(ax, 0.2 + 4.5 * 0.62 - 0.03, 0.45, 'nhóm 3 số 1: C(3, 2) = 3', fs=8, color=BLUE)
    txt(ax, 4.3, 0.9, '→  3 + 3 = 6 đoạn', fs=10, ha='left', bold=True, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'S[0] ← 0;  S[i] ← S[i − 1] + a[i]', 0, 0)
    f.node('b', 'proc', 'Sắp xếp S[0..n]', 0, -0.6)
    f.node('c', 'proc', 'Với mỗi nhóm c giá trị bằng nhau liền nhau:  ans += c(c − 1)/2', 0, -1.2)
    f.node('d', 'end', 'In ans', 0, -1.8)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    plot(F('plot')); groups(F('groups')); opt_flow(F('opt'))
