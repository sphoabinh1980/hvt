from figlib import *

def isp(x):
    return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))

def register(path):
    N = 20
    fig, ax = new(6.8, 2.75)
    cw, x0 = 0.29, 0.95
    for i, x in enumerate(range(1, N + 1)):
        cell(ax, x0 + i * cw, 2.2, cw - 0.02, 0.3, str(x), 'navy', fs=7.5)
        cell(ax, x0 + i * cw, 1.85, cw - 0.02, 0.3, '', 'done' if isp(x) else 'gray')
        s = isp(x) and isp(x + 2)
        inq = 6 <= x <= 18
        cell(ax, x0 + i * cw, 1.5, cw - 0.02, 0.3, '1' if s else '0', ('ans' if inq else 'yellow') if s else ('green' if inq else 'plain'), fs=8, lw=1.0 if (s and inq) else None)
    txt(ax, x0 - 0.1, 2.35, 'x', fs=8, ha='right', color=NAVY, bold=True)
    txt(ax, x0 - 0.1, 2.0, 'ng.tố?', fs=8, ha='right', color=NAVY, bold=True)
    txt(ax, x0 - 0.1, 1.65, 's[x]', fs=8, ha='right', color=NAVY, bold=True)
    for p in [3, 5, 11, 17]:
        xa = x0 + (p - 1) * cw + cw / 2; xb = x0 + (p + 1) * cw + cw / 2
        ax.add_patch(matplotlib.patches.Arc(((xa + xb) / 2, 2.5), xb - xa, 0.3, theta1=0, theta2=180, color=DRED, lw=1))
    xa = x0 + 5 * cw; xb = x0 + 18 * cw
    ax.annotate('', xy=(xa, 1.3), xytext=(xb, 1.3), arrowprops=dict(arrowstyle='<->', color=GREEN, lw=1.2))
    txt(ax, (xa + xb) / 2, 1.13, 'truy vấn [6, 20]: đếm s[p] với p ∈ [a, b − 2] = [6, 18]', fs=8, color=GREEN, bold=True)
    txt(ax, 3.4, 0.7, 'Mỗi cặp (p, p + 2) được ghi danh tại p. Cặp nằm trọn trong [a, b]  ⇔  a ≤ p  và  p + 2 ≤ b.', fs=8.3, color=NAVY)
    txt(ax, 3.4, 0.42, 'Đáp số = t[b − 2] − t[a − 1], với t là mảng tiền tố của s.   Ở đây: 2 cặp (11, 13), (17, 19).', fs=8.3, color=DRED)
    save(fig, path)

def trap(path):
    fig, ax = new(6.8, 1.75)
    cw, x0 = 0.42, 0.4
    for i, x in enumerate(range(3, 16)):
        inq = 6 <= x <= 12
        cell(ax, x0 + i * cw, 0.85, cw - 0.03, 0.34, str(x), 'done' if isp(x) else ('plain' if inq else 'gray'), fs=8.5)
    a = x0 + 3 * cw; b = x0 + 10 * cw
    ax.add_patch(Rectangle((a - 0.03, 0.8), b - a + 0.03, 0.44, fill=False, edgecolor=GREEN, lw=2))
    txt(ax, (a + b) / 2, 1.4, 'đoạn [6, 12]', fs=8.5, color=GREEN, bold=True)
    for p, ok in [(5, False), (11, False)]:
        xa = x0 + (p - 3) * cw + cw / 2; xb = x0 + (p - 1) * cw + cw / 2
        ax.add_patch(matplotlib.patches.Arc(((xa + xb) / 2, 0.85), xb - xa, 0.45, theta1=180, theta2=360, color=DRED, lw=1.3))
    txt(ax, x0 + 9 * cw, 0.4, '(11, 13): 13 > 12, "thò" ra phải', fs=8, color=DRED, ha='left')
    txt(ax, x0 + 0.1, 0.4, '(5, 7): 5 < 6, thò ra trái', fs=8, color=DRED, ha='left')
    txt(ax, 3.4, 0.08, 't[12] − t[5] đếm nhầm cặp (11, 13): in 1 thay vì 0.', fs=8.5, color=NAVY, bold=True)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b;  c ← 0', 0, 0)
    f.node('l', 'proc', 'với p = a .. b − 2:  nếu isPrime(p) và isPrime(p + 2): c ← c + 1', 0, -0.62)
    f.node('o', 'end', 'In c', 0, -1.24)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng tới 10⁷ + 2', 0, 0)
    f.node('a', 'proc', 't[x] ← t[x − 1] + [x và x + 2 đều nguyên tố],  x = 1..10⁷', 0, -0.6)
    f.node('c', 'dec', 'b − 2 < a ?', 0, -1.38)
    f.node('z', 'io', 'In 0', 2.3, -1.38)
    f.node('o', 'io', 'In t[b − 2] − t[a − 1]', 0, -2.18)
    f.edge('s', 'a'); f.edge('a', 'c'); f.edge('c', 'z', 'r', 'l', label='Đúng'); f.edge('c', 'o', label='Sai', lpos=(0.3, -1.85))
    f.draw(path)

import matplotlib
def make(F):
    register(F('register')); naive_flow(F('naive')); trap(F('trap')); opt_flow(F('opt'))
