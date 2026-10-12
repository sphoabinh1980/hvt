from figlib import *

def tree(path):
    n = 12
    fig, ax = new(7.6, 3.5)
    seen = {1}
    levels = [[('1', None, 'live')]]
    while True:
        nxt = []
        for s, par, st in levels[-1]:
            if st != 'live': continue
            for d in '01':
                t = s + d; r = int(t) % n
                if r in seen: nxt.append((t, s, 'dead'))
                else: seen.add(r); nxt.append((t, s, 'live'))
        levels.append(nxt)
        if any(int(t) % n == 0 for t, p, st in nxt if st == 'live'): break
    levels[-1] = [x for x in levels[-1] if x[1] == '1110']   # tầng cuối: chỉ vẽ nhánh chứa đáp số
    pos = {}
    for lv, row in enumerate(levels):
        y = 3.1 - lv * 0.75
        k = len(row)
        w = 7.2 / max(k, 1)
        for i, (s, par, st) in enumerate(row):
            x = 0.2 + w * (i + 0.5)
            if lv == len(levels) - 1:
                x = pos[par][0] + (-0.45 if s.endswith('0') else 0.45)
            r = int(s) % n
            kind = 'ans' if r == 0 else ('gray' if st == 'dead' else 'done')
            bw = 0.11 * len(s) + 0.2
            cell(ax, x - bw / 2, y - 0.14, bw, 0.28, s, kind, fs=7.2, bold=r == 0)
            txt(ax, x, y - 0.27, 'dư %d' % r, fs=6.3, color=DRED if r == 0 else (GRAY if st == 'dead' else BLUE))
            if par is not None and par in pos:
                px, py = pos[par]
                line(ax, [(px, py - 0.3), (x, y + 0.14)], color='#BFBFBF' if st == 'dead' else NAVY, lw=0.8)
            if st == 'live':
                pos[s] = (x, y)
    txt(ax, 3.8, -0.45, 'n = 12. Ô xám: số dư đã gặp, bị cắt bỏ (mọi số sinh ra từ nó cũng lặp lại). Ô vàng: 11100 chia hết cho 12.', fs=7.8, color=NAVY)
    save(fig, path)

def pigeon(path):
    fig, ax = new(7.6, 1.55)
    rs = [1, 4, 6, 5, 2, 0]
    for k in range(6):
        x = 0.15 + k * 1.22
        cell(ax, x, 0.85, 1.1, 0.36, '1' * (k + 1), 'ans' if rs[k] == 0 else 'done', fs=8.5, bold=rs[k] == 0)
        txt(ax, x + 0.55, 0.62, 'mod 7 = %d' % rs[k], fs=7.6, color=DRED if rs[k] == 0 else BLUE)
    txt(ax, 3.8, 0.18, 'Trong 1, 11, 111, ..., hai số cùng số dư thì hiệu của chúng (dạng 11...100...0) chia hết cho n.', fs=8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'start', 'Đọc n;  k ← 1', 0, 0)
    f.node('b', 'proc', 'x ← số có các chữ số là các bit của k  (k = 5 → 101)', 0, -0.6)
    f.node('c', 'dec', 'x mod n = 0 ?', 0, -1.35)
    f.node('d', 'proc', 'k ← k + 1', 2.7, -1.35)
    f.node('e', 'end', 'In x', 0, -2.15)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd', 'r', 'l', label='Sai')
    f.edge('d', 'b', 't', 'r', via=[(2.7, -0.6)])
    f.edge('c', 'e', label='Đúng', lpos=(0.3, -1.8))
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'Hàng đợi ← {số dư của "1"}', 0, 0)
    f.node('b', 'proc', 'lấy r ở đầu hàng đợi', 0, -0.6)
    f.node('c', 'dec', 'r = 0 ?', 0, -1.3)
    f.node('d', 'proc', 'với d = 0, 1:  t ← (10r + d) mod n\nnếu t chưa gặp: ghi par[t] = r, dig[t] = d, đưa t vào hàng đợi', 3.4, -1.3)
    f.node('e', 'end', 'Lần ngược par từ 0, đọc các chữ số dig', 0, -2.1)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd', 'r', 'l', label='Sai')
    f.edge('d', 'b', 't', 'r', via=[(3.4, -0.6)])
    f.edge('c', 'e', label='Đúng', lpos=(0.3, -1.75))
    f.draw(path)

def make(F):
    tree(F('tree')); pigeon(F('pigeon')); naive_flow(F('naive')); opt_flow(F('opt'))
