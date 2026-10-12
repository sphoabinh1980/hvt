from figlib import *

def cycles(path):
    fig, ax = new(6.6, 3.45)
    cw, ch, x0, y0 = 0.5, 0.27, 1.05, 2.85
    txt(ax, 0.55, y0 + 0.2, 'd', fs=9, bold=True, color=NAVY)
    for b in range(1, 9):
        cell(ax, x0 + (b - 1) * cw, y0 + 0.07, cw, ch, 'b=%d' % b, 'navy', fs=8, bold=True)
    txt(ax, x0 + 8 * cw + 0.55, y0 + 0.2, 'chu kì', fs=8.5, bold=True, color=NAVY)
    for d in range(10):
        y = y0 - 0.2 - d * ch
        cell(ax, 0.42, y, 0.32, ch, str(d), 'in', fs=9, bold=True)
        seq = []
        v = 1
        for b in range(1, 9):
            v = v * d % 10
            seq.append(v)
        per = next(p for p in (1, 2, 4) if all(seq[i] == seq[i + p] for i in range(4)))
        for b in range(1, 9):
            kind = 'ans' if b <= per else 'done'
            cell(ax, x0 + (b - 1) * cw, y, cw, ch, str(seq[b - 1]), kind, fs=9, lw=1.0 if kind == 'ans' else None)
        txt(ax, x0 + 8 * cw + 0.55, y + ch / 2, str(per), fs=9, bold=True, color=DRED if per == 4 else NAVY)
    txt(ax, 3.3, 0.05, 'Mọi chu kì đều là ước của 4: chữ số cuối của dᵇ chỉ phụ thuộc vào b mod 4 (khi b ≥ 1).', fs=8.3, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc a, b (long long)', 0, 0)
    f.node('i', 'proc', 'd ← a mod 10;  r ← 1', 0, -0.6)
    f.node('c', 'dec', 'đã nhân đủ b lần?', 0, -1.35)
    f.node('m', 'proc', 'r ← r · d mod 10', -2.1, -1.35)
    f.node('o', 'end', 'In r', 0, -2.15)
    f.edge('s', 'i'); f.edge('i', 'c')
    f.edge('c', 'm', 'l', 'r', label='Sai')
    f.edge('m', 'c', 't', 't', via=[(-2.1, -0.95), (0, -0.95)])
    f.edge('c', 'o', label='Đúng', lpos=(0.3, -1.85))
    f.draw(path)

def mod4(path):
    fig, ax = new(6.6, 2.75)
    b = '98765432109876543210'
    x0, cw = 0.2, 0.26
    txt(ax, 0.2, 2.29, 'b =', fs=10, bold=True, color=NAVY, ha='left')
    for i, c in enumerate(b):
        kind = 'ans' if i >= len(b) - 2 else 'in'
        cell(ax, x0 + 0.35 + i * cw, 2.12, cw, 0.34, c, kind, fs=10, bold=kind == 'ans')
    xs = x0 + 0.35
    ax.annotate('', xy=(xs, 1.95), xytext=(xs + (len(b) - 2) * cw, 1.95), arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1))
    txt(ax, xs + (len(b) - 2) * cw / 2, 1.78, '= (phần đầu) · 100: chia hết cho 4 vì 100 = 4 · 25', fs=8.5, color=GRAY)
    xe = xs + (len(b) - 2) * cw
    ax.annotate('', xy=(xe, 1.95), xytext=(xe + 2 * cw, 1.95), arrowprops=dict(arrowstyle='<->', color=DRED, lw=1))
    txt(ax, xe - 0.1, 1.55, '10 mod 4 = 2', fs=8.5, color=DRED, bold=True)
    txt(ax, 0.35, 1.2, 'Cách 1 (Horner):  e ← (e · 10 + c) mod 4  cho từng chữ số c, từ trái sang phải.', fs=8.8, ha='left')
    txt(ax, 0.35, 0.85, 'Cách 2: chỉ cần hai chữ số cuối, vì b = 100 · q + (hai chữ số cuối).', fs=8.8, ha='left')
    txt(ax, 0.35, 0.45, 'Ví dụ 2: chữ số cuối của a là 9, b ≡ 2 (mod 4) → 9² = 81 → đáp số 1.', fs=8.8, ha='left', color=DRED, bold=True)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc xâu a, b', 0, 0)
    f.node('z', 'dec', 'b = "0" ?', 0, -0.72)
    f.node('o1', 'io', 'In 1', 2.0, -0.72)
    f.node('d', 'proc', 'd ← chữ số cuối của a', 0, -1.5)
    f.node('e', 'proc', 'e ← b mod 4 (Horner)', 0, -2.1)
    f.node('c', 'dec', 'e = 0 ?', 0, -2.85)
    f.node('f', 'proc', 'e ← 4', 2.0, -2.85)
    f.node('r', 'proc', 'r ← dᵉ mod 10', 0, -3.65)
    f.node('o', 'io', 'In r', 0, -4.25)
    f.edge('s', 'z'); f.edge('z', 'o1', 'r', 'l', label='Đúng')
    f.edge('z', 'd', label='Sai', lpos=(0.28, -1.22)); f.edge('d', 'e'); f.edge('e', 'c')
    f.edge('c', 'f', 'r', 'l', label='Đúng'); f.edge('c', 'r', label='Sai', lpos=(0.28, -3.35))
    f.edge('f', 'r', 'b', 'r', via=[(2.0, -3.65)])
    f.edge('r', 'o')
    f.draw(path)

def make(F):
    cycles(F('cycles')); naive_flow(F('naive')); mod4(F('mod4')); opt_flow(F('opt'))
