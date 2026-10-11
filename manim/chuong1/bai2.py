"""BÀI 2 — Quy hoạch động trên dãy (LOINHUAN — Kadane, HAINAM — chọn hay bỏ)."""

from common import *  # noqa: F401,F403
from bai1 import list_cards, line_box

PROFIT = [-2, 3, -1, 4, -7, 2, 5, -3]
MUSH = [3, 4, 3, 1, 5, 9, 5]


def kadane(a):
    best, kinds = [], []
    for i, x in enumerate(a):
        if i == 0:
            best.append(x)
            kinds.append("B")
        else:
            ext = best[-1] + x
            if ext >= x:
                best.append(ext)
                kinds.append("A")
            else:
                best.append(x)
                kinds.append("B")
    return best, kinds


def pick_skip(a):
    dp = []
    for i, x in enumerate(a):
        if i == 0:
            dp.append(x)
        elif i == 1:
            dp.append(max(dp[0], x))
        else:
            dp.append(max(dp[i - 1], dp[i - 2] + x))
    return dp


BEST, KINDS = kadane(PROFIT)
DP = pick_skip(MUSH)
assert BEST == [-2, 3, 2, 6, -1, 2, 7, 4] and max(BEST) == 7
assert DP == [3, 4, 6, 6, 11, 15, 16]


class B2Scene(NarratedScene):
    lesson_tag = "BÀI 2"
    lesson_title = "Quy hoạch động trên dãy"


def bar_chart(values, unit=0.32, width=0.7, gap=0.22, labels=True):
    """Biểu đồ cột lãi/lỗ, trục ngang tại y = 0 của nhóm."""
    bars = VGroup()
    n = len(values)
    total_w = n * width + (n - 1) * gap
    for i, v in enumerate(values):
        h = max(abs(v) * unit, 0.04)
        col = GOOD if v >= 0 else BAD
        r = Rectangle(width=width, height=h, fill_color=col, fill_opacity=0.9, stroke_width=0)
        x = -total_w / 2 + width / 2 + i * (width + gap)
        r.move_to([x, h / 2 if v >= 0 else -h / 2, 0])
        val = TB(str(v), size=26, color=INK)
        val.next_to(r, UP if v >= 0 else DOWN, buff=0.08)
        day = T(f"N{i + 1}", size=22, color=MUTED)
        day.move_to([x, -0.3 if v >= 0 else 0.3, 0])
        bars.add(VGroup(r, val, day))
    axis = Line([-total_w / 2 - 0.2, 0, 0], [total_w / 2 + 0.2, 0, 0], color=MUTED, stroke_width=2)
    g = VGroup(axis, bars)
    g.bars = bars
    return g


def make_mushroom(weight, scale=1.0):
    stem = RoundedRectangle(width=0.28, height=0.42, corner_radius=0.08, fill_color="#F5E6C8", fill_opacity=1,
                            stroke_color="#C9B48A", stroke_width=2)
    cap = Sector(radius=0.45, angle=PI, start_angle=0, fill_color="#DC2626", fill_opacity=1,
                 stroke_color="#7F1D1D", stroke_width=2)
    cap.next_to(stem, UP, buff=-0.05)
    dots = VGroup(*[Dot(radius=0.05, color=WHITE).move_to(cap.get_center() + [dx, dy, 0])
                    for dx, dy in [(-0.18, -0.02), (0.05, 0.1), (0.2, -0.04)]])
    lab = TB(str(weight), size=28, color=INK).next_to(stem, DOWN, buff=0.1)
    g = VGroup(stem, cap, dots, lab).scale(scale)
    g.lab = lab
    return g


def mushroom_row(weights, spacing=1.05):
    row = VGroup(*[make_mushroom(w) for w in weights]).arrange(RIGHT, buff=spacing - 0.9)
    idx = VGroup(*[T(f"cây {i + 1}", size=20, color=MUTED).next_to(m, DOWN, buff=0.08) for i, m in enumerate(row)])
    return VGroup(row, idx), row


# ----------------------------------------------------------------------------
class B2_00_Intro(B2Scene):
    def construct(self):
        tag = TB("BÀI 2", size=80, color=ACCENT)
        ttl = TB("Quy hoạch động trên dãy", size=48)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Hai kiểu trạng thái:",
            "    “kết thúc tại i” và “xét i phần tử đầu”",
            "✓ Đoạn con tổng lớn nhất: Kadane O(n)",
            "✓ Không chọn hai phần tử kề: “chọn hay bỏ”",
            "✓ Thêm một chiều vào trạng thái",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 2: Quy hoạch động trên dãy."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), run_time=1.5)
            self.play(GrowFromCenter(line), run_time=0.5)
        with self.voice("Học xong bài này, em sẽ biết hai kiểu trạng thái quan trọng nhất trên dãy: "
                        "kết thúc tại i, và xét i phần tử đầu."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ giải bài đoạn con có tổng lớn nhất trong O của n bằng thuật toán Kadane, "
                        "giải bài chọn các phần tử không kề nhau bằng lập luận chọn hay bỏ, "
                        "và biết cách thêm một chiều vào trạng thái khi trạng thái thiếu thông tin."):
            for g in goals[2:]:
                self.play(FadeIn(g, shift=RIGHT * 0.3), run_time=0.7)
        self.clear_body()


# ----------------------------------------------------------------------------
class B2_01_KhoiDong(B2Scene):
    def construct(self):
        self.show_header("Khởi động: Thời kì kinh doanh tốt nhất")
        intro = VGroup(T("Lãi (+) / lỗ (−) của 8 ngày:", size=32),
                       M("−2, 3, −1, 4, −7, 2, 5, −3", size=32, color=ACCENT)).arrange(DOWN, buff=0.15)
        chart = bar_chart(PROFIT)
        q = VGroup(T("Chọn một chuỗi ngày LIÊN TIẾP", size=32),
                   T("có tổng lãi lớn nhất?", size=32)).arrange(DOWN, buff=0.12)
        verdict = placeholder(7, 1.2)
        fit_stack(intro, chart, q, verdict, buff=0.6, max_scale=1.2)
        with self.voice("Một cửa hàng ghi lại lãi, là số dương, hoặc lỗ, là số âm, của từng ngày trong tám ngày: "
                        "trừ 2, 3, trừ 1, 4, trừ 7, 2, 5, trừ 3."):
            self.play(FadeIn(intro), run_time=0.8)
            self.play(Create(chart[0]), LaggedStart(*[GrowFromEdge(b[0], DOWN if PROFIT[i] >= 0 else UP)
                                                      for i, b in enumerate(chart.bars)], lag_ratio=0.15),
                      run_time=1.6)
            self.play(*[FadeIn(b[1]) for b in chart.bars], *[FadeIn(b[2]) for b in chart.bars], run_time=0.6)
        with self.voice("Chủ cửa hàng muốn chọn một chuỗi ngày liên tiếp để viết báo cáo thời kì kinh doanh tốt nhất, "
                        "tức là chuỗi có tổng lãi lớn nhất. Em chọn chuỗi nào?"):
            self.play(FadeIn(q), run_time=0.8)
        b1 = SurroundingRectangle(VGroup(*chart.bars[1:4]), color=ORANGE, buff=0.1, stroke_width=5)
        t1 = TB("Ngày 2 → 4: 3 − 1 + 4 = 6", size=32, color=ORANGE).move_to(verdict)
        with self.voice("Nhiều bạn sẽ khoanh từ ngày 2 đến ngày 4, tổng bằng 6, vì có hai số dương lớn."):
            self.play(Create(b1), FadeIn(t1), run_time=1.0)
        b2 = SurroundingRectangle(VGroup(*chart.bars[5:7]), color=GOOD, buff=0.1, stroke_width=6)
        t2 = TB("Ngày 6 → 7: 2 + 5 = 7 ✓", size=36, color=GOOD).move_to(verdict)
        with self.voice("Nhưng hãy nhìn kĩ cuối dãy! Ngày 6 và ngày 7 cho tổng 2 cộng 5, bằng 7, còn lớn hơn."):
            self.play(Create(b2), b1.animate.set_stroke(opacity=0.3), Transform(t1, t2), run_time=1.0)
            self.play(Indicate(t1, color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán LOINHUAN")
        box = tag_box("BÀI TOÁN: LOINHUAN", [
            "Cho dãy n số nguyên a₁, a₂, …, aₙ",
            "là lãi (lỗ) của n ngày.",
            "Tìm một đoạn ngày liên tiếp KHÁC RỖNG",
            "có tổng lớn nhất, in ra tổng đó.",
            "1 ≤ n ≤ 10⁶,  |aᵢ| ≤ 10⁹",
        ], width=7.4, size=30)
        box[3][4].set_color(ORANGE)
        ex1 = VGroup(M("−2 3 −1 4 −7 2 5 −3", size=28), TB("→ 7", size=34, color=ACCENT)).arrange(RIGHT, buff=0.4)
        ex2 = VGroup(M("−5 −1 −8", size=28), TB("→ −1", size=34, color=ACCENT)).arrange(RIGHT, buff=0.4)
        note = VGroup(T("Mọi số đều âm: đáp án là số âm lớn nhất,", size=28, color=BAD),
                      T("KHÔNG phải 0 (đoạn phải khác rỗng)!", size=28, color=BAD)).arrange(DOWN, buff=0.1)
        fit_stack(box, ex1, ex2, note, buff=0.5, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán LOINHUAN: cho dãy n số nguyên là lãi lỗ của n ngày. "
                        "Hãy tìm một đoạn ngày liên tiếp khác rỗng có tổng lớn nhất. n lên tới một triệu."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Ví dụ một là dãy vừa rồi, đáp án 7."):
            self.play(FadeIn(ex1), run_time=0.6)
        with self.voice("Ví dụ hai nhắc ta một chi tiết dễ quên: dãy trừ 5, trừ 1, trừ 8, đáp án là trừ 1. "
                        "Đoạn phải khác rỗng, nên khi mọi số đều âm, đáp án là số âm lớn nhất chứ không phải 0."):
            self.play(FadeIn(ex2), run_time=0.6)
            self.play(FadeIn(note), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B2_02_NgayTho(B2Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: Thử mọi đoạn")
        cells = array_row(PROFIT, w=0.85, h=0.85, size=30, index_from=1)
        lr_slot = placeholder(7, 0.6)
        sum_slot = placeholder(7, 0.8)
        code = code_block("""
long long answer = a[1];
for (int left = 1; left <= n; left++) {
    long long sum = 0;
    for (int right = left; right <= n; right++) {
        sum += a[right];
        answer = max(answer, sum);
    }
}""", size=22)
        sc = fit_stack(cells, lr_slot, sum_slot, code, buff=0.45, max_scale=1.2)
        with self.voice("Một đoạn được xác định bởi ngày bắt đầu l và ngày kết thúc r. "
                        "Cách đơn giản nhất là thử mọi cặp l và r."):
            self.play(FadeIn(cells), run_time=0.8)
        with self.voice("Khéo hơn một chút: khi cố định l và tăng dần r, tổng đoạn từ l đến r bằng tổng đoạn từ l đến r trừ 1, "
                        "cộng thêm a r. Nhờ vậy mỗi đoạn chỉ tốn một phép cộng."):
            box = SurroundingRectangle(cells.cells[0], color=ACCENT, buff=0.04, stroke_width=6)
            lab = TB("l = 1, r = 1", size=32, color=ACCENT).scale(sc).move_to(lr_slot)
            sm = TB("sum = −2", size=34, color=INK).move_to(sum_slot)
            self.play(Create(box), FadeIn(lab), FadeIn(sm), run_time=0.6)
            s_ = 0
            for left in (0, 1):
                s_ = 0
                for right in range(left, len(PROFIT) if left == 1 else 4):
                    s_ += PROFIT[right]
                    nb = SurroundingRectangle(VGroup(*cells.cells[left:right + 1]), color=ACCENT, buff=0.04,
                                              stroke_width=6)
                    self.play(Transform(box, nb),
                              Transform(lab, TB(f"l = {left + 1}, r = {right + 1}", size=32, color=ACCENT).scale(
                                  sc).move_to(lr_slot)),
                              Transform(sm, TB(f"sum = {s_}", size=34).move_to(sum_slot)), run_time=0.28)
        with self.voice("Đây là code thử mọi đoạn trong O của n bình phương."):
            self.play(FadeIn(code, shift=UP * 0.2), FadeOut(box), FadeOut(lab), FadeOut(sm), run_time=0.8)

        self.clear_body()
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "l = 1: vòng trong chạy n lần",
            "l = 2: n − 1 lần … l = n: 1 lần",
            "Tổng: n + (n−1) + … + 1 = n(n+1)/2",
            "⇒ độ phức tạp O(n²)",
        ], accent=ORANGE, width=7.4, size=30)
        # tam giác số đoạn
        tri = VGroup()
        n_ = 8
        for l in range(n_):
            for r in range(l, n_):
                sq = Square(0.42, fill_color=ORANGE, fill_opacity=0.75, stroke_color=BG, stroke_width=2)
                sq.move_to([r * 0.46, -l * 0.46, 0])
                tri.add(sq)
        tri_lab = T("mỗi ô = một đoạn [l, r]", size=24, color=MUTED).next_to(tri, DOWN, buff=0.2)
        times = VGroup(
            VGroup(T("n = 10⁴:", size=30), TB("5·10⁷ phép — kịp", size=30, color=GOOD)).arrange(RIGHT, buff=0.2),
            VGroup(T("n = 10⁶:", size=30), TB("5·10¹¹ phép — gần 1 giờ!", size=30, color=BAD)).arrange(RIGHT,
                                                                                                    buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fit_stack(cnt, VGroup(tri, tri_lab), times, buff=0.55, max_scale=1.15)
        with self.voice("Đếm số phép tính: với l bằng 1, vòng trong chạy n lần; với l bằng 2 chạy n trừ 1 lần; "
                        "cứ thế đến l bằng n chạy 1 lần."):
            self.play(FadeIn(cnt[0:3]), FadeIn(cnt[3][0:2]), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(s) for s in tri], lag_ratio=0.03), FadeIn(tri_lab), run_time=1.8)
        with self.voice("Tổng cộng n nhân n cộng 1 chia 2 lần, cỡ n bình phương chia 2. Độ phức tạp O của n bình phương."):
            self.play(FadeIn(cnt[3][2:]), run_time=0.8)
        with self.voice("Với n bằng mười nghìn, khoảng năm mươi triệu phép, chạy kịp. Nhưng với n bằng một triệu, "
                        "khoảng năm trăm tỉ phép, cần gần một giờ!"):
            self.play(FadeIn(times[0]), run_time=0.6)
            self.play(FadeIn(times[1]), run_time=0.6)

        self.clear_body()
        stuck = tag_box("BẾ TẮC", [
            "Có tới n(n+1)/2 đoạn khác nhau,",
            "và ta đang “chạm” vào từng đoạn một.",
            "",
            "Phải tìm đáp án MÀ KHÔNG CẦN",
            "xét riêng từng đoạn.",
            "Nhưng làm sao biết đoạn nào tốt",
            "nếu không thử?",
        ], accent=BAD, width=7.4, size=32)
        fit_stack(stuck, max_scale=1.2)
        with self.voice("Bế tắc! Có tới n nhân n cộng 1 chia 2 đoạn khác nhau, và cách làm trên chạm vào từng đoạn một. "
                        "Muốn nhanh hơn, ta phải tìm được đáp án mà không cần xét riêng từng đoạn. "
                        "Nhưng làm sao biết đoạn nào tốt nếu không thử?"):
            self.play(FadeIn(stuck, shift=UP * 0.3), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B2_03_KetThucTaiI(B2Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Trạng thái “kết thúc tại i”")
        s1 = VGroup(TB("Bước 1: Thử trạng thái quen thuộc", size=32, color=ACCENT),
                    T("F(i) = tổng lớn nhất của một đoạn", size=30),
                    T("nằm trong i ngày đầu", size=30)).arrange(DOWN, buff=0.15)
        cells = array_row(PROFIT[:6], w=0.95, h=0.85, size=30, index_from=1)
        far = SurroundingRectangle(VGroup(*cells.cells[1:4]), color=BLUEC, buff=0.05, stroke_width=6)
        far_l = T("đoạn tốt nhất trong 5 ngày đầu", size=24, color=BLUEC).next_to(far, DOWN, buff=0.15)
        q = T("Ngày 6 có nối được vào nó không?", size=28, color=ORANGE)
        conc = VGroup(TB("F THIẾU THÔNG TIN:", size=32, color=BAD),
                      T("nhớ “đoạn tốt nhất” nhưng quên nó nằm ở đâu!", size=28)).arrange(DOWN, buff=0.12)
        fit_stack(s1, VGroup(cells, far, far_l), q, conc, buff=0.6, max_scale=1.4)
        with self.voice("Bước một: theo thói quen từ Bài 1, ta thử đặt F của i là tổng lớn nhất của một đoạn nằm trong "
                        "i ngày đầu."):
            self.play(FadeIn(s1), run_time=0.8)
        with self.voice("Để tính F của i, ta hỏi: đoạn tốt nhất trong i ngày đầu có chứa ngày i không? "
                        "Nếu không chứa, nó chính là F của i trừ 1."):
            self.play(FadeIn(cells), run_time=0.6)
            self.play(Create(far), FadeIn(far_l), run_time=0.8)
        with self.voice("Nếu có chứa, nó là một đoạn kết thúc đúng tại ngày i. Nhưng F của i trừ 1 không cho ta biết gì "
                        "về các đoạn kết thúc tại ngày i trừ 1, vì đoạn tốt nhất có thể nằm tận đầu dãy, "
                        "không nối được với ngày i!"):
            self.play(FadeIn(q), Indicate(cells.cells[5], color=ORANGE), run_time=1.0)
            gap = Cross(cells.cells[4], stroke_color=BAD, stroke_width=6)
            self.play(Create(gap), run_time=0.6)
        with self.voice("Trạng thái F thiếu thông tin: nó nhớ đoạn tốt nhất nhưng quên mất đoạn ấy nằm ở đâu. "
                        "Đây là lúc ta đổi trạng thái."):
            self.play(FadeIn(conc, shift=UP * 0.2), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 2: Đoạn tốt nhất kết thúc ĐÚNG tại i")
        defi = panel(VGroup(TB("best(i) =", size=34, color=ACCENT),
                            T("tổng lớn nhất của một đoạn", size=30),
                            T("kết thúc ĐÚNG tại ngày i", size=30)).arrange(DOWN, buff=0.12), stroke=ACCENT)
        row = array_row(PROFIT[4:7], w=1.1, h=0.9, size=32, index_from=5)
        A_br = SurroundingRectangle(VGroup(*row.cells[0:2]), color=BLUEC, buff=0.06, stroke_width=6)
        A_new = SurroundingRectangle(row.cells[2], color=BLUEC, buff=0.12, stroke_width=6)
        A_lab = VGroup(TB("Cách A: nối dài", size=30, color=BLUEC),
                       T("đoạn kết thúc tại i−1, thêm ngày i", size=26),
                       M("best(i−1) + aᵢ", size=30, color=BLUEC)).arrange(DOWN, buff=0.1)
        B_lab = VGroup(TB("Cách B: bắt đầu mới", size=30, color=GOOD),
                       T("đoạn chỉ gồm đúng ngày i", size=26),
                       M("aᵢ", size=30, color=GOOD)).arrange(DOWN, buff=0.1)
        for lab_ in (A_lab, B_lab):
            lab_.arrange(RIGHT, buff=0.25)
            lab_[1].next_to(lab_[0], DOWN, buff=0.1, aligned_edge=LEFT)
            lab_[2].next_to(lab_[0], RIGHT, buff=0.3)
        labs = VGroup(A_lab, B_lab).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        formula = tag_box("CÔNG THỨC (THUẬT TOÁN KADANE)", [
            "best(1) = a₁",
            "best(i) = max( aᵢ , best(i−1) + aᵢ )",
            "Đáp án = max( best(1), …, best(n) )",
        ], accent=ACCENT, width=7.4, size=30)
        fit_stack(defi, VGroup(row, A_br, A_new), labs, formula, buff=0.55, max_scale=1.5)
        with self.voice("Bước hai: đặt best của i là tổng lớn nhất của một đoạn kết thúc đúng tại ngày i."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Một đoạn kết thúc tại ngày i chỉ có hai dạng. Cách A: đoạn dài hơn một ngày, tức là một đoạn "
                        "kết thúc tại ngày i trừ 1 rồi nối thêm ngày i. Tốt nhất là nối vào đoạn tốt nhất kết thúc tại "
                        "i trừ 1, được best của i trừ 1 cộng a i."):
            self.play(FadeIn(row), run_time=0.5)
            self.play(Create(A_br), FadeIn(A_lab), run_time=1.0)
        with self.voice("Cách B: đoạn chỉ gồm đúng ngày i, tổng bằng a i."):
            self.play(ReplacementTransform(A_br, A_new), run_time=0.6)
            self.play(A_new.animate.set_color(GOOD), FadeIn(B_lab), run_time=0.6)
        with self.voice("Ta được công thức của thuật toán Kadane: best của i bằng max của a i, và best của i trừ 1 cộng a i."):
            self.play(FadeIn(formula[0:3]), FadeIn(formula[3][0:2]), run_time=1.0)
        with self.voice("Diễn giải bằng lời: nếu đoạn tốt nhất kết thúc tại ngày trước có tổng âm thì vứt nó đi, "
                        "bắt đầu lại từ ngày i; ngược lại thì nối tiếp."):
            self.play(Indicate(formula[3][1], color=ACCENT), run_time=1.0)
        with self.voice("Vì mọi đoạn đều kết thúc tại một ngày nào đó, đoạn tốt nhất của cả dãy là đoạn tốt nhất trong "
                        "các best của i. Đó là lí do đáp án là max của cả bảng, chứ không phải ô cuối cùng."):
            self.play(FadeIn(formula[3][2]), run_time=0.8)
            self.play(Circumscribe(formula[3][2], color=ORANGE), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
KADANE_CODE = """
long long bestEndingHere = 0, answer = 0;
for (int day = 1; day <= dayCount; day++) {
    long long profit;
    cin >> profit;
    if (day == 1) bestEndingHere = profit;
    else bestEndingHere = max(profit, bestEndingHere + profit);
    if (day == 1) answer = bestEndingHere;
    else answer = max(answer, bestEndingHere);
}
cout << answer << '\\n';
"""


class B2_04_ChayTay(B2Scene):
    def construct(self):
        self.show_header("Bước 3: Chạy tay trên ví dụ")
        a_row = array_row(PROFIT, w=0.86, h=0.8, size=28, index_from=1, label="a")
        b_row = array_row([""] * 8, w=0.86, h=0.9, size=30, label="best", show_index=False)
        for k, c in enumerate(b_row.cells):
            c.move_to(a_row.cells[k].get_center() + DOWN * 1.0)
        b_row.lab.next_to(b_row.cells, LEFT, buff=0.15)
        tables = VGroup(a_row, b_row)
        legend = VGroup(
            VGroup(Square(0.32, fill_color=GOOD, fill_opacity=1, stroke_width=0), T("bắt đầu mới (B)", size=26)).arrange(
                RIGHT, buff=0.15),
            VGroup(Square(0.32, fill_color=BLUEC, fill_opacity=1, stroke_width=0), T("nối dài (A)", size=26)).arrange(
                RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.6)
        eq_slot = placeholder(7.2, 1.0)
        why_slot = placeholder(7.2, 1.0)
        sc = fit_stack(tables, legend, eq_slot, why_slot, buff=0.55, max_scale=1.2)
        with self.voice("Bước ba: chạy tay trên ví dụ. Hàng trên là dãy a, hàng dưới là bảng best. "
                        "Màu xanh lá là bắt đầu đoạn mới, màu xanh dương là nối dài."):
            self.play(FadeIn(tables), FadeIn(legend), run_time=1.0)
        lines = {
            0: ("best của 1 bằng a 1, bằng trừ 2.", "best(1) = a₁ = −2", ""),
            1: ("best của 2 bằng max của 3, và trừ 2 cộng 3. Bằng 3: đoạn trước có tổng âm nên bỏ đi, bắt đầu lại từ ngày 2.",
                "best(2) = max(3, −2 + 3) = 3", "đoạn trước âm → bỏ, bắt đầu lại"),
            2: ("best của 3 bằng max của trừ 1, và 3 trừ 1. Bằng 2, nối dài.", "best(3) = max(−1, 3 − 1) = 2", "nối dài"),
            3: ("best của 4 bằng max của 4, và 2 cộng 4. Bằng 6, nối dài, ứng với đoạn ngày 2 đến 4.",
                "best(4) = max(4, 2 + 4) = 6", "đoạn ngày 2 → 4"),
            4: ("best của 5 bằng max của trừ 7, và 6 trừ 7. Bằng trừ 1: vẫn nối dài, dù tổng đã âm.",
                "best(5) = max(−7, 6 − 7) = −1", "vẫn nối dài (−1 > −7)"),
            5: ("best của 6 bằng max của 2, và trừ 1 cộng 2. Bằng 2: đoạn trước âm, bắt đầu lại từ ngày 6.",
                "best(6) = max(2, −1 + 2) = 2", "đoạn trước âm → bắt đầu lại"),
            6: ("best của 7 bằng max của 5, và 2 cộng 5. Bằng 7: đây là ô lớn nhất, ứng với đoạn ngày 6 đến 7.",
                "best(7) = max(5, 2 + 5) = 7", "ô LỚN NHẤT: đoạn ngày 6 → 7"),
            7: ("best của 8 bằng max của trừ 3, và 7 trừ 3, bằng 4.", "best(8) = max(−3, 7 − 3) = 4", ""),
        }
        eq = why = None
        for i in range(8):
            sp, f, w = lines[i]
            col = GOOD if KINDS[i] == "B" else BLUEC
            new_eq = M(f, size=30, color=INK).scale(sc).move_to(eq_slot)
            new_why = T(w, size=28, color=col if i != 6 else ACCENT).scale(sc).move_to(why_slot)
            with self.voice(sp):
                c = b_row.cells[i]
                anims = [a_row.cells[i][0].animate.set_stroke(ACCENT, 6)]
                if i > 0:
                    anims.append(b_row.cells[i - 1][0].animate.set_stroke(ACCENT, 6))
                if eq is None:
                    eq, why = new_eq, new_why
                    self.play(FadeIn(eq), FadeIn(why), *anims, run_time=0.6)
                else:
                    self.play(Transform(eq, new_eq), Transform(why, new_why), *anims, run_time=0.6)
                self.play(c[0].animate.set_fill(col, 1), Transform(c[1], set_cell_value(c, BEST[i], color=BG)),
                          run_time=0.5)
                back = [a_row.cells[i][0].animate.set_stroke(MUTED, 2)]
                if i > 0:
                    back.append(b_row.cells[i - 1][0].animate.set_stroke(MUTED, 2))
                self.play(*back, run_time=0.3)
        with self.voice("Đáp án là max của cả bảng: 7, ở ngày 7. Chú ý ô cuối best của 8 chỉ bằng 4, "
                        "nên không thể lấy ô cuối làm đáp án."):
            self.play(Circumscribe(b_row.cells[6], color=ACCENT), Transform(eq, TB("Đáp án = max(best) = 7", size=38,
                                                                                    color=ACCENT).scale(sc).move_to(
                eq_slot)), FadeOut(why), run_time=1.0)
            self.play(Indicate(b_row.cells[7], color=BAD), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao best(i) đúng? — Không cần mảng")
        proof = tag_box("VÌ SAO best(i) ĐÚNG?", [
            "Xét đoạn tốt nhất [l, i] kết thúc tại i.",
            "• l < i: phần [l, i−1] phải là đoạn tốt nhất",
            "  kết thúc tại i−1 (nếu không, thay vào",
            "  sẽ tốt hơn — vô lí) ⇒ tổng best(i−1) + aᵢ",
            "• l = i: tổng là aᵢ",
            "⇒ lấy max của hai giá trị là đúng.",
        ], accent=GOOD, width=7.4, size=28)
        code = code_block(KADANE_CODE, size=20)
        cx = VGroup(TB("O(n)", size=40, color=GOOD), T("thời gian,", size=30), TB("O(1)", size=40, color=GOOD),
                    T("bộ nhớ", size=30)).arrange(RIGHT, buff=0.2)
        fit_stack(proof, code, cx, buff=0.5)
        with self.voice("Vì sao best của i đúng? Xét đoạn tốt nhất từ l đến i. Nếu l nhỏ hơn i, phần từ l đến i trừ 1 phải "
                        "là đoạn tốt nhất kết thúc tại i trừ 1, vì nếu có đoạn tổng lớn hơn, thay vào sẽ được đoạn tốt hơn, "
                        "vô lí. Nếu l bằng i thì tổng là a i. Vậy lấy max của hai giá trị là đúng."):
            self.play(FadeIn(proof), run_time=1.0)
        with self.voice("Ô best của i chỉ phụ thuộc best của i trừ 1, nên ta chỉ cần một biến, vừa đọc dữ liệu vừa tính. "
                        "Ngày đầu tiên được xử lí riêng, để đáp án khởi đầu bằng a 1 chứ không phải 0."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 4, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
            self.play(Transform(hl, line_box(code, 6, ACCENT)), run_time=0.5)
        with self.voice("Độ phức tạp O của n thời gian và O của 1 bộ nhớ. Tổng có thể tới mười mũ mười lăm, "
                        "nên phải dùng long long."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B2_05_HaiNam(B2Scene):
    def construct(self):
        self.show_header("4. Bài toán HAINAM: “Chọn hay bỏ”")
        box = tag_box("BÀI TOÁN: HAINAM", [
            "Một luống có n cây nấm xếp thành hàng,",
            "cây thứ i nặng aᵢ gam. Hái bao nhiêu cũng được",
            "nhưng KHÔNG hái hai cây đứng cạnh nhau.",
            "Tổng khối lượng lớn nhất hái được?",
        ], accent=BLUEC, width=7.4, size=28)
        mr, row = mushroom_row(MUSH)
        greedy_l = TB("Tham lam (hái cây nặng nhất còn được phép): 14", size=28, color=ORANGE)
        best_l = TB("Tối ưu: cây 1, 3, 5, 7 → 3 + 3 + 5 + 5 = 16", size=28, color=GOOD)
        lesson = T("Đáp án tốt nhất KHÔNG hái cây nặng nhất!", size=30, color=ACCENT)
        fit_stack(box, mr, greedy_l, best_l, lesson, buff=0.5, max_scale=1.2)
        with self.voice("Kiểu trạng thái thứ hai trên dãy là xét i phần tử đầu, đi kèm câu hỏi: phần tử thứ i được chọn "
                        "hay bị bỏ? Bài toán HAINAM: trên một luống có n cây nấm xếp thành hàng."):
            self.play(FadeIn(box), run_time=1.0)
        with self.voice("Em được hái bao nhiêu cây cũng được, nhưng không được hái hai cây đứng cạnh nhau, để nấm còn lan "
                        "bào tử. Ví dụ bảy cây nặng 3, 4, 3, 1, 5, 9, 5 gam."):
            self.play(LaggedStart(*[GrowFromEdge(m, DOWN) for m in row], lag_ratio=0.12), FadeIn(mr[1]), run_time=1.5)

        def ring(i, col):
            return SurroundingRectangle(row[i], color=col, buff=0.08, stroke_width=6, corner_radius=0.1)

        rings = VGroup()
        with self.voice("Chiến lược tham lam: hái cây nặng nhất còn được phép. Chọn cây 6, nặng 9 gam, rồi cây 2, 4 gam, "
                        "rồi cây 4, 1 gam. Tổng 14."):
            for i in (5, 1, 3):
                r = ring(i, ORANGE)
                rings.add(r)
                self.play(Create(r), run_time=0.5)
            self.play(FadeIn(greedy_l), run_time=0.5)
        with self.voice("Nhưng đáp án là 16, hái các cây 1, 3, 5, 7. Và đáp án ấy không hái cây nặng nhất!"):
            self.play(rings.animate.set_stroke(opacity=0.2), run_time=0.4)
            gr = VGroup(*[ring(i, GOOD) for i in (0, 2, 4, 6)])
            self.play(LaggedStart(*[Create(r) for r in gr], lag_ratio=0.25), run_time=1.2)
            self.play(FadeIn(best_l), run_time=0.5)
            self.play(FadeIn(lesson), run_time=0.5)

        self.clear_body()
        naive = tag_box("Ý TƯỞNG NGÂY THƠ: THỬ MỌI TẬP CON", [
            "Mỗi cây: hái hoặc không ⇒ 2ⁿ cách chọn.",
            "Bỏ các tập có hai cây kề nhau.",
            "O(2ⁿ · n): chỉ chạy được n ≤ 20.",
        ], accent=ORANGE, width=7.4, size=30)
        stuck = tag_box("BẾ TẮC", [
            "n = 40 đã có hơn 10¹² tập con.",
            "Để quyết định cây i, có thật sự cần biết",
            "TOÀN BỘ các cây trước đã chọn ra sao?",
        ], accent=BAD, width=7.4, size=30)
        fit_stack(naive, stuck, buff=0.8, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: mỗi cây có hai lựa chọn, hái hoặc không, nên có 2 mũ n cách chọn. "
                        "Duyệt mọi tập con, bỏ các tập có hai cây kề nhau. Chỉ chạy được n khoảng 20."):
            self.play(FadeIn(naive), run_time=0.8)
        with self.voice("Với n bằng 40 đã có hơn một nghìn tỉ tập con. Nhưng để quyết định có hái cây i hay không, "
                        "ta có thật sự cần biết toàn bộ các cây trước đó đã được chọn ra sao không?"):
            self.play(FadeIn(stuck), run_time=0.8)

        self.clear_body()
        self.show_header("Phá bế tắc: chỉ cần biết cây i−1")
        defi = panel(VGroup(TB("dp(i) =", size=34, color=ACCENT),
                            T("tổng lớn nhất khi chỉ xét i cây đầu tiên", size=28)).arrange(DOWN, buff=0.1),
                     stroke=ACCENT)
        opts = VGroup(
            panel(VGroup(TB("Bỏ cây i", size=30, color=BLUEC), T("cây 1..i−1 tùy ý", size=24),
                         M("dp(i−1)", size=30, color=BLUEC)).arrange(DOWN, buff=0.1), width=3.6, stroke=BLUEC),
            panel(VGroup(TB("Hái cây i", size=30, color=GOOD), T("cây i−1 phải bỏ", size=24),
                         M("dp(i−2) + aᵢ", size=30, color=GOOD)).arrange(DOWN, buff=0.1), width=3.6, stroke=GOOD),
        ).arrange(RIGHT, buff=0.2)
        formula = tag_box("CÔNG THỨC “CHỌN HAY BỎ”", [
            "dp(0) = 0;  dp(1) = a₁",
            "dp(i) = max( dp(i−1), dp(i−2) + aᵢ )",
            "Đáp án: dp(n) — ô cuối cùng!",
        ], accent=ACCENT, width=7.4, size=30)
        fit_stack(defi, opts, formula, buff=0.6, max_scale=1.2)
        with self.voice("Đặt dp của i là tổng lớn nhất khi chỉ xét i cây đầu tiên. Hỏi về cây thứ i: có hai khả năng."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Bỏ cây i: các cây từ 1 đến i trừ 1 tùy ý, tốt nhất là dp của i trừ 1."):
            self.play(FadeIn(opts[0], shift=UP * 0.2), run_time=0.7)
        with self.voice("Hái cây i: thì cây i trừ 1 chắc chắn bị bỏ, còn các cây từ 1 đến i trừ 2 tùy ý, "
                        "tốt nhất là dp của i trừ 2 cộng a i."):
            self.play(FadeIn(opts[1], shift=UP * 0.2), run_time=0.7)
        with self.voice("Công thức chọn hay bỏ: dp của i bằng max của dp của i trừ 1, và dp của i trừ 2 cộng a i. "
                        "Khác với bài Kadane, ở đây trạng thái i phần tử đầu đã bao trùm mọi lựa chọn, "
                        "nên ô cuối chính là đáp án."):
            self.play(FadeIn(formula), run_time=1.0)

        self.clear_body()
        self.show_header("Điền bảng dp cho ví dụ")
        mr2, row2 = mushroom_row(MUSH)
        dp_row = array_row([""] * 7, w=0.95, h=0.9, size=32, label="dp", show_index=False)
        for k, c in enumerate(dp_row.cells):
            c.move_to([row2[k].get_center()[0], 0, 0])
        dp_row.lab.next_to(dp_row.cells, LEFT, buff=0.15)
        eq_slot = placeholder(7.2, 1.0)
        sc = fit_stack(mr2, dp_row, eq_slot, buff=0.7, max_scale=1.2)
        self.play(FadeIn(mr2), FadeIn(dp_row), run_time=0.8)
        eq = None
        for i in range(7):
            if i == 0:
                f, sp = "dp(1) = a₁ = 3", "dp của 1 bằng 3."
            elif i == 1:
                f, sp = "dp(2) = max(3, 4) = 4", "dp của 2 bằng max của 3 và 4, bằng 4."
            else:
                skip, take = DP[i - 1], DP[i - 2] + MUSH[i]
                f = f"dp({i + 1}) = max({skip}, {DP[i - 2]} + {MUSH[i]}) = {DP[i]}"
                choice = "hái" if take > skip else "bỏ"
                sp = (f"dp của {i + 1}: bỏ thì được {skip}, hái thì được {DP[i - 2]} cộng {MUSH[i]} bằng {take}. "
                      f"Chọn {choice}, dp bằng {DP[i]}.")
            new_eq = M(f, size=30).scale(sc).move_to(eq_slot)
            with self.voice(sp):
                c = dp_row.cells[i]
                if eq is None:
                    eq = new_eq
                    self.play(FadeIn(eq), Indicate(row2[i], color=ACCENT), run_time=0.6)
                else:
                    self.play(Transform(eq, new_eq), Indicate(row2[i], color=ACCENT), run_time=0.6)
                taken = i < 2 or (DP[i - 2] + MUSH[i] > DP[i - 1])
                self.play(c[0].animate.set_fill(GOOD if taken else BLUEC, 1),
                          Transform(c[1], set_cell_value(c, DP[i], color=BG)), run_time=0.5)
        with self.voice("Đáp án dp của 7 bằng 16, đúng như ta đã thấy."):
            self.play(Circumscribe(dp_row.cells[6], color=ACCENT), run_time=1.0)

        self.clear_body()
        self.show_header("Cách nhìn khác: Thêm một chiều cho trạng thái")
        hai_vals, bo_vals = [], []
        h_prev, b_prev = None, 0
        for i, x in enumerate(MUSH):
            h = (b_prev + x)
            b = 0 if i == 0 else max(h_prev, b_prev)
            hai_vals.append(h)
            bo_vals.append(b)
            h_prev, b_prev = h, b
        assert max(hai_vals[-1], bo_vals[-1]) == 16
        defs = VGroup(
            rich("<span foreground='#4ADE80'><b>hai(i)</b></span> = tốt nhất trong i cây đầu, cây i ĐƯỢC hái", size=26),
            rich("<span foreground='#60A5FA'><b>bo(i)</b></span> = tốt nhất trong i cây đầu, cây i BỊ bỏ", size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        rec = VGroup(M("hai(i) = bo(i−1) + aᵢ", size=30, color=GOOD),
                     M("bo(i)  = max(hai(i−1), bo(i−1))", size=30, color=BLUEC)).arrange(DOWN, aligned_edge=LEFT,
                                                                                    buff=0.15)
        h_row = array_row(hai_vals, w=0.9, h=0.85, size=30, label="hai", index_from=1)
        b_row = array_row(bo_vals, w=0.9, h=0.85, size=30, label="bo", show_index=False)
        for k, c in enumerate(b_row.cells):
            c.move_to(h_row.cells[k].get_center() + DOWN * 0.95)
        b_row.lab.next_to(b_row.cells, LEFT, buff=0.15)
        for c in h_row.cells:
            c[0].set_fill("#14532D", 1)
        for c in b_row.cells:
            c[0].set_fill("#1E3A8A", 1)
        ans = TB("Đáp án = max(hai(n), bo(n)) = max(16, 15) = 16", size=30, color=ACCENT)
        tip = VGroup(T("Điều kiện phụ thuộc “phần tử trước ra sao”", size=26, color=MUTED),
                     T("⇒ đưa thông tin ấy VÀO trạng thái.", size=26, color=MUTED)).arrange(DOWN, buff=0.1)
        fit_stack(defs, rec, VGroup(h_row, b_row), ans, tip, buff=0.5, max_scale=1.2)
        with self.voice("Nếu em thấy công thức dp của i trừ 2 khó nghĩ ra, có một cách máy móc hơn và dùng được cho rất "
                        "nhiều bài: ghi luôn trạng thái của phần tử i vào trạng thái."):
            self.play(FadeIn(defs), run_time=1.0)
        with self.voice("Hai của i là tổng lớn nhất khi cây i được hái: cây trước phải bị bỏ, nên bằng bo của i trừ 1 "
                        "cộng a i. Bo của i là khi cây i bị bỏ: cây trước tùy ý, bằng max của hai và bo tại i trừ 1."):
            self.play(FadeIn(rec[0]), run_time=0.6)
            self.play(FadeIn(rec[1]), run_time=0.6)
        with self.voice("Điền hai hàng song song, ta được hàng hai và hàng bo như thế này."):
            self.play(FadeIn(h_row), FadeIn(b_row), run_time=1.0)
        with self.voice("Đáp án là max của hai của n và bo của n, bằng max của 16 và 15, bằng 16."):
            self.play(FadeIn(ans), Circumscribe(h_row.cells[6], color=ACCENT), run_time=1.0)
        with self.voice("Đây là kĩ thuật thêm chiều trạng thái: khi điều kiện của bài phụ thuộc vào phần tử trước đó ra sao, "
                        "ta đưa thông tin ấy vào trạng thái. Kĩ thuật này sẽ được dùng lại rất nhiều lần ở các bài sau."):
            self.play(FadeIn(tip), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B2_06_TongKet(B2Scene):
    def construct(self):
        self.show_header("5. So sánh hai kiểu trạng thái")
        heads = ["", "“Kết thúc tại i”", "“Xét i phần tử đầu”"]
        data = [
            ["Ý nghĩa", "bắt buộc dùng\nphần tử i làm cuối", "chỉ dùng 1..i,\ncó thể bỏ i"],
            ["Dùng khi", "đoạn liên tiếp,\ndãy con nối tiếp", "tập con với\nđiều kiện cục bộ"],
            ["Đáp án", "max trên MỌI i", "ô cuối dp(n)"],
            ["Ví dụ", "Kadane, LIS", "hái nấm, cái túi"],
        ]
        colw = [1.6, 2.95, 2.95]
        table = VGroup()
        for r, rowdata in enumerate([heads] + data):
            cells_ = VGroup()
            x = -sum(colw) / 2
            h = 0.8 if r == 0 else 1.15
            for cidx, (txt, w) in enumerate(zip(rowdata, colw)):
                fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
                rect = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
                rect.move_to([x + w / 2, 0, 0])
                col = BG if r == 0 else (ACCENT if cidx == 0 else INK)
                t = (TB if r == 0 or cidx == 0 else T)(txt, size=24, color=col, max_width=w - 0.15, line_spacing=0.9)
                cells_.add(VGroup(rect, t.move_to(rect)))
                x += w
            table.add(cells_)
        table.arrange(DOWN, buff=0)
        fit_stack(table, max_scale=1.2)
        with self.voice("So sánh hai kiểu trạng thái. Kết thúc tại i: lời giải bắt buộc dùng phần tử i làm phần tử cuối. "
                        "Xét i phần tử đầu: lời giải chỉ dùng các phần tử 1 đến i, có thể không dùng i."):
            self.play(FadeIn(table[0]), FadeIn(table[1]), run_time=1.0)
        with self.voice("Kết thúc tại i dùng khi lời giải là một đoạn liên tiếp, hoặc một dãy con có nối tiếp. "
                        "Xét i phần tử đầu dùng khi lời giải là một tập con với điều kiện cục bộ."):
            self.play(FadeIn(table[2]), run_time=0.7)
        with self.voice("Đáp án: với kết thúc tại i là max trên mọi i; với xét i phần tử đầu là ô cuối cùng."):
            self.play(FadeIn(table[3]), run_time=0.7)
        with self.voice("Ví dụ: Kadane và dãy con tăng dài nhất; hái nấm và bài cái túi."):
            self.play(FadeIn(table[4]), run_time=0.7)

        self.clear_body()
        self.show_header("6. Mở rộng")
        ext = [
            ("Tìm luôn đoạn tốt nhất", "Lưu start: cách B → start = i; cách A → giữ nguyên",
             "Mở rộng một: muốn in ra đoạn tốt nhất, lưu thêm ngày bắt đầu start. Chọn cách B thì start bằng i, "
             "cách A thì giữ nguyên. Đây là dạng truy vết đơn giản."),
            ("Nhìn bằng mảng cộng dồn", "tổng[l, r] = S(r) − S(l−1): trừ S nhỏ nhất đã gặp",
             "Mở rộng hai: gọi S là mảng cộng dồn. Tổng đoạn l đến r bằng S r trừ S l trừ 1. Muốn đoạn kết thúc tại r "
             "tốt nhất, trừ đi S nhỏ nhất đã gặp. Cách này giải được biến thể đoạn có độ dài ít nhất L."),
            ("Biến thể “chọn hay bỏ”", "≤ k phần tử liên tiếp · vòng tròn · xóa ≤ 1 phần tử",
             "Mở rộng ba: các biến thể như không chọn quá k phần tử liên tiếp, dãy xếp vòng tròn, hay được xóa tối đa "
             "một phần tử, đều giải bằng cách thêm chiều vào trạng thái."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Khởi tạo đáp án bằng 0", "Kadane sai khi mọi số đều âm",
             "Bẫy một: khởi tạo đáp án bằng 0 trong bài Kadane, sai khi mọi số đều âm."),
            ("Lấy best(n) làm đáp án", "Sai! Đáp án là max của mọi best(i)",
             "Bẫy hai: lấy best của n làm đáp án. Sai, đáp án là max của mọi best của i."),
            ("Dùng kiểu int", "Tổng có thể tới 10¹⁵ → long long",
             "Bẫy ba: dùng kiểu int, trong khi tổng có thể tới mười mũ mười lăm."),
            ("Quên trường hợp n = 1", "dp(i − 2) với i = 1 là chỉ số âm",
             "Bẫy bốn: quên trường hợp n bằng 1 trong bài hái nấm, truy cập chỉ số âm."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 2", [
            "• Trạng thái phải ĐỦ THÔNG TIN để viết",
            "   công thức chuyển. Thiếu thì ĐỔI trạng thái",
            "   (kết thúc tại i) hoặc THÊM CHIỀU.",
            "• “Kết thúc tại i”: đáp án = max mọi i.",
            "• “Xét i phần tử đầu”: đáp án ở ô cuối.",
            "• Câu thần chú: “Phần tử cuối được",
            "   chọn hay bị bỏ?”",
        ], accent=GOOD, width=7.4, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: trạng thái phải đủ thông tin để viết được công thức chuyển. Nếu thiếu, hãy đổi trạng thái, "
                        "như kết thúc tại i, hoặc thêm chiều, như phần tử i được chọn hay không."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:3]), run_time=1.0)
        with self.voice("Kết thúc tại i thì đáp án là max trên mọi i; xét i phần tử đầu thì đáp án ở ô cuối. "
                        "Và câu hỏi thần chú: phần tử cuối được chọn hay bị bỏ?"):
            self.play(FadeIn(mem[3][3:]), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Chạy Kadane cho dãy:", "4, −5, 3, −1, 2, −6, 5"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        row = array_row([""] * 7, w=0.95, h=0.95, size=34, label="best", index_from=1)
        ans = TB("Đáp án: 5", size=40, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: BÀI 3", size=42, color=ACCENT),
                     T("Quy hoạch động trên lưới và truy vết", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, row, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: chạy thuật toán Kadane cho dãy 4, trừ 5, 3, trừ 1, 2, trừ 6, 5. "
                        "Dừng video và thử nhé!"):
            self.play(FadeIn(q), FadeIn(row), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        vals, _ = kadane([4, -5, 3, -1, 2, -6, 5])
        assert vals == [4, -1, 3, 2, 4, -2, 5]
        with self.voice("Bảng best lần lượt là 4, trừ 1, 3, 2, 4, trừ 2, 5. Max của bảng là 5."):
            for k, v in enumerate(vals):
                c = row.cells[k]
                self.play(Transform(c[1], set_cell_value(c, v, color=BG)),
                          c[0].animate.set_fill(GOOD if v == 5 else ACCENT, 1), run_time=0.35)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Bài tiếp theo: quy hoạch động trên lưới và truy vết. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)


SCENES = [B2_00_Intro, B2_01_KhoiDong, B2_02_NgayTho, B2_03_KetThucTaiI, B2_04_ChayTay, B2_05_HaiNam,
          B2_06_TongKet]
