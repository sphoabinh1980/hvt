from figlib import *

def steps(path):
    fig, ax = new(7.6, 2.5)
    txt(ax, 0.05, 2.35, 'Ví dụ 2: a = 10⁹, b = 2 (ô thấp nhất bên phải)', fs=9, ha='left', bold=True, color=NAVY)
    rows = [('khởi đầu', ['1'], ''),
            ('× 10⁹ lần 1', ['1', '0'], 'd[0]: t = 1 · 10⁹ + 0 → ô 0, nhớ 1;  còn nhớ 1 → thêm ô mới'),
            ('× 10⁹ lần 2', ['1', '0', '0'], 'd[0]: t = 0 → ô 0;  d[1]: t = 10⁹ → ô 0, nhớ 1 → thêm ô mới')]
    w = 1.15
    for r, (lab, cells, note) in enumerate(rows):
        y = 1.75 - r * 0.6
        txt(ax, 0.05, y + 0.18, lab, fs=8.4, ha='left', color=NAVY)
        for k, v in enumerate(cells):
            x = 1.25 + (3 - len(cells) + k) * w
            cell(ax, x, y, w - 0.06, 0.36, v, 'ans' if (k == 0 and r > 0) else 'done', fs=8.5)
        txt(ax, 4.75, y + 0.18, note, fs=7.4, ha='left', color=GRAY)
    save(fig, path)

def printing(path):
    fig, ax = new(7.6, 1.9)
    txt(ax, 0.05, 1.7, 'Ví dụ 1: 3⁴⁰ được lưu thành [56928801, 157665459, 12] (ô thấp nhất trước)', fs=8.8, ha='left', bold=True, color=NAVY)
    cells = [('12', '%lld', 'ans'), ('157665459', '%09lld', 'done'), ('056928801', '%09lld', 'done')]
    x = 0.4
    for v, f, k in cells:
        w = 0.32 + 0.15 * len(v)
        cell(ax, x, 0.95, w, 0.4, '', k)
        cw = 10 * 0.6 / 72
        x1 = x + w / 2 - cw * len(v) / 2
        for q, ch in enumerate(v):
            red = v.startswith('0') and q == 0
            txt(ax, x1 + (q + 0.5) * cw, 1.15, ch, fs=10, family='monospace', color=DRED if red else '#1A1A1A', bold=red)
        txt(ax, x + w / 2, 0.75, f, fs=8, color=BLUE, family='monospace')
        x += w + 0.15
    txt(ax, x + 0.15, 1.15, '→  12157665459056928801', fs=9.5, ha='left', color=DRED, bold=True)
    txt(ax, 0.4, 0.35, 'In bằng %lld cho mọi ô sẽ mất chữ số 0 đỏ: 1215766545956928801 (19 chữ số, sai).', fs=8.2, ha='left', color=GRAY)
    save(fig, path)

def opt_flow(path):
    f = Flow()
    f.node('a', 'start', 'd ← [1]', 0, 0)
    f.node('b', 'proc', 'lặp b lần:  c ← 0;  với mọi ô i:  t ← d[i] · a + c\nd[i] ← t mod 10⁹;  c ← t div 10⁹;  nếu c > 0 thêm ô c', 0, -0.7)
    f.node('c', 'proc', 'xóa ô 0 thừa ở đầu (khi a = 0)', 0, -1.4)
    f.node('d', 'end', 'In ô cao nhất bằng %lld, các ô sau bằng %09lld', 0, -2.0)
    f.edge('a', 'b'); f.edge('b', 'c'); f.edge('c', 'd')
    f.draw(path)

def make(F):
    steps(F('steps')); printing(F('print')); opt_flow(F('opt'))
