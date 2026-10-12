from figlib import *

def mrseq(path):
    n = 25326001
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    fig, ax = new(6.8, 2.75)
    cw, x0 = 1.0, 1.25
    heads = ['aᵈ', 'a²ᵈ', 'a⁴ᵈ', 'a⁸ᵈ', 'a¹⁶ᵈ']
    for j, h in enumerate(heads):
        cell(ax, x0 + j * cw, 2.25, cw - 0.04, 0.3, h, 'navy', fs=8, bold=True)
    for i, a in enumerate([2, 3, 5, 7]):
        y = 1.85 - i * 0.4
        x = pow(a, d, n)
        seq = [x]
        for _ in range(s): seq.append(seq[-1] * seq[-1] % n)
        good = seq[0] in (1, n - 1) or (n - 1) in seq[:s]
        cell(ax, 0.3, y, 0.85, 0.32, 'a = %d' % a, 'in' if good else 'pink', fs=8.5, bold=True)
        for j, v in enumerate(seq):
            if v == n - 1: k, t = 'green', 'n − 1'
            elif v == 1: k, t = 'gray', '1'
            else: k, t = 'plain', str(v)
            if not good: k = 'ans' if j == s else ('pink' if v not in (1,) else 'gray')
            cell(ax, x0 + j * cw, y, cw - 0.04, 0.32, t, k, fs=7.5, lw=1.0 if k == 'ans' else None)
        txt(ax, x0 + 5 * cw + 0.08, y + 0.16, 'cho qua' if good else 'NHÂN CHỨNG', fs=8, ha='left', color=GREEN if good else DRED, bold=True)
    txt(ax, 3.4, 0.15, 'n = 25 326 001,  n − 1 = 1 582 875 · 2⁴.  Cơ số 7: dãy không bắt đầu bằng 1 và không chứa n − 1 ⇒ n là hợp số.', fs=7.8, color=NAVY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'isPrime(n)', 0, 0)
    f.node('a', 'proc', 'loại n < 2; nhận 2, 3; loại bội của 2, 3', 0, -0.6)
    f.node('b', 'proc', 'thử i, i + 2 với i = 5, 11, 17, ... khi i · i ≤ n', 0, -1.2)
    f.node('c', 'end', 'không ước nào chia hết: nguyên tố', 0, -1.8)
    f.edge('s', 'a'); f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def bits(path):
    fig, ax = new(6.6, 1.7)
    sc = 4.6 / 128
    for i, (lab, b, k) in enumerate([('x, y < n < 2⁶⁴', 64, 'done'), ('x · y < 2¹²⁸', 128, 'pink'), ('unsigned long long', 64, 'green')]):
        y = 1.2 - i * 0.42
        txt(ax, 1.75, y + 0.15, lab, fs=8.3, ha='right', color=NAVY)
        cell(ax, 1.9, y, b * sc, 0.3, '%d bit' % b, k, fs=8)
    txt(ax, 1.9 + 64 * sc + 0.1, 0.39, '← nửa trên bị cắt bỏ âm thầm!', fs=8, color=DRED, bold=True, ha='left')
    save(fig, path)

def mr_flow(path):
    f = Flow()
    f.node('s', 'start', 'isPrime(n), n ≥ 2', 0, 0)
    f.node('a', 'dec', 'n chia hết một cơ số p ?', 0, -0.8)
    f.node('a1', 'end', 'trả về n = p', 2.8, -0.8)
    f.node('b', 'proc', 'n − 1 = d · 2ˢ, d lẻ', 0, -1.6)
    f.node('c', 'dec', 'còn cơ số a ?', 0, -2.35)
    f.node('c1', 'end', 'nguyên tố', 2.4, -2.35)
    f.node('x', 'proc', 'x ← aᵈ mod n', 0, -3.1)
    f.node('y', 'dec', 'x = 1 hoặc x = n − 1, hoặc\nbình phương ≤ s − 1 lần gặp n − 1 ?', 0, -4.05, w=3.6, h=0.75)
    f.node('y1', 'end', 'hợp số', 3.4, -4.05)
    f.edge('s', 'a'); f.edge('a', 'a1', 'r', 'l', label='Đúng'); f.edge('a', 'b', label='Sai', lpos=(0.3, -1.25))
    f.edge('b', 'c'); f.edge('c', 'c1', 'r', 'l', label='Sai'); f.edge('c', 'x', label='Đúng', lpos=(0.32, -2.75)); f.edge('x', 'y')
    f.edge('y', 'y1', 'r', 'l', label='Sai')
    f.edge('y', 'c', 'l', 'l', via=[(-2.6, -4.05), (-2.6, -2.35)], label='Đúng', lpos=(-2.35, -3.9))
    f.draw(path)

def make(F):
    mrseq(F('mrseq')); naive_flow(F('naive')); bits(F('bits')); mr_flow(F('opt'))
