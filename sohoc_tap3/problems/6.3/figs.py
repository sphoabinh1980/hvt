from figlib import *

def three(path):
    fig, ax = new(6.8, 2.3)
    ds = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    nd = lambda x: sum(1 for k in range(1, x + 1) if x % k == 0)
    cw = 0.6
    txt(ax, 0.1, 2.05, 'Ước của 36 và số ước của từng ước:', fs=8.8, ha='left', bold=True, color=NAVY)
    for i, d in enumerate(ds):
        k = 'ans' if nd(d) == 3 else 'done'
        cell(ax, 0.15 + i * cw, 1.35, cw - 0.06, 0.4, str(d), k, fs=10, bold=k == 'ans')
        txt(ax, 0.15 + i * cw + cw / 2 - 0.03, 1.15, 'd = %d' % nd(d), fs=7.5, color=DRED if nd(d) == 3 else GRAY)
    txt(ax, 0.1, 0.7, 'x có đúng 3 ước  ⇔  x = p² với p nguyên tố  (ước: 1, p, p²).', fs=9, ha='left', color=NAVY, bold=True)
    txt(ax, 0.1, 0.4, 'Vậy đáp số = số số nguyên tố p mà p² | a  =  số thừa số nguyên tố của a có số mũ ≥ 2.', fs=8.5, ha='left', color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a;  cnt ← 0;  p ← 2', 0, 0)
    f.node('c', 'dec', 'p · p ≤ a ?', 0, -0.74)
    f.node('d', 'proc', 'chia a cho p tới hết, được số mũ e;\nnếu e ≥ 2: cnt ← cnt + 1;  p ← p + 1', 0, -1.6)
    f.node('o', 'end', 'In cnt', 2.4, -0.74)
    f.edge('s', 'c'); f.edge('c', 'd', label='Đúng', lpos=(0.32, -1.15))
    f.edge('d', 'c', 'l', 'l', via=[(-2.4, -1.6), (-2.4, -0.74)]); f.edge('c', 'o', 'r', 'l', label='Sai')
    f.draw(path)

def cases(path):
    fig, ax = new(6.8, 2.4)
    items = [('r = 1', 'không còn gì', '+0', 'gray'), ('r = q', 'q > 10⁴ nguyên tố', '+0', 'done'),
             ('r = q²', 'r chính phương', '+1', 'ans'), ('r = q · q\'', 'q ≠ q\'', '+0', 'done')]
    for i, (a, b, c, k) in enumerate(items):
        x = 0.1 + i * 1.68
        cell(ax, x, 1.2, 1.55, 0.5, a, k, fs=10, bold=True, lw=1.4 if k == 'ans' else None)
        txt(ax, x + 0.78, 0.98, b, fs=8, color=NAVY)
        txt(ax, x + 0.78, 0.72, c, fs=10, color=DRED if c == '+1' else GRAY, bold=True)
    txt(ax, 3.4, 2.1, 'Sau khi bóc hết thừa số ≤ 10⁴, mọi thừa số còn lại > 10⁴. Vì (10⁴)³ = 10¹² ≥ a, còn nhiều nhất 2 thừa số:', fs=8.2, color=NAVY)
    txt(ax, 3.4, 0.3, 'Chỉ cần kiểm tra r có phải số chính phương lớn hơn 1 không: không cần biết q là bao nhiêu!', fs=8.3, color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng 1229 số nguyên tố ≤ 10⁴', 0, 0)
    f.node('a', 'proc', 'với mỗi p ≤ 10⁴:  chia r cho p tới hết; e ≥ 2 thì cnt++', 0, -0.62)
    f.node('b', 'dec', 'r > 1 và r chính phương ?', 0, -1.45)
    f.node('c', 'proc', 'cnt ← cnt + 1', 2.9, -1.45)
    f.node('o', 'end', 'In cnt', 0, -2.3)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'c', 'r', 'l', label='Đúng'); f.edge('b', 'o', label='Sai', lpos=(0.3, -1.95))
    f.edge('c', 'o', 'b', 'r', via=[(2.9, -2.3)])
    f.draw(path)

def make(F):
    three(F('three')); naive_flow(F('naive')); cases(F('cases')); opt_flow(F('opt'))
