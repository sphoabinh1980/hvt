"""BÀI 12 — Đếm, đồ thị có hướng, xác suất và kì vọng: DUONGMOTCHIEU (thứ tự tô pô), XUCXAC, kì vọng số lần tung."""

from fractions import Fraction

from shared import *  # noqa: F401,F403

# ---------------------------------------------------------------- DUONGMOTCHIEU
GN = 6
GEDGES = [(1, 2), (1, 3), (2, 4), (3, 4), (2, 5), (4, 6), (5, 6), (3, 6)]


def kahn(n, edges):
    out = {v: [] for v in range(1, n + 1)}
    indeg = {v: 0 for v in range(1, n + 1)}
    for a, b in edges:
        out[a].append(b)
        indeg[b] += 1
    order = [v for v in range(1, n + 1) if indeg[v] == 0]
    k = 0
    while k < len(order):
        for nx in out[order[k]]:
            indeg[nx] -= 1
            if indeg[nx] == 0:
                order.append(nx)
        k += 1
    return order, out


def count_paths(n, edges):
    order, out = kahn(n, edges)
    ways = {v: 0 for v in range(1, n + 1)}
    ways[1] = 1
    for v in order:
        for nx in out[v]:
            ways[nx] += ways[v]
    return ways


TOPO, OUT = kahn(GN, GEDGES)
assert TOPO == [1, 2, 3, 5, 4, 6]
INDEG0 = {v: sum(1 for a, b in GEDGES if b == v) for v in range(1, GN + 1)}
assert INDEG0 == {1: 0, 2: 1, 3: 1, 4: 2, 5: 1, 6: 3}
WAYS = count_paths(GN, GEDGES)
assert WAYS == {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 4}
assert count_paths(GN, GEDGES + [(1, 4)])[6] == 5
PATHS = [(1, 2, 4, 6), (1, 3, 4, 6), (1, 2, 5, 6), (1, 3, 6)]
assert len(PATHS) == WAYS[6]

# ---------------------------------------------------------------- XUCXAC


def dice_counts(n):
    cnt = {0: 1}
    for _ in range(n):
        nxt = {}
        for s, c in cnt.items():
            for f in range(1, 7):
                nxt[s + f] = nxt.get(s + f, 0) + c
        cnt = nxt
    return cnt


D2, D3 = dice_counts(2), dice_counts(3)
assert D2[7] == 6 and Fraction(D2[7], 36) == Fraction(1, 6)
assert D3[10] == 27 and D3[11] == 27 and Fraction(54, 216) == Fraction(1, 4)
assert D2[10] == 3
assert sum(D2.values()) == 36 and sum(D3.values()) == 216

# ---------------------------------------------------------------- KÌ VỌNG


def expect(target):
    e = [Fraction(0)] * (target + 6)
    for s in range(target - 1, -1, -1):
        e[s] = 1 + sum(e[s + f] for f in range(1, 7)) / 6
    return e


E6 = expect(6)
assert E6[0] == Fraction(7, 6) ** 5 and abs(float(E6[0]) - 2.1614) < 1e-4
E6F = [round(float(x), 4) for x in E6[:6]]
assert E6F == [2.1614, 1.8526, 1.588, 1.3611, 1.1667, 1.0]
assert expect(2)[0] == Fraction(7, 6)

TOPO_CODE = """
vector<int> order;
for (int v = 1; v <= n; v++)
  if (inDeg[v] == 0) order.push_back(v);
for (int k = 0; k < order.size(); k++)
  for (int nx : out[order[k]])
    if (--inDeg[nx] == 0) order.push_back(nx);
ways[1] = 1;
for (int v : order)
  for (int nx : out[v])
    ways[nx] = (ways[nx] + ways[v]) % MOD;
"""

DICE_CODE = """
vector<double> chance(6 * n + 1, 0.0);
chance[0] = 1.0;
for (int die = 1; die <= n; die++) {
  vector<double> next(6 * n + 1, 0.0);
  for (int s = 0; s <= 6 * (die - 1); s++)
    for (int f = 1; f <= 6; f++)
      next[s + f] += chance[s] / 6.0;
  chance = next;
}
"""

EXP_CODE = """
vector<double> expect(target + 6, 0.0);
for (int s = target - 1; s >= 0; s--) {
  double total = 0.0;
  for (int f = 1; f <= 6; f++)
    total += expect[s + f];
  expect[s] = 1.0 + total / 6.0;
}
"""


class B12Scene(NarratedScene):
    lesson_tag = "BÀI 12"
    lesson_title = "Đếm, đồ thị có hướng, xác suất, kì vọng"


GPOS = {1: (-3.1, 0), 2: (-1.4, 1.4), 3: (-1.4, -1.4), 4: (0.6, 0), 5: (1.3, 1.6), 6: (2.9, 0)}


def dag(edges=GEDGES, pos=GPOS, r=0.4):
    nodes = {v: VGroup(Circle(radius=r, fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=4),
                       TB(str(v), size=30)).move_to([x, y, 0]) for v, (x, y) in pos.items()}
    for nd in nodes.values():
        nd[1].move_to(nd[0])
    arrows = {}
    for a, b in edges:
        pa, pb = np.array(nodes[a][0].get_center()), np.array(nodes[b][0].get_center())
        d = (pb - pa) / np.linalg.norm(pb - pa)
        arrows[(a, b)] = Arrow(pa + d * r, pb - d * r, buff=0.02, color=MUTED, stroke_width=4,
                               max_tip_length_to_length_ratio=0.15, tip_length=0.22)
    g = VGroup(*arrows.values(), *nodes.values())
    g.nodes, g.arrows = nodes, arrows
    return g


def bars(counts, highlight=(), w=0.38, unit=0.13, color=BLUEC, label_size=18):
    g = VGroup()
    keys = sorted(counts)
    for s in keys:
        h = max(counts[s] * unit, 0.03)
        r = Rectangle(width=w * 0.85, height=h, fill_color=ACCENT if s in highlight else color, fill_opacity=0.9,
                      stroke_width=0)
        lab = T(str(s), size=label_size, color=ACCENT if s in highlight else MUTED)
        top = T(str(counts[s]), size=label_size, color=INK)
        col = VGroup(r, lab, top)
        g.add(col)
    for k, col in enumerate(g):
        col[0].move_to([k * w, col[0].height / 2, 0])
        col[1].next_to(col[0], DOWN, buff=0.08).set_y(-0.2)
        col[2].next_to(col[0], UP, buff=0.05)
    return g


# ----------------------------------------------------------------------------
class B12_00_Intro(B12Scene):
    def construct(self):
        tag = TB("BÀI 12", size=80, color=ACCENT)
        ttl = VGroup(TB("Đếm, đồ thị có hướng,", size=46), TB("xác suất và kì vọng", size=46, color=GOOD)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Mọi bài QHĐ là một DAG trạng thái",
            "✓ Thứ tự điền bảng = THỨ TỰ TÔ PÔ",
            "✓ Đếm đường đi, đường dài nhất trên DAG",
            "✓ Xác suất: cộng có trọng số",
            "✓ Kì vọng: tính NGƯỢC từ trạng thái cuối",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 12, bài cuối của Chương 3: Đếm, đồ thị có hướng, xác suất và kì vọng."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ thấy rằng mọi bài quy hoạch động đều là một đồ thị có hướng không chu trình giữa "
                        "các trạng thái, và thứ tự điền bảng chính là thứ tự tô pô."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ đếm số đường đi và tìm đường đi dài nhất trên đồ thị đó; tính xác suất bằng cách thay số cách "
                        "bằng xác suất; và tính kì vọng bằng quy hoạch động ngược từ trạng thái cuối."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_01_KhoiDong(B12Scene):
    def construct(self):
        self.show_header("Khởi động: Ba câu hỏi, một ý tưởng")
        qs = [
            ("🏠 → 🏫", "Đường một chiều, không vòng lại. Từ nhà (nút 1)", "đến trường (nút 6) có bao nhiêu lộ trình?", BLUEC),
            ("🎲🎲", "Tung hai con xúc xắc: xác suất", "tổng bằng 7 là bao nhiêu?", GOOD),
            ("🎲 …", "Tung liên tục tới khi tổng ≥ 6:", "TRUNG BÌNH phải tung bao nhiêu lần?", PURPLE),
        ]
        cards = VGroup()
        for k, (_, a, b, col) in enumerate(qs, 1):
            body = VGroup(TB(f"Câu {k}", size=28, color=col), T(a, size=27), T(b, size=27)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            c = panel(body, width=7.5, stroke=col, pad=0.28)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.28)
            cards.add(c)
        cards.arrange(DOWN, buff=0.35)
        one = TB("Cả ba giải bằng CÙNG MỘT ý tưởng!", size=34, color=ACCENT)
        fit_stack(cards, one, buff=0.6, max_scale=1.2)
        speech = [
            "Câu hỏi một: thành phố có những con đường một chiều nối các nút giao thông, không có đường nào cho phép đi vòng "
            "trở lại chỗ cũ. Từ nhà, nút 1, đến trường, nút 6, có bao nhiêu lộ trình khác nhau?",
            "Câu hỏi hai, rất khác: tung hai con xúc xắc, xác suất tổng bằng 7 là bao nhiêu?",
            "Câu hỏi ba: tung xúc xắc liên tục cho tới khi tổng điểm đạt ít nhất 6. Trung bình phải tung bao nhiêu lần?",
        ]
        for c, sp in zip(cards, speech):
            with self.voice(sp):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Cả ba câu hỏi đều giải bằng cùng một ý tưởng. Cùng tìm hiểu nhé!"):
            self.play(FadeIn(one, scale=1.1), run_time=0.6)

        self.clear_body()
        self.show_header("1. Bài toán DUONGMOTCHIEU")
        task = tag_box("BÀI TOÁN: DUONGMOTCHIEU", [
            "Đồ thị có hướng n đỉnh, m cạnh, KHÔNG có chu trình",
            "(n ≤ 10⁵, m ≤ 2·10⁵). Đếm số đường đi từ đỉnh 1",
            "tới đỉnh n, lấy dư cho 10⁹ + 7.",
        ], width=7.5, size=27)
        g = dag()
        paths_slot = placeholder(7.0, 1.6)
        res = TB("Đáp án: 4 đường", size=36, color=GOOD)
        fit_stack(task, g, paths_slot, res, buff=0.55, max_scale=1.2)
        with self.voice("Bài toán DUONGMOTCHIEU: cho đồ thị có hướng n đỉnh, m cạnh, không có chu trình. Đếm số đường đi từ đỉnh "
                        "1 tới đỉnh n, lấy dư cho 10 mũ 9 cộng 7."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Ví dụ: sáu đỉnh, tám cạnh. Mọi cạnh đều một chiều, và không có chu trình."):
            self.play(*[FadeIn(nd) for nd in g.nodes.values()], run_time=0.5)
            self.play(LaggedStart(*[GrowArrow(a) for a in g.arrows.values()], lag_ratio=0.1), run_time=1.2)
        cols = [GOOD, ORANGE, PURPLE, BLUEC]
        plist = VGroup(*[M(" → ".join(map(str, p)), size=26, color=c) for p, c in zip(PATHS, cols)]
                       ).arrange_in_grid(rows=2, cols=2, buff=(0.6, 0.15)).move_to(paths_slot)
        if plist.width > paths_slot.width:
            plist.scale_to_fit_width(paths_slot.width)
        with self.voice("Có bốn đường: 1, 2, 4, 6; 1, 3, 4, 6; 1, 2, 5, 6; và 1, 3, 6."):
            for p, c, lab in zip(PATHS, cols, plist):
                edges = [g.arrows[(a, b)] for a, b in zip(p, p[1:])]
                self.play(*[e.animate.set_color(c).set_stroke(width=7) for e in edges], FadeIn(lab), run_time=0.5)
                self.play(*[e.animate.set_color(MUTED).set_stroke(width=4) for e in edges], run_time=0.3)
            self.play(FadeIn(res), run_time=0.4)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_02_NgayTho(B12Scene):
    def construct(self):
        self.show_header("Ý tưởng ngây thơ: Đệ quy thử mọi đường")
        f = VGroup(T("đếm(u) = số đường từ u tới n:", size=29),
                   M("đếm(n) = 1;  đếm(u) = Σ đếm(v), u → v", size=26, color=ACCENT)).arrange(DOWN, buff=0.12)
        # bậc thang k tầng
        k = 4
        top = VGroup(*[Dot(radius=0.13, color=BLUEC).move_to([-2.4 + i * 1.6, 0.7, 0]) for i in range(k)])
        bot = VGroup(*[Dot(radius=0.13, color=BLUEC).move_to([-2.4 + i * 1.6, -0.7, 0]) for i in range(k)])
        s = Dot(radius=0.16, color=GOOD).move_to([-3.8, 0, 0])
        t = Dot(radius=0.16, color=BAD).move_to([3.6, 0, 0])
        ladder_edges = VGroup()
        for a in (top[0], bot[0]):
            ladder_edges.add(Arrow(s.get_center(), a.get_center(), buff=0.15, color=MUTED, stroke_width=3, tip_length=0.15))
        for i in range(k - 1):
            for a in (top[i], bot[i]):
                for b in (top[i + 1], bot[i + 1]):
                    ladder_edges.add(Arrow(a.get_center(), b.get_center(), buff=0.15, color=MUTED, stroke_width=3,
                                           tip_length=0.15))
        for a in (top[-1], bot[-1]):
            ladder_edges.add(Arrow(a.get_center(), t.get_center(), buff=0.15, color=MUTED, stroke_width=3, tip_length=0.15))
        ladder = VGroup(ladder_edges, top, bot, s, t)
        lad_lab = T("Đồ thị “bậc thang” k tầng: 2ᵏ đường đi", size=27, color=ORANGE)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "đếm(u) đi theo TỪNG ĐƯỜNG một: số lời gọi",
            "= tổng số đường đi, tăng theo HÀM MŨ.",
            "100 đỉnh ⇒ ≈ 2⁵⁰ ≈ 10¹⁵ đường!",
        ], accent=BLUEC, width=7.5, size=27)
        cnt[3][2].set_color(BAD)
        fit_stack(f, VGroup(ladder, lad_lab).arrange(DOWN, buff=0.3), cnt, buff=0.7, max_scale=1.2)
        with self.voice("Cách ngây thơ: hàm đệ quy đếm của u, số đường đi từ u tới n. Nếu u là n thì có 1 đường; ngược lại, cộng "
                        "đếm của v với mọi cạnh từ u tới v."):
            self.play(FadeIn(f), run_time=0.8)
        with self.voice("Hàm này đi theo từng đường một. Ví dụ đồ thị bậc thang gồm k tầng, mỗi tầng hai đỉnh nối chéo sang tầng "
                        "sau: mỗi tầng nhân đôi số đường, có 2 mũ k đường."):
            self.play(FadeIn(ladder), run_time=1.0)
            self.play(FadeIn(lad_lab), run_time=0.4)
        with self.voice("Số lời gọi bằng tổng số đường đi, tăng theo hàm mũ. Với 100 đỉnh đã có khoảng 2 mũ 50, một triệu tỉ "
                        "đường."):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Bế tắc: Điền bảng theo thứ tự nào?")
        g = dag()
        dead = VGroup(T("Đỉnh 4 được tới từ cả 2 lẫn 3:", size=29),
                      T("đếm(4) bị gọi lại cho MỖI đường đi tới 4", size=29, color=BAD)).arrange(DOWN, buff=0.1)
        ask = VGroup(T("Bài toán con gối nhau, nhưng TRẠNG THÁI là ĐỈNH;", size=28),
                     T("các đỉnh không xếp sẵn “nhỏ trước lớn sau”", size=28),
                     T("như dãy hay lưới.", size=28),
                     TB("Điền bảng theo thứ tự nào?", size=34, color=ACCENT)).arrange(DOWN, buff=0.12)
        fit_stack(g, dead, ask, buff=0.7, max_scale=1.2)
        self.play(FadeIn(g), run_time=0.6)
        with self.voice("Bế tắc nằm ở đâu? Đỉnh 4 được tới từ cả đỉnh 2 lẫn đỉnh 3, nên đếm của 4 bị gọi lại cho mỗi đường đi "
                        "tới 4."):
            self.play(g.arrows[(2, 4)].animate.set_color(ORANGE).set_stroke(width=7),
                      g.arrows[(3, 4)].animate.set_color(ORANGE).set_stroke(width=7),
                      g.nodes[4][0].animate.set_stroke(BAD, 6), run_time=0.8)
            self.play(FadeIn(dead), run_time=0.6)
        with self.voice("Đây vẫn là bài toán con gối nhau, nhưng trạng thái là các đỉnh của đồ thị, và các đỉnh không xếp sẵn theo "
                        "thứ tự nhỏ trước lớn sau như dãy hay lưới. Vậy điền bảng theo thứ tự nào?"):
            self.play(FadeIn(ask), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_03_ToPo(B12Scene):
    def construct(self):
        self.show_header("Phá bế tắc: Thứ tự tô pô")
        f = panel(VGroup(M("ways(v) = Σ ways(u),  mọi cạnh u → v", size=28, color=ACCENT),
                         M("ways(1) = 1", size=28)).arrange(DOWN, buff=0.12), stroke=ACCENT, width=7.5)
        why = VGroup(T("Mọi đường tới v đều vào v bằng cạnh CUỐI u → v", size=27),
                     T("⇒ mọi u có cạnh vào v phải được tính TRƯỚC", size=27, color=GOOD)).arrange(DOWN, buff=0.1)
        defn = tag_box("THỨ TỰ TÔ PÔ", [
            "Thứ tự các đỉnh mà MỌI CẠNH đi từ đỉnh",
            "đứng trước tới đỉnh đứng sau.",
            "Có thứ tự tô pô ⟺ đồ thị KHÔNG có chu trình.",
        ], accent=PURPLE, width=7.5, size=28)
        kahn_box = tag_box("THUẬT TOÁN KAHN", [
            "• Cho các đỉnh có bán bậc vào 0 vào hàng đợi",
            "• Lấy một đỉnh ra, “xóa” các cạnh đi ra từ nó",
            "• Đỉnh nào bán bậc vào về 0 thì vào hàng đợi",
        ], accent=BLUEC, width=7.5, size=28)
        fit_stack(f, why, defn, kahn_box, buff=0.5, max_scale=1.2)
        with self.voice("Phá bế tắc. Đặt ways của v là số đường đi từ 1 tới v. Mọi đường tới v đều đi vào v bằng cạnh cuối cùng "
                        "từ u tới v, nên ways của v bằng tổng ways của u, với mọi cạnh từ u tới v. ways của 1 bằng 1."):
            self.play(FadeIn(f), FadeIn(why[0]), run_time=1.0)
        with self.voice("Để tính ways của v, mọi đỉnh u có cạnh vào v phải được tính trước."):
            self.play(FadeIn(why[1]), run_time=0.5)
        with self.voice("Một thứ tự các đỉnh mà mọi cạnh đều đi từ đỉnh đứng trước tới đỉnh đứng sau được gọi là thứ tự tô pô. "
                        "Đồ thị có hướng có thứ tự tô pô khi và chỉ khi nó không có chu trình."):
            self.play(FadeIn(defn), run_time=0.8)
        with self.voice("Thuật toán Kahn tìm thứ tự tô pô: lấy các đỉnh không có cạnh đi vào, tức bán bậc vào bằng 0, cho vào "
                        "hàng đợi. Mỗi lần lấy một đỉnh ra, xóa các cạnh đi ra từ nó; đỉnh nào có bán bậc vào giảm về 0 thì cho "
                        "vào hàng đợi."):
            self.play(FadeIn(kahn_box), run_time=0.8)

        # ---- Kahn chạy từng bước
        self.clear_body()
        self.show_header("Thuật toán Kahn chạy trên ví dụ")
        g = dag()
        n, arrows = g.nodes, g.arrows
        deg_slot = {v: placeholder(0.9, 0.4).next_to(n[v][0], DOWN if v != 5 else UP, buff=0.08) for v in n}
        order = array_row([""] * 6, w=0.95, h=0.85, size=34, show_index=False, label="order")
        legend = T("số nhỏ màu cam = bán bậc vào còn lại", size=24, color=MUTED)
        sc = fit_stack(VGroup(g, *deg_slot.values()), legend, order, buff=0.6, max_scale=1.15)
        deg = dict(INDEG0)
        dtags = {v: TB(str(deg[v]), size=24, color=ORANGE).scale(sc).move_to(deg_slot[v]) for v in n}
        self.play(FadeIn(g), run_time=0.5)
        with self.voice("Ban đầu, bán bậc vào: đỉnh 1 là 0, đỉnh 2, 3, 5 là 1, đỉnh 4 là 2, đỉnh 6 là 3. Chỉ đỉnh 1 có bán bậc "
                        "vào 0."):
            self.play(*[FadeIn(t) for t in dtags.values()], FadeIn(legend), FadeIn(order), run_time=0.8)
        pos_k = 0

        def put(v):
            nonlocal pos_k
            c = order.cells[pos_k]
            pos_k += 1
            return [c[0].animate.set_fill(GOOD, 1), Transform(c[1], set_cell_value(c, v, color=BG))]

        speech = {
            1: "Lấy đỉnh 1 ra, xóa hai cạnh tới 2 và 3: bán bậc vào của chúng về 0, cho vào hàng đợi.",
            2: "Lấy đỉnh 2: xóa cạnh tới 4, còn 1; xóa cạnh tới 5, về 0, cho 5 vào hàng đợi.",
            3: "Lấy đỉnh 3: cạnh tới 4 bị xóa, 4 về 0, vào hàng đợi; cạnh tới 6 bị xóa, 6 còn 2.",
            5: "Lấy đỉnh 5: 6 còn 1.",
            4: "Lấy đỉnh 4: 6 về 0, vào hàng đợi.",
            6: "Lấy đỉnh 6, không còn cạnh nào. Thứ tự tô pô: 1, 2, 3, 5, 4, 6.",
        }
        self.play(*put(1), n[1][0].animate.set_stroke(GOOD, 6), run_time=0.5)
        for v in TOPO:
            with self.voice(speech[v]):
                self.play(n[v][0].animate.set_fill(GOOD, 0.5), run_time=0.3)
                anims, newly = [], []
                for nx in OUT[v]:
                    deg[nx] -= 1
                    anims.append(arrows[(v, nx)].animate.set_opacity(0.15))
                    anims.append(Transform(dtags[nx], TB(str(deg[nx]), size=24, color=ORANGE if deg[nx] else GOOD)
                                           .scale(sc).move_to(deg_slot[nx])))
                    if deg[nx] == 0:
                        newly.append(nx)
                if anims:
                    self.play(*anims, run_time=0.6)
                for nx in newly:
                    self.play(*put(nx), n[nx][0].animate.set_stroke(GOOD, 6), run_time=0.4)
        note = T("(1 2 3 4 5 6 cũng là một thứ tự tô pô hợp lệ)", size=24, color=MUTED).scale(sc).next_to(order, DOWN, buff=0.2)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)

        # ---- ways theo thứ tự tô pô
        self.clear_body()
        self.show_header("Đếm đường đi theo thứ tự tô pô")
        g = dag()
        n, arrows = g.nodes, g.arrows
        w_slot = {v: placeholder(1.2, 0.45).next_to(n[v][0], DOWN if v != 5 else UP, buff=0.08) for v in n}
        calc_slot = placeholder(7.2, 0.7)
        res = TB("ways(6) = 4  ✓", size=36, color=GOOD)
        sc = fit_stack(VGroup(g, *w_slot.values()), calc_slot, res, buff=0.6, max_scale=1.15)
        self.play(FadeIn(g), run_time=0.5)
        ways = {v: 0 for v in n}
        ways[1] = 1
        wt = {v: TB(f"{ways[v]}", size=26, color=ACCENT if ways[v] else MUTED).scale(sc).move_to(w_slot[v]) for v in n}
        with self.voice("Giờ duyệt các đỉnh theo thứ tự tô pô, và đẩy ways của mỗi đỉnh sang mọi đỉnh kề. Ban đầu ways của 1 bằng "
                        "1, các đỉnh khác bằng 0."):
            self.play(*[FadeIn(t) for t in wt.values()], run_time=0.6)
        sp = {
            1: "Đỉnh 1 đẩy 1 sang đỉnh 2 và đỉnh 3.",
            2: "Đỉnh 2 đẩy 1 sang đỉnh 4 và đỉnh 5.",
            3: "Đỉnh 3 đẩy 1 sang đỉnh 4, thành 2, và sang đỉnh 6, thành 1.",
            5: "Đỉnh 5 đẩy 1 sang đỉnh 6, thành 2.",
            4: "Đỉnh 4 đẩy 2 sang đỉnh 6: 2 cộng 2 bằng 4.",
        }
        cur = None
        for v in TOPO[:-1]:
            line = M(", ".join(f"ways({nx}) += {ways[v]}" for nx in OUT[v]), size=26).scale(sc).move_to(calc_slot)
            with self.voice(sp[v]):
                self.play(n[v][0].animate.set_fill(ACCENT, 0.5), run_time=0.3)
                self.play(FadeIn(line) if cur is None else Transform(cur, line),
                          *[arrows[(v, nx)].animate.set_color(ACCENT).set_stroke(width=7) for nx in OUT[v]], run_time=0.5)
                if cur is None:
                    cur = line
                for nx in OUT[v]:
                    ways[nx] += ways[v]
                self.play(*[Transform(wt[nx], TB(str(ways[nx]), size=26, color=ACCENT).scale(sc).move_to(w_slot[nx]))
                            for nx in OUT[v]], run_time=0.5)
                self.play(*[arrows[(v, nx)].animate.set_color(MUTED).set_stroke(width=4) for nx in OUT[v]],
                          n[v][0].animate.set_fill(PANEL_2, 1), run_time=0.3)
        assert ways == WAYS
        with self.voice("Kết quả ways của 6 bằng 4, đúng bốn đường như ta đã liệt kê."):
            self.play(FadeIn(res), Indicate(wt[6], color=GOOD, scale_factor=1.5), run_time=0.8)

        self.clear_body()
        self.show_header("DUONGMOTCHIEU.CPP: O(n + m)")
        code = code_block(TOPO_CODE, size=21)
        note = VGroup(T("Pha 1: tìm thứ tự tô pô (Kahn)", size=28, color=BLUEC),
                      T("Pha 2: duyệt theo thứ tự đó, ĐẨY ways sang đỉnh kề", size=28, color=GOOD),
                      T("Mỗi đỉnh, mỗi cạnh xử lí 2 lần: O(n + m)", size=28, color=ACCENT)).arrange(DOWN, buff=0.12)
        fit_stack(code, note, buff=0.7, max_scale=1.2)
        with self.voice("Code có hai pha. Pha một tìm thứ tự tô pô bằng thuật toán Kahn: danh sách order vừa là hàng đợi vừa là "
                        "kết quả."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 2, BLUEC)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 5, BLUEC)), run_time=0.4)
            self.play(FadeIn(note[0]), run_time=0.3)
        with self.voice("Pha hai duyệt các đỉnh theo thứ tự đó, và đẩy ways của v sang mọi đỉnh kề, lấy dư cho MOD. Mỗi đỉnh và "
                        "mỗi cạnh được xử lí đúng hai lần: O của n cộng m."):
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.4)
            self.play(FadeIn(note[1:]), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_04_DAG(B12Scene):
    def construct(self):
        self.show_header("Mọi bài quy hoạch động là một DAG")
        intro = VGroup(T("Mỗi TRẠNG THÁI là một đỉnh; cạnh A → B", size=28),
                       T("nếu B được tính từ A.", size=28)).arrange(DOWN, buff=0.1)
        # Bài 1: chuỗi
        chain = VGroup(*[VGroup(Circle(radius=0.3, fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=3),
                                T(f"{k}", size=22)) for k in range(7)]).arrange(RIGHT, buff=0.45)
        for c in chain:
            c[1].move_to(c[0])
        c_arcs = VGroup()
        for d, col in ((1, BLUEC), (2, GOOD), (3, ORANGE)):
            a, b = chain[6 - d][0], chain[6][0]
            c_arcs.add(CurvedArrow(a.get_top() + UP * 0.02, b.get_top() + UP * 0.02, angle=-PI * 0.5 if d > 1 else -PI * 0.3,
                                   color=col, stroke_width=3, tip_length=0.15))
        c_lab = T("Bài 1: i − 3, i − 2, i − 1 → i", size=26, color=MUTED)
        g1 = VGroup(placeholder(6, 1.1), chain, c_lab).arrange(DOWN, buff=0.15)
        c_arcs.shift(chain.get_center() - chain.get_center())
        # Bài 3: lưới
        grid = VGroup(*[Square(0.8, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED, stroke_width=2)
                        for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0)
        target = grid[4]
        target.set_fill(ACCENT, 0.8)
        grid[1].set_fill(GOOD, 0.6)
        grid[3].set_fill(GOOD, 0.6)
        ga = VGroup(Arrow(grid[1].get_center(), target.get_center(), buff=0.05, color=INK, stroke_width=5, tip_length=0.2),
                    Arrow(grid[3].get_center(), target.get_center(), buff=0.05, color=INK, stroke_width=5, tip_length=0.2))
        g_lab = T("Bài 3: ô trên, ô trái → ô", size=26, color=MUTED)
        g3 = VGroup(VGroup(grid, ga), g_lab).arrange(DOWN, buff=0.15)
        # Bài 8: đoạn
        segs = VGroup(*[Line(LEFT * w / 2, RIGHT * w / 2, color=c, stroke_width=8) for w, c in
                        ((1.0, BLUEC), (2.0, GOOD), (3.0, ACCENT))]).arrange(DOWN, buff=0.2)
        s_lab = T("Bài 8: đoạn ngắn → đoạn dài", size=26, color=MUTED)
        g8 = VGroup(segs, s_lab).arrange(DOWN, buff=0.15)
        row = VGroup(g3, g8).arrange(RIGHT, buff=0.8)
        key = tag_box("MỌI BÀI QUY HOẠCH ĐỘNG LÀ MỘT DAG", [
            "Không chu trình (nếu có, công thức “tự gọi",
            "chính mình”). Mọi thứ tự điền bảng đúng = một",
            "THỨ TỰ TÔ PÔ. Đếm cách = đếm đường đi;",
            "tối ưu = đường dài nhất / ngắn nhất trên DAG.",
        ], accent=PURPLE, width=7.5, size=27)
        fit_stack(intro, g1, row, key, buff=0.55, max_scale=1.2)
        for k, d in enumerate((1, 2, 3)):
            a, b = chain[6 - d][0], chain[6][0]
            c_arcs[k].become(CurvedArrow(a.get_top() + UP * 0.02, b.get_top() + UP * 0.02, angle=-PI * (0.55 + 0.1 * d),
                                         color=c_arcs[k].get_color(), stroke_width=4, tip_length=0.18))
        with self.voice("Bây giờ nhìn lại mọi thứ đã học. Hãy vẽ mỗi trạng thái là một đỉnh, và vẽ cạnh từ trạng thái A tới trạng "
                        "thái B nếu B được tính từ A."):
            self.play(FadeIn(intro), run_time=0.6)
        with self.voice("Ở Bài 1, đó là các cạnh từ i trừ 3, i trừ 2, i trừ 1 tới i."):
            self.play(FadeIn(chain), FadeIn(c_lab), run_time=0.6)
            self.play(*[Create(a) for a in c_arcs], run_time=0.8)
        with self.voice("Ở Bài 3, là các cạnh từ ô trên và ô trái. Ở Bài 8, là từ đoạn ngắn tới đoạn dài."):
            self.play(FadeIn(g3), run_time=0.6)
            self.play(FadeIn(g8), run_time=0.6)
        with self.voice("Đồ thị này không có chu trình: nếu có, công thức sẽ tự gọi chính mình và không tính được. Mọi thứ tự điền "
                        "bảng đúng mà em đã học đều là một thứ tự tô pô của đồ thị trạng thái. Bài toán đếm cách là đếm đường đi; "
                        "bài toán tối ưu là tìm đường dài nhất hoặc ngắn nhất trên DAG."):
            self.play(FadeIn(key), run_time=1.0)

        self.clear_body()
        self.show_header("Biến thể: Đường đi dài nhất")
        f = panel(M("longest(v) = max(longest(u) + w(u, v))", size=27, color=ACCENT), stroke=ACCENT, width=7.5)
        sub = T("với mọi cạnh u → v: thay phép CỘNG bằng phép MAX", size=27)
        cmp_ = VGroup(
            VGroup(TB("Đồ thị tổng quát", size=30, color=BAD), T("(có chu trình): CỰC KHÓ", size=28)).arrange(DOWN, buff=0.1),
            VGroup(TB("Trên DAG", size=30, color=GOOD), T("chỉ O(n + m)", size=28)).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.0)
        moral = TB("Không chu trình = điều kiện sống còn của QHĐ", size=30, color=ACCENT)
        fit_stack(f, sub, cmp_, moral, buff=0.8, max_scale=1.2)
        with self.voice("Biến thể: đường đi dài nhất. Thay phép cộng bằng phép max: longest của v bằng max của longest u cộng độ "
                        "dài cạnh từ u tới v."):
            self.play(FadeIn(f), FadeIn(sub), run_time=0.8)
        with self.voice("Trên đồ thị tổng quát có chu trình, tìm đường đi dài nhất là bài toán cực khó; nhưng trên DAG thì chỉ O "
                        "của n cộng m."):
            self.play(FadeIn(cmp_), run_time=0.8)
        with self.voice("Không có chu trình chính là điều kiện sống còn của quy hoạch động."):
            self.play(FadeIn(moral), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_05_XucXac(B12Scene):
    def construct(self):
        self.show_header("2. Xác suất: Bài toán XUCXAC")
        task = tag_box("BÀI TOÁN: XUCXAC", [
            "Tung n con xúc xắc cân đối 6 mặt (n ≤ 100).",
            "Tính xác suất để tổng số chấm nằm trong [A, B].",
        ], width=7.5, size=28)
        ex = VGroup(
            VGroup(M("2 7 7", size=30, color=BLUEC), T("→", size=30), TB("0.166667", size=32, color=GOOD),
                   T("6 trong 36 kết quả", size=24, color=MUTED)).arrange(RIGHT, buff=0.25),
            VGroup(M("3 10 11", size=30, color=BLUEC), T("→", size=30), TB("0.250000", size=32, color=GOOD),
                   T("54 trong 216", size=24, color=MUTED)).arrange(RIGHT, buff=0.25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        naive = VGroup(T("Ngây thơ: liệt kê 6ⁿ kết quả.", size=28),
                       T("n = 10: hơn 60 triệu; n = 100: không tưởng.", size=28, color=BAD)).arrange(DOWN, buff=0.1)
        form = tag_box("CÔNG THỨC XÁC SUẤT", [
            "P(i, s) = xác suất i con đầu có tổng ĐÚNG BẰNG s",
            "P(i, s) = Σ P(i − 1, s − f) · 1/6,  f = 1..6",
            "P(0, 0) = 1.  Đáp án: Σ P(n, s), A ≤ s ≤ B",
            "n × 6n ô, mỗi ô 6 phép: O(36n²) ≈ 3,6·10⁵",
        ], accent=GOOD, width=7.5, size=27)
        form[3][1].set_color(ACCENT)
        fit_stack(task, ex, naive, form, buff=0.5, max_scale=1.2)
        with self.voice("Câu hỏi thứ hai, về xác suất. Bài XUCXAC: tung n con xúc xắc cân đối 6 mặt, n tới 100. Tính xác suất "
                        "để tổng số chấm nằm trong đoạn A đến B."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Ví dụ: hai con, tổng bằng 7: 6 trong 36 kết quả, xác suất một phần sáu. Ba con, tổng 10 hoặc 11: 27 cộng "
                        "27 bằng 54 trong 216 kết quả, xác suất một phần tư."):
            self.play(FadeIn(ex), run_time=0.8)
        with self.voice("Cách ngây thơ liệt kê 6 mũ n kết quả: n bằng 10 đã hơn 60 triệu, n bằng 100 thì không tưởng."):
            self.play(FadeIn(naive), run_time=0.6)
        with self.voice("Quy hoạch động: đặt P của i, s là xác suất để i con xúc xắc đầu tiên có tổng đúng bằng s. Con thứ i ra "
                        "mỗi mặt f với xác suất một phần sáu, độc lập với các con trước, nên P của i, s bằng tổng P của i trừ 1, s "
                        "trừ f, nhân một phần sáu."):
            self.play(FadeIn(form[0:3]), FadeIn(form[3][0:2]), run_time=1.0)
        with self.voice("Cơ sở P của 0, 0 bằng 1. Bảng có n nhân 6n ô, mỗi ô 6 phép: với n bằng 100 chỉ khoảng ba trăm sáu mươi "
                        "nghìn phép."):
            self.play(FadeIn(form[3][2:]), run_time=0.6)

        self.clear_body()
        self.show_header("Phân bố tổng của 2 và 3 con xúc xắc")
        d1 = bars({f: 1 for f in range(1, 7)}, unit=0.35, w=0.5)
        d2 = bars(D2, highlight=(7,), unit=0.3, w=0.5)
        d3 = bars(D3, highlight=(10, 11), unit=0.075, w=0.44, label_size=16)
        t1 = T("1 con: mỗi tổng 1..6 có 1 cách", size=26, color=MUTED)
        t2 = VGroup(T("2 con: số cách tổng s =", size=26, color=MUTED),
                    T("tổng 6 ô kề nhau của hàng trên", size=26, color=MUTED)).arrange(DOWN, buff=0.06)
        t3 = T("3 con: tổng 10, 11 có 27 + 27 = 54 cách / 216", size=26, color=ACCENT)
        b1 = VGroup(t1, d1).arrange(DOWN, buff=0.2)
        b2 = VGroup(t2, d2).arrange(DOWN, buff=0.2)
        b3 = VGroup(t3, d3).arrange(DOWN, buff=0.2)
        sc = fit_stack(b1, b2, b3, buff=0.55, max_scale=1.2)
        with self.voice("Xem bảng chạy thế nào. Dưới đây là số cách, tức xác suất nhân 6 mũ i. Với một con xúc xắc, mỗi tổng từ 1 "
                        "đến 6 có đúng một cách."):
            self.play(FadeIn(t1), LaggedStart(*[GrowFromEdge(c[0], DOWN) for c in d1], lag_ratio=0.1),
                      *[FadeIn(c[1:]) for c in d1], run_time=1.0)
        win = SurroundingRectangle(VGroup(*[d1[k][0] for k in range(6)]), color=ACCENT, buff=0.08)
        with self.voice("Thêm con thứ hai: số cách để tổng bằng s là tổng số cách ở s trừ 1, s trừ 2, cho đến s trừ 6 của hàng "
                        "trên. Tổng 7 gom được cả sáu ô, nên có 6 cách, nhiều nhất."):
            self.play(FadeIn(t2), run_time=0.4)
            self.play(Create(win), run_time=0.4)
            self.play(LaggedStart(*[GrowFromEdge(c[0], DOWN) for c in d2], lag_ratio=0.08),
                      *[FadeIn(c[1:]) for c in d2], run_time=1.4)
            self.play(FadeOut(win), run_time=0.3)
        with self.voice("Con thứ ba: phân bố có hình quả chuông. Tổng 10 và 11 mỗi tổng có 27 cách, cộng lại 54 trên 216, đúng "
                        "một phần tư."):
            self.play(FadeIn(t3), LaggedStart(*[GrowFromEdge(c[0], DOWN) for c in d3], lag_ratio=0.05),
                      *[FadeIn(c[1:]) for c in d3], run_time=1.6)

        self.clear_body()
        self.show_header("XUCXAC.CPP: Quy hoạch động xác suất")
        code = code_block(DICE_CODE, size=21)
        note = VGroup(T("So với bài đếm: chỉ NHÂN thêm xác suất (1/6)", size=28, color=GOOD),
                      T("Đếm số nguyên rồi chia 6ⁿ? 6¹⁰⁰ vượt mọi kiểu số", size=27),
                      T("nguyên ⇒ làm trực tiếp với double an toàn hơn.", size=27)).arrange(DOWN, buff=0.12)
        fit_stack(code, note, buff=0.7, max_scale=1.2)
        with self.voice("Code: mảng chance giữ phân bố của các con đã tung. Với mỗi con mới, tạo mảng next, và đẩy chance của s "
                        "chia 6 sang s cộng f với mọi mặt f."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 1, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 6, GOOD)), run_time=0.4)
        with self.voice("So với bài đếm, chỉ có một thay đổi: mỗi cách chuyển trạng thái được nhân với xác suất của nó. Ta cũng có "
                        "thể đếm số cách rồi chia cho 6 mũ n, nhưng 6 mũ 100 vượt xa mọi kiểu số nguyên; làm trực tiếp với số "
                        "thực an toàn hơn."):
            self.play(FadeOut(hl), FadeIn(note), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_06_KyVong(B12Scene):
    def construct(self):
        self.show_header("3. Kì vọng: Tung tới khi đủ điểm")
        task = tag_box("BÀI TOÁN: KÌ VỌNG SỐ LẦN TUNG", [
            "Tung một con xúc xắc liên tục, cộng dồn số chấm,",
            "dừng khi tổng đạt ÍT NHẤT N. Trung bình phải",
            "tung bao nhiêu lần?",
        ], accent=PURPLE, width=7.5, size=28)
        kv = VGroup(T("Kì vọng = trung bình có trọng số (trọng số = xác suất)", size=26),
                    T("Tuyến tính: kì vọng của tổng = tổng các kì vọng", size=26, color=GOOD)).arrange(DOWN, buff=0.1)
        defn = VGroup(T("E[s] = số lần trung bình CÒN PHẢI tung,", size=28, color=ACCENT),
                      T("khi tổng hiện tại là s", size=28, color=ACCENT)).arrange(DOWN, buff=0.08)
        form = tag_box("CÔNG THỨC KÌ VỌNG", [
            "E[s] = 1 + (1/6)·(E[s+1] + … + E[s+6]),  s < N",
            "E[s] = 0 với s ≥ N",
            "Tính s GIẢM DẦN từ N − 1 về 0. Đáp án E[0].",
        ], accent=GOOD, width=7.5, size=27)
        fit_stack(task, kv, defn, form, buff=0.55, max_scale=1.2)
        with self.voice("Câu hỏi thứ ba: tung một con xúc xắc liên tục và cộng dồn số chấm, dừng khi tổng đạt ít nhất N. Trung "
                        "bình phải tung bao nhiêu lần?"):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Kì vọng của một đại lượng ngẫu nhiên là trung bình có trọng số của các giá trị có thể, với trọng số là "
                        "xác suất. Tính chất quan trọng nhất là tính tuyến tính: kì vọng của tổng bằng tổng các kì vọng."):
            self.play(FadeIn(kv), run_time=0.8)
        with self.voice("Đặt E của s là số lần trung bình còn phải tung, khi tổng hiện tại là s."):
            self.play(FadeIn(defn), run_time=0.6)
        with self.voice("Nếu s đã đạt N thì đã dừng: E bằng 0. Nếu s nhỏ hơn N, ta tung thêm 1 lần, được mặt f với xác suất "
                        "một phần sáu, rồi ở vào trạng thái s cộng f. Vậy E của s bằng 1 cộng trung bình của sáu giá trị E kế "
                        "tiếp. Tính s giảm dần từ N trừ 1 về 0."):
            self.play(FadeIn(form), run_time=1.0)

        self.clear_body()
        self.show_header("Bảng E với N = 6 (tính từ phải sang trái)")
        vals = [f"{x:.4f}".replace(".", ",") for x in E6F]
        cells = VGroup()
        for k in range(12):
            if k < 6:
                sq = Rectangle(width=1.1, height=0.95, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED, stroke_width=2)
                cells.add(VGroup(sq, TB("0", size=30).move_to(sq).set_opacity(0)))
            else:
                cells.add(cell("0", w=0.5, h=0.95, size=24, fill=BG, color=MUTED))
        cells.arrange(RIGHT, buff=0)
        idx = VGroup(*[T(str(k), size=20, color=MUTED).next_to(cells[k], UP, buff=0.08) for k in range(12)])
        lab = TB("E", size=34, color=ACCENT).next_to(cells, LEFT, buff=0.2)
        row = VGroup(cells, idx, lab)
        row.cells = cells
        stop = T("s ≥ 6: đã dừng, E = 0", size=24, color=MUTED)
        calc_slot = placeholder(7.4, 1.4)
        big = VGroup(TB("E[0] ≈ 2,1614 lần", size=40, color=GOOD),
                     T("Thú vị: với N ≤ 7, E[0] = (7/6)^(N−1); N = 6: (7/6)⁵", size=25, color=MUTED)).arrange(DOWN, buff=0.15)
        sc = fit_stack(row, stop, calc_slot, big, buff=0.6, max_scale=1.2)
        stop.next_to(VGroup(*row.cells[6:]), DOWN, buff=0.15 * sc)
        with self.voice("Chạy với N bằng 6. Các ô từ 6 trở đi đã dừng, E bằng 0. Ta tính từ phải sang trái."):
            self.play(FadeIn(row), FadeIn(stop), run_time=0.8)
        explain = {
            5: ("E[5] = 1 + (0+0+0+0+0+0)/6 = 1",
                "Từ tổng 5, tung thêm một lần là chắc chắn đạt 6: E của 5 bằng 1."),
            4: ("E[4] = 1 + (1+0+0+0+0+0)/6 ≈ 1,1667",
                "Từ tổng 4: tung một lần, nếu ra 1 thì về tổng 5, còn phải tung thêm. E của 4 bằng 1 cộng một phần sáu, "
                "khoảng 1 phẩy 1667."),
            3: ("E[3] = 1 + (1,1667 + 1)/6 ≈ 1,3611", "E của 3 bằng 1 cộng một phần sáu của 1 phẩy 1667 cộng 1, khoảng 1 phẩy 3611."),
            2: ("E[2] = 1 + (1,3611 + 1,1667 + 1)/6 ≈ 1,5880", "E của 2 khoảng 1 phẩy 588."),
            1: ("E[1] ≈ 1,8526", "E của 1 khoảng 1 phẩy 8526."),
            0: ("E[0] = 1 + (E[1] + … + E[6])/6 ≈ 2,1614", "Và E của 0, đáp án, khoảng 2 phẩy 1614."),
        }
        cur = None
        for s in range(5, -1, -1):
            txt, sp = explain[s]
            line = M(txt, size=24, color=INK).scale(sc)
            if line.width > calc_slot.width:
                line.scale_to_fit_width(calc_slot.width)
            line.move_to(calc_slot)
            with self.voice(sp):
                src = VGroup(*row.cells[s + 1:s + 7])
                br = SurroundingRectangle(src, color=ACCENT, buff=0.04)
                self.play(Create(br), FadeIn(line) if cur is None else Transform(cur, line), run_time=0.5)
                if cur is None:
                    cur = line
                c = row.cells[s]
                self.play(c[0].animate.set_fill(GOOD, 1), Transform(c[1], set_cell_value(c, vals[s], color=BG)), run_time=0.5)
                self.play(FadeOut(br), run_time=0.3)
        with self.voice("Vậy trung bình cần khoảng 2 phẩy 16 lần tung. Một điều thú vị: với N không quá 7, E của 0 đúng bằng 7 "
                        "phần 6, mũ N trừ 1."):
            self.play(FadeIn(big), run_time=0.8)

        self.clear_body()
        self.show_header("Chiều tính: xuôi hay ngược?")
        dirs = VGroup(
            panel(VGroup(TB("XÁC SUẤT: tính XUÔI →", size=30, color=BLUEC),
                         T("từ trạng thái đầu: đã biết xác suất tới đây", size=26)).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
                  stroke=BLUEC, width=7.5),
            panel(VGroup(TB("KÌ VỌNG “số bước còn lại”: NGƯỢC ←", size=30, color=GOOD),
                         T("từ trạng thái cuối: giá trị ở cuối đã biết = 0", size=26)).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
                  stroke=GOOD, width=7.5),
        ).arrange(DOWN, buff=0.35)
        for p in dirs:
            p[1].align_to(p[0], LEFT).shift(RIGHT * 0.3)
        code = code_block(EXP_CODE, size=22)
        fit_stack(dirs, code, buff=0.7, max_scale=1.2)
        with self.voice("Chú ý chiều tính. Xác suất thường được tính xuôi, từ trạng thái đầu, vì ta biết xác suất đã tới đây."):
            self.play(FadeIn(dirs[0]), run_time=0.6)
        with self.voice("Còn kì vọng số bước còn lại được tính ngược, từ trạng thái cuối, vì giá trị ở cuối đã biết bằng 0."):
            self.play(FadeIn(dirs[1]), run_time=0.6)
        with self.voice("Code chỉ vài dòng: mảng expect có thêm 6 ô bằng 0 ở cuối; duyệt s giảm dần, cộng sáu ô kế tiếp, chia 6, "
                        "cộng 1."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 1, GOOD)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 5, GOOD)), run_time=0.4)
        self.clear_body()


# ----------------------------------------------------------------------------
class B12_07_TongKet(B12Scene):
    def construct(self):
        self.show_header("4. Mở rộng")
        ext = [
            ("Đếm cấu trúc tổ hợp", "dãy ngoặc đúng: trạng thái (i, số ngoặc mở ≥ 0)",
             "Mở rộng một: đếm cấu trúc tổ hợp. Ví dụ đếm dãy ngoặc đúng độ dài 2n: trạng thái là i kí tự đã viết, và số ngoặc "
             "mở chưa đóng, luôn không âm. Mở ngoặc làm nó tăng 1, đóng ngoặc làm giảm 1. Đáp án là trạng thái 2n, 0."),
            ("Đồ thị có chu trình", "không có thứ tự tô pô: Dijkstra / giải hệ phương trình",
             "Mở rộng hai: nếu đồ thị trạng thái có chu trình, ví dụ trò chơi có thể quay lại vị trí cũ, thì không có thứ tự tô "
             "pô, quy hoạch động thông thường không dùng được. Đường ngắn nhất thì dùng Dijkstra; kì vọng có chu trình thì "
             "phải giải hệ phương trình."),
            ("Lấy dư phép chia", "chia 6 ⇒ nhân nghịch đảo 6^(p−2) mod p (Fermat)",
             "Mở rộng ba: khi đề yêu cầu xác suất dạng phân số lấy dư theo số nguyên tố p, thay phép chia cho 6 bằng nhân với "
             "nghịch đảo modulo của 6, tính bằng lũy thừa nhanh 6 mũ p trừ 2, theo định lí Fermat nhỏ."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Đồ thị có chu trình", "Kahn không lấy hết đỉnh: kiểm tra order.size() == n",
             "Bẫy một: đồ thị có chu trình nhưng vẫn áp dụng thứ tự tô pô. Kahn sẽ không lấy được hết các đỉnh; hãy kiểm tra "
             "kích thước order bằng n."),
            ("Khởi tạo sai", "ways = 1 cho MỌI đỉnh bán bậc vào 0 ⇒ đếm thừa",
             "Bẫy hai: đỉnh không tới được từ 1 có ways bằng 0, vẫn đúng; nhưng nếu khởi tạo ways bằng 1 cho mọi đỉnh có bán "
             "bậc vào 0, sẽ đếm cả đường không bắt đầu từ 1."),
            ("Sai số số thực", "in đủ chữ số; tránh trừ hai số gần bằng nhau",
             "Bẫy ba: sai số số thực. In đủ số chữ số yêu cầu, và tránh trừ hai số gần bằng nhau."),
            ("Kì vọng tính xuôi", "“số bước còn lại” phải tính từ trạng thái cuối",
             "Bẫy bốn: tính kì vọng số bước còn lại theo chiều xuôi. Phải tính từ trạng thái cuối."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 12", [
            "• Trạng thái là đỉnh, phép chuyển là cạnh:",
            "   QHĐ = duyệt DAG theo THỨ TỰ TÔ PÔ",
            "• Đếm: cộng số cách. Xác suất: cộng",
            "   (xác suất nguồn × xác suất chuyển).",
            "   Tối ưu: max / min.",
            "• Kì vọng: E = 1 + trung bình có trọng số",
            "   của E kế tiếp, tính NGƯỢC từ cuối",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: trạng thái là đỉnh, phép chuyển là cạnh; quy hoạch động chính là duyệt DAG theo thứ tự tô pô."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:2]), run_time=1.0)
        with self.voice("Đếm thì cộng số cách. Xác suất thì cộng xác suất nguồn nhân xác suất chuyển. Tối ưu thì lấy max hoặc min. "
                        "Kì vọng bằng 1 cộng trung bình có trọng số của E các trạng thái kế tiếp, tính ngược từ cuối."):
            self.play(FadeIn(mem[3][2:]), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Thêm cạnh 1 → 4 vào ví dụ", "DUONGMOTCHIEU: có bao nhiêu đường?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.2)
        g = dag(GEDGES + [(1, 4)])
        g.arrows[(1, 4)].set_color(ACCENT).set_stroke(width=6)
        ans = VGroup(T("ways(4) = 1 + 1 + 1 = 3", size=30, color=ACCENT),
                     TB("ways(6) = 3 + 1 + 1 = 5", size=38, color=GOOD)).arrange(DOWN, buff=0.12)
        fit_stack(q, timer_slot, g, ans, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: nếu thêm cạnh từ 1 tới 4 vào ví dụ DUONGMOTCHIEU, có bao nhiêu đường đi? Dừng video "
                        "và thử nhé!"):
            self.play(FadeIn(q), FadeIn(g), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=80, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("ways của 4 giờ nhận thêm 1 từ đỉnh 1, thành 3. ways của 6 bằng ways 4 cộng ways 5 cộng ways 3, bằng 3 cộng "
                        "1 cộng 1, bằng 5 đường."):
            self.play(FadeIn(ans), run_time=0.8)

        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
        done = VGroup(TB("HOÀN THÀNH", size=60, color=GOOD), TB("CHƯƠNG 3", size=72, color=ACCENT)).arrange(DOWN, buff=0.2)
        recap = VGroup(*[T(t, size=30) for t in [
            "Bài 8 · QHĐ trên đoạn",
            "Bài 9 · Trạng thái tập con (bitmask)",
            "Bài 10 · QHĐ chữ số",
            "Bài 11 · QHĐ trên cây",
            "Bài 12 · Đếm, DAG, xác suất, kì vọng",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        nxt = VGroup(TB("Tiếp theo: CHƯƠNG 4", size=40, color=ACCENT),
                     T("Tối ưu hóa quy hoạch động", size=32),
                     T("(Bài 13)", size=26, color=MUTED)).arrange(DOWN, buff=0.15)
        fit_stack(done, recap, nxt, buff=0.9, max_scale=1.2)
        with self.voice("Chúc mừng các em đã hoàn thành Chương 3! Ta đã đi qua quy hoạch động trên đoạn, trạng thái tập con, quy "
                        "hoạch động chữ số, quy hoạch động trên cây, và cuối cùng là đếm, đồ thị có hướng, xác suất và kì vọng."):
            self.play(FadeIn(done, scale=1.2), run_time=1.0)
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in recap], lag_ratio=0.3), run_time=1.6)
        with self.voice("Chương 4 sẽ trả lời một câu hỏi mới: khi công thức đã đúng nhưng chương trình vẫn chạy quá thời gian, làm "
                        "sao tối ưu hóa? Hẹn gặp lại các em ở Bài 13!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.play(FadeOut(VGroup(done, recap, nxt)), run_time=0.6)
