from figlib import *

def bits(path):
    fig, ax = new(6.6, 2.6)
    cw, x0 = 1.1, 1.45
    rows = ['bit của b = 10', 'a (bình phương dần)', 'r sau bước này']
    for k, lab in enumerate(rows):
        txt(ax, x0 - 0.1, 2.0 - k * 0.5 + 0.17, lab, fs=8, ha='right', color=NAVY, bold=True)
    b = [0, 1, 0, 1]
    r = 1
    for i in range(4):
        X = x0 + i * cw
        cell(ax, X, 2.35, cw - 0.06, 0.3, 'lượt %d' % (i + 1), 'navy', fs=8, bold=True)
        cell(ax, X, 2.0, cw - 0.06, 0.34, str(b[i]), 'ans' if b[i] else 'gray', fs=10, bold=True, lw=1.0 if b[i] else None)
        cell(ax, X, 1.5, cw - 0.06, 0.34, '2%s = %d' % (['¹', '²', '⁴', '⁸'][i], 2 ** (2 ** i)), 'done', fs=8.5)
        if b[i]: r *= 2 ** (2 ** i)
        cell(ax, X, 1.0, cw - 0.06, 0.34, str(r), 'green' if b[i] else 'plain', fs=9, bold=b[i] == 1)
    txt(ax, x0 + 4 * cw + 0.05, 1.17, '= 2¹⁰', fs=9, ha='left', color=DRED, bold=True)
    txt(ax, 3.3, 0.5, '10 = 1010₂ = 8 + 2  ⇒  2¹⁰ = 2⁸ · 2².  Mỗi lượt: nếu bit thấp nhất là 1 thì r ← r · a;  luôn a ← a².', fs=8.3, color=NAVY)
    txt(ax, 3.3, 0.2, 'Số lượt = số chữ số nhị phân của b: 60 lượt với b ≤ 10¹⁸.', fs=8.3, color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b;  x ← a mod M;  r ← 1', 0, 0)
    f.node('l', 'proc', 'lặp b lần:  r ← r · x mod M', 0, -0.6)
    f.node('o', 'end', 'In r', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'power(a, b)', 0, 0)
    f.node('a', 'proc', 'a ← a mod M;  r ← 1', 0, -0.6)
    f.node('c', 'dec', 'b > 0 ?', 0, -1.32)
    f.node('d', 'dec', 'b lẻ ?', 0, -2.15)
    f.node('m', 'proc', 'r ← r · a mod M', 2.2, -2.15)
    f.node('q', 'proc', 'a ← a · a mod M;  b ← b / 2', 0, -2.95)
    f.node('o', 'end', 'trả về r', 2.2, -1.32)
    f.edge('s', 'a'); f.edge('a', 'c'); f.edge('c', 'd', label='Đúng', lpos=(0.32, -1.75)); f.edge('d', 'm', 'r', 'l', label='Đúng')
    f.edge('d', 'q', label='Sai', lpos=(0.3, -2.6)); f.edge('m', 'q', 'b', 'r', via=[(2.2, -2.95)])
    f.edge('q', 'c', 'l', 'l', via=[(-2.1, -2.95), (-2.1, -1.32)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def make(F):
    bits(F('bits')); naive_flow(F('naive')); opt_flow(F('opt'))
