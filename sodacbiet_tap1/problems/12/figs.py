from figlib import *

def squares(path):
    fig, ax = new(7.6, 1.9)
    rows = [('76', '5776'), ('376', '141376'), ('625', '390625')]
    for i, (n, sq) in enumerate(rows):
        y = 1.55 - i * 0.5
        txt(ax, 1.0, y, n + '² =', fs=10, ha='right', bold=True, family='monospace')
        x = 1.2
        for j, ch in enumerate(sq):
            hl = j >= len(sq) - len(n)
            cell(ax, x + j * 0.32, y - 0.16, 0.3, 0.32, ch, 'ans' if hl else 'plain', fs=9.5, bold=hl)
    txt(ax, 3.8, 1.15, 'Các chữ số cuối của n²', fs=8.8, ha='left', color=DRED, bold=True)
    txt(ax, 3.8, 0.85, 'chính là n (ô vàng).', fs=8.8, ha='left', color=DRED, bold=True)
    save(fig, path)

def lift(path):
    fig, ax = new(7.6, 2.6)
    fam6 = [('6', '36'), ('76', '5776'), ('376', '141376'), ('9376', '87909376'), ('09376', '…09376'), ('109376', '…109376')]
    fam5 = [('5', '25'), ('25', '625'), ('625', '390625'), ('0625', '…0625'), ('90625', '…90625'), ('890625', '…890625')]
    for r, fam in enumerate([fam6, fam5]):
        y = 2.0 - r * 1.1
        txt(ax, 0.1, y + 0.45, 'họ bắt đầu từ %s:' % fam[0][0], fs=8.5, ha='left', bold=True, color=NAVY)
        for k, (x, sq) in enumerate(fam):
            X = 0.15 + k * 1.22
            lead0 = x.startswith('0')
            cell(ax, X, y - 0.2, 1.0, 0.38, x, 'gray' if lead0 else 'ans', fs=9, bold=not lead0)
            txt(ax, X + 0.5, y - 0.36, 'k = %d' % (k + 1), fs=7, color=GRAY)
            if k < 5: arrow(ax, (X + 1.02, y), (X + 1.2, y), color=NAVY)
    txt(ax, 3.8, -0.05, 'Mỗi bước thêm đúng một chữ số bên trái (chỉ có một chữ số thỏa mãn). Ô xám bắt đầu bằng 0: không phải số k chữ số, bỏ qua nhưng vẫn nâng tiếp.', fs=7.6, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc K', 0, 0)
    f.node('b', 'proc', 'với n = 1 .. 10ᴷ − 1:  p ← 10^(số chữ số của n)\nnếu n² mod p = n thì in n   (n² bằng __int128)', 0, -0.7)
    f.node('c', 'end', 'Kết thúc', 0, -1.4)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'với x₀ ∈ {5, 6}:  x ← x₀;  p ← 10', 0, 0)
    f.node('b', 'proc', 'nếu x ≥ p / 10 (đủ k chữ số): ghi nhận x', 0, -0.6)
    f.node('c', 'proc', 'tìm chữ số d để y = x + d · p thỏa y² ≡ y (mod 10p)\nx ← y;  p ← 10p', 0, -1.3)
    f.node('d', 'end', 'Thêm 1, sắp xếp, in', 0, -2.0)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.edge('c', 'b', 'r', 'r', via=[(3.3, -1.3), (3.3, -0.6)], label='k < K', lpos=(3.75, -0.95))
    f.edge('c', 'd')
    f.draw(path)

def make(F):
    squares(F('squares')); lift(F('lift')); naive_flow(F('naive')); opt_flow(F('opt'))
