"""BÀI 7 — Quy hoạch động trên hai xâu (SUACHINHTA — khoảng cách sửa xâu, dãy con chung dài nhất)."""

from shared import *  # noqa: F401,F403

S_TXT, T_TXT = "HOXINHH", "HOCSINH"
A_DNA, B_DNA = "ACCGTA", "CAGTTA"


def edit_table(s, t):
    n, m = len(s), len(t)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
    return d


def edit_trace(d, s, t):
    i, j, steps = len(s), len(t), []
    while i or j:
        if i and j and s[i - 1] == t[j - 1] and d[i][j] == d[i - 1][j - 1]:
            steps.append(("giữ", i, j, i - 1, j - 1))
            i, j = i - 1, j - 1
        elif i and j and d[i][j] == d[i - 1][j - 1] + 1:
            steps.append(("thay", i, j, i - 1, j - 1))
            i, j = i - 1, j - 1
        elif i and d[i][j] == d[i - 1][j] + 1:
            steps.append(("xóa", i, j, i - 1, j))
            i -= 1
        else:
            steps.append(("chèn", i, j, i, j - 1))
            j -= 1
    return steps


def lcs_table(s, t):
    n, m = len(s), len(t)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            L[i][j] = L[i - 1][j - 1] + 1 if s[i - 1] == t[j - 1] else max(L[i - 1][j], L[i][j - 1])
    return L


def lcs_trace(L, s, t):
    i, j, path, chars = len(s), len(t), [], []
    while i and j:
        if s[i - 1] == t[j - 1]:
            path.append((i, j, i - 1, j - 1, True))
            chars.append(s[i - 1])
            i, j = i - 1, j - 1
        elif L[i - 1][j] >= L[i][j - 1]:
            path.append((i, j, i - 1, j, False))
            i -= 1
        else:
            path.append((i, j, i, j - 1, False))
            j -= 1
    return path, "".join(reversed(chars))


D = edit_table(S_TXT, T_TXT)
TRACE = edit_trace(D, S_TXT, T_TXT)
L = lcs_table(A_DNA, B_DNA)
LTRACE, LCS_STR = lcs_trace(L, A_DNA, B_DNA)
assert D[7][7] == 3 and D[2][3] == 1 and D[3][4] == 2 and D[2][2] == 0
assert [k for k, *_ in reversed(TRACE) if k != "giữ"] == ["chèn", "thay", "xóa"]
assert L[6][6] == 4 and LCS_STR == "AGTA"
assert edit_table("TRUONG", "TRUNG")[6][5] == 1 and lcs_table("GATTACA", "TACGAT")[7][6] == 4


class B7Scene(NarratedScene):
    lesson_tag = "BÀI 7"
    lesson_title = "Quy hoạch động trên hai xâu"


class CharTable(VGroup):
    """Bảng (n+1)×(m+1) với nhãn kí tự: hàng = xâu s, cột = xâu t."""

    def __init__(self, s, t, w=0.78, h=0.66):
        super().__init__()
        self.cells = {}
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                sq = Rectangle(width=w, height=h, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED,
                               stroke_width=1.5).move_to([j * w, -i * h, 0])
                ghost = TB("0", size=h * 40).move_to(sq).set_opacity(0)
                self.cells[(i, j)] = VGroup(sq, ghost)
                self.add(self.cells[(i, j)])
        top = VGroup(*[TB(c, size=26, color=BLUEC).next_to(self.cells[(0, j + 1)], UP, buff=0.12)
                       for j, c in enumerate(t)])
        left = VGroup(*[TB(c, size=26, color=ORANGE).next_to(self.cells[(i + 1, 0)], LEFT, buff=0.15)
                        for i, c in enumerate(s)])
        e1 = T("∅", size=24, color=MUTED).next_to(self.cells[(0, 0)], UP, buff=0.12)
        e2 = T("∅", size=24, color=MUTED).next_to(self.cells[(0, 0)], LEFT, buff=0.15)
        self.labels = VGroup(top, left, e1, e2)
        self.top, self.left = top, left
        self.add(self.labels)

    def fill(self, i, j, v, fill=None, color=INK):
        c = self.cells[(i, j)]
        anims = []
        if fill:
            anims.append(c[0].animate.set_fill(fill, 1))
        anims.append(Transform(c[1], set_cell_value(c, v, color=color, size=c[0].height * 40)))
        return anims

    def set_now(self, i, j, v, fill=None, color=INK):
        c = self.cells[(i, j)]
        if fill:
            c[0].set_fill(fill, 1)
        c[1].become(set_cell_value(c, v, color=color, size=c[0].height * 40))


def letter_box(ch, col=PANEL_2, size=0.7, tcol=INK):
    sq = RoundedRectangle(width=size, height=size, corner_radius=0.08, fill_color=col, fill_opacity=1,
                          stroke_color=MUTED, stroke_width=1.5)
    t = TB(ch, size=size * 46, color=tcol).move_to(sq) if ch else VGroup()
    return VGroup(sq, t)


def alignment(top, bot, kinds, size=0.72):
    """Gióng hàng hai xâu: mỗi cột (kí tự trên, kí tự dưới, loại)."""
    colmap = {"giữ": PANEL_2, "thay": ORANGE, "xóa": BAD, "chèn": GOOD}
    cols = VGroup()
    for a, b, k in zip(top, bot, kinds):
        c = colmap[k]
        ta = letter_box(a, c if a else BG, size, BG if k != "giữ" else INK)
        tb = letter_box(b, c if b else BG, size, BG if k != "giữ" else INK)
        if not a:
            ta[0].set_stroke(opacity=0.25)
        if not b:
            tb[0].set_stroke(opacity=0.25)
        lab = T(k, size=size * 26, color=MUTED if k == "giữ" else c)
        cols.add(VGroup(ta, tb, lab).arrange(DOWN, buff=0.08))
    return cols.arrange(RIGHT, buff=0.08)


ALIGN_TOP = ["H", "O", "", "X", "I", "N", "H", "H"]
ALIGN_BOT = ["H", "O", "C", "S", "I", "N", "", "H"]
ALIGN_KIND = ["giữ", "giữ", "chèn", "thay", "giữ", "giữ", "xóa", "giữ"]


# ----------------------------------------------------------------------------
class B7_00_Intro(B7Scene):
    def construct(self):
        tag = TB("BÀI 7", size=80, color=ACCENT)
        ttl = TB("Quy hoạch động trên hai xâu", size=46)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Trạng thái (i, j) trên hai TIỀN TỐ",
            "✓ Khoảng cách sửa xâu: chèn, xóa, thay",
            "✓ Dãy con chung dài nhất (LCS)",
            "✓ Truy vết; tiết kiệm bộ nhớ bằng hai hàng",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 7, bài cuối của Chương 2: Quy hoạch động trên hai xâu."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ xây dựng trạng thái i, j trên hai tiền tố, khung sườn của hầu hết các bài trên "
                        "hai xâu, và giải bài khoảng cách sửa xâu cùng bài dãy con chung dài nhất."):
            self.play(FadeIn(goals[0:3], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em cũng sẽ truy vết trên bảng để in ra cách sửa, và tiết kiệm bộ nhớ bằng hai hàng khi chỉ cần giá trị."):
            self.play(FadeIn(goals[3], shift=RIGHT * 0.3), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B7_01_KhoiDong(B7Scene):
    def construct(self):
        self.show_header("Khởi động: Bộ gõ đoán từ")
        phone = RoundedRectangle(width=4.6, height=2.4, corner_radius=0.35, fill_color=PANEL, fill_opacity=1,
                                 stroke_color=MUTED, stroke_width=3)
        typed = VGroup(T("Em gõ:", size=26, color=MUTED), M("HOXINHH", size=40, color=BAD)).arrange(RIGHT, buff=0.25)
        sugg = VGroup(T("Gợi ý:", size=26, color=MUTED), M("HOCSINH", size=40, color=GOOD)).arrange(RIGHT, buff=0.25)
        VGroup(typed, sugg).arrange(DOWN, buff=0.35).move_to(phone)
        ph = VGroup(phone, typed, sugg)
        ops = VGroup(*[panel(VGroup(TB(a, size=28, color=c), T(b, size=22)).arrange(DOWN, buff=0.06), pad=0.18, stroke=c)
                       for a, b, c in [("CHÈN", "thêm 1 kí tự", GOOD), ("XÓA", "bỏ 1 kí tự", BAD),
                                       ("THAY", "đổi 1 kí tự", ORANGE)]]).arrange(RIGHT, buff=0.25)
        q = TB("Cần ÍT NHẤT mấy thao tác?", size=34, color=ACCENT)
        al = alignment(ALIGN_TOP, ALIGN_BOT, ALIGN_KIND)
        ans = TB("3 thao tác: chèn C, thay X → S, xóa H", size=30, color=GOOD)
        fit_stack(ph, ops, q, al, ans, buff=0.5, max_scale=1.15)
        with self.voice("Em gõ vội chữ HOXINHH thay vì HOCSINH. Bộ gõ trên điện thoại vẫn đoán ra từ em muốn gõ. Nó làm thế nào?"):
            self.play(FadeIn(phone), Write(typed), run_time=1.0)
            self.play(FadeIn(sugg, shift=UP * 0.2), run_time=0.6)
        with self.voice("Một cách là đo xem cần ít nhất bao nhiêu thao tác sửa: chèn một kí tự, xóa một kí tự, hoặc thay một kí tự "
                        "bằng kí tự khác, để biến từ gõ nhầm thành từng từ trong từ điển, rồi gợi ý từ gần nhất."):
            self.play(LaggedStart(*[FadeIn(o, shift=UP * 0.2) for o in ops], lag_ratio=0.3), run_time=1.2)
        with self.voice("Hãy thử: cần mấy thao tác để biến HOXINHH thành HOCSINH?"):
            self.play(Write(q), run_time=0.8)
        with self.voice("Đáp án là 3. Viết dưới dạng gióng hàng hai xâu: mỗi cột là một cặp kí tự giống nhau, không tốn gì; "
                        "một cặp khác nhau là thay; một kí tự của s đứng một mình là xóa; một kí tự của t đứng một mình là chèn."):
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in al], lag_ratio=0.15), run_time=1.6)
            self.play(FadeIn(ans), run_time=0.5)

        self.clear_body()
        self.show_header("1. Bài toán SUACHINHTA")
        box = tag_box("BÀI TOÁN: SUACHINHTA", [
            "Cho hai xâu s và t. Mỗi thao tác: CHÈN một kí tự,",
            "XÓA một kí tự, hoặc THAY một kí tự bằng kí tự khác.",
            "Tìm số thao tác ÍT NHẤT để biến s thành t",
            "(khoảng cách sửa xâu, khoảng cách Levenshtein).",
            "|s|, |t| ≤ 5000",
        ], width=7.5, size=28)
        box[3][4].set_color(ORANGE)
        ex = VGroup(M("HOXINHH → HOCSINH", size=32), TB("= 3", size=40, color=GOOD)).arrange(RIGHT, buff=0.3)
        fit_stack(box, ex, buff=0.8, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán SUACHINHTA: cho hai xâu s và t. Mỗi thao tác được phép chèn, xóa, "
                        "hoặc thay một kí tự. Tìm số thao tác ít nhất để biến s thành t. Đây gọi là khoảng cách sửa xâu, "
                        "hay khoảng cách Levenshtein. Hai xâu dài tới năm nghìn kí tự."):
            self.play(FadeIn(box), run_time=1.0)
            self.play(FadeIn(ex), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B7_02_NgayTho(B7Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: thử thao tác ở cuối xâu")
        look = VGroup(T("Nhìn vào KÍ TỰ CUỐI của hai xâu:", size=30),
                      rich("…<span foreground='#FB923C'><b>H</b></span>   và   …<span foreground='#60A5FA'><b>H</b></span>",
                           size=40, font=MONO)).arrange(DOWN, buff=0.2)
        cases = VGroup(
            panel(VGroup(TB("Giống nhau", size=28, color=GOOD), T("để nguyên, bỏ cả hai kí tự cuối", size=24)).arrange(
                DOWN, buff=0.08), width=7.4, stroke=GOOD),
            panel(VGroup(TB("Khác nhau: thử cả 3 cách", size=28, color=ORANGE),
                         T("xóa cuối s · chèn cuối t · thay cuối s bằng cuối t", size=24)).arrange(DOWN, buff=0.08),
                  width=7.4, stroke=ORANGE)).arrange(DOWN, buff=0.25)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Khác nhau ⇒ mỗi lời gọi sinh 3 lời gọi con,",
            "độ sâu tới |s| + |t| ⇒ có thể cỡ 3^(|s|+|t|).",
            "Hai xâu dài 20: hoàn toàn không chạy nổi!",
        ], accent=ORANGE, width=7.5, size=28)
        fit_stack(look, cases, cnt, buff=0.6, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: nhìn vào kí tự cuối của hai xâu."):
            self.play(FadeIn(look), run_time=0.8)
        with self.voice("Nếu chúng giống nhau, cứ để nguyên và giải bài toán cho hai xâu đã bỏ kí tự cuối. Nếu khác nhau, có ba cách "
                        "xử lí kí tự cuối: xóa kí tự cuối của s, chèn kí tự cuối của t vào cuối s, hoặc thay kí tự cuối của s bằng "
                        "kí tự cuối của t. Thử cả ba bằng đệ quy và lấy cách ít thao tác nhất."):
            self.play(FadeIn(cases[0]), run_time=0.6)
            self.play(FadeIn(cases[1]), run_time=0.6)
        with self.voice("Đếm số phép tính: khi hai kí tự cuối khác nhau, mỗi lời gọi sinh ra ba lời gọi con, độ sâu có thể tới tổng "
                        "độ dài hai xâu. Số lời gọi có thể cỡ 3 mũ tổng độ dài. Hai xâu dài 20 là hoàn toàn không chạy nổi."):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        stuck = tag_box("BẾ TẮC", [
            "Tham số của hàm chỉ là một cặp (i, j):",
            "0 ≤ i ≤ |s|,  0 ≤ j ≤ |t|",
            "⇒ tối đa (|s|+1)(|t|+1) ≈ 25 triệu cặp.",
            "Hàng tỉ tỉ lời gọi chỉ xoay quanh",
            "25 triệu bài toán con: quá nhiều trùng lặp!",
        ], accent=BAD, width=7.5, size=30)
        fit_stack(stuck, max_scale=1.2)
        with self.voice("Bế tắc! Nhưng tham số của hàm chỉ là một cặp i, j: i kí tự đầu của s và j kí tự đầu của t. Có tối đa khoảng "
                        "hai mươi lăm triệu cặp khác nhau với xâu dài năm nghìn. Hàng tỉ tỉ lời gọi chỉ xoay quanh hai mươi lăm "
                        "triệu bài toán con: quá nhiều trùng lặp!"):
            self.play(FadeIn(stuck), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B7_03_BangD(B7Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Bảng d(i, j)")
        defi = panel(VGroup(TB("d(i, j) =", size=34, color=ACCENT),
                            T("số thao tác ít nhất để biến", size=28),
                            T("i kí tự đầu của s thành j kí tự đầu của t", size=28)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        w = 1.35
        c_ij = Square(w, fill_color=ACCENT, fill_opacity=0.9, stroke_color=INK, stroke_width=2)
        c_d = Square(w, fill_color=PANEL_2, fill_opacity=1, stroke_color=ORANGE, stroke_width=3).next_to(c_ij, UL, buff=0)
        c_u = Square(w, fill_color=PANEL_2, fill_opacity=1, stroke_color=BAD, stroke_width=3).next_to(c_ij, UP, buff=0)
        c_l = Square(w, fill_color=PANEL_2, fill_opacity=1, stroke_color=GOOD, stroke_width=3).next_to(c_ij, LEFT, buff=0)
        tx = VGroup(TB("(i, j)", size=24, color=BG).move_to(c_ij), T("(i−1, j−1)", size=20).move_to(c_d),
                    T("(i−1, j)", size=20).move_to(c_u), T("(i, j−1)", size=20).move_to(c_l))
        arr = VGroup(Arrow(c_d.get_center(), c_ij.get_center(), buff=0.4, color=ORANGE, stroke_width=6),
                     Arrow(c_u.get_center(), c_ij.get_center(), buff=0.4, color=BAD, stroke_width=6),
                     Arrow(c_l.get_center(), c_ij.get_center(), buff=0.4, color=GOOD, stroke_width=6))
        labs = VGroup(T("chéo: giữ / THAY", size=24, color=ORANGE), T("trên: XÓA sᵢ", size=24, color=BAD),
                      T("trái: CHÈN tⱼ", size=24, color=GOOD)).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        diag = VGroup(VGroup(c_ij, c_d, c_u, c_l, tx, arr), labs).arrange(RIGHT, buff=0.5)
        formula = tag_box("CÔNG THỨC KHOẢNG CÁCH SỬA XÂU", [
            "• Cơ sở: d(i, 0) = i;  d(0, j) = j",
            "• sᵢ = tⱼ:  d(i, j) = d(i−1, j−1)",
            "• sᵢ ≠ tⱼ:  d(i, j) = 1 + min(trên, trái, chéo)",
            "• Điền từng hàng, trái sang phải",
        ], width=7.5, size=28)
        formula[3][2].set_color(ACCENT)
        fit_stack(defi, diag, formula, buff=0.55, max_scale=1.25)
        with self.voice("Bước một: trạng thái trên hai tiền tố. Đặt d của i, j là số thao tác ít nhất để biến i kí tự đầu của s "
                        "thành j kí tự đầu của t. Đáp án là d tại độ dài hai xâu."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Bước hai: nhìn vào cột cuối cùng của phép gióng hàng tốt nhất. Chỉ có ba khả năng, ứng với ba ô có thể "
                        "dẫn tới ô i, j."):
            self.play(FadeIn(c_ij), FadeIn(tx[0]), run_time=0.4)
        with self.voice("Đi chéo: ghép s i với t j, giữ nguyên nếu giống, thay nếu khác. Đi từ trên xuống: xóa s i. "
                        "Đi từ trái sang: chèn t j."):
            for k, (c, t) in enumerate([(c_d, tx[1]), (c_u, tx[2]), (c_l, tx[3])]):
                self.play(FadeIn(c), FadeIn(t), GrowArrow(arr[k]), FadeIn(labs[k]), run_time=0.6)
        with self.voice("Công thức: cơ sở d của i, 0 bằng i, xóa hết i kí tự; d của 0, j bằng j, chèn đủ j kí tự. Nếu s i bằng t j, "
                        "d của i, j bằng ô chéo. Nếu khác, bằng 1 cộng min của ô trên, ô trái và ô chéo."):
            self.play(FadeIn(formula), run_time=1.0)
        with self.voice("Khi hai kí tự bằng nhau, ghép chúng với nhau luôn là tốt nhất: nếu một cách sửa tốt nhất không ghép chúng, "
                        "ta luôn biến đổi được thành một cách không tệ hơn mà có ghép."):
            self.play(Indicate(formula[3][1], color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("Chạy tay: s = HOXINHH, t = HOCSINH")
        tbl = CharTable(S_TXT, T_TXT)
        eq_slot = placeholder(7.4, 1.1)
        sc = fit_stack(tbl, eq_slot, buff=0.5, max_scale=1.25)
        eq = [None]

        def say_eq(text, color=INK):
            new = M(text, size=28, color=color).scale(sc)
            if new.width > 7.4:
                new.scale_to_fit_width(7.4)
            new.move_to(eq_slot)
            if eq[0] is None:
                eq[0] = new
                return FadeIn(new)
            return Transform(eq[0], new)

        with self.voice("Bảng có hàng là các kí tự của s, cột là các kí tự của t. Hàng 0 và cột 0 là cơ sở: 0, 1, 2, cho tới 7."):
            self.play(FadeIn(tbl), run_time=0.8)
            anims = []
            for j in range(8):
                anims += tbl.fill(0, j, j, fill="#334155")
            for i in range(1, 8):
                anims += tbl.fill(i, 0, i, fill="#334155")
            self.play(LaggedStart(*anims, lag_ratio=0.03), run_time=1.2)

        def fill_row(i, rt=1.2):
            anims = []
            for j in range(1, 8):
                same = S_TXT[i - 1] == T_TXT[j - 1]
                anims.append(AnimationGroup(*tbl.fill(i, j, D[i][j], fill="#166534" if same else "#1E3A8A")))
            self.play(LaggedStart(*anims, lag_ratio=0.2), run_time=rt)

        with self.voice("Hàng H và hàng O. Ô xanh lá là ô có hai kí tự bằng nhau, lấy ô chéo. d của 2, 2 bằng 0: HO và HO giống hệt."):
            self.play(say_eq("d(2,2) = d(1,1) = 0  (HO = HO)", GOOD), run_time=0.4)
            fill_row(1)
            fill_row(2)
            self.play(Indicate(tbl.cells[(2, 2)], color=GOOD), run_time=0.6)
        with self.voice("d của 2, 3 bằng 1 cộng min của 2, 0 và 1, bằng 1: HO thành HOC cần chèn C."):
            self.play(say_eq("d(2,3) = 1 + min(2, 0, 1) = 1  (chèn C)", ACCENT), Indicate(tbl.cells[(2, 3)], color=ACCENT),
                      run_time=0.8)
        with self.voice("Hàng X: d của 3, 4, với X khác S, bằng 1 cộng min của 2, 1, 1, bằng 2."):
            fill_row(3)
            self.play(say_eq("d(3,4) = 1 + min(2, 1, 1) = 2", ACCENT), Indicate(tbl.cells[(3, 4)], color=ACCENT), run_time=0.8)
        with self.voice("Cứ thế điền các hàng I, N, H, H."):
            for i in range(4, 8):
                fill_row(i, rt=1.0)
        with self.voice("Ô cuối: s 7 bằng t 7 bằng H, nên d của 7, 7 bằng d của 6, 6, bằng 3. Đáp án 3."):
            self.play(say_eq("d(7,7) = d(6,6) = 3", GOOD), Circumscribe(tbl.cells[(7, 7)], color=ACCENT), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
TWO_ROW_CODE = """
for (int j = 0; j <= m; j++) prev[j] = j;
for (int i = 1; i <= n; i++) {
    cur[0] = i;
    for (int j = 1; j <= m; j++) {
        if (s[i - 1] == t[j - 1]) cur[j] = prev[j - 1];
        else cur[j] = 1 + min({prev[j],       // xóa
                               cur[j - 1],    // chèn
                               prev[j - 1]}); // thay
    }
    swap(prev, cur);
}
"""


class B7_04_TruyVet(B7Scene):
    def construct(self):
        self.show_header("Bước 4: Truy vết — đọc ra cách sửa")
        tbl = CharTable(S_TXT, T_TXT)
        for i in range(8):
            for j in range(8):
                tbl.set_now(i, j, D[i][j])
        ops_slot = placeholder(7.4, 1.0)
        sc = fit_stack(tbl, ops_slot, buff=0.5, max_scale=1.25)
        with self.voice("Truy vết: đi ngược từ ô cuối. Nếu hai kí tự bằng nhau và ô chéo bằng nhau, đi chéo, giữ nguyên. Nếu không, "
                        "tìm ô trong ba ô kề có giá trị bằng ô hiện tại trừ 1: chéo là thay, lên trên là xóa, sang trái là chèn."):
            self.play(FadeIn(tbl), run_time=0.8)
        rec = None
        done = []
        colmap = {"giữ": MUTED, "thay": ORANGE, "xóa": BAD, "chèn": GOOD}
        for kind, i, j, pi, pj in TRACE:
            done.append(kind)
            col = colmap[kind]
            what = {"giữ": f"giữ {S_TXT[i - 1]}", "thay": f"thay {S_TXT[i - 1]} → {T_TXT[j - 1]}",
                    "xóa": f"xóa {S_TXT[i - 1]}" if i else "", "chèn": f"chèn {T_TXT[j - 1]}"}[kind]
            if kind == "giữ":
                sp = f"Ô {i}, {j}: hai kí tự cùng là {S_TXT[i - 1]}, đi chéo, giữ nguyên."
            elif kind == "thay":
                sp = f"Ô {i}, {j}: {S_TXT[i - 1]} khác {T_TXT[j - 1]}, ô chéo nhỏ hơn 1: thay {S_TXT[i - 1]} thành {T_TXT[j - 1]}."
            elif kind == "xóa":
                sp = f"Ô {i}, {j}: ô phía trên nhỏ hơn 1: xóa chữ {S_TXT[i - 1]}."
            else:
                sp = f"Ô {i}, {j}: ô bên trái nhỏ hơn 1: chèn chữ {T_TXT[j - 1]}."
            with self.voice(sp):
                arr = Arrow(tbl.cells[(i, j)].get_center(), tbl.cells[(pi, pj)].get_center(), buff=0.15 * sc, color=col
                            if kind != "giữ" else ACCENT, stroke_width=6, max_tip_length_to_length_ratio=0.3)
                txt = TB(what, size=34, color=col if kind != "giữ" else INK).scale(sc).move_to(ops_slot)
                anims = [GrowArrow(arr), tbl.cells[(i, j)][0].animate.set_fill(col if kind != "giữ" else "#166534", 1)]
                if rec is None:
                    rec = txt
                    anims.append(FadeIn(rec))
                else:
                    anims.append(Transform(rec, txt))
                self.play(*anims, run_time=0.55)
        al = alignment(ALIGN_TOP, ALIGN_BOT, ALIGN_KIND).scale(sc * 0.9).move_to(ops_slot)
        with self.voice("Đường đi cho đúng cách sửa ở đầu bài: chèn C, thay X bằng S, xóa một chữ H. Tổng 3 thao tác."):
            self.play(FadeOut(rec), FadeIn(al), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 5: Chỉ cần hai hàng")
        idea = VGroup(T("Hàng i chỉ dùng hàng i−1 và chính nó ⇒", size=28),
                      T("giữ prev (hàng trên) và cur (hàng đang điền),", size=28),
                      T("điền xong thì ĐỔI VAI (swap, O(1)).", size=28, color=ACCENT)).arrange(DOWN, buff=0.1)
        code = code_block(TWO_ROW_CODE, size=20)
        mem = VGroup(T("Bộ nhớ:", size=30), TB("25 triệu ô", size=34, color=BAD), T("→", size=30),
                     TB("2 · 5001 ô", size=34, color=GOOD)).arrange(RIGHT, buff=0.2)
        cx = VGroup(TB("O(|s|·|t|)", size=40, color=GOOD), T("5000 × 5000 ≈ 2,5·10⁷ phép, khoảng 0,1 giây", size=26)).arrange(
            DOWN, buff=0.1)
        fit_stack(idea, code, mem, cx, buff=0.5)
        with self.voice("Bước năm: hàng i chỉ dùng hàng i trừ 1 và chính nó, nên ta giữ hai mảng: prev là hàng trên, cur là "
                        "hàng đang điền. Điền xong thì đổi vai. Lệnh swap của hai vector chỉ đổi con trỏ bên trong, tốn O của 1."):
            self.play(FadeIn(idea), run_time=0.8)
            self.play(FadeIn(code), run_time=0.8)
        with self.voice("Chú ý cur 0 bằng i ở đầu mỗi hàng: đó là cơ sở d của i, 0 bằng i."):
            hl = line_box(code, 2, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
        with self.voice("Bộ nhớ giảm từ hai mươi lăm triệu ô xuống hai nhân năm nghìn ô. Độ phức tạp O của tích hai độ dài: "
                        "hai xâu dài năm nghìn cần khoảng hai mươi lăm triệu phép, chạy khoảng 0 phẩy 1 giây."):
            self.play(FadeOut(hl), FadeIn(mem), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B7_05_LCS(B7Scene):
    def construct(self):
        self.show_header("4. Dãy con chung dài nhất (LCS)")
        dna = VGroup(VGroup(T("s =", size=30, color=MUTED), M(A_DNA, size=40, color=ORANGE)).arrange(RIGHT, buff=0.25),
                     VGroup(T("t =", size=30, color=MUTED), M(B_DNA, size=40, color=BLUEC)).arrange(RIGHT, buff=0.25)).arrange(
            DOWN, buff=0.2)
        q = VGroup(T("Xâu dài nhất xuất hiện (không nhất thiết liên tiếp)", size=27),
                   T("trong CẢ HAI xâu?  Ví dụ: AGTA, độ dài 4", size=27, color=GOOD)).arrange(DOWN, buff=0.1)
        rules = VGroup(
            panel(VGroup(TB("sᵢ = tⱼ", size=30, color=GOOD), T("ghép làm kí tự cuối", size=24),
                         M("L(i−1, j−1) + 1", size=26, color=GOOD)).arrange(DOWN, buff=0.08), width=3.65, stroke=GOOD),
            panel(VGroup(TB("sᵢ ≠ tⱼ", size=30, color=BLUEC), T("bỏ một trong hai", size=24),
                         M("max(trên, trái)", size=26, color=BLUEC)).arrange(DOWN, buff=0.08), width=3.65, stroke=BLUEC),
        ).arrange(RIGHT, buff=0.2)
        fit_stack(dna, q, rules, buff=0.7, max_scale=1.25)
        with self.voice("Bài toán thứ hai trên hai xâu nổi tiếng không kém: các nhà sinh học so sánh hai đoạn ADN bằng cách tìm dãy con "
                        "chung dài nhất, tức là dãy kí tự dài nhất xuất hiện, không nhất thiết liên tiếp, trong cả hai xâu."):
            self.play(FadeIn(dna), run_time=0.8)
        with self.voice("Ví dụ ACCGTA và CAGTTA: một dãy con chung dài nhất là AGTA, độ dài 4."):
            self.play(FadeIn(q), run_time=0.6)
        with self.voice("Vẫn trạng thái trên hai tiền tố: L của i, j là độ dài dãy con chung dài nhất của i kí tự đầu s và j kí tự "
                        "đầu t. Nếu hai kí tự cuối bằng nhau, ghép chúng làm kí tự cuối: ô chéo cộng 1. Nếu khác nhau, ít nhất một "
                        "trong hai không thuộc dãy chung; bỏ nó đi: max của ô trên và ô trái."):
            self.play(FadeIn(rules[0]), run_time=0.6)
            self.play(FadeIn(rules[1]), run_time=0.6)

        self.clear_body()
        self.show_header("Bảng L và truy vết")
        tbl = CharTable(A_DNA, B_DNA, w=0.85, h=0.7)
        res_slot = placeholder(7.4, 1.2)
        sc = fit_stack(tbl, res_slot, buff=0.5, max_scale=1.25)
        self.play(FadeIn(tbl), run_time=0.6)
        with self.voice("Hàng 0 và cột 0 bằng 0. Điền từng hàng: ô xanh lá là hai kí tự bằng nhau, lấy chéo cộng 1."):
            anims = []
            for j in range(7):
                anims += tbl.fill(0, j, 0, fill="#334155")
            for i in range(1, 7):
                anims += tbl.fill(i, 0, 0, fill="#334155")
            self.play(LaggedStart(*anims, lag_ratio=0.03), run_time=0.8)
            for i in range(1, 7):
                row = []
                for j in range(1, 7):
                    same = A_DNA[i - 1] == B_DNA[j - 1]
                    row.append(AnimationGroup(*tbl.fill(i, j, L[i][j], fill="#166534" if same else "#1E3A8A")))
                self.play(LaggedStart(*row, lag_ratio=0.2), run_time=0.8)
        with self.voice("Ô cuối L của 6, 6 bằng 4."):
            self.play(Circumscribe(tbl.cells[(6, 6)], color=ACCENT), run_time=0.8)
        picked = ""
        with self.voice("Truy vết: từ ô cuối, nếu hai kí tự bằng nhau thì ghi nhận kí tự và đi chéo; nếu không, đi về phía ô lớn hơn "
                        "trong hai ô trên và trái. Các ô vàng là các kí tự chung A, G, T, A."):
            for i, j, pi, pj, take in LTRACE:
                arr = Arrow(tbl.cells[(i, j)].get_center(), tbl.cells[(pi, pj)].get_center(), buff=0.15 * sc,
                            color=ACCENT if take else MUTED, stroke_width=5, max_tip_length_to_length_ratio=0.3)
                anims = [GrowArrow(arr)]
                if take:
                    picked = A_DNA[i - 1] + picked
                    anims.append(tbl.cells[(i, j)][0].animate.set_fill(ACCENT, 1))
                    anims.append(tbl.cells[(i, j)][1].animate.set_color(BG))
                self.play(*anims, run_time=0.35)
            res = VGroup(T("Dãy con chung dài nhất:", size=30), TB(LCS_STR, size=44, color=ACCENT)).arrange(RIGHT, buff=0.3)
            self.play(FadeIn(res.scale(sc).move_to(res_slot)), run_time=0.5)

        self.clear_body()
        self.show_header("Mối liên hệ giữa hai bài toán")
        rel = tag_box("CHỈ ĐƯỢC CHÈN VÀ XÓA (không thay)", [
            "Số thao tác ít nhất = |s| + |t| − 2·L",
            "giữ nguyên dãy con chung dài nhất,",
            "xóa mọi kí tự còn lại của s,",
            "chèn mọi kí tự còn lại của t.",
            "Ví dụ ADN: 6 + 6 − 2·4 = 4 thao tác",
        ], accent=PURPLE, width=7.5, size=29)
        rel[3][4].set_color(GOOD)
        code = code_block("""
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) {
        if (s[i - 1] == t[j - 1])
            common[i][j] = common[i - 1][j - 1] + 1;
        else
            common[i][j] = max(common[i - 1][j],
                               common[i][j - 1]);
    }
""", size=22)
        fit_stack(rel, code, buff=0.8)
        with self.voice("Mối liên hệ giữa hai bài toán: nếu chỉ được chèn và xóa, không được thay, số thao tác ít nhất bằng tổng hai "
                        "độ dài trừ hai lần L. Giữ nguyên dãy con chung dài nhất, xóa mọi kí tự còn lại của s và chèn mọi kí tự "
                        "còn lại của t. Với ví dụ ADN: 6 cộng 6 trừ 8, bằng 4 thao tác."):
            self.play(FadeIn(rel), run_time=1.0)
        with self.voice("Code dãy con chung dài nhất chỉ vài dòng, cùng khung sườn với bài sửa xâu."):
            self.play(FadeIn(code), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B7_06_TongKet(B7Scene):
    def construct(self):
        self.show_header("5. Mở rộng")
        ext = [
            ("Chi phí khác nhau cho từng thao tác", "Thay các số 1 bằng chi phí chèn / xóa / thay",
             "Mở rộng một: nếu chèn, xóa, thay có chi phí khác nhau, hoặc chi phí thay phụ thuộc vào hai kí tự, chỉ cần thay "
             "các số 1 trong công thức. Khung sườn không đổi."),
            ("Dãy con đối xứng dài nhất", "= LCS của s và xâu ĐẢO NGƯỢC của s (hoặc Bài 8)",
             "Mở rộng hai: dãy con đối xứng dài nhất của s chính là dãy con chung dài nhất của s và xâu đảo ngược của s."),
            ("Đếm, khớp mẫu, siêu dãy chung", "cnt(i, j); mẫu có ? và *; siêu dãy dài |s| + |t| − L",
             "Mở rộng ba: đếm số lần t xuất hiện như dãy con của s, khớp mẫu có kí tự đại diện, hay siêu dãy chung ngắn nhất "
             "dài tổng hai độ dài trừ L, đều là bảng trên hai tiền tố."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Lệch chỉ số", "sᵢ trong công thức là s[i − 1] trong C++",
             "Bẫy một: lệch chỉ số. Trong công thức, s i là kí tự thứ i đếm từ 1, còn trong C++ là s i trừ 1."),
            ("Quên cơ sở d(i, 0) = i, d(0, j) = j", "Bảng sửa xâu sai toàn bộ",
             "Bẫy hai: quên cơ sở d của i, 0 bằng i và d của 0, j bằng j, bảng sẽ sai toàn bộ."),
            ("Tràn bộ nhớ", "5001 × 5001 int = 100 MB: dùng hai hàng",
             "Bẫy ba: tràn bộ nhớ. Bảng năm nghìn nhân năm nghìn kiểu int cần một trăm megabyte. Dùng hai hàng khi không cần "
             "truy vết."),
            ("Nhầm dãy con với xâu con", "Xâu con chung (liên tiếp): kiểu “kết thúc tại”",
             "Bẫy bốn: nhầm dãy con với xâu con. Xâu con chung dài nhất, liên tiếp, có công thức khác: kiểu kết thúc tại."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 7", [
            "• Hai xâu: trạng thái (i, j) trên hai TIỀN TỐ;",
            "   nhìn CẶP KÍ TỰ CUỐI.",
            "• Sửa xâu: bằng nhau đi chéo miễn phí;",
            "   khác nhau 1 + min(trên, trái, chéo).",
            "• LCS: bằng nhau chéo + 1;",
            "   khác nhau max(trên, trái).",
            "• Hai hàng là đủ nếu chỉ cần giá trị.",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: bài trên hai xâu dùng trạng thái i, j trên hai tiền tố, và nhìn cặp kí tự cuối. Sửa xâu: bằng nhau "
                        "thì đi chéo miễn phí, khác nhau thì 1 cộng min của trên, trái, chéo."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Dãy con chung dài nhất: bằng nhau thì chéo cộng 1, khác nhau thì max của trên và trái. Và hai hàng là đủ nếu "
                        "chỉ cần giá trị."):
            self.play(FadeIn(mem[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Khoảng cách sửa xâu giữa", "TRUONG và TRUNG?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        al = alignment(list("TRUONG"), ["T", "R", "U", "", "N", "G"], ["giữ", "giữ", "giữ", "xóa", "giữ", "giữ"], size=0.85)
        ans = TB("Đáp án 1: xóa chữ O", size=36, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: CHƯƠNG 3", size=42, color=ACCENT), T("Bài 8: Quy hoạch động trên đoạn", size=32)).arrange(
            DOWN, buff=0.2)
        fit_stack(q, timer_slot, al, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: khoảng cách sửa xâu giữa TRUONG và TRUNG là bao nhiêu? Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp án 1: chỉ cần xóa chữ O."):
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in al], lag_ratio=0.15), run_time=1.0)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Chúc mừng các em đã hoàn thành Chương 2! Tiếp theo là Chương 3: Quy hoạch động nâng cao, mở đầu với quy hoạch "
                        "động trên đoạn. Hẹn gặp lại!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
