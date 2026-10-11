"""BÀI 4 — Cái túi 0/1 và cái túi không giới hạn (BALOCUUTRO, DOITEM)."""

from shared import *  # noqa: F401,F403

W_ITEMS = [6, 5, 5, 3]
V_ITEMS = [30, 20, 22, 9]
CAP = 10


def knapsack(w, v, cap):
    f = [[0] * (cap + 1)]
    for i in range(len(w)):
        row = f[-1][:]
        for c in range(w[i], cap + 1):
            row[c] = max(row[c], f[-1][c - w[i]] + v[i])
        f.append(row)
    return f


F = knapsack(W_ITEMS, V_ITEMS, CAP)
assert F[4][10] == 42 and F[4][9] == 39 and knapsack(W_ITEMS, V_ITEMS, 11)[4][11] == 52


def trace(f, w):
    steps, c = [], len(f[0]) - 1
    for i in range(len(f) - 1, 0, -1):
        if f[i][c] == f[i - 1][c]:
            steps.append((i, c, i - 1, c, False))
        else:
            steps.append((i, c, i - 1, c - w[i - 1], True))
            c -= w[i - 1]
    return steps


TRACE = trace(F, W_ITEMS)
assert [s[4] for s in TRACE] == [False, True, True, False]

COINS = [1, 2, 5]
WAYS_ROWS = []
_w = [1, 0, 0, 0, 0, 0]
for _c in COINS:
    for _s in range(_c, 6):
        _w[_s] += _w[_s - _c]
    WAYS_ROWS.append(_w[:])
assert WAYS_ROWS[-1][5] == 4
ORDERED = [1, 0, 0, 0, 0, 0]
for _s in range(1, 6):
    ORDERED[_s] = sum(ORDERED[_s - c] for c in COINS if _s >= c)
assert ORDERED[5] == 9


class B4Scene(NarratedScene):
    lesson_tag = "BÀI 4"
    lesson_title = "Cái túi 0/1 và cái túi không giới hạn"


ITEM_COLORS = ["#B45309", "#0E7490", "#7C3AED", "#BE185D"]


def make_crate(k, w, v, size=1.5):
    box = RoundedRectangle(width=size, height=size, corner_radius=0.1, fill_color=ITEM_COLORS[k], fill_opacity=1,
                           stroke_color=INK, stroke_width=2)
    slats = VGroup(*[Line(box.get_left() + RIGHT * 0.08 + UP * dy, box.get_right() + LEFT * 0.08 + UP * dy,
                          color=INK, stroke_width=1.5, stroke_opacity=0.35) for dy in (-size / 4, size / 4)])
    name = TB(f"Kiện {k + 1}", size=size * 14, color=INK).move_to(box.get_top() + DOWN * size * 0.18)
    kg = TB(f"{w} kg", size=size * 20, color=INK).move_to(box.get_center() + DOWN * size * 0.02)
    val = TB(f"{v}", size=size * 19, color=ACCENT).move_to(box.get_bottom() + UP * size * 0.2)
    g = VGroup(box, slats, name, kg, val)
    return g


def make_truck(cap=10):
    body = RoundedRectangle(width=4.2, height=1.6, corner_radius=0.15, fill_color="#334155", fill_opacity=1,
                            stroke_color=INK, stroke_width=2)
    cab = RoundedRectangle(width=1.2, height=1.2, corner_radius=0.15, fill_color="#475569", fill_opacity=1,
                           stroke_color=INK, stroke_width=2)
    cab.next_to(body, RIGHT, buff=0.05).align_to(body, DOWN)
    win = RoundedRectangle(width=0.6, height=0.45, corner_radius=0.08, fill_color="#93C5FD", fill_opacity=1,
                           stroke_width=0).move_to(cab.get_center() + UP * 0.2 + RIGHT * 0.15)
    wheels = VGroup(*[Circle(radius=0.28, fill_color="#111827", fill_opacity=1, stroke_color=MUTED, stroke_width=3)
                      .move_to(p) for p in [body.get_corner(DL) + RIGHT * 0.7, body.get_corner(DR) + LEFT * 0.7,
                                            cab.get_bottom() + RIGHT * 0.1]])
    wheels.shift(DOWN * 0.15)
    lab = TB(f"chở tối đa {cap} kg", size=24, color=ACCENT).move_to(body.get_top() + UP * 0.3)
    g = VGroup(body, cab, win, wheels, lab)
    g.body = body
    return g


class Table2D(VGroup):
    """Bảng f(i, c): hàng i = 0..m-1, cột c = 0..n-1, có nhãn hàng/cột."""

    def __init__(self, m, n, w=0.62, h=0.62, row_labels=None, col_title="c", row_title="i"):
        super().__init__()
        self.cells = {}
        self.w, self.h = w, h
        for i in range(m):
            for c in range(n):
                sq = Rectangle(width=w, height=h, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED,
                               stroke_width=1.5).move_to([c * w, -i * h, 0])
                ghost = TB("0", size=h * 36).move_to(sq).set_opacity(0)  # chỗ giữ để Transform hoạt động
                self.cells[(i, c)] = VGroup(sq, ghost)
                self.add(self.cells[(i, c)])
        cl = VGroup(*[T(str(c), size=20, color=MUTED).next_to(self.cells[(0, c)], UP, buff=0.08) for c in range(n)])
        labels = row_labels or [str(i) for i in range(m)]
        rl = VGroup(*[T(labels[i], size=20, color=MUTED).next_to(self.cells[(i, 0)], LEFT, buff=0.12)
                      for i in range(m)])
        ct = T(col_title, size=22, color=ACCENT).next_to(cl, UP, buff=0.08)
        self.labels = VGroup(cl, rl, ct)
        self.add(self.labels)

    def value(self, i, c, v, color=INK):
        cellg = self.cells[(i, c)]
        return set_cell_value(cellg, v, color=color, size=cellg[0].height * 36)

    def fill(self, i, c, v, fill=None, color=INK):
        cellg = self.cells[(i, c)]
        anims = []
        if fill:  # ô nền trước, chữ sau: giữ chữ nằm trên khi chạy trong LaggedStart
            anims.append(cellg[0].animate.set_fill(fill, 1))
        anims.append(Transform(cellg[1], self.value(i, c, v, color)))
        return anims


# ----------------------------------------------------------------------------
class B4_00_Intro(B4Scene):
    def construct(self):
        chap = TB("CHƯƠNG 2", size=44, color=ACCENT)
        title = VGroup(TB("CÁC MÔ HÌNH", size=64), TB("KINH ĐIỂN", size=64)).arrange(DOWN, buff=0.2)
        bar = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        cover = VGroup(chap, title, bar).arrange(DOWN, buff=0.35)
        quote = VGroup(T("Bài chia kẹo là cái túi,", size=32), T("bài xếp hàng là dãy con tăng,", size=32),
                       T("so sánh ADN là dãy con chung.", size=32)).arrange(DOWN, buff=0.15)
        key = TB("Nhận ra mô hình = đi được nửa đường!", size=32, color=GOOD)
        fit_stack(cover, quote, key, buff=0.8, max_scale=1.2)
        with self.voice("Chào các em! Chúng ta bước sang Chương 2: Các mô hình kinh điển."):
            self.play(FadeIn(chap, shift=DOWN * 0.3), Write(title), run_time=1.8)
            self.play(GrowFromCenter(bar), run_time=0.5)
        with self.voice("Phần lớn các bài quy hoạch động trong đề thi không mới hoàn toàn. Chúng là những mô hình kinh điển "
                        "được khoác một câu chuyện khác."):
            self.play(FadeIn(quote[0]), run_time=0.6)
        with self.voice("Bài chia kẹo là cái túi, bài xếp hàng là dãy con tăng, bài so sánh hai đoạn ADN là dãy con chung."):
            self.play(FadeIn(quote[1]), run_time=0.6)
            self.play(FadeIn(quote[2]), run_time=0.6)
        with self.voice("Nhận ra mô hình ẩn sau câu chuyện là đã đi được nửa đường."):
            self.play(Write(key), run_time=1.0)

        self.clear_body()
        heading = TB("TRONG CHƯƠNG NÀY", size=42, color=ACCENT)
        items = [("Bài 4", "Cái túi 0/1 và không giới hạn"), ("Bài 5", "Cái túi mở rộng"),
                 ("Bài 6", "Dãy con tăng dài nhất"), ("Bài 7", "Quy hoạch động trên hai xâu")]
        cards = VGroup()
        for tag, ttl in items:
            pill = RoundedRectangle(width=1.4, height=0.7, corner_radius=0.35, fill_color=ACCENT, fill_opacity=1,
                                    stroke_width=0)
            row = VGroup(VGroup(pill, TB(tag, size=30, color=BG).move_to(pill)), TB(ttl, size=30)).arrange(RIGHT, buff=0.3)
            c = panel(row, width=7.5, pad=0.25)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.25)
            cards.add(c)
        cards.arrange(DOWN, buff=0.3)
        fit_stack(heading, cards, buff=0.6, max_scale=1.2)
        with self.voice("Chương này giới thiệu bốn mô hình quan trọng nhất: cái túi, trong hai bài, dãy con tăng dài nhất, "
                        "và quy hoạch động trên hai xâu."):
            self.play(FadeIn(heading), run_time=0.5)
            for c in cards:
                self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.6)

        self.clear_body()
        tag = TB("BÀI 4", size=80, color=ACCENT)
        ttl = VGroup(TB("Cái túi 0/1 và", size=48), TB("cái túi không giới hạn", size=48)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Mô hình hóa thành bảng hai chiều f(i, c)",
            "✓ Truy vết: chọn NHỮNG đồ vật nào",
            "✓ Một mảng: 0/1 duyệt GIẢM, không giới hạn TĂNG",
            "✓ Đếm tổ hợp và đếm chỉnh hợp",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Bài 4: Cái túi 0/1 và cái túi không giới hạn."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ mô hình hóa bài toán chọn đồ vật với giới hạn sức chứa thành bảng hai chiều "
                        "f của i, c, và truy vết để biết chọn những đồ vật nào."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ hiểu sâu vì sao khi dùng mảng một chiều, cái túi 0/1 phải duyệt sức chứa giảm dần, còn cái túi "
                        "không giới hạn duyệt tăng dần. Và phân biệt đếm tổ hợp với đếm chỉnh hợp chỉ bằng cách đổi thứ tự "
                        "hai vòng lặp."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B4_01_KhoiDong(B4Scene):
    def construct(self):
        self.show_header("Khởi động: Xe cứu trợ chở 10 kg")
        truck = make_truck()
        crates = VGroup(*[make_crate(k, W_ITEMS[k], V_ITEMS[k]) for k in range(4)]).arrange(RIGHT, buff=0.35)
        ratio = VGroup(*[T(f"{V_ITEMS[k] / W_ITEMS[k]:.1f}".replace(".", ",") + "/kg", size=22, color=MUTED)
                         .next_to(crates[k], DOWN, buff=0.12) for k in range(4)])
        res_slot = placeholder(7.4, 1.2)
        q = VGroup(T("Mỗi kiện chỉ có MỘT, chở cả kiện hoặc không.", size=28),
                   T("Chọn những kiện nào để tổng giá trị lớn nhất?", size=28, color=ACCENT)).arrange(DOWN, buff=0.12)
        sc = fit_stack(truck, VGroup(crates, ratio), q, res_slot, buff=0.6, max_scale=1.1)
        with self.voice("Một xe cứu trợ chở được tối đa 10 ki lô gam. Trong kho có bốn kiện hàng."):
            self.play(FadeIn(truck, shift=RIGHT * 0.5), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in crates], lag_ratio=0.2), run_time=1.2)
        with self.voice("Kiện 1 nặng 6 ki lô gam, giá trị 30. Kiện 2 nặng 5, giá trị 20. Kiện 3 nặng 5, giá trị 22. "
                        "Kiện 4 nặng 3, giá trị 9."):
            for c in crates:
                self.play(Indicate(c, scale_factor=1.08), run_time=0.45)
        with self.voice("Mỗi kiện chỉ có một, chở cả kiện hoặc không chở. Em chọn những kiện nào để tổng giá trị lớn nhất?"):
            self.play(FadeIn(q), run_time=0.8)
        with self.voice("Kiện 1 có giá trị lớn nhất, lại có giá trị trên mỗi ki lô gam cao nhất, 5 đơn vị một ki lô gam. "
                        "Chọn nó trước chắc chắn là khôn ngoan, phải không?"):
            self.play(FadeIn(ratio), run_time=0.6)
            self.play(Indicate(ratio[0], color=ACCENT, scale_factor=1.4), run_time=0.8)

        body = truck.body
        slot_x = [body.get_left()[0] + 0.15 * sc]

        def load(k):
            c = crates[k]
            target = c.copy().scale(0.75)
            target.move_to([slot_x[0] + target.width / 2, body.get_center()[1], 0])
            slot_x[0] += target.width + 0.05
            return c.animate.scale(0.75).move_to(target)

        with self.voice("Thử tham lam theo tỉ số: chọn kiện 1 trước. Xe còn trống 4 ki lô gam, chỉ nhét thêm được kiện 4. "
                        "Tổng giá trị 39."):
            self.play(load(0), run_time=0.8)
            self.play(load(3), run_time=0.8)
            g = TB("Tham lam theo tỉ số: 30 + 9 = 39", size=32, color=ORANGE).scale(sc).move_to(res_slot)
            self.play(FadeIn(g), run_time=0.5)
        with self.voice("Nhưng hai kiện 5 ki lô gam, dù tỉ số thấp hơn, ghép lại vừa khít 10 ki lô gam và cho tổng 42!"):
            back = VGroup(crates[0], crates[3])
            self.play(back.animate.set_opacity(0.25), run_time=0.4)
            slot_x[0] = body.get_left()[0] + 0.15 * sc
            self.play(load(1), run_time=0.7)
            self.play(load(2), run_time=0.7)
            b = TB("Tối ưu: kiện 2 + 3 = 20 + 22 = 42", size=32, color=GOOD).scale(sc).move_to(res_slot)
            self.play(Transform(g, b), run_time=0.6)
        with self.voice("Vấn đề của tham lam ở đây là sức chứa còn thừa bị lãng phí. Đồ vật không chia nhỏ được, nên giá trị "
                        "trên ki lô gam không còn là thước đo đúng. Nếu được cắt nhỏ kiện hàng, tham lam lại đúng: đó là bài "
                        "cái túi phân số."):
            self.play(Indicate(g, color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("1. Bài toán BALOCUUTRO")
        box = tag_box("BÀI TOÁN: BALOCUUTRO", [
            "n kiện hàng, kiện i nặng wᵢ kg, giá trị vᵢ.",
            "Xe chở tối đa W kg.",
            "Chọn một số kiện (mỗi kiện tối đa một lần),",
            "tổng khối lượng ≤ W, tổng giá trị LỚN NHẤT.",
            "In thêm các kiện được chọn.",
            "n ≤ 100,  W ≤ 10⁴",
        ], width=7.4, size=30)
        box[3][5].set_color(ORANGE)
        ex = VGroup(T("Ví dụ:", size=30, color=MUTED), TB("42", size=40, color=ACCENT),
                    T("chọn kiện 2 và 3 (nặng đúng 10 kg)", size=28)).arrange(RIGHT, buff=0.3)
        fit_stack(box, ex, buff=0.8, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán BALOCUUTRO: n kiện hàng, kiện i nặng w i và có giá trị v i. "
                        "Xe chở tối đa W ki lô gam. Chọn một số kiện, mỗi kiện tối đa một lần, có tổng khối lượng không vượt "
                        "quá W và tổng giá trị lớn nhất, đồng thời in ra các kiện được chọn."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Với ví dụ, đáp án là 42, chọn kiện 2 và kiện 3."):
            self.play(FadeIn(ex), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B4_02_NgayTho(B4Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: Thử mọi tập con")
        idea = VGroup(T("Mỗi kiện: BỎ hoặc LẤY", size=32),
                      T("Trạng thái (i, c): đã xét i kiện, xe còn trống c kg", size=27, color=MUTED)).arrange(DOWN, buff=0.12)
        # cây quyết định 3 tầng
        nodes = {"r": (0, 10)}
        edges = []

        def kids(key, i, c):
            out = [(key + "b", i + 1, c, "bỏ")]
            if c >= W_ITEMS[i]:
                out.append((key + "l", i + 1, c - W_ITEMS[i], f"lấy {i + 1}"))
            return out

        levels = [["r"]]
        for depth in range(3):
            nxt = []
            for key in levels[-1]:
                i, c = nodes[key]
                for k2, i2, c2, lab in kids(key, i, c):
                    nodes[k2] = (i2, c2)
                    edges.append((key, k2, lab))
                    nxt.append(k2)
            levels.append(nxt)
        pos = {}
        ys = [0, -1.5, -3.0, -4.5]
        for d, lv in enumerate(levels):
            n_ = len(lv)
            span = 7.2 if d == 3 else (5.4 if d == 2 else 3.6)
            for k, key in enumerate(lv):
                x = 0 if n_ == 1 else -span / 2 + k * span / (n_ - 1)
                pos[key] = np.array([x, ys[d], 0])
        mobs = {}
        for key, (i, c) in nodes.items():
            dup = (i, c) == (3, 5)
            box = RoundedRectangle(width=1.4, height=0.7, corner_radius=0.12,
                                   fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=2.5)
            t = TB(f"({i}, {c})", size=28).move_to(box)
            mobs[key] = VGroup(box, t).move_to(pos[key])
        emobs = VGroup()
        elabs = VGroup()
        for a, b, lab in edges:
            e = Line(mobs[a].get_bottom(), mobs[b].get_top(), color=MUTED, stroke_width=2.5)
            emobs.add(e)
            elabs.add(T(lab, size=22, color=GOOD if "lấy" in lab else MUTED).move_to(e.point_from_proportion(0.5) +
                                                                                     LEFT * 0.35))
        tree = VGroup(emobs, elabs, *mobs.values())
        note = placeholder(7.2, 1.0)
        sc = fit_stack(idea, tree, note, buff=0.5, max_scale=1.2)
        with self.voice("Mỗi kiện có hai lựa chọn: bỏ hoặc lấy. Ta viết hàm thử với trạng thái i, c: đã quyết định xong i kiện "
                        "đầu, xe còn trống c ki lô gam. Thử bỏ kiện tiếp theo, rồi thử lấy nó nếu còn đủ chỗ."):
            self.play(FadeIn(idea), run_time=0.8)
            self.play(FadeIn(mobs["r"]), run_time=0.4)
            for d in range(1, 4):
                anims = []
                for a, b, lab in edges:
                    if b in levels[d]:
                        idx = edges.index((a, b, lab))
                        anims += [Create(emobs[idx]), FadeIn(elabs[idx]), FadeIn(mobs[b])]
                self.play(*anims, run_time=0.8)
        dups = [k for k, v in nodes.items() if v == (3, 5)]
        with self.voice("Nhìn tầng thứ ba: trạng thái 3, 5 xuất hiện hai lần. Một lần là lấy kiện 2, bỏ kiện 3. "
                        "Lần kia là bỏ kiện 2, lấy kiện 3."):
            self.play(*[mobs[k][0].animate.set_fill(ACCENT, 1) for k in dups],
                      *[mobs[k][1].animate.set_color(BG) for k in dups], run_time=0.8)
            self.play(*[Indicate(mobs[k], color=ACCENT, scale_factor=1.2) for k in dups], run_time=1.0)
        t = VGroup(T("Từ đây, cả hai đối mặt ĐÚNG CÙNG MỘT bài toán con:", size=26),
                   T("chọn trong kiện 4..n với 5 kg trống!", size=26, color=ACCENT)).arrange(DOWN, buff=0.08)
        t.scale(sc).move_to(note)
        with self.voice("Từ đây trở đi, hai nhánh này đối mặt đúng cùng một bài toán con: chọn trong các kiện còn lại với 5 ki lô "
                        "gam trống. Quay lui giải bài toán con đó hai lần, và với n lớn thì hàng tỉ lần."):
            self.play(FadeIn(t), run_time=0.8)

        self.clear_body()
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Số tập con: 2ⁿ.  n = 30: ≈ 10⁹;  n = 100: ≈ 1,3·10³⁰",
            "Nhưng mỗi nút chỉ mô tả bởi HAI số (i, c):",
            "0 ≤ i ≤ n, 0 ≤ c ≤ W ⇒ tối đa (n+1)(W+1) trạng thái",
            "n = 100, W = 10⁴: chỉ khoảng 10⁶ trạng thái!",
        ], accent=ORANGE, width=7.5, size=28)
        cmp = VGroup(
            VGroup(TB("10³⁰", size=56, color=BAD), T("nút trên cây", size=26, color=MUTED)).arrange(DOWN, buff=0.1),
            TB("vs", size=36, color=MUTED),
            VGroup(TB("10⁶", size=56, color=GOOD), T("trạng thái khác nhau", size=26, color=MUTED)).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.6)
        stuck = tag_box("BẾ TẮC", [
            "Các nút trùng nhau nhiều không tưởng.",
            "Làm sao giải mỗi trạng thái (i, c) đúng một lần?",
        ], accent=BAD, width=7.4, size=29)
        fit_stack(cnt, cmp, stuck, buff=0.7, max_scale=1.2)
        with self.voice("Đếm số phép tính: số tập con là 2 mũ n. Với n bằng 30 đã có khoảng một tỉ tập con, n bằng 100 có khoảng "
                        "mười mũ ba mươi."):
            self.play(FadeIn(cnt[0:3]), FadeIn(cnt[3][0]), run_time=0.8)
        with self.voice("Nhưng mỗi nút của cây chỉ được mô tả bởi hai số i và c. Vậy chỉ có tối đa n cộng 1 nhân W cộng 1 trạng thái "
                        "khác nhau: với n bằng 100, W bằng mười nghìn là khoảng một triệu."):
            self.play(FadeIn(cnt[3][1:]), run_time=0.8)
        with self.voice("Mười mũ ba mươi nút trên cây, nhưng chỉ một triệu trạng thái khác nhau: các nút trùng nhau nhiều không tưởng."):
            self.play(FadeIn(cmp, scale=1.1), run_time=0.8)
        with self.voice("Làm sao để giải mỗi trạng thái i, c đúng một lần?"):
            self.play(FadeIn(stuck), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
KNAP_LABELS = ["0", "1 (6kg,30)", "2 (5kg,20)", "3 (5kg,22)", "4 (3kg,9)"]


class B4_03_BangF(B4Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Bảng f(i, c)")
        defi = panel(VGroup(TB("f(i, c) =", size=34, color=ACCENT),
                            T("giá trị lớn nhất khi chỉ chọn trong i kiện đầu", size=28),
                            T("và tổng khối lượng không vượt quá c", size=28)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        opts = VGroup(
            panel(VGroup(TB("Bỏ kiện i", size=30, color=BLUEC), T("sức chứa vẫn c", size=24),
                         M("f(i−1, c)", size=28, color=BLUEC)).arrange(DOWN, buff=0.1), width=3.65, stroke=BLUEC),
            panel(VGroup(TB("Lấy kiện i", size=30, color=GOOD), T("(khi c ≥ wᵢ)", size=24),
                         M("f(i−1, c−wᵢ) + vᵢ", size=26, color=GOOD)).arrange(DOWN, buff=0.1), width=3.65, stroke=GOOD),
        ).arrange(RIGHT, buff=0.2)
        formula = tag_box("CÔNG THỨC CÁI TÚI 0/1", [
            "f(i, c) = max( f(i−1, c), f(i−1, c−wᵢ) + vᵢ )",
            "• Cơ sở: f(0, c) = 0 với mọi c",
            "• Đáp án: f(n, W); điền i tăng dần",
        ], width=7.5, size=28)
        formula[3][0].set_color(ACCENT)
        cmp = VGroup(T("Giống bài hái nấm (“chọn hay bỏ”), nhưng ràng buộc là", size=26, color=MUTED),
                     T("TỔNG KHỐI LƯỢNG ⇒ thêm chiều c: “còn bao nhiêu chỗ”.", size=26, color=MUTED)).arrange(DOWN, buff=0.08)
        fit_stack(defi, opts, formula, cmp, buff=0.5, max_scale=1.3)
        with self.voice("Bước một: đặt f của i, c là tổng giá trị lớn nhất khi chỉ được chọn trong i kiện đầu, và tổng khối lượng "
                        "không vượt quá c. Nhìn vào kiện thứ i, và hỏi: kiện cuối được lấy hay bỏ?"):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Bỏ kiện i: chỉ còn i trừ 1 kiện đầu, sức chứa vẫn là c, giá trị f của i trừ 1, c."):
            self.play(FadeIn(opts[0], shift=UP * 0.2), run_time=0.7)
        with self.voice("Lấy kiện i, chỉ khi c lớn hơn hoặc bằng w i: kiện i chiếm w i ki lô gam, i trừ 1 kiện đầu chia nhau "
                        "phần còn lại c trừ w i. Giá trị f của i trừ 1, c trừ w i, cộng v i."):
            self.play(FadeIn(opts[1], shift=UP * 0.2), run_time=0.7)
        with self.voice("Công thức cái túi 0/1: f của i, c bằng max của hai khả năng đó. Cơ sở: f của 0, c bằng 0 với mọi c. "
                        "Đáp án là f của n, W. Điền i tăng dần, vì hàng i chỉ cần hàng i trừ 1."):
            self.play(FadeIn(formula), run_time=1.0)
        with self.voice("So với bài hái nấm ở Bài 2: cùng là chọn hay bỏ phần tử cuối, nhưng ràng buộc giờ là tổng khối lượng, "
                        "nên trạng thái cần thêm chiều thứ hai c để nhớ còn bao nhiêu chỗ."):
            self.play(FadeIn(cmp), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 2: Chạy tay — điền bảng f")
        tbl = Table2D(5, CAP + 1, w=0.6, h=0.62, row_labels=KNAP_LABELS)
        for c in range(CAP + 1):
            tbl.cells[(0, c)][1].become(tbl.value(0, c, 0, color=MUTED))
        eq_slot = placeholder(7.4, 1.2)
        why_slot = placeholder(7.4, 0.8)
        sc = fit_stack(tbl, eq_slot, why_slot, buff=0.5, max_scale=1.3)

        eq = [None]
        why = [None]

        def say_eq(text, color=INK, note=""):
            new = M(text, size=28, color=color).scale(sc)
            if new.width > 7.4:
                new.scale_to_fit_width(7.4)
            new.move_to(eq_slot)
            anims = []
            if eq[0] is None:
                eq[0] = new
                anims.append(FadeIn(new))
            else:
                anims.append(Transform(eq[0], new))
            nn = T(note, size=26, color=MUTED).scale(sc)
            if nn.width > 7.4:
                nn.scale_to_fit_width(7.4)
            nn.move_to(why_slot)
            if why[0] is None:
                why[0] = nn
                anims.append(FadeIn(nn))
            else:
                anims.append(Transform(why[0], nn))
            return anims

        with self.voice("Bước hai: chạy tay trên ví dụ. Hàng 0 là cơ sở: không có kiện nào thì giá trị bằng 0, với mọi sức chứa c "
                        "từ 0 đến 10."):
            self.play(FadeIn(tbl), run_time=1.0)

        def fill_row(i, rt=0.12):
            anims = []
            for c in range(CAP + 1):
                v = F[i][c]
                took = c >= W_ITEMS[i - 1] and F[i][c] != F[i - 1][c]
                anims.append(AnimationGroup(*tbl.fill(i, c, v, fill="#166534" if took else "#1E3A8A")))
            self.play(LaggedStart(*anims, lag_ratio=0.25), run_time=max(1.2, rt * 11))

        with self.voice("Hàng kiện 1, nặng 6, giá trị 30: với c nhỏ hơn 6 không lấy được, f bằng 0. Với c từ 6 trở lên lấy được, "
                        "f bằng 30. Ô xanh lá là ô có lấy kiện i, ô xanh dương là ô bỏ kiện i."):
            self.play(*say_eq("f(1, c) = 30 nếu c ≥ 6, ngược lại 0", ACCENT, "kiện 1: 6 kg, giá trị 30"), run_time=0.5)
            fill_row(1)
        with self.voice("Hàng kiện 2, nặng 5, giá trị 20: f của 2, 5 bằng max của f 1, 5 bằng 0, và f 1, 0 cộng 20. Bằng 20."):
            self.play(*say_eq("f(2,5) = max(f(1,5), f(1,0) + 20) = max(0, 20) = 20", ACCENT, "kiện 2: 5 kg, giá trị 20"),
                      run_time=0.5)
            fill_row(2)
        with self.voice("Với c từ 6 đến 10: lấy kiện 2 thì phần còn lại không quá 5 ki lô gam, không đủ cho kiện 1, nên chỉ được "
                        "20, nhỏ hơn 30. Giữ 30."):
            self.play(*[Indicate(tbl.cells[(2, c)], color=BLUEC, scale_factor=1.1) for c in range(6, 11)], run_time=1.0)
        with self.voice("Hàng kiện 3, nặng 5, giá trị 22."):
            self.play(*say_eq("kiện 3: 5 kg, giá trị 22", ACCENT, ""), run_time=0.4)
            fill_row(3)
        src_b = SurroundingRectangle(tbl.cells[(2, 10)], color=BLUEC, buff=0.02, stroke_width=6)
        src_g = SurroundingRectangle(tbl.cells[(2, 5)], color=GOOD, buff=0.02, stroke_width=6)
        dst = SurroundingRectangle(tbl.cells[(3, 10)], color=ACCENT, buff=0.02, stroke_width=6)
        with self.voice("Ô đáng chú ý nhất: f của 3, 10 bằng max của ô xanh dương f 2, 10 bằng 30, và ô xanh lá f 2, 5 cộng 22, "
                        "bằng 42. Đây là lúc hai kiện 5 ki lô gam gặp nhau!"):
            self.play(*say_eq("f(3,10) = max(f(2,10), f(2,5) + 22) = max(30, 42) = 42", GOOD, "hai kiện 5 kg “gặp nhau”"),
                      Create(src_b), Create(src_g), run_time=0.8)
            self.play(Create(dst), Indicate(tbl.cells[(3, 10)], color=ACCENT), run_time=1.0)
        self.play(FadeOut(VGroup(src_b, src_g, dst)), run_time=0.4)
        with self.voice("Hàng kiện 4, nặng 3, giá trị 9: f của 4, 9 bằng max của 30, và f 3, 6 cộng 9 bằng 39, là kiện 1 cùng kiện 4. "
                        "Còn f của 4, 10 bằng max của 42 và 39, vẫn là 42."):
            self.play(*say_eq("f(4,9) = max(30, 30 + 9) = 39;  f(4,10) = max(42, 39) = 42", ACCENT, "kiện 4: 3 kg, giá trị 9"),
                      run_time=0.5)
            fill_row(4)
            self.play(Circumscribe(tbl.cells[(4, 10)], color=ACCENT), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao đúng? Độ phức tạp?")
        why_box = tag_box("VÌ SAO ĐÚNG?", [
            "Xét cách chọn tốt nhất cho (i, c).",
            "• Không chứa kiện i: là cách chọn trong i−1 kiện",
            "  với sức chứa c ⇒ đúng bằng f(i−1, c).",
            "• Chứa kiện i: phần còn lại là cách chọn trong",
            "  i−1 kiện, sức chứa c−wᵢ, và phải TỐT NHẤT",
            "  ⇒ f(i−1, c−wᵢ) + vᵢ.  Lấy max hai trường hợp.",
        ], accent=GOOD, width=7.5, size=28)
        cx = VGroup(TB("O(n·W)", size=48, color=GOOD), T("n = 100, W = 10⁴: khoảng 10⁶ phép", size=28)).arrange(DOWN, buff=0.15)
        pseudo = tag_box("ĐỘ PHỨC TẠP “GIẢ ĐA THỨC”", [
            "W là GIÁ TRỊ của dữ liệu, không phải số lượng.",
            "W = 10⁹ ⇒ bảng 10¹¹ ô: không điền nổi!",
            "⇒ đổi vai khối lượng và giá trị (Bài 5).",
        ], accent=ORANGE, width=7.5, size=28)
        fit_stack(why_box, cx, pseudo, buff=0.6, max_scale=1.2)
        with self.voice("Vì sao đúng? Xét một cách chọn tốt nhất cho i, c. Nếu nó không chứa kiện i, nó là cách chọn hợp lệ trong "
                        "i trừ 1 kiện với sức chứa c, nên bằng f của i trừ 1, c. Nếu nó chứa kiện i, phần còn lại là cách chọn "
                        "trong i trừ 1 kiện với sức chứa c trừ w i, và phần này phải tốt nhất. Lấy max hai trường hợp ra đúng f."):
            self.play(FadeIn(why_box), run_time=1.0)
        with self.voice("Độ phức tạp: bảng có n cộng 1 nhân W cộng 1 ô, mỗi ô O của 1, nên O của n nhân W. Với n bằng 100, "
                        "W bằng mười nghìn, khoảng một triệu phép."):
            self.play(FadeIn(cx), run_time=0.8)
        with self.voice("Chú ý: O của n nhân W trông như đa thức, nhưng W là giá trị của dữ liệu chứ không phải số lượng. Nếu W bằng "
                        "một tỉ, bảng có một trăm tỉ ô, không thể điền nổi. Khi ấy phải đổi vai khối lượng và giá trị, ở Bài 5."):
            self.play(FadeIn(pseudo), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
TRACE_CODE = """
best[i] = best[i - 1];          // điền sẵn trường hợp "bỏ kiện i"
...
int load = capacity;
for (int i = itemCount; i >= 1; i--) {
    if (best[i][load] != best[i - 1][load]) {
        chosen.push_back(i);
        load -= weight[i];
    }
}
reverse(chosen.begin(), chosen.end());
"""


class B4_04_TruyVet(B4Scene):
    def construct(self):
        self.show_header("4. Truy vết: Đã chọn những kiện nào?")
        rule = VGroup(T("Đi ngược từ ô (n, W). Tại ô (i, c):", size=28),
                      rich("• f(i,c) = f(i−1,c): <span foreground='#60A5FA'>BỎ kiện i</span>, lên hàng trên giữ c", size=26),
                      rich("• khác: <span foreground='#4ADE80'>LẤY kiện i</span>, nhảy tới (i−1, c−wᵢ)", size=26)).arrange(
            DOWN, aligned_edge=LEFT, buff=0.12)
        tbl = Table2D(5, CAP + 1, w=0.6, h=0.62, row_labels=KNAP_LABELS)
        for i in range(5):
            for c in range(CAP + 1):
                tbl.cells[(i, c)][1].become(tbl.value(i, c, F[i][c]))
        rec_slot = placeholder(7.4, 1.0)
        sc = fit_stack(rule, tbl, rec_slot, buff=0.55, max_scale=1.3)
        with self.voice("Bảng f cho biết giá trị tốt nhất. Muốn biết đã chọn những kiện nào, ta truy vết: đi ngược từ ô n, W."):
            self.play(FadeIn(tbl), run_time=0.8)
        with self.voice("Tại ô i, c: nếu f của i, c bằng f của i trừ 1, c, thì có một cách tốt nhất bỏ kiện i, ta lên hàng trên "
                        "giữ nguyên c. Ngược lại, kiện i chắc chắn được lấy: ghi nhận kiện i, và nhảy tới ô i trừ 1, c trừ w i."):
            self.play(FadeIn(rule), run_time=1.0)
        chosen = []
        rec = None
        lines = [
            "Tại ô 4, 10: f bằng 42, ô trên cũng bằng 42. Bỏ kiện 4, đi lên.",
            "Tại ô 3, 10: f bằng 42, ô trên chỉ bằng 30. Khác nhau: lấy kiện 3! Nhảy tới ô 2, 10 trừ 5, tức ô 2, 5.",
            "Tại ô 2, 5: f bằng 20, ô trên bằng 0. Lấy kiện 2! Nhảy tới ô 1, 0.",
            "Tại ô 1, 0: f bằng 0, ô trên cũng bằng 0. Bỏ kiện 1.",
        ]
        cur = SurroundingRectangle(tbl.cells[(4, 10)], color=ACCENT, buff=0.02, stroke_width=7)
        self.play(Create(cur), run_time=0.4)
        for (i, c, pi, pc, take), sp in zip(TRACE, lines):
            if take:
                chosen.append(i)
            with self.voice(sp):
                col = GOOD if take else BLUEC
                arr = Arrow(tbl.cells[(i, c)].get_center(), tbl.cells[(pi, pc)].get_center(), buff=0.18, color=col,
                            stroke_width=7, max_tip_length_to_length_ratio=0.25)
                txt = VGroup(T("Kiện được chọn:", size=30, color=MUTED),
                             TB(", ".join(str(k) for k in sorted(chosen)) if chosen else "—", size=36, color=GOOD))
                txt.arrange(RIGHT, buff=0.3).scale(sc).move_to(rec_slot)
                anims = [GrowArrow(arr), tbl.cells[(i, c)][0].animate.set_fill("#166534" if take else "#1E3A8A", 1)]
                if rec is None:
                    rec = txt
                    anims.append(FadeIn(rec))
                else:
                    anims.append(Transform(rec, txt))
                self.play(*anims, run_time=0.8)
                self.play(cur.animate.move_to(tbl.cells[(pi, pc)]), run_time=0.4)
        with self.voice("Kết quả: chọn kiện 2 và kiện 3, tổng giá trị 42. Vì đi ngược, nhớ đảo lại để in theo thứ tự tăng dần."):
            self.play(Indicate(rec, color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("Code truy vết")
        code = code_block(TRACE_CODE, size=20)
        note = VGroup(T("best[i] = best[i−1] sao chép cả hàng trên:", size=28),
                      T("điền sẵn trường hợp “bỏ kiện i” cho mọi c;", size=28),
                      T("vòng sau chỉ xét “lấy kiện i” với load ≥ wᵢ.", size=28)).arrange(DOWN, buff=0.1)
        fit_stack(code, note, buff=0.8)
        with self.voice("Trong chương trình hoàn chỉnh, chú ý câu lệnh best i bằng best i trừ 1: nó sao chép cả hàng trên xuống, "
                        "tức là điền sẵn trường hợp bỏ kiện i cho mọi c. Vòng lặp sau đó chỉ cần xét trường hợp lấy kiện i."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 0, ACCENT)
            self.play(FadeIn(hl), FadeIn(note), run_time=0.8)
        with self.voice("Phần truy vết đi từ kiện cuối về kiện đầu: nếu ô khác ô phía trên thì ghi nhận kiện i và trừ sức chứa."):
            self.play(Transform(hl, line_box(code, 4, GOOD)), run_time=0.6)
            self.play(Transform(hl, line_box(code, 6, GOOD)), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
ONE_ROW_CODE = """
vector<long long> best(capacity + 1, 0);
for (int i = 1; i <= itemCount; i++)
    for (int load = capacity; load >= weight[i]; load--)
        best[load] = max(best[load],
                         best[load - weight[i]] + value[i]);
"""


class B4_05_MotMang(B4Scene):
    def construct(self):
        self.show_header("5. Một mảng và chiều duyệt GIẢM dần")
        idea = VGroup(T("Hàng i chỉ cần hàng i−1 ⇒ dùng MỘT mảng g[c]:", size=28),
                      T("trước khi xét kiện i: g[c] = f(i−1, c)", size=28, color=MUTED),
                      T("cần g[c] cũ và g[c − wᵢ] CŨ (ô bên trái)", size=28, color=ACCENT)).arrange(DOWN, buff=0.1)
        row = array_row(F[1], w=0.62, h=0.75, size=28, label="g")
        cap_l = T("Xét kiện 2 (5 kg, 20): duyệt c = 10 → 5", size=28, color=GOOD)
        eq_slot = placeholder(7.2, 0.9)
        sc = fit_stack(idea, cap_l, row, eq_slot, buff=0.55, max_scale=1.25)
        with self.voice("Hàng i chỉ cần hàng i trừ 1. Hãy thử dùng một mảng một chiều g thay cho cả bảng. Trước khi xét kiện i, "
                        "g c đang là f của i trừ 1, c. Sau khi xét xong, g c phải là f của i, c."):
            self.play(FadeIn(idea[:2]), run_time=0.8)
            self.play(FadeIn(row), run_time=0.6)
        with self.voice("Công thức cần g c cũ, và g c trừ w i cũ, tức là ô bên trái chưa bị cập nhật."):
            self.play(FadeIn(idea[2]), run_time=0.6)
        eq = None
        new_row = F[2]
        with self.voice("Nếu duyệt c giảm dần từ W xuống w i, thì khi tính g c, ô g c trừ w i nằm bên trái và chưa được đụng tới: "
                        "nó vẫn là giá trị cũ. Đúng như ta cần!"):
            self.play(FadeIn(cap_l), run_time=0.5)
            for c in range(10, 4, -1):
                src = SurroundingRectangle(row.cells[c - 5], color=BLUEC, buff=0.02, stroke_width=5)
                dst = SurroundingRectangle(row.cells[c], color=ACCENT, buff=0.02, stroke_width=5)
                cand = F[1][c - 5] + 20
                f = M(f"g[{c}] = max({F[1][c]}, g[{c - 5}] + 20 = {cand}) = {new_row[c]}", size=28,
                      color=GOOD if new_row[c] != F[1][c] else INK).scale(sc).move_to(eq_slot)
                anims = [Create(src), Create(dst)]
                if eq is None:
                    eq = f
                    anims.append(FadeIn(eq))
                else:
                    anims.append(Transform(eq, f))
                self.play(*anims, run_time=0.35)
                self.play(Transform(row.cells[c][1], set_cell_value(row.cells[c], new_row[c])),
                          row.cells[c][0].animate.set_fill("#166534" if new_row[c] != F[1][c] else PANEL_2, 1),
                          run_time=0.3)
                self.play(FadeOut(src), FadeOut(dst), run_time=0.15)
        with self.voice("Ô 10 đọc ô 5 khi ô 5 còn mang giá trị cũ bằng 0, nên không lấy kiện 2 hai lần. Kết quả chính là hàng 2 của bảng."):
            self.play(Indicate(row.cells[5], color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("Lỗi kinh điển: duyệt TĂNG dần")
        setup = T("Một kiện 3 kg, giá trị 9; W = 10", size=30, color=ACCENT)
        down = [0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9]
        up = [0, 0, 0, 9, 9, 9, 18, 18, 18, 27, 27]
        r_down = array_row([0] * 11, w=0.62, h=0.75, size=28, label="giảm")
        r_up = array_row([0] * 11, w=0.62, h=0.75, size=28, label="tăng", show_index=False)
        for k, c in enumerate(r_up.cells):
            c.move_to(r_down.cells[k].get_center() + DOWN * 1.2)
        r_up.lab.next_to(r_up.cells, LEFT, buff=0.25)
        verdict = VGroup(T("Tăng dần: g[c − 3] ĐÃ chứa kiện này ⇒", size=28),
                         TB("lấy một kiện NHIỀU LẦN (27 = 9 × 3)!", size=30, color=BAD)).arrange(DOWN, buff=0.1)
        code = code_block(ONE_ROW_CODE, size=20)
        mem = VGroup(T("Bộ nhớ:", size=30), TB("O(n·W)", size=36, color=BAD), T("→", size=30),
                     TB("O(W)", size=36, color=GOOD), T("(mất truy vết)", size=26, color=MUTED)).arrange(RIGHT, buff=0.2)
        fit_stack(setup, VGroup(r_down, r_up), verdict, code, mem, buff=0.5, max_scale=1.2)
        with self.voice("Nếu lỡ duyệt c tăng dần thì sao? Thử với một kiện 3 ki lô gam, giá trị 9, sức chứa 10."):
            self.play(FadeIn(setup), FadeIn(r_down), FadeIn(r_up), run_time=0.8)
        with self.voice("Duyệt giảm dần: mọi ô từ 3 trở đi bằng 9. Đúng, vì chỉ có một kiện."):
            self.play(LaggedStart(*[AnimationGroup(r_down.cells[c][0].animate.set_fill("#166534" if down[c] else PANEL_2, 1),
                                                   Transform(r_down.cells[c][1], set_cell_value(r_down.cells[c], down[c])))
                                    for c in range(10, -1, -1)], lag_ratio=0.2), run_time=1.5)
        with self.voice("Duyệt tăng dần: ô 3 bằng 9, rồi ô 6 đọc ô 3 đã được cập nhật, thành 18. Ô 9 đọc ô 6, thành 27. "
                        "Ô g c trừ w i đã chứa kiện i, cộng thêm lần nữa nghĩa là lấy kiện i hai, ba lần!"):
            for c in range(11):
                col = BAD if up[c] > 9 else ("#166534" if up[c] else PANEL_2)
                self.play(Transform(r_up.cells[c][1], set_cell_value(r_up.cells[c], up[c])),
                          r_up.cells[c][0].animate.set_fill(col, 1), run_time=0.18)
            self.play(FadeIn(verdict), run_time=0.6)
        with self.voice("Vậy cái túi 0/1 với một mảng phải duyệt sức chứa giảm dần. Bộ nhớ giảm từ O của n nhân W xuống O của W. "
                        "Cái giá phải trả, như ở Bài 3, là không truy vết trực tiếp được nữa."):
            self.play(FadeIn(code), run_time=0.8)
            self.play(FadeIn(line_box(code, 2, GOOD)), FadeIn(mem), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
STAMP_CODE = """
vector<long long> ways(target + 1, 0);
ways[0] = 1;
for (int type = 0; type < typeCount; type++) {
    int stamp; cin >> stamp;
    for (int sum = stamp; sum <= target; sum++)
        ways[sum] = (ways[sum] + ways[sum - stamp]) % MOD;
}
"""


def stamp(v, size=0.62):
    col = {1: "#0EA5E9", 2: "#F59E0B", 5: "#EC4899"}[v]
    sq = Square(size, fill_color=col, fill_opacity=1, stroke_color=INK, stroke_width=2)
    inner = Square(size * 0.78, stroke_color=INK, stroke_width=1, stroke_opacity=0.6).move_to(sq)
    return VGroup(sq, inner, TB(str(v), size=size * 42, color=BG).move_to(sq))


class B4_06_KhongGioiHan(B4Scene):
    def construct(self):
        self.show_header("6. Cái túi KHÔNG GIỚI HẠN")
        intro = VGroup(T("Mỗi loại kiện có VÔ SỐ chiếc ⇒", size=30),
                       T("lấy kiện i nhiều lần là ĐƯỢC PHÉP!", size=30, color=GOOD)).arrange(DOWN, buff=0.1)
        formula = tag_box("CÔNG THỨC KHÔNG GIỚI HẠN", [
            "f(i, c) = max( f(i−1, c), f(i, c−wᵢ) + vᵢ )",
            "f(i, …): sau khi lấy một chiếc loại i,",
            "vẫn được lấy tiếp loại i.",
        ], accent=GOOD, width=7.5, size=28)
        formula[3][0].set_color(GOOD)
        heads = ["", "Cái túi 0/1", "Không giới hạn"]
        data = [["Mỗi loại dùng", "tối đa 1 lần", "bao nhiêu cũng được"],
                ["Vế “lấy”", "f(i−1, c−wᵢ)+vᵢ", "f(i, c−wᵢ)+vᵢ"],
                ["Một mảng", "c GIẢM dần", "c TĂNG dần"]]
        colw = [2.0, 2.75, 2.75]
        table = VGroup()
        for r, rowd in enumerate([heads] + data):
            cells_ = VGroup()
            x = -sum(colw) / 2
            for ci, (txt, w) in enumerate(zip(rowd, colw)):
                fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
                rect = Rectangle(width=w, height=0.85, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
                rect.move_to([x + w / 2, 0, 0])
                col = BG if r == 0 else (ACCENT if ci == 0 else (BAD if (r == 3 and ci == 1) else (GOOD if r == 3 else INK)))
                t = (TB if r == 0 or ci == 0 or r == 3 else T)(txt, size=24, color=col, max_width=w - 0.15)
                cells_.add(VGroup(rect, t.move_to(rect)))
                x += w
            table.add(cells_)
        table.arrange(DOWN, buff=0)
        fit_stack(intro, formula, table, buff=0.6, max_scale=1.2)
        with self.voice("Điều gì xảy ra nếu mỗi loại kiện có vô số chiếc? Khi ấy lấy kiện i nhiều lần là được phép, và vòng lặp "
                        "tăng dần vừa rồi lại chính là lời giải đúng! Lỗi trở thành tính năng."):
            self.play(FadeIn(intro), run_time=0.8)
        with self.voice("Công thức cái túi không giới hạn: vế lấy dùng f của i, c trừ w i, tức là hàng hiện tại: sau khi lấy một "
                        "chiếc loại i, vẫn được lấy tiếp loại i. Trên mảng một chiều, điều đó tương ứng với duyệt c tăng dần."):
            self.play(FadeIn(formula), run_time=0.8)
        with self.voice("So sánh: cái túi 0/1, mỗi loại dùng tối đa một lần, vế lấy dùng hàng trên, một mảng thì c giảm dần. "
                        "Cái túi không giới hạn, dùng bao nhiêu cũng được, vế lấy dùng hàng hiện tại, một mảng thì c tăng dần."):
            for r in table:
                self.play(FadeIn(r, shift=UP * 0.15), run_time=0.45)

        self.clear_body()
        self.show_header("7. Bài toán DOITEM: Đếm tổ hợp")
        box = tag_box("BÀI TOÁN: DOITEM", [
            "k loại tem mệnh giá c₁, …, cₖ (vô số mỗi loại).",
            "Có bao nhiêu cách dán để tổng ĐÚNG BẰNG S?",
            "Không kể thứ tự dán. Lấy dư 10⁹ + 7.",
        ], accent=BLUEC, width=7.4, size=29)
        combos = [[5], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        crow = VGroup()
        for cb in combos:
            crow.add(VGroup(*[stamp(v, 0.55) for v in cb]).arrange(RIGHT, buff=0.08))
        crow.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        lab = TB("Tem 1, 2, 5; S = 5: 4 tổ hợp", size=32, color=ACCENT)
        seq = T("…nhưng 9 dãy CÓ THỨ TỰ (2+2+1, 2+1+2, 1+2+2, …)", size=26, color=MUTED)
        fit_stack(box, lab, crow, seq, buff=0.5, max_scale=1.2)
        with self.voice("Bài toán DOITEM: bưu điện có k loại tem, mỗi loại vô số tem. Có bao nhiêu cách dán tem để tổng mệnh giá "
                        "đúng bằng S? Hai cách giống nhau nếu số tem mỗi loại như nhau, không kể thứ tự dán."):
            self.play(FadeIn(box), run_time=0.8)
        with self.voice("Ví dụ tem 1, 2, 5 và S bằng 5: có 4 cách. 5; 2 cộng 2 cộng 1; 2 cộng 1 cộng 1 cộng 1; và năm tem 1."):
            self.play(FadeIn(lab), run_time=0.5)
            for r in crow:
                self.play(LaggedStart(*[FadeIn(s, scale=0.6) for s in r], lag_ratio=0.2), run_time=0.6)
        with self.voice("Nhưng nếu kể thứ tự dán thì có tới 9 dãy khác nhau. Hai câu hỏi khác nhau, hai đáp số khác nhau."):
            self.play(FadeIn(seq), run_time=0.6)

        self.clear_body()
        self.show_header("Công thức đếm tổ hợp")
        formula = tag_box("CÔNG THỨC ĐẾM TỔ HỢP", [
            "ways(i, s) = ways(i−1, s) + ways(i, s−cᵢ)",
            "không dùng tem i   +   dùng ít nhất một tem i",
            "Một mảng: vòng ngoài LOẠI TEM, vòng trong s TĂNG",
        ], accent=BLUEC, width=7.5, size=28)
        formula[3][0].set_color(ACCENT)
        rows = VGroup()
        start = array_row([1, 0, 0, 0, 0, 0], w=0.85, h=0.75, size=30, label="đầu")
        rows.add(start)
        for k, c in enumerate(COINS):
            r = array_row(WAYS_ROWS[k], w=0.85, h=0.75, size=30, label=f"+tem {c}", show_index=False)
            rows.add(r)
        rows.arrange(DOWN, buff=0.18, aligned_edge=RIGHT)
        res = TB("ways(5) = 4", size=40, color=GOOD)
        fit_stack(formula, rows, res, buff=0.5, max_scale=1.2)
        with self.voice("Đây là cái túi không giới hạn phiên bản đếm. Đặt ways của i, s là số cách tạo tổng s chỉ dùng i loại tem "
                        "đầu. Xét loại tem i: hoặc không dùng tem loại i nào, hoặc dùng ít nhất một tem loại i. Bỏ đi một tem đó, "
                        "ta được một cách tạo tổng s trừ c i, vẫn từ i loại tem đầu."):
            self.play(FadeIn(formula), run_time=1.0)
        with self.voice("Ban đầu chỉ có ways của 0 bằng 1: tổng 0 có đúng một cách, không dán tem nào."):
            self.play(FadeIn(rows[0]), run_time=0.6)
        sp = {1: "Thêm tem 1: mọi tổng đều có đúng 1 cách.",
              2: "Thêm tem 2: mỗi ô cộng thêm ô cách nó 2 bước bên trái. Được 1, 1, 2, 2, 3, 3.",
              5: "Thêm tem 5: chỉ ô 5 thay đổi, cộng thêm ô 0. ways của 5 bằng 4."}
        for k, c in enumerate(COINS):
            with self.voice(sp[c]):
                self.play(FadeIn(rows[k + 1].lab), *[FadeIn(cc[0]) for cc in rows[k + 1].cells], run_time=0.4)
                prev = WAYS_ROWS[k - 1] if k else [1, 0, 0, 0, 0, 0]
                for s in range(6):
                    cc = rows[k + 1].cells[s]
                    changed = WAYS_ROWS[k][s] != prev[s]
                    self.play(FadeIn(cc[1]), cc[0].animate.set_fill("#166534" if changed else PANEL_2, 1), run_time=0.16)
        with self.voice("Đáp số 4, đúng như liệt kê."):
            self.play(FadeIn(res), Circumscribe(rows[3].cells[5], color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("Đổi thứ tự hai vòng lặp thì sao?")
        code = code_block(STAMP_CODE, size=20)
        ordered = array_row(ORDERED, w=0.85, h=0.75, size=30, label="dãy")
        rule = tag_box("QUY TẮC NHỚ THỨ TỰ VÒNG LẶP", [
            "• Ngoài ĐỒ VẬT, trong TỔNG: mỗi đồ vật",
            "  “quyết định xong” rồi mới sang đồ khác",
            "  ⇒ đếm TỔ HỢP (không kể thứ tự).",
            "• Ngoài TỔNG, trong ĐỒ VẬT: ở mỗi tổng chọn",
            "  bất kì đồ vật làm phần tử CUỐI",
            "  ⇒ đếm DÃY CÓ THỨ TỰ (chỉnh hợp lặp).",
        ], accent=ACCENT, width=7.5, size=27)
        fit_stack(code, ordered, rule, buff=0.55)
        with self.voice("Đây là code đếm tổ hợp: vòng ngoài duyệt loại tem, vòng trong duyệt tổng tăng dần."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 2, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
        with self.voice("Nếu đổi lại, vòng ngoài là tổng, vòng trong là các loại tem, thì ways s bằng tổng ways s trừ c, nghĩa là tem "
                        "cuối cùng được dán là tem c. Đây đúng là công thức bài nhảy đá ở Bài 1: nó đếm các dãy có thứ tự, "
                        "cho kết quả 9."):
            self.play(FadeIn(ordered), run_time=0.8)
            self.play(Circumscribe(ordered.cells[5], color=ORANGE), run_time=0.8)
        with self.voice("Quy tắc nhớ: vòng ngoài là đồ vật, vòng trong là tổng: đếm tổ hợp. Vòng ngoài là tổng, vòng trong là đồ "
                        "vật: đếm dãy có thứ tự, tức chỉnh hợp lặp."):
            self.play(FadeIn(rule), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B4_07_TongKet(B4Scene):
    def construct(self):
        self.show_header("8. Mở rộng")
        ext = [
            ("Bắt buộc chứa ĐÚNG W kg", "f(0, 0) = 0, f(0, c > 0) = −∞; kiểm tra ô nguồn ≠ −∞",
             "Mở rộng một: nếu đề yêu cầu tổng khối lượng đúng bằng W, khởi tạo f của 0, 0 bằng 0 và f của 0, c bằng âm vô "
             "cùng với c lớn hơn 0. Nhớ kiểm tra ô nguồn khác âm vô cùng trước khi cộng."),
            ("Tổng con (subset sum)", "reach[s] |= reach[s − aᵢ], s giảm; bitset (Bài 5)",
             "Mở rộng hai: hỏi có chọn được tập con tổng đúng bằng S không, là cái túi 0/1 với giá trị đúng sai, "
             "có thể tăng tốc bằng bitset ở Bài 5."),
            ("Hai giới hạn", "Khối lượng ≤ W và thể tích ≤ V: f(i, w, v), O(n·W·V)",
             "Mở rộng ba: hai giới hạn khối lượng và thể tích thì thêm một chiều vào trạng thái."),
            ("Đồ vật chia nhóm", "Mỗi nhóm ≤ 1 món: ngoài nhóm, giữa c giảm, trong các món",
             "Mở rộng bốn: đồ vật chia nhóm, mỗi nhóm chọn tối đa một món. Vòng ngoài duyệt nhóm, vòng giữa duyệt c giảm dần, "
             "vòng trong duyệt các món trong nhóm."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Duyệt sai chiều", "0/1 phải GIẢM dần, không giới hạn phải TĂNG dần",
             "Bẫy một: duyệt sai chiều trên mảng một chiều."),
            ("Tham lam theo tỉ số", "Chỉ đúng khi được chia nhỏ đồ vật",
             "Bẫy hai: tham lam theo tỉ số giá trị trên khối lượng, chỉ đúng khi được chia nhỏ đồ vật."),
            ("“Không vượt quá” vs “đúng bằng”", "Khác nhau ở phần khởi tạo",
             "Bẫy ba: nhầm không vượt quá với đúng bằng. Hai yêu cầu khác nhau ở phần khởi tạo."),
            ("Tràn bộ nhớ", "Bảng 100 × 10⁶ long long = 800 MB: dùng một mảng",
             "Bẫy bốn: tràn bộ nhớ. Bảng một trăm nhân một triệu kiểu long long cần tám trăm megabyte. "
             "Hãy dùng mảng một chiều khi không cần truy vết."),
            ("Đổi nhầm thứ tự vòng lặp", "Ra chỉnh hợp thay vì tổ hợp (hoặc ngược lại)",
             "Bẫy năm: đổi nhầm thứ tự vòng lặp trong bài đếm."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 4", [
            "• 0/1: f(i,c) = max(f(i−1,c), f(i−1,c−wᵢ)+vᵢ);",
            "   một mảng thì c GIẢM dần.",
            "• Không giới hạn: dùng f(i, c−wᵢ);",
            "   một mảng thì c TĂNG dần.",
            "• Đếm: ngoài đồ vật = TỔ HỢP,",
            "   ngoài tổng = CHỈNH HỢP.",
            "• O(n·W) phụ thuộc GIÁ TRỊ W: kiểm tra W nhỏ.",
        ], accent=GOOD, width=7.5, size=29)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: cái túi 0/1, f của i, c bằng max của f i trừ 1, c và f i trừ 1, c trừ w i cộng v i; một mảng "
                        "thì c giảm dần. Cái túi không giới hạn dùng f của i, c trừ w i; một mảng thì c tăng dần."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Bài đếm: vòng ngoài đồ vật là tổ hợp, vòng ngoài tổng là chỉnh hợp. Và độ phức tạp O của n nhân W phụ thuộc "
                        "vào giá trị W: luôn kiểm tra W có đủ nhỏ không."):
            self.play(FadeIn(mem[3][4:]), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Ví dụ BALOCUUTRO, nếu xe", "chở được 11 kg thì đáp án?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        crates = VGroup(*[make_crate(k, W_ITEMS[k], V_ITEMS[k], size=1.4) for k in range(4)]).arrange(RIGHT, buff=0.3)
        ans = VGroup(TB("52", size=56, color=GOOD), T("kiện 1 + kiện 3: 6 + 5 = 11 kg, 30 + 22", size=28)).arrange(DOWN, buff=0.15)
        nxt = VGroup(TB("Tiếp theo: BÀI 5", size=42, color=ACCENT), T("Cái túi mở rộng", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, crates, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: với ví dụ xe cứu trợ, nếu xe chở được 11 ki lô gam thì đáp án là bao nhiêu? "
                        "Dừng video và thử nhé!"):
            self.play(FadeIn(q), FadeIn(crates), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp án 52: chọn kiện 1 và kiện 3, nặng đúng 11 ki lô gam."):
            self.play(Indicate(crates[0], color=GOOD), Indicate(crates[2], color=GOOD), run_time=0.8)
            self.play(crates[1].animate.set_opacity(0.25), crates[3].animate.set_opacity(0.25), FadeIn(ans), run_time=0.6)
        with self.voice("Bài tiếp theo: cái túi mở rộng, với số lượng giới hạn và sức chứa khổng lồ. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
