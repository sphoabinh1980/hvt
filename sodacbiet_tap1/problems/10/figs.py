from figlib import *
import math

def n153(path):
    fig, ax = new(7.6, 1.5)
    for i, (d, v) in enumerate([(1, 1), (5, 125), (3, 27)]):
        x = 0.4 + i * 0.6
        cell(ax, x, 0.75, 0.5, 0.5, str(d), 'in', fs=13, bold=True)
    txt(ax, 2.4, 1.0, '1³ + 5³ + 3³  =  1 + 125 + 27  =  153', fs=12, ha='left', bold=True, color=NAVY)
    txt(ax, 3.8, 0.3, 'Số có 3 chữ số; mỗi chữ số lũy thừa 3 (số chữ số), cộng lại được chính nó: số tự luân.', fs=8.2, color=GRAY)
    save(fig, path)

def bound(path):
    fig = plt.figure(figsize=(7.2, 2.5), dpi=200)
    ax = fig.add_axes([0.1, 0.2, 0.6, 0.72])
    Ls = list(range(1, 75))
    ys = [math.log10(L) + L * math.log10(9) - (L - 1) for L in Ls]
    ax.plot(Ls, ys, color=BLUE, lw=2)
    ax.axhline(0, color=DRED, lw=1.2)
    ax.axvline(61, color=GRAY, ls='--', lw=1)
    ax.fill_between(Ls, ys, 0, where=[y < 0 for y in ys], color='#F8DEDD')
    ax.text(62, 0.4, 'L = 61', fontsize=8, color=GRAY)
    ax.set_xlabel('số chữ số L', fontsize=8); ax.set_ylabel('log₁₀(L·9ᴸ / 10ᴸ⁻¹)', fontsize=8)
    ax.tick_params(labelsize=7)
    for sp in ('top', 'right'): ax.spines[sp].set_visible(False)
    fig.text(0.73, 0.55, 'Đường xanh trên 0: tổng lớn nhất\nvẫn ≥ số nhỏ nhất có L chữ số.', fontsize=7.6, color=NAVY)
    fig.text(0.73, 0.3, 'Từ L = 61 đường xanh dưới 0:\nkhông có số tự luân nào\ndài hơn 60 chữ số.', fontsize=7.6, color=DRED)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=200, facecolor='white', bbox_inches='tight', pad_inches=0.06); plt.close(fig)

def multiset(path):
    fig, ax = new(7.6, 2.0)
    rows = [('{1, 3, 5}', '1³ + 3³ + 5³ = 153', '153 → {1, 3, 5}', True), ('{0, 3, 7}', '0³ + 3³ + 7³ = 370', '370 → {0, 3, 7}', True),
            ('{1, 2, 3}', '1³ + 2³ + 3³ = 36', '36: chỉ có 2 chữ số', False)]
    for i, (a, b, c, ok) in enumerate(rows):
        y = 1.6 - i * 0.5
        cell(ax, 0.2, y - 0.17, 1.1, 0.34, a, 'in', fs=9, bold=True)
        arrow(ax, (1.35, y), (1.65, y), color=GRAY)
        txt(ax, 1.7, y, b, fs=8.8, ha='left')
        arrow(ax, (3.85, y), (4.15, y), color=GRAY)
        txt(ax, 4.2, y, c, fs=8.8, ha='left')
        txt(ax, 6.9, y, '✓' if ok else '✗', fs=12, color=GREEN if ok else RED, bold=True)
    txt(ax, 3.8, 0.1, 'Tổng chỉ phụ thuộc vào TẬP chữ số; mỗi tập chỉ cần tính một lần rồi kiểm tra tập chữ số của kết quả.', fs=8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc K', 0, 0)
    f.node('b', 'proc', 'với n = 1 .. 10ᴷ − 1:  L ← số chữ số;  s ← Σ dᴸ\nnếu s = n thì in n', 0, -0.7)
    f.node('c', 'end', 'Kết thúc', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'với L = 1..K:  pw[d] ← dᴸ', 0, 0)
    f.node('b', 'proc', 'chọn cnt[0], cnt[1], ..., cnt[9] ≥ 0 có tổng L  (đệ quy)', 0, -0.6)
    f.node('c', 'proc', 's ← Σ cnt[d] · pw[d]', 0, -1.2)
    f.node('d', 'dec', 's có L chữ số và\ntập chữ số của s = cnt ?', 0, -2.0)
    f.node('e', 'proc', 'ghi nhận s', 3.2, -2.0)
    f.node('g', 'end', 'Sắp xếp, in các số đã ghi nhận', 0, -2.9)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e', 'r', 'l', label='Đúng')
    f.edge('d', 'g', label='Sai', lpos=(0.3, -2.6))
    f.draw(path)

def make(F):
    n153(F('n153')); bound(F('bound')); multiset(F('multiset')); naive_flow(F('naive')); opt_flow(F('opt'))
