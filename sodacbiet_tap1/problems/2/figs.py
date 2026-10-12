from figlib import *
import math

def mantissa(path):
    fig, ax = new(7.6, 2.6)
    txt(ax, 0.1, 2.4, 'x = 100 · log₁₀2 = 30,10299957...', fs=10, ha='left', bold=True, color=NAVY)
    cell(ax, 0.25, 1.75, 1.3, 0.4, '30', 'done', fs=11, bold=True)
    cell(ax, 1.6, 1.75, 2.1, 0.4, '0,10299957...', 'ans', fs=11, bold=True)
    txt(ax, 0.9, 1.55, 'phần nguyên', fs=7.8, color=BLUE)
    txt(ax, 2.65, 1.55, 'phần lẻ', fs=7.8, color=DRED)
    txt(ax, 4.0, 2.05, '2¹⁰⁰ = 10³⁰ · 10^0,10299957 = 10³⁰ · 1,2676506...', fs=9.2, ha='left')
    txt(ax, 4.0, 1.75, '→ có 30 + 1 = 31 chữ số, bắt đầu bằng 126...', fs=9.2, ha='left', color=DRED, bold=True)
    X0, L, y = 0.4, 6.8, 0.55
    line(ax, [(X0, y), (X0 + L, y)], color=NAVY, lw=1.6)
    for d in range(1, 11):
        x = X0 + L * math.log10(d)
        line(ax, [(x, y - 0.08), (x, y + 0.08)], color=NAVY, lw=1.2)
        txt(ax, x, y - 0.24, str(d), fs=8.5, color=NAVY, bold=True)
    for d in range(1, 4):
        a, b = X0 + L * math.log10(d), X0 + L * math.log10(d + 1)
        txt(ax, (a + b) / 2 + (0.35 if d == 1 else 0), y + 0.2, 'chữ số đầu %d' % d, fs=6.8, color=GRAY)
    xm = X0 + L * 0.10299957
    ax.plot([xm], [y], 'o', ms=9, color=DRED, zorder=6)
    arrow(ax, (xm + 0.6, y + 0.65), (xm + 0.05, y + 0.08), color=DRED)
    txt(ax, xm + 0.65, y + 0.72, '10^0,103 = 1,2677', fs=8.5, color=DRED, ha='left', bold=True)
    txt(ax, X0 + L / 2, 0.02, 'Trục logarit: vị trí của phần lẻ trong [0, 1) quyết định các chữ số đầu', fs=8, color=GRAY)
    save(fig, path)

def benford(path):
    fig, ax = new(7.4, 2.7)
    obs = [301, 176, 125, 97, 79, 69, 56, 52, 45]
    th = [1000 * math.log10(1 + 1 / d) for d in range(1, 10)]
    X0, bw, sc = 0.6, 0.62, 0.0068
    line(ax, [(X0 - 0.1, 0.4), (X0 + 9 * 0.72, 0.4)], color=GRAY, lw=1)
    for i in range(9):
        x = X0 + i * 0.72
        cell(ax, x, 0.4, bw, obs[i] * sc, '', 'done')
        txt(ax, x + bw / 2, 0.4 + obs[i] * sc + 0.12, str(obs[i]), fs=7.5, color=NAVY)
        ax.plot([x + 0.05, x + bw - 0.05], [0.4 + th[i] * sc] * 2, color=DRED, lw=2, zorder=5)
        txt(ax, x + bw / 2, 0.24, str(i + 1), fs=8.5, bold=True)
    txt(ax, 4.6, 2.45, 'Cột xanh: số lũy thừa 2¹, ..., 2¹⁰⁰⁰ có chữ số đầu là d', fs=8.2, ha='left', color=NAVY)
    txt(ax, 4.6, 2.18, 'Vạch đỏ: dự đoán 1000 · log₁₀(1 + 1/d)', fs=8.2, ha='left', color=DRED)
    txt(ax, 3.8, 0.02, 'chữ số đầu d', fs=8, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc a, b;  d ← số lớn 1', 0, 0)
    f.node('b', 'proc', 'lặp b lần: d ← d · a  (nhân số lớn với số nhỏ)', 0, -0.6)
    f.node('c', 'proc', 'đổi d thành xâu s', 0, -1.2)
    f.node('e', 'end', 'In 3 kí tự đầu và 3 kí tự cuối của s', 0, -1.8)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'e')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc a, b', 0, 0)
    f.node('b', 'proc', 'x ← b · log₁₀ a  (long double);  f ← x − ⌊x⌋', -1.9, -0.75)
    f.node('c', 'proc', 'đầu ← ⌊10^(f + 2)⌋', -1.9, -1.45)
    f.node('d', 'proc', 'cuối ← aᵇ mod 1000\n(lũy thừa nhanh)', 2.0, -1.1)
    f.node('e', 'end', 'In đầu và cuối (cuối đủ 3 chữ số: %03lld)', 0, -2.2)
    f.edge('a', 'b', 'b', 't', via=[(0, -0.35), (-1.9, -0.35)]); f.edge('b', 'c')
    f.edge('a', 'd', 'b', 't', via=[(0, -0.35), (2.0, -0.35)])
    f.edge('c', 'e', 'b', 't', via=[(-1.9, -1.85), (0, -1.85)]); f.edge('d', 'e', 'b', 't', via=[(2.0, -1.85), (0, -1.85)])
    f.draw(path)

def make(F):
    mantissa(F('mantissa')); benford(F('benford')); naive_flow(F('naive')); opt_flow(F('opt'))
