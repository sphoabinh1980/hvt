from figlib import *

def table(path):
    can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    fig, ax = new(6.9, 3.6)
    cw, ch, x0, y0 = 0.47, 0.27, 1.0, 3.15
    for j, c in enumerate(chi):
        cell(ax, x0 + j * cw, y0, cw - 0.03, 0.27, c, 'navy', fs=6.5, bold=True)
    year = {}
    for x in range(60): year[(x % 10, x % 12)] = x
    for i, cn in enumerate(can):
        y = y0 - (i + 1) * ch
        cell(ax, x0 - 0.62, y, 0.58, ch - 0.03, cn, 'in', fs=7, bold=True)
        for j in range(12):
            if (i, j) in year:
                x = year[(i, j)]
                k = 'ans' if x == 42 else 'done'
                cell(ax, x0 + j * cw, y, cw - 0.03, ch - 0.03, str(x), k, fs=7.5, bold=x == 42, lw=1.0 if x == 42 else None)
            else:
                cell(ax, x0 + j * cw, y, cw - 0.03, ch - 0.03, '', 'gray')
    txt(ax, 3.45, 0.18, 'Ô vàng: Bính Ngọ = năm thứ 42 (năm 2026). Ô xám: Can và Chi khác tính chẵn lẻ, không bao giờ xuất hiện. Có lcm(10, 12) = 60 tên.', fs=7.6, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc m₁..m_k', 0, 0)
    f.node('a', 'proc', 'liệt kê tên của các năm 0 .. m₁···m_k − 1, đếm tên khác nhau', 0, -0.6)
    f.node('b', 'proc', 'mỗi câu hỏi: thử từng năm x ∈ [L, R]', 0, -1.2)
    f.node('o', 'end', 'In kết quả', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'o')
    f.draw(path)

def big(path):
    fig, ax = new(6.9, 1.9)
    x0, sc = 0.3, 6.3
    line(ax, [(x0, 0.95), (x0 + sc, 0.95)], color=GRAY)
    ax.plot([x0 + 0.62 * sc] * 2, [0.7, 1.25], color=GREEN, ls='--', lw=1.3)
    txt(ax, x0 + 0.62 * sc, 1.38, 'R', fs=9, color=GREEN, bold=True)
    ax.plot([x0 + 0.95 * sc] * 2, [0.7, 1.25], color=DRED, ls='--', lw=1.3)
    txt(ax, x0 + 0.95 * sc, 1.38, 'M', fs=9, color=DRED, bold=True)
    ax.add_patch(Circle((x0 + 0.33 * sc, 0.95), 0.09, facecolor='#FFE699', edgecolor=DRED, lw=1.4, zorder=4))
    txt(ax, x0 + 0.33 * sc, 0.68, 'r', fs=9, bold=True, color=DRED)
    txt(ax, x0, 0.68, '0', fs=8.5, color=NAVY)
    txt(ax, 3.45, 1.7, 'Khi M > R, lớp x ≡ r (mod M) có nhiều nhất MỘT phần tử trong [0, R]: chính là r.', fs=8.4, color=NAVY, bold=True)
    txt(ax, 3.45, 0.25, 'Không cần gộp tiếp (M có thể tới 10¹²⁰): chỉ kiểm tra r với các phương trình còn lại.', fs=8.4, color=DRED)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng spf tới 10⁶; phân tích mọi mᵢ', 0, 0)
    f.node('a', 'proc', 'số tên = Π p^(số mũ lớn nhất)  mod (10⁹ + 7)', 0, -0.6)
    f.node('b', 'proc', 'mỗi câu hỏi: (r, M) ← (0, 1); duyệt từng phương trình:\nM ≤ R: gộp (vô nghiệm → 0);   M > R: chỉ kiểm tra r mod mᵢ = cᵢ', 0, -1.32)
    f.node('c', 'proc', 'M ≤ R: đếm cấp số cộng trong [L, R];   M > R: 1 nếu L ≤ r ≤ R', 0, -2.05)
    f.node('o', 'end', 'In kết quả', 0, -2.65)
    for a, b in [('s', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'o')]: f.edge(a, b)
    f.draw(path)

def make(F):
    table(F('table')); naive_flow(F('naive')); big(F('big')); opt_flow(F('opt'))
