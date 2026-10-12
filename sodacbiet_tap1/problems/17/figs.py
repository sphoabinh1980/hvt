from figlib import *

def isp(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

def grid(path):
    fig, ax = new(7.6, 4.6)
    txt(ax, 3.9, 4.45, 'nửa đầu ab (a: hàng, b: cột)  →  số đối xứng aba', fs=9, color=NAVY, bold=True)
    for b in range(10):
        txt(ax, 0.95 + b * 0.68, 4.1, str(b), fs=8.5, color=GRAY)
    for a in range(1, 10):
        y = 3.7 - (a - 1) * 0.42
        txt(ax, 0.35, y + 0.17, 'a = %d' % a, fs=8.5, color=GRAY)
        for b in range(10):
            x = a * 100 + b * 10 + a
            skip = a % 2 == 0 or a == 5
            kind = 'gray' if skip else 'ans' if isp(x) else 'plain'
            cell(ax, 0.65 + b * 0.68, y, 0.62, 0.34, str(x), kind, fs=8, bold=kind == 'ans', color=GRAY if skip else None)
    y0 = -0.15
    cell(ax, 0.65, y0, 0.35, 0.25, '', 'gray'); txt(ax, 1.08, y0 + 0.12, 'bỏ qua: chữ số đầu chẵn hoặc 5', fs=8, ha='left')
    cell(ax, 3.55, y0, 0.35, 0.25, '', 'plain'); txt(ax, 3.98, y0 + 0.12, 'kiểm tra: hợp số', fs=8, ha='left')
    cell(ax, 5.45, y0, 0.35, 0.25, '', 'ans'); txt(ax, 5.88, y0 + 0.12, 'nguyên tố (15 số)', fs=8, ha='left')
    save(fig, path)

def eleven(path):
    fig, ax = new(7.4, 1.7)
    ds = '2442'
    sg = ['+', '−', '+', '−']
    for i, (d, s) in enumerate(zip(ds, sg)):
        cell(ax, 0.3 + i * 0.5, 0.85, 0.45, 0.45, d, 'done', fs=12, bold=True)
        txt(ax, 0.52 + i * 0.5, 0.6, s, fs=11, color=RED if s == '−' else GREEN, bold=True)
    txt(ax, 2.55, 1.07, '→  2 − 4 + 4 − 2 = 0  →  2442 chia hết cho 11 (2442 = 11 · 222)', fs=9.5, ha='left', color=NAVY)
    txt(ax, 0.3, 0.2, 'Độ dài chẵn: hai chữ số đối xứng nhau luôn mang dấu ngược nhau, nên tổng đan dấu luôn bằng 0.', fs=9, ha='left', color=DRED)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R;  cnt ← 0', 0, 0)
    f.node('b', 'proc', 'với x = L .. R: nếu x đối xứng và x nguyên tố (thử chia tới √x) thì cnt++', 0, -0.65)
    f.node('c', 'end', 'In cnt', 0, -1.3)
    f.edge('a', 'b'); f.edge('b', 'c')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'io', 'Đọc L, R;  cnt ← [11 thuộc [L, R]]', 0, 0)
    f.node('b', 'proc', 'với mỗi nửa đầu a (1 .. 9 999 999), tăng dần:', 0, -0.62)
    f.node('c', 'dec', 'chữ số đầu chẵn\nhoặc bằng 5 ?', 0, -1.45)
    f.node('d', 'proc', 'nhảy tới chữ số đầu tiếp theo', 3.2, -1.45)
    f.node('e', 'proc', 'x ← ghép a với a bỏ chữ số cuối, đảo ngược (độ dài lẻ)\nx > R: sang độ dài tiếp;  x ≥ L và Miller–Rabin(x): cnt++', 0, -2.35)
    f.node('g', 'end', 'In cnt', 0, -3.05)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd', 'r', 'l', label='Đúng'); f.edge('c', 'e', label='Sai', lpos=(0.3, -1.95)); f.edge('e', 'g')
    f.draw(path)

def make(F):
    grid(F('grid')); eleven(F('eleven')); naive_flow(F('naive')); opt_flow(F('opt'))
