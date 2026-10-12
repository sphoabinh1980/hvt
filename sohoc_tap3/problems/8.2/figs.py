from figlib import *

def arcs(path):
    ps = [3, 5, 7, 11, 13, 17, 19]
    fig, ax = new(6.8, 2.3)
    x0, sc = 0.3, 6.2 / 20
    def X(v): return x0 + (v - 3) * sc
    line(ax, [(X(3), 0.8), (X(22), 0.8)], color=GRAY)
    for v in range(3, 23):
        ax.plot([X(v)] * 2, [0.75, 0.85], color=GRAY, lw=0.7)
        txt(ax, X(v), 0.58, str(v), fs=7.5, color=NAVY if v in ps else GRAY, bold=v in ps)
    for p in ps:
        ax.add_patch(Circle((X(p), 0.8), 0.08, facecolor='#9DC3E6', edgecolor=BLUE, zorder=4))
    for a, b in zip(ps, ps[1:]):
        g = b - a
        col = DRED if (a, b) == (7, 11) else (GREEN if (a, b) == (3, 5) else '#A6A6A6')
        lw = 2 if col != '#A6A6A6' else 1
        ax.add_patch(matplotlib.patches.Arc(((X(a) + X(b)) / 2, 0.8), X(b) - X(a), 0.25 * g + 0.3, theta1=0, theta2=180, color=col, lw=lw))
        txt(ax, (X(a) + X(b)) / 2, 0.8 + (0.25 * g + 0.3) / 2 + 0.1, str(g), fs=8, color=col, bold=True)
    txt(ax, X(22) - 0.1, 2.0, 'đỏ: lớn nhất (4), chọn (7, 11)', fs=8, ha='right', color=DRED, bold=True)
    txt(ax, X(22) - 0.1, 1.75, 'xanh lá: nhỏ nhất (2), chọn (3, 5)', fs=8, ha='right', color=GREEN, bold=True)
    txt(ax, 3.4, 0.22, 'Không tính khoảng từ L = 3 tới số nguyên tố đầu tiên, hay từ số cuối tới R = 22.', fs=8, color=GRAY)
    save(fig, path)

def naive_flow(path):
    f = Flow()
    f.node('s', 'start', 'Đọc L, R;  prev ← không có', 0, 0)
    f.node('l', 'proc', 'với x = L..R tăng dần:  nếu x nguyên tố:', 0, -0.6)
    f.node('u', 'proc', 'nếu có prev: g ← x − prev; cập nhật max/min khi lớn hơn hẳn/nhỏ hơn hẳn;\nprev ← x', 0, -1.25)
    f.node('o', 'end', 'In cặp lớn nhất và cặp nhỏ nhất (hoặc −1)', 0, -1.95)
    f.edge('s', 'l'); f.edge('l', 'u'); f.edge('u', 'o')
    f.draw(path)

def opt_flow(path):
    f = Flow()
    f.node('s', 'start', 'Sàng nhỏ tới 10⁶;  sàng đoạn [L, R]', 0, 0)
    f.node('l', 'proc', 'duyệt ô x − L tăng dần; mỗi số nguyên tố mới tạo một cặp với prev', 0, -0.6)
    f.node('o', 'end', 'In kết quả', 0, -1.2)
    f.edge('s', 'l'); f.edge('l', 'o')
    f.draw(path)

import matplotlib
def make(F):
    arcs(F('arcs')); naive_flow(F('naive')); opt_flow(F('opt'))
