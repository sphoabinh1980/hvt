from figlib import *

def mirror(path):
    fig, ax = new(7.6, 2.2)
    c = 0.42
    def row(x0, y, digs, kinds, lab):
        for i, (d, k) in enumerate(zip(digs, kinds)):
            cell(ax, x0 + i * c, y, c - 0.04, 0.38, d, k, fs=10, bold=k == 'ans')
        txt(ax, x0 - 0.15, y + 0.19, lab, fs=8.5, ha='right', color=NAVY, bold=True)
    txt(ax, 0.9, 1.95, 'nửa đầu', fs=8, color=DRED)
    row(1.0, 1.4, '202', ['ans'] * 3, 'h = 202')
    row(4.2, 1.4, '20202', ['ans'] * 3 + ['done'] * 2, 'độ dài lẻ:')
    row(4.2, 0.75, '202202', ['ans'] * 3 + ['done'] * 3, 'độ dài chẵn:')
    arrow(ax, (2.3, 1.59), (3.1, 1.59), color=GRAY)
    arrow(ax, (2.3, 1.45), (3.1, 0.95), color=GRAY)
    txt(ax, 3.8, 0.2, 'Ô vàng: nửa đầu (chọn tự do, chữ số đầu khác 0). Ô xanh: chép ngược nửa đầu (bỏ chữ số giữa nếu độ dài lẻ).', fs=7.8, color=NAVY)
    save(fig, path)

def count2026(path):
    fig, ax = new(7.6, 2.4)
    segs = [('1..9', 9, 'in'), ('11..99', 9, 'done'), ('101..999', 90, 'green')]
    x = 0.2
    for lab, n, k in segs:
        w = 0.5 + n / 90 * 1.6
        cell(ax, x, 1.55, w, 0.42, '%d số' % n, k, fs=8.5, bold=True)
        txt(ax, x + w / 2, 2.12, lab, fs=8, color=NAVY)
        x += w + 0.08
    txt(ax, x + 0.1, 1.76, '= 108 số đối xứng có ít hơn 4 chữ số', fs=8.5, ha='left', color=NAVY)
    txt(ax, 0.2, 1.15, 'Bốn chữ số, nửa đầu h có 2 chữ số, h ≤ 20 (hai chữ số đầu của 2026):', fs=8.5, ha='left', bold=True, color=NAVY)
    for i, hh in enumerate(range(10, 21)):
        p = int(str(hh) + str(hh)[::-1])
        k = 'ans' if hh == 20 else 'done'
        cell(ax, 0.2 + i * 0.66, 0.5, 0.62, 0.38, str(p), k, fs=7.6, bold=hh == 20)
        txt(ax, 0.2 + i * 0.66 + 0.31, 0.33, 'h=%d' % hh, fs=6.5, color=GRAY)
    txt(ax, 3.8, 0.05, 'h = 10..19: 10 số (chắc chắn < 2026);  h = 20: 2002 ≤ 2026 nên đếm thêm 1.  Tổng 108 + 10 + 1 = 119.', fs=8, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R;  cnt ← 0', 0, 0)
    f.node('b', 'proc', 'với x = L..R:  nếu rev(x) = x thì cnt++', 0, -0.6)
    f.node('c', 'end', 'In cnt', 0, -1.2)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'dem(n):  len ← số chữ số của n', 0, 0)
    f.node('b', 'proc', 'cnt ← Σ 9 · 10^(⌈L/2⌉ − 1) với L = 1..len − 1', 0, -0.6)
    f.node('c', 'proc', 'half ← ⌈len/2⌉ chữ số đầu của n;  cnt += half − 10^(⌈len/2⌉ − 1)', 0, -1.2)
    f.node('d', 'proc', 'nếu gương(half) ≤ n thì cnt++', 0, -1.8)
    f.node('e', 'end', 'Đáp số: dem(R) − dem(L − 1)', 0, -2.4)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd'); f.edge('d', 'e')
    f.draw(path)

def make(F):
    mirror(F('mirror')); count2026(F('count')); naive_flow(F('naive')); opt_flow(F('opt'))
