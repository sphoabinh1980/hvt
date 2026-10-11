"""BÀI 1 — Từ đệ quy đến bảng phương án (bài NHAYDA và PHIQUA)."""

import math

from common import *  # noqa: F401,F403

SLIP = (3,)
F_VALUES = [1, 1, 2, 0, 3, 5]  # f(0..5) khi đá 3 trơn


def frog_on(stone, s=1.0):
    return stone.get_center() + UP * 0.5 * s


def frog_hop(frog, stone, s=1.0):
    return MoveAlongPath(frog, ArcBetweenPoints(frog.get_center(), frog_on(stone, s), angle=-PI * 0.65))


class B1Scene(NarratedScene):
    lesson_tag = "BÀI 1"
    lesson_title = "Từ đệ quy đến bảng phương án"


def list_cards(items, accent=ACCENT, stroke=None, title_size=30, body_size=25, width=7.5, prefix=""):
    """Danh sách thẻ (tiêu đề + mô tả)."""
    cards = VGroup()
    for ttl, body in items:
        g = VGroup(TB(prefix + ttl, size=title_size, color=accent), T(body, size=body_size, color=INK))
        g.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        c = panel(g, width=width, pad=0.28, stroke=stroke or MUTED)
        c[1].align_to(c[0], LEFT).shift(RIGHT * 0.28)
        cards.add(c)
    return cards.arrange(DOWN, buff=0.28)


# ----------------------------------------------------------------------------
class B1_00_Intro(B1Scene):
    def construct(self):
        chap = TB("CHƯƠNG 1", size=44, color=ACCENT)
        title = VGroup(TB("NỀN TẢNG", size=64), TB("QUY HOẠCH ĐỘNG", size=64)).arrange(DOWN, buff=0.2)
        sub = T("Dynamic Programming · Tin học HSG", size=28, color=MUTED)
        bar = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        cover = VGroup(chap, title, sub, bar).arrange(DOWN, buff=0.35)
        quote = VGroup(T("“Người không nhớ quá khứ", size=36, slant=ITALIC),
                       T("sẽ phải sống lại nó.”", size=36, slant=ITALIC)).arrange(DOWN, buff=0.15)
        idea = tag_box("QUY HOẠCH ĐỘNG LÀ GÌ?", [
            "Chia bài toán lớn thành các bài toán con,",
            "giải mỗi bài toán con ĐÚNG MỘT LẦN,",
            "ghi kết quả vào bảng rồi ghép lại.",
        ], width=7.4, size=30)
        fit_stack(cover, quote, idea, buff=0.7, max_scale=1.2)
        with self.voice("Chào các em! Hôm nay chúng ta bắt đầu Chương 1: Nền tảng quy hoạch động."):
            self.play(FadeIn(chap, shift=DOWN * 0.3), Write(title), run_time=1.8)
            self.play(FadeIn(sub), GrowFromCenter(bar), run_time=0.8)
        with self.voice("Có một câu nói: Người không nhớ quá khứ sẽ phải sống lại nó. "
                        "Một chương trình cũng vậy."):
            self.play(FadeIn(quote, shift=UP * 0.2), run_time=1.2)
        counter = VGroup(T("f(2) được tính lại:", size=32, color=MUTED), TB("×1", size=44, color=BAD))
        counter.arrange(RIGHT, buff=0.3).move_to(idea).align_to(idea, LEFT)
        with self.voice("Nếu không ghi lại những gì đã tính, nó sẽ giải đi giải lại cùng một bài toán con, "
                        "hàng tỉ lần."):
            self.play(FadeIn(counter), run_time=0.5)
            for k in ["×10", "×1 000", "×1 000 000", "×1 000 000 000"]:
                new = TB(k, size=44, color=BAD).next_to(counter[0], RIGHT, buff=0.3)
                self.play(Transform(counter[1], new), run_time=0.45)
        with self.voice("Quy hoạch động là nghệ thuật chia bài toán lớn thành các bài toán con, "
                        "giải mỗi bài toán con đúng một lần, ghi kết quả vào bảng, rồi ghép chúng lại."):
            self.play(FadeOut(counter), FadeIn(idea, shift=UP * 0.3), run_time=1.0)

        self.clear_body()
        heading = TB("TRONG CHƯƠNG NÀY", size=42, color=ACCENT)
        items = [
            ("Bài 1", "Từ đệ quy đến bảng phương án", "Quy hoạch động là gì?"),
            ("Bài 2", "Quy hoạch động trên dãy", "“Kết thúc tại i” và “chọn hay bỏ”"),
            ("Bài 3", "Quy hoạch động trên lưới", "và truy vết đường đi"),
        ]
        cards = VGroup()
        for tag, ttl, sub_ in items:
            pill = RoundedRectangle(width=1.4, height=0.7, corner_radius=0.35, fill_color=ACCENT,
                                    fill_opacity=1, stroke_width=0)
            left = TB(tag, size=30, color=BG).move_to(pill)
            txt = VGroup(TB(ttl, size=30), T(sub_, size=24, color=MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            row = VGroup(VGroup(pill, left), txt).arrange(RIGHT, buff=0.3)
            c = panel(row, width=7.5, pad=0.28)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.28)
            cards.add(c)
        cards.arrange(DOWN, buff=0.35)
        goal = VGroup(T("Mục tiêu: biến chương trình chạy hàng giờ", size=30, color=GOOD),
                      T("thành chương trình chạy trong chớp mắt!", size=30, color=GOOD)).arrange(DOWN, buff=0.15)
        fit_stack(heading, cards, goal, buff=0.6, max_scale=1.2)
        with self.voice("Chương này gồm ba bài. Bài 1: Từ đệ quy đến bảng phương án. "
                        "Bài 2: Quy hoạch động trên dãy. Bài 3: Quy hoạch động trên lưới và truy vết."):
            self.play(FadeIn(heading), run_time=0.5)
            for c in cards:
                self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.7)
        with self.voice("Em sẽ tự tay biến một chương trình đệ quy chạy hàng giờ thành một chương trình "
                        "chạy trong chớp mắt, rồi học bốn câu hỏi giúp em giải mọi bài quy hoạch động."):
            self.play(Write(goal), run_time=1.5)
        self.clear_body()


# ----------------------------------------------------------------------------
class B1_01_KhoiDong(B1Scene):
    def construct(self):
        self.show_header("Khởi động: Nhảy đá qua suối")
        s = stream_with_stones(5, slippery=SLIP)
        bank_l = T("bờ bên này", size=22, color=MUTED).next_to(s.stones[0], DOWN, buff=0.75)
        bank_r = T("bờ bên kia", size=22, color=MUTED).next_to(s.stones[5], DOWN, buff=0.75)
        top = VGroup(s, bank_l, bank_r)
        chips = VGroup(*[panel(TB(f"+{k}", size=34, color=BG), color=ACCENT, stroke=ACCENT, pad=0.16)
                         for k in (1, 2, 3)]).arrange(RIGHT, buff=0.2)
        rule = VGroup(T("Mỗi lần nhảy tới trước", size=30), chips, T("đá", size=30)).arrange(RIGHT, buff=0.22)
        slip_note = VGroup(make_stone(3, slippery=True).scale(0.8),
                           T("Đá 3 phủ rêu: đặt chân lên là ngã!", size=30, color=BAD)).arrange(RIGHT, buff=0.3)
        path_lbl = TB("Ví dụ: 0 → 2 → 4 → 5", size=40, color=ACCENT)
        q = TB("Có bao nhiêu cách qua suối?", size=44)
        million = T("Nếu có 1 000 000 hòn đá?", size=36, color=ORANGE)
        fast = T("…vẫn tính ra trong < 0,1 giây!", size=36, color=GOOD)
        sc = fit_stack(top, rule, slip_note, path_lbl, q, million, fast, buff=0.55, max_scale=1.05)
        frog = make_frog(sc).move_to(frog_on(s.stones[0], sc))
        with self.voice("Trước mặt em là một dãy đá bắc qua suối, đánh số từ 0, là bờ bên này, "
                        "đến 5, là bờ bên kia."):
            self.play(FadeIn(s.water), run_time=0.6)
            self.play(LaggedStart(*[GrowFromCenter(st) for st in s.stones], lag_ratio=0.15), run_time=1.5)
            self.play(FadeIn(bank_l), FadeIn(bank_r), FadeIn(frog, shift=DOWN * 0.3), run_time=0.6)
        with self.voice("Mỗi lần, em nhảy tới trước một, hai, hoặc ba hòn đá."):
            self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.8)
            arcs = VGroup(*[jump_arc(s.stones[0].get_top(), s.stones[k].get_top()) for k in (1, 2, 3)])
            self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.4), run_time=1.5)
            self.play(FadeOut(arcs), run_time=0.4)
        with self.voice("Hòn đá số 3 phủ rêu rất trơn, đặt chân lên là ngã."):
            self.play(Indicate(s.stones[3], color=BAD, scale_factor=1.3), FadeIn(slip_note), run_time=1.2)
        with self.voice("Ví dụ, đây là một cách qua suối: từ 0 nhảy tới 2, rồi tới 4, rồi tới 5."):
            self.play(FadeIn(path_lbl), run_time=0.4)
            for a, b in [(0, 2), (2, 4), (4, 5)]:
                arc = jump_arc(s.stones[a].get_top(), s.stones[b].get_top())
                self.play(Create(arc), frog_hop(frog, s.stones[b], sc), run_time=0.7)
        with self.voice("Câu hỏi: có bao nhiêu cách qua suối? Em hãy thử liệt kê trước khi xem tiếp nhé."):
            self.play(Write(q), run_time=1.2)
            self.play(Indicate(q, color=ACCENT), run_time=1.0)
        with self.voice("Còn nếu dãy có một triệu hòn đá thì sao? Liệt kê là vô vọng, "
                        "vì số cách còn lớn hơn số nguyên tử trong vũ trụ."):
            self.play(FadeIn(million, shift=UP * 0.2), run_time=0.8)
        with self.voice("Thế nhưng cuối bài này, em sẽ tính ra con số đó, lấy dư, trong chưa đầy một phần mười giây."):
            self.play(FadeIn(fast, shift=UP * 0.2), run_time=0.8)

        self.clear_body()
        self.show_header("Bài toán NHAYDA")
        box = tag_box("BÀI TOÁN: NHAYDA", [
            "Có n + 1 hòn đá đánh số 0, 1, …, n.",
            "Đứng ở đá 0, muốn tới đá n.",
            "Mỗi bước: từ đá i tới i+1, i+2 hoặc i+3.",
            "Có m đá trơn, không được đặt chân lên.",
            "Đếm số cách đi, lấy dư cho 10⁹ + 7.",
        ], width=7.4, size=30)
        lim = T("Giới hạn: 1 ≤ n ≤ 10⁶", size=34, color=ORANGE)
        rows_data = [
            (TB("Vào", size=28, color=MUTED), TB("Ra", size=28, color=MUTED), TB("Giải thích", size=28, color=MUTED)),
            (M("5 1\n3", size=30), TB("5", size=38, color=ACCENT), T("Đá 3 trơn", size=30)),
            (M("4 0", size=30), TB("7", size=38, color=ACCENT), T("Không có đá trơn", size=30)),
        ]
        table = VGroup()
        for k, row in enumerate(rows_data):
            for x, m in zip([-2.6, -1.1, 1.3], row):
                m.move_to([x, -k * 1.15, 0])
            table.add(VGroup(*row))
        fit_stack(box, lim, table, buff=0.6, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán NHAYDA. Có n cộng 1 hòn đá đánh số từ 0 đến n. "
                        "Mỗi bước nhảy từ đá i tới đá i cộng 1, i cộng 2, hoặc i cộng 3."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Có m hòn đá trơn không được đặt chân lên. Hãy đếm số cách đi từ đá 0 tới đá n, "
                        "lấy dư cho mười mũ chín cộng bảy. Giới hạn: n lên tới một triệu."):
            self.play(FadeIn(lim), run_time=0.6)
        with self.voice("Hai ví dụ: n bằng 5 với đá 3 trơn thì có 5 cách. "
                        "n bằng 4, không có đá trơn, thì có 7 cách."):
            self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.2) for r in table], lag_ratio=0.5), run_time=2.0)
        self.clear_body()


# ----------------------------------------------------------------------------
WAYS_TO_5 = [  # xếp theo hòn đá cuối trước đích
    (4, [0, 1, 4, 5]), (4, [0, 1, 2, 4, 5]), (4, [0, 2, 4, 5]),
    (2, [0, 1, 2, 5]), (2, [0, 2, 5]),
]


def mini_path(path, slippery=SLIP, highlight=None, w=0.52, n=5):
    """Một dòng ô nhỏ 0..n, tô các ô trên đường đi và vẽ cung nhảy."""
    cells = VGroup()
    for i in range(n + 1):
        fill = PANEL_2
        if i in slippery:
            fill = "#7F1D1D"
        if i in path:
            fill = BLUEC
        if highlight is not None and i == highlight:
            fill = ACCENT
        cells.add(cell(i, w=w, h=w, fill=fill, size=22, color=BG if (i in path) else INK, sw=1.5))
    cells.arrange(RIGHT, buff=0.12)
    arcs = VGroup()
    for a, b in zip(path, path[1:]):
        arcs.add(ArcBetweenPoints(cells[a].get_top(), cells[b].get_top(), angle=-PI * 0.6, color=INK,
                                  stroke_width=2.5))
    return VGroup(cells, arcs)


class B1_02_LietKe(B1Scene):
    def construct(self):
        self.show_header("1. Ý tưởng ngây thơ: Liệt kê mọi cách")
        idea = wrap_lines(["• Thử nhảy 1, 2, 3 bước", "• Gặp đá trơn / vượt quá n → bỏ",
                           "• Tới đá n → đếm thêm 1 cách"], size=34)
        fit_stack(idea, max_scale=1.2)
        with self.voice("Cách tự nhiên nhất là thử mọi khả năng: từ đá đang đứng, thử nhảy một, hai, ba bước. "
                        "Gặp đá trơn hoặc vượt quá đá n thì bỏ. Tới được đá n thì đếm thêm một cách."):
            for l in idea:
                self.play(FadeIn(l, shift=RIGHT * 0.2), run_time=0.6)

        lines = VGroup()
        for last, p in WAYS_TO_5:
            r = mini_path(p, highlight=last)
            l = M(" → ".join(map(str, p)), size=24)
            lines.add(VGroup(r, l).arrange(RIGHT, buff=0.35))
        g4 = VGroup(*lines[:3]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        g2 = VGroup(*lines[3:]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        t4 = TB("Đứng ở đá 4 rồi nhảy lên 5: 3 cách", size=26, color=ACCENT)
        t3 = TB("Đứng ở đá 3: 0 cách (đá trơn)", size=26, color=BAD)
        t2 = TB("Đứng ở đá 2 rồi nhảy lên 5: 2 cách", size=26, color=GOOD)
        block = VGroup(t4, g4, t3, t2, g2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        block[2].shift(DOWN * 0.15)
        block[3:].shift(DOWN * 0.3)
        fit_stack(block, max_scale=1.35)
        b4 = SurroundingRectangle(g4, color=ACCENT, buff=0.12, corner_radius=0.12)
        b2 = SurroundingRectangle(g2, color=GOOD, buff=0.12, corner_radius=0.12)
        with self.voice("Với ví dụ thứ nhất, ta liệt kê được đúng năm cách. Để không sót, "
                        "ta xếp chúng theo hòn đá đứng ngay trước khi nhảy lên đá 5, tô màu vàng."):
            self.play(FadeOut(idea), run_time=0.4)
            self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.3) for l in lines], lag_ratio=0.35), run_time=2.5)
        with self.voice("Ba cách đầu kết thúc bằng bước nhảy từ 4 sang 5. Hai cách sau kết thúc bằng bước nhảy từ 2 sang 5. "
                        "Không có cách nào đi qua đá 3, vì đá 3 trơn."):
            self.play(Create(b4), FadeIn(t4), run_time=0.9)
            self.play(Create(b2), FadeIn(t2), run_time=0.9)
            self.play(FadeIn(t3), run_time=0.6)

        self.clear_body()
        self.show_header("Quan sát vàng: Nhìn vào bước nhảy cuối")
        s = stream_with_stones(5, slippery=SLIP)
        eq1 = T("cách tới 5  =", size=32)
        eq2 = VGroup(T("cách tới 4", size=32, color=ACCENT), T("+", size=32), T("cách tới 3", size=32, color=BAD),
                     T("+", size=32), T("cách tới 2", size=32, color=GOOD)).arrange(RIGHT, buff=0.15)
        nums = VGroup(TB("5", size=56), TB("=", size=56), TB("3", size=56, color=ACCENT), TB("+", size=56),
                      TB("0", size=56, color=BAD), TB("+", size=56), TB("2", size=56, color=GOOD)).arrange(RIGHT, buff=0.3)
        box = tag_box("CÔNG THỨC TRUY HỒI", [
            "f(i) = số cách đi từ đá 0 tới đá i",
            "",
            "f(i) = f(i−1) + f(i−2) + f(i−3)",
            "",
            "f(0) = 1  (đứng yên ở đá 0 là một cách)",
            "f(i) = 0 nếu i < 0",
            "f(i) = 0 nếu đá i trơn",
        ], width=7.4, size=30)
        box[3][2].set_color(ACCENT)
        fit_stack(s, VGroup(eq1, eq2).arrange(DOWN, buff=0.2), nums, box, buff=0.5, max_scale=1.1)
        self.play(FadeIn(s), run_time=0.6)
        with self.voice("Đây là quan sát quan trọng nhất của cả bài. Mọi cách tới đá 5 đều phải đặt chân lần cuối "
                        "lên đá 4, đá 3, hoặc đá 2, vì mỗi bước nhảy tối đa ba đá."):
            arcs = VGroup(*[jump_arc(s.stones[k].get_top(), s.stones[5].get_top(),
                                     color={4: ACCENT, 3: BAD, 2: GOOD}[k]) for k in (4, 3, 2)])
            self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.4), run_time=2.0)
        with self.voice("Bỏ bước cuối đi, ba cách đầu trở thành đúng tất cả các cách tới đá 4, "
                        "không thừa không thiếu. Hai cách sau trở thành tất cả các cách tới đá 2."):
            self.play(FadeIn(eq1), FadeIn(eq2), run_time=1.0)
        with self.voice("Vậy số cách tới đá 5 bằng 3 cộng 0 cộng 2, bằng 5. "
                        "Bài toán lớn được ghép từ ba bài toán cùng dạng nhưng nhỏ hơn!"):
            self.play(LaggedStart(*[FadeIn(n_, shift=UP * 0.2) for n_ in nums], lag_ratio=0.15), run_time=1.6)
            self.play(Circumscribe(nums, color=ACCENT), run_time=1.2)
        with self.voice("Tổng quát: gọi f của i là số cách đi từ đá 0 tới đá i. Xét bước nhảy cuối cùng, "
                        "ta có công thức truy hồi: f của i bằng f của i trừ 1, cộng f của i trừ 2, cộng f của i trừ 3."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
            self.play(Indicate(box[3][2], color=ACCENT, scale_factor=1.08), run_time=1.0)
        with self.voice("Kèm theo các quy ước: f của 0 bằng 1, vì đứng yên ở đá 0 cũng là một cách. "
                        "f của chỉ số âm bằng 0, và f tại đá trơn cũng bằng 0."):
            self.play(Circumscribe(VGroup(box[3][4], box[3][5], box[3][6]), color=GOOD), run_time=1.5)
        self.clear_body()


# ----------------------------------------------------------------------------
NAIVE_CODE = """
long long countWays(int stone) {
    if (stone < 0) return 0;
    if (isSlippery[stone]) return 0;
    if (stone == 0) return 1;
    long long a = countWays(stone - 1);
    long long b = countWays(stone - 2);
    long long c = countWays(stone - 3);
    return a + b + c;
}
"""


def line_box(code, i, color=ACCENT):
    line = code.code_lines[i]
    r = Rectangle(width=code.background.width - 0.1, height=line.height + 0.12, stroke_width=0,
                  fill_color=color, fill_opacity=0.25)
    r.move_to([code.background.get_center()[0], line.get_center()[1], 0])
    return r


class B1_03_DeQuy(B1Scene):
    def construct(self):
        self.show_header("Cài đặt ngây thơ: Đệ quy trực tiếp")
        code = code_block(NAIVE_CODE, size=24)
        ok = VGroup(T("countWays(5) → 5 ✓", size=30, color=GOOD), T("n = 4 → 7 ✓", size=30, color=GOOD))
        ok.arrange(RIGHT, buff=0.6)
        qm = TB("Vậy vấn đề nằm ở đâu?", size=42, color=ORANGE)
        fit_stack(code, ok, qm, buff=0.6)
        with self.voice("Công thức trên có thể chép gần như nguyên văn thành một hàm đệ quy."):
            self.play(FadeIn(code, shift=UP * 0.3), run_time=1.2)
        hl = line_box(code, 1, BAD)
        with self.voice("Ba dòng đầu là trường hợp cơ sở: chỉ số âm trả về 0, đá trơn trả về 0, đá 0 trả về 1."):
            self.play(FadeIn(hl), run_time=0.4)
            for i in (2, 3):
                self.play(Transform(hl, line_box(code, i, BAD if i < 3 else GOOD)), run_time=0.6)
        with self.voice("Ba dòng tiếp theo là ba lời gọi đệ quy, đúng như công thức: f của i trừ 1, i trừ 2, i trừ 3."):
            for i in (4, 5, 6):
                self.play(Transform(hl, line_box(code, i, ACCENT)), run_time=0.6)
        with self.voice("Hàm chạy đúng: với ví dụ thứ nhất trả về 5, ví dụ thứ hai trả về 7. Vậy vấn đề nằm ở đâu?"):
            self.play(Transform(hl, line_box(code, 7, GOOD)), run_time=0.5)
            self.play(FadeIn(ok), run_time=0.6)
            self.play(Write(qm), run_time=0.8)

        self.clear_body()
        cnt = tag_box("ĐẾM TỪNG BƯỚC", [
            "C(i) = số lời gọi hàm khi tính f(i)",
            "C(i) = 1 + C(i−1) + C(i−2) + C(i−3)",
            "i tăng 1  ⇒  C(i) tăng ≈ 1,84 lần",
            "⇒  độ phức tạp HÀM MŨ  O(1,84ⁿ)",
        ], accent=ORANGE, width=7.4, size=30)
        data = [(10, 979, "979"), (20, 433993, "4,3·10⁵"), (30, 192299281, "1,9·10⁸"),
                (40, 85206376417, "8,5·10¹⁰")]
        max_h = 4.0
        bars = VGroup()
        for k, (n_, c, lab) in enumerate(data):
            h = max_h * math.log10(c) / math.log10(data[-1][1])
            bar = Rectangle(width=1.1, height=h, fill_color=ORANGE, fill_opacity=0.9, stroke_width=0)
            bar.move_to([-2.7 + k * 1.8, h / 2, 0])
            nl = T(f"n = {n_}", size=26, color=MUTED).next_to(bar, DOWN, buff=0.15)
            vl = TB(lab, size=28).next_to(bar, UP, buff=0.12)
            bars.add(VGroup(bar, nl, vl))
        axis = Line([-3.6, 0, 0], [3.6, 0, 0], color=MUTED, stroke_width=2)
        cap = T("số lời gọi (thang logarit)", size=24, color=MUTED).move_to([-1.5, max_h + 0.3, 0])
        clock = TB("≈ 15 phút!", size=36, color=BAD).move_to([-1.6, max_h - 0.5, 0])
        chart = VGroup(axis, bars, cap, clock)
        fit_stack(cnt, chart, buff=0.8, max_scale=1.15)
        with self.voice("Hãy đếm số lời gọi hàm. Gọi C của i là số lời gọi khi tính f của i. "
                        "Lời gọi f của i sinh thêm ba lời gọi con, nên C của i bằng 1 cộng C của i trừ 1, "
                        "cộng C của i trừ 2, cộng C của i trừ 3."):
            self.play(FadeIn(cnt[0:3]), FadeIn(cnt[3][0]), run_time=0.8)
            self.play(FadeIn(cnt[3][1]), run_time=0.6)
        with self.voice("Dãy này tăng giống dãy Tribonacci: mỗi khi i tăng 1, số lời gọi tăng khoảng 1 phẩy 84 lần. "
                        "Đó là độ phức tạp hàm mũ."):
            self.play(FadeIn(cnt[3][2]), run_time=0.6)
            self.play(FadeIn(cnt[3][3]), run_time=0.6)
        with self.voice("Đo thực tế: n bằng 20 cần khoảng bốn trăm ba mươi nghìn lời gọi. "
                        "n bằng 30 cần gần hai trăm triệu lời gọi, đã vượt một giây."):
            self.play(Create(axis), FadeIn(cap), run_time=0.5)
            for b in bars[:3]:
                self.play(GrowFromEdge(b[0], DOWN), FadeIn(b[1]), FadeIn(b[2]), run_time=0.7)
        with self.voice("n bằng 40 cần tám mươi lăm tỉ lời gọi, tức là khoảng mười lăm phút!"):
            self.play(GrowFromEdge(bars[3][0], DOWN), FadeIn(bars[3][1]), FadeIn(bars[3][2]), run_time=0.9)
            self.play(FadeIn(clock, scale=1.4), run_time=0.6)

        self.clear_body()
        stuck = tag_box("BẾ TẮC", [
            "Với n = 10⁶, chương trình đệ quy",
            "sẽ không bao giờ chạy xong.",
            "",
            "Nhưng chỉ có n + 1 giá trị khác nhau:",
            "f(0), f(1), …, f(n).",
            "",
            "Máy tính đã làm gì với",
            "hàng tỉ lời gọi còn lại?",
        ], accent=BAD, width=7.4, size=32)
        fit_stack(stuck, max_scale=1.2)
        with self.voice("Bế tắc! Với n bằng một triệu, chương trình đệ quy sẽ không bao giờ chạy xong."):
            self.play(FadeIn(stuck[0:3]), FadeIn(stuck[3][0:2]), run_time=1.0)
        with self.voice("Thế nhưng nhìn lại: chỉ có n cộng 1 đại lượng khác nhau là f của 0, f của 1, cho tới f của n. "
                        "Vậy máy tính đã làm gì với hàng tỉ lời gọi còn lại?"):
            self.play(FadeIn(stuck[3][2:5]), run_time=1.0)
            self.play(FadeIn(stuck[3][5:]), run_time=1.0)
            self.play(Indicate(stuck[3][6:], color=BAD), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
def build_call_tree(n=5, slippery=SLIP):
    """Danh sách nút (id, v, depth, parent, children, x) theo thứ tự DFS, bỏ lời gọi chỉ số âm."""
    nodes = []

    def rec(v, depth, parent):
        nid = len(nodes)
        nodes.append({"id": nid, "v": v, "depth": depth, "parent": parent, "children": []})
        if parent is not None:
            nodes[parent]["children"].append(nid)
        if v == 0 or v in slippery:
            return
        for d in (1, 2, 3):
            if v - d >= 0:
                rec(v - d, depth + 1, nid)

    rec(n, 0, None)
    leaf_x = [0]

    def place(nid):
        ch = nodes[nid]["children"]
        if not ch:
            nodes[nid]["x"] = leaf_x[0]
            leaf_x[0] += 1
        else:
            for c in ch:
                place(c)
            nodes[nid]["x"] = sum(nodes[c]["x"] for c in ch) / len(ch)

    place(0)
    return nodes, leaf_x[0]


class B1_04_CayLoiGoi(B1Scene):
    def construct(self):
        self.show_header("2. Phá bế tắc — Bước 1: Vẽ cây lời gọi")
        nodes, leaves = build_call_tree()
        top_y, dy = 4.7, 1.3
        dx = 7.2 / max(leaves - 1, 1)
        x0 = CENTER_X - 3.6
        R = 0.42
        mobs, edge_of = {}, {}
        for nd in nodes:
            pos = np.array([x0 + nd["x"] * dx, top_y - nd["depth"] * dy, 0])
            slip = nd["v"] in SLIP
            circ = Circle(radius=R, fill_color="#7F1D1D" if slip else PANEL_2, fill_opacity=1,
                          stroke_color=BAD if slip else BLUEC, stroke_width=3).move_to(pos)
            mobs[nd["id"]] = VGroup(circ, TB(f"f({nd['v']})", size=26).move_to(pos))
        for nd in nodes:
            if nd["parent"] is not None:
                edge_of[nd["id"]] = Line(mobs[nd["parent"]][0].get_center(), mobs[nd["id"]][0].get_center(),
                                         buff=R, color=MUTED, stroke_width=2.5)

        def subtree(nid):
            out = [nid]
            for c in nodes[nid]["children"]:
                out += subtree(c)
            return out

        with self.voice("Mỗi lời gọi f của i sinh ra các lời gọi con f của i trừ 1, i trừ 2, i trừ 3. "
                        "Hãy vẽ hết ra cho ví dụ n bằng 5, đá 3 trơn, bỏ qua các lời gọi có chỉ số âm."):
            by_depth = {}
            for nd in nodes:
                by_depth.setdefault(nd["depth"], []).append(nd["id"])
            for d in sorted(by_depth):
                anims = []
                for nid in by_depth[d]:
                    if nid in edge_of:
                        anims.append(Create(edge_of[nid]))
                    anims.append(GrowFromCenter(mobs[nid]))
                self.play(*anims, run_time=0.8)

        counts = {}
        for nd in nodes:
            counts.setdefault(nd["v"], []).append(nd["id"])
        specs = [(2, ACCENT, "f(2) bị tính 2 lần", "Chỉ với 5 hòn đá mà f của 2 đã bị tính hai lần."),
                 (1, ORANGE, "f(1) bị tính 3 lần", "f của 1 bị tính ba lần."),
                 (0, PURPLE, "f(0) bị gọi 5 lần", "Còn f của 0 bị gọi tới năm lần.")]
        rows = VGroup(*[TB(t, size=36, color=c) for _, c, t, _ in specs]).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        rows.move_to([CENTER_X, -2.7, 0])
        for (v, col, _, sent), row in zip(specs, rows):
            with self.voice(sent):
                self.play(*[mobs[i][0].animate.set_fill(col, 0.9) for i in counts[v]],
                          *[mobs[i][1].animate.set_color(BG) for i in counts[v]], run_time=0.7)
                self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)

        boxes = VGroup(*[SurroundingRectangle(VGroup(*[mobs[i] for i in subtree(nid)]), color=ACCENT, buff=0.1,
                                              corner_radius=0.2, stroke_width=5) for nid in counts[2]])
        with self.voice("Quan trọng hơn: mỗi lần tính lại f của 2 là một lần dựng lại nguyên cả cây con bên dưới nó. "
                        "Với n lớn, các cây con trùng nhau chồng lên nhau theo cấp số nhân."):
            self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.5), run_time=1.6)
            self.play(Indicate(boxes, color=ACCENT), run_time=1.0)

        sign = tag_box("DẤU HIỆU: BÀI TOÁN CON GỐI NHAU", [
            "Cùng một bài toán con xuất hiện",
            "ở nhiều nhánh khác nhau.",
            "Số bài toán con khác nhau thì ít (n + 1),",
            "số lần gặp lại chúng thì khổng lồ.",
        ], accent=ACCENT, width=7.5, size=28)
        sign.move_to([CENTER_X, -2.75, 0])
        with self.voice("Đây là dấu hiệu nhận biết số một của quy hoạch động: bài toán con gối nhau. "
                        "Số bài toán con khác nhau thì ít, nhưng số lần gặp lại chúng thì khổng lồ."):
            self.play(FadeOut(rows), FadeIn(sign, shift=UP * 0.3), run_time=1.0)

        # ---- Bước 2: đệ quy có nhớ, chạy DFS trên chính cây này
        self.play(FadeOut(sign), FadeOut(boxes), run_time=0.5)
        self.show_header("Bước 2: Nhớ lại những gì đã tính")
        self.play(*[mobs[nd["id"]][0].animate.set_fill("#7F1D1D" if nd["v"] in SLIP else PANEL_2, 1)
                    for nd in nodes],
                  *[mobs[nd["id"]][1].animate.set_color(INK) for nd in nodes], run_time=0.6)
        memo = array_row(["-1"] * 6, w=1.0, h=0.9, size=32, label="memo")
        memo.move_to([CENTER_X + 0.3, -2.45, 0])
        note = T("−1 = “chưa tính”", size=28, color=MUTED).next_to(memo, DOWN, buff=0.3)
        with self.voice("Ý tưởng rất đời thường: tính xong f của i thì ghi vào sổ, gọi là mảng memo. "
                        "Lần sau cần f của i, ta tra sổ thay vì tính lại. Giá trị trừ 1 nghĩa là chưa tính."):
            self.play(FadeIn(memo), FadeIn(note), run_time=1.0)

        memo_val, visited, events = {}, set(), []

        def dfs(nid):
            v = nodes[nid]["v"]
            visited.add(nid)
            if v in SLIP:
                events.append(("slip", nid))
                return 0
            if v == 0:
                events.append(("base", nid))
                return 1
            if v in memo_val:
                events.append(("hit", nid))
                return memo_val[v]
            events.append(("enter", nid))
            total = sum(dfs(c) for c in nodes[nid]["children"])
            memo_val[v] = total
            events.append(("store", nid, total))
            return total

        dfs(0)

        def play_event(ev, rt=0.45):
            kind, nid = ev[0], ev[1]
            if kind == "store":
                c = memo.cells[nodes[nid]["v"]]
                self.play(c[0].animate.set_fill(GOOD, 1), Transform(c[1], set_cell_value(c, ev[2], color=BG)),
                          mobs[nid][0].animate.set_fill(GOOD, 0.9), run_time=rt + 0.1)
            elif kind == "hit":
                sub = [i for i in subtree(nid) if i != nid]
                self.play(mobs[nid][0].animate.set_fill(BLUEC, 1),
                          Indicate(memo.cells[nodes[nid]["v"]], color=BLUEC), run_time=rt + 0.2)
                if sub:
                    self.play(*[mobs[i].animate.set_opacity(0.12) for i in sub],
                              *[edge_of[i].animate.set_opacity(0.12) for i in sub], run_time=0.6)
            else:
                self.play(mobs[nid][0].animate.set_stroke(BAD if kind == "slip" else ACCENT, 7), run_time=rt)

        k = 0
        with self.voice("Bây giờ chạy lại hàm với sổ ghi nhớ. Theo dõi thứ tự gọi: f của 5 gọi f của 4, "
                        "f của 4 gọi f của 3, là đá trơn, trả về 0."):
            for ev in events[:3]:
                play_event(ev)
            k = 3
        with self.voice("Tiếp tục xuống f của 2, f của 1, f của 0. Tính xong f của 1 bằng 1, ghi vào sổ. "
                        "Tính xong f của 2 bằng 2, ghi vào sổ."):
            while events[k][0] != "hit":
                play_event(events[k])
                k += 1
        with self.voice("Đến lượt f của 4 cần f của 1: sổ đã có! Tra sổ ngay, không cần gọi xuống nữa. "
                        "Cả nhánh con bên dưới bị cắt bỏ."):
            play_event(events[k])
            k += 1
        with self.voice("f của 4 bằng 0 cộng 2 cộng 1, bằng 3, ghi vào sổ. Quay về f của 5: f của 3 trơn, "
                        "còn f của 2 lại có sẵn trong sổ. Cây con thứ hai của f của 2 không cần dựng lại!"):
            while k < len(events):
                play_event(events[k], rt=0.35)
                k += 1
        res = TB("f(5) = 5 — tiết kiệm được các nút mờ!", size=32, color=GOOD).move_to(note)
        with self.voice("Kết quả f của 5 bằng 5, và những nút mờ đi là những lời gọi đã được tiết kiệm."):
            unvisited = [nd["id"] for nd in nodes if nd["id"] not in visited]
            if unvisited:
                self.play(*[mobs[i].animate.set_opacity(0.12) for i in unvisited],
                          *[edge_of[i].animate.set_opacity(0.12) for i in unvisited if i in edge_of], run_time=0.8)
            self.play(ReplacementTransform(note, res), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
MEMO_CODE = """
vector<long long> memo;   // -1 = chưa tính
long long countWays(int stone) {
    if (stone < 0) return 0;
    if (isSlippery[stone]) return 0;
    if (stone == 0) return 1;
    if (memo[stone] != -1) return memo[stone];
    long long a = countWays(stone - 1);
    long long b = countWays(stone - 2);
    long long c = countWays(stone - 3);
    memo[stone] = (a + b + c) % MOD;
    return memo[stone];
}
"""


class B1_05_Memo(B1Scene):
    def construct(self):
        self.show_header("Bước 2: Đệ quy có nhớ (memoization)")
        code = code_block(MEMO_CODE, size=22)
        cmp = VGroup(
            VGroup(T("Đệ quy ngây thơ", size=28, color=MUTED), TB("O(1,84ⁿ)", size=44, color=BAD)).arrange(DOWN),
            TB("→", size=60, color=ACCENT),
            VGroup(T("Đệ quy có nhớ", size=28, color=MUTED), TB("O(n)", size=44, color=GOOD)).arrange(DOWN),
        ).arrange(RIGHT, buff=0.6)
        n40 = VGroup(T("n = 40:", size=30), TB("85 tỉ", size=36, color=BAD), T("lời gọi →", size=30),
                     TB("≈ 120", size=36, color=GOOD)).arrange(RIGHT, buff=0.2)
        fit_stack(code, cmp, n40, buff=0.6)
        with self.voice("Đây là code đệ quy có nhớ. So với bản ngây thơ, chỉ thêm hai dòng."):
            self.play(FadeIn(code, shift=UP * 0.3), run_time=1.0)
        hl = line_box(code, 5, BLUEC)
        with self.voice("Dòng thứ nhất: nếu sổ đã có giá trị thì trả về ngay."):
            self.play(FadeIn(hl), run_time=0.5)
        with self.voice("Dòng thứ hai: tính xong thì ghi vào sổ, nhớ lấy dư cho MOD."):
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.5)
        with self.voice("Mỗi giá trị f của i giờ chỉ được tính thật đúng một lần. Có n cộng 1 giá trị, mỗi giá trị "
                        "tính bằng ba lời gọi con, nên tổng số lời gọi chỉ khoảng 3 n. "
                        "Độ phức tạp giảm từ hàm mũ xuống O của n."):
            self.play(FadeOut(hl), FadeIn(cmp), run_time=1.0)
            self.play(Indicate(cmp[2], color=GOOD), run_time=1.0)
        with self.voice("Với n bằng 40, số lời gọi giảm từ tám mươi lăm tỉ xuống còn khoảng một trăm hai mươi!"):
            self.play(FadeIn(n40, shift=UP * 0.2), run_time=1.0)

        self.clear_body()
        self.show_header("Nhưng… coi chừng tràn ngăn xếp!")
        labels = ["f(1 000 000)", "f(999 999)", "f(999 998)", "f(999 997)", "f(999 996)", "…", "…"]
        frames = VGroup()
        for lab in labels:
            r = RoundedRectangle(width=3.2, height=0.8, corner_radius=0.12, fill_color=PANEL_2, fill_opacity=1,
                                 stroke_color=BLUEC, stroke_width=2)
            frames.add(VGroup(r, M(lab, size=26).move_to(r)))
        frames.arrange(UP, buff=0.15)
        stack_area = SurroundingRectangle(frames, color=MUTED, buff=0.2, stroke_width=3)
        cap = T("ngăn xếp: chỉ vài MB", size=26, color=MUTED).next_to(stack_area, UP, buff=0.15)
        side = wrap_lines(["Gọi f(10⁶)", "→ f(999 999)", "→ f(999 998)", "→ …", "",
                           "Chồng 1 000 000", "tầng trước khi", "chạm f(0)!"], size=30)
        left = VGroup(cap, stack_area, frames)
        top = VGroup(left, side).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        boom = TB("STACK OVERFLOW!", size=54, color=BAD)
        fit_stack(top, boom, buff=0.6)
        frames_order = list(frames)  # từ dưới lên
        with self.voice("Tuy nhiên, khi gọi f của một triệu, hàm sẽ gọi f của chín trăm chín mươi chín nghìn chín trăm "
                        "chín mươi chín, rồi tiếp tục chồng lên nhau một triệu tầng trước khi chạm tới f của 0."):
            self.play(Create(stack_area), FadeIn(cap), run_time=0.6)
            for fr in frames_order:
                self.play(FadeIn(fr, shift=DOWN * 0.4), run_time=0.3)
            self.play(FadeIn(side), run_time=0.6)
        with self.voice("Mỗi tầng chiếm một phần bộ nhớ ngăn xếp, mà ngăn xếp trên nhiều máy chấm chỉ vài megabyte. "
                        "Kết quả: chương trình bị lỗi tràn ngăn xếp ở test lớn."):
            self.play(stack_area.animate.set_stroke(BAD, 6), *[fr[0].animate.set_fill("#7F1D1D").set_stroke(BAD) for fr in frames],
                      run_time=0.6)
            self.play(Wiggle(frames), FadeIn(boom, scale=1.5), run_time=1.2)
        self.clear_body()


# ----------------------------------------------------------------------------
BOTTOM_UP_CODE = """
ways[0] = 1;
for (int stone = 1; stone <= stoneCount; stone++) {
    if (isSlippery[stone]) continue;
    for (int jump = 1; jump <= 3; jump++)
        if (stone - jump >= 0)
            ways[stone] = (ways[stone]
                         + ways[stone - jump]) % MOD;
}
"""


def stream_and_row(n=5, slippery=SLIP, label="f", spacing=1.22):
    s = stream_with_stones(n, slippery=slippery, spacing=spacing)
    row = array_row([""] * (n + 1), w=1.0, h=0.9, size=36, label=label, show_index=False)
    for k, c in enumerate(row.cells):
        c.move_to([s.stones[k].get_center()[0], s.get_bottom()[1] - 0.75, 0])
    row.lab.next_to(row.cells, LEFT, buff=0.15)
    return VGroup(s, row), s, row


class B1_06_DienBang(B1Scene):
    def construct(self):
        self.show_header("Bước 3: Bỏ đệ quy — Điền bảng từ dưới lên")
        obs = wrap_lines([
            "Tính f(i) chỉ cần f(i−1), f(i−2), f(i−3):",
            "toàn là ô có chỉ số NHỎ HƠN.",
            "⇒ Tính f(0), f(1), f(2), … tăng dần thì",
            "ô cần dùng chắc chắn đã có sẵn!",
        ], size=30)
        obs[2:].set_color(ACCENT)
        sr, s, row = stream_and_row()
        eq_slot = placeholder(7.0, 1.4)
        sc = fit_stack(obs, sr, eq_slot, buff=0.6, max_scale=1.15)
        with self.voice("Hãy để ý: để tính f của i, ta chỉ cần f của i trừ 1, i trừ 2, i trừ 3, "
                        "đều là những ô có chỉ số nhỏ hơn."):
            self.play(FadeIn(obs[:2]), run_time=0.8)
        with self.voice("Vậy nếu ta tính lần lượt f của 0, f của 1, f của 2, theo thứ tự tăng dần, "
                        "thì khi tới ô i, ba ô cần dùng chắc chắn đã có sẵn. Không cần đệ quy nữa!"):
            self.play(FadeIn(obs[2:]), run_time=0.8)
            self.play(FadeIn(sr), run_time=0.8)

        def put(i, val, color=ACCENT):
            c = row.cells[i]
            return [c[0].animate.set_fill(color, 1), Transform(c[1], set_cell_value(c, val, color=BG))]

        eq = None

        def show_eq(new_eq, *extra):
            nonlocal eq
            new_eq.scale(sc).move_to(eq_slot)
            if eq is None:
                eq = new_eq
                self.play(FadeIn(eq), *extra, run_time=0.8)
            else:
                self.play(Transform(eq, new_eq), *extra, run_time=0.8)

        with self.voice("Bắt đầu: f của 0 bằng 1, đứng yên ở đá 0 cũng là một cách."):
            self.play(*put(0, 1, GOOD), run_time=0.7)
        for i in range(1, 6):
            srcs = [j for j in (i - 1, i - 2, i - 3) if j >= 0]
            if i in SLIP:
                with self.voice(f"Ô số {i} là đá trơn: luôn bằng 0, bỏ qua."):
                    show_eq(TB(f"f({i}) = 0   (đá trơn)", size=34, color=BAD))
                    self.play(*put(i, 0, BAD), run_time=0.6)
                continue
            terms = " + ".join(f"f({j})" for j in srcs)
            vals = " + ".join(str(F_VALUES[j]) for j in srcs)
            new_eq = VGroup(M(f"f({i}) = {terms}", size=32),
                            M(f"     = {vals} = {F_VALUES[i]}", size=32, color=ACCENT)).arrange(DOWN, aligned_edge=LEFT,
                                                                                            buff=0.15)
            spoken_terms = ", cộng ".join(f"f của {j}" for j in srcs)
            spoken_vals = " cộng ".join(str(F_VALUES[j]) for j in srcs)
            with self.voice(f"f của {i} bằng {spoken_terms}, tức là {spoken_vals}, bằng {F_VALUES[i]}."):
                arrows = VGroup(*[CurvedArrow(row.cells[j].get_bottom() + DOWN * 0.05,
                                              row.cells[i].get_bottom() + DOWN * 0.05, angle=PI / 2.2,
                                              color=GOOD, stroke_width=4, tip_length=0.2) for j in srcs])
                show_eq(new_eq, *[row.cells[j][0].animate.set_stroke(GOOD, 6) for j in srcs], Create(arrows))
                self.play(*put(i, F_VALUES[i]), run_time=0.6)
                self.play(FadeOut(arrows), *[row.cells[j][0].animate.set_stroke(MUTED, 2) for j in srcs],
                          run_time=0.4)
        with self.voice("Ô cuối cùng f của 5 bằng 5, đúng như ta đã liệt kê!"):
            self.play(Circumscribe(row.cells[5], color=GOOD), run_time=1.0)

        name = T("Bảng ways được gọi là BẢNG PHƯƠNG ÁN", size=30, color=ACCENT)
        row_t = VGroup(row).copy()
        code = code_block(BOTTOM_UP_CODE, size=22)
        cx = VGroup(T("n lần × 3 lần =", size=32), TB("O(n)", size=44, color=GOOD)).arrange(RIGHT, buff=0.2)
        note = T("n = 10⁶: ≈ 3·10⁶ phép cộng, vài mili giây", size=28, color=MUTED)
        fit_stack(name, row_t, code, cx, note, buff=0.5)
        self.play(FadeOut(eq), FadeOut(s), FadeOut(obs), Transform(VGroup(row), row_t), run_time=0.8)
        with self.voice("Code điền bảng rất gọn: đặt ways của 0 bằng 1, rồi duyệt từng hòn đá theo thứ tự tăng dần, "
                        "bỏ qua đá trơn, cộng dồn ba ô phía trước."):
            self.play(FadeIn(code, shift=UP * 0.3), run_time=1.0)
        with self.voice("Bảng ways được gọi là bảng phương án. Vòng ngoài chạy n lần, vòng trong 3 lần, "
                        "nên độ phức tạp O của n. Với n bằng một triệu chỉ cần khoảng ba triệu phép cộng, "
                        "chạy trong vài mili giây, và không còn tầng đệ quy nào."):
            self.play(FadeIn(name), run_time=0.6)
            self.play(FadeIn(cx), run_time=0.6)
            self.play(FadeIn(note), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
SLIDE_CODE = """
long long beforeThree = 0, beforeTwo = 0, beforeOne = 1;
for (int stone = 1; stone <= stoneCount; stone++) {
    long long current = (beforeOne + beforeTwo
                         + beforeThree) % MOD;
    if (isSlippery[stone]) current = 0;
    beforeThree = beforeTwo;
    beforeTwo = beforeOne;
    beforeOne = current;
}
"""


class B1_07_TietKiem(B1Scene):
    def construct(self):
        self.show_header("Bước 4: Tiết kiệm bộ nhớ — chỉ nhớ ba ô")
        row = array_row([1, 1, 2, 0, 3, 5], w=1.05, h=0.95, size=38, label="f")
        legend = VGroup(
            VGroup(Square(0.3, color=GOOD, stroke_width=5), T("beforeThree · beforeTwo · beforeOne", size=24,
                                                              color=GOOD)).arrange(RIGHT, buff=0.2),
            VGroup(Square(0.3, color=ACCENT, stroke_width=5), T("current", size=24, color=ACCENT)).arrange(RIGHT,
                                                                                                     buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        code = code_block(SLIDE_CODE, size=20)
        mem = VGroup(T("Bộ nhớ cho bảng:", size=32), TB("O(n)", size=40, color=BAD), T("→", size=32),
                     TB("O(1)", size=40, color=GOOD)).arrange(RIGHT, buff=0.2)
        fit_stack(VGroup(row, legend).arrange(DOWN, buff=0.45), code, mem, buff=0.6)
        with self.voice("Khi tính tới ô i, các ô từ i trừ 4 trở về trước không bao giờ được dùng lại nữa."):
            self.play(FadeIn(row), run_time=0.8)
        step = row.cells[1].get_center()[0] - row.cells[0].get_center()[0]
        win = SurroundingRectangle(VGroup(*row.cells[0:3]), color=GOOD, buff=0.05, stroke_width=7)
        cur = SurroundingRectangle(row.cells[3], color=ACCENT, buff=0.05, stroke_width=7)
        with self.voice("Vậy ta chỉ cần giữ ba giá trị gần nhất trong ba biến, và trượt chúng sang phải sau mỗi bước, "
                        "giống như một cửa sổ trượt."):
            self.play(Create(win), Create(cur), FadeIn(legend), run_time=1.0)
            for _ in (1, 2):
                self.play(win.animate.shift(RIGHT * step), cur.animate.shift(RIGHT * step), run_time=0.7)
            self.play(FadeIn(code), run_time=0.8)
        with self.voice("Bộ nhớ cho bảng phương án giảm từ O của n xuống O của 1."):
            self.play(FadeIn(mem), run_time=0.8)
        with self.voice("Ở bài này cải tiến đó chưa thật cần, vì mảng đá trơn vẫn tốn O của n. Nhưng ở những bài bảng "
                        "hai chiều, kĩ thuật chỉ giữ vài hàng gần nhất có thể là ranh giới giữa được điểm và bị tràn bộ nhớ."):
            self.play(Indicate(mem, color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("Tổng kết bốn cách làm")
        heads = ["Cách làm", "Thời gian", "Bộ nhớ", "Ghi chú"]
        data = [
            ["Đệ quy ngây thơ", "O(1,84ⁿ)", "O(n) stack", "chỉ n ≤ 25"],
            ["Đệ quy có nhớ", "O(n)", "O(n)+stack", "dễ tràn stack"],
            ["Điền bảng", "O(n)", "O(n)", "nên dùng"],
            ["Ba biến trượt", "O(n)", "O(1)", "bộ nhớ eo hẹp"],
        ]
        colw = [2.5, 1.6, 1.75, 1.85]
        table = VGroup()
        for r, rowdata in enumerate([heads] + data):
            cells_ = VGroup()
            x = -sum(colw) / 2
            for cidx, (txt, w) in enumerate(zip(rowdata, colw)):
                fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
                rect = Rectangle(width=w, height=1.0, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
                rect.move_to([x + w / 2, -r * 1.0, 0])
                col = BG if r == 0 else ((BAD if r == 1 else GOOD) if cidx == 1 else INK)
                t = (TB if r == 0 or cidx == 0 else T)(txt, size=24, color=col, max_width=w - 0.15)
                cells_.add(VGroup(rect, t.move_to(rect)))
                x += w
            table.add(cells_)
        path = VGroup(*[panel(T(t, size=26), pad=0.15, color=PANEL_2, stroke=ACCENT)
                        for t in ["Đệ quy", "Có nhớ", "Điền bảng", "Trượt"]]).arrange(RIGHT, buff=0.4)
        arrows = VGroup(*[Arrow(path[k].get_right(), path[k + 1].get_left(), buff=0.03, color=ACCENT,
                                stroke_width=4, max_tip_length_to_length_ratio=0.5) for k in range(3)])
        cap = TB("Con đường nâng cấp", size=32, color=ACCENT)
        flow = VGroup(cap, VGroup(path, arrows)).arrange(DOWN, buff=0.35)
        fit_stack(table, flow, buff=0.9)
        with self.voice("Tóm lại bốn cách làm. Đệ quy ngây thơ: thời gian hàm mũ, chỉ chạy được n khoảng 25."):
            self.play(FadeIn(table[0]), FadeIn(table[1], shift=UP * 0.2), run_time=1.0)
        with self.voice("Đệ quy có nhớ: O của n, dễ viết nhưng có thể tràn ngăn xếp."):
            self.play(FadeIn(table[2], shift=UP * 0.2), run_time=0.7)
        with self.voice("Điền bảng: O của n, không đệ quy, là cách nên dùng."):
            self.play(FadeIn(table[3], shift=UP * 0.2), run_time=0.7)
            self.play(Indicate(table[3], color=GOOD, scale_factor=1.04), run_time=0.8)
        with self.voice("Ba biến trượt: thời gian O của n, bộ nhớ O của 1, dùng khi bộ nhớ eo hẹp."):
            self.play(FadeIn(table[4], shift=UP * 0.2), run_time=0.7)
        with self.voice("Hãy nhớ con đường nâng cấp này: đệ quy, đệ quy có nhớ, điền bảng, rồi tiết kiệm bộ nhớ."):
            self.play(FadeIn(cap), run_time=0.4)
            self.play(LaggedStart(*[FadeIn(p) for p in path], lag_ratio=0.3), Create(arrows), run_time=1.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B1_08_BonCauHoi(B1Scene):
    def construct(self):
        self.show_header("3. Quy hoạch động là gì?")
        dp = tag_box("QUY HOẠCH ĐỘNG", [
            "(tiếng Anh: Dynamic Programming)",
            "• Chia thành bài toán con cùng dạng, nhỏ hơn",
            "• Giải mỗi bài toán con đúng một lần",
            "• Lưu kết quả vào bảng, dùng lại khi cần",
            "⇒ Mạnh khi các bài toán con GỐI NHAU",
        ], accent=ACCENT, width=7.4, size=28)
        dp[3][0].set_color(MUTED)
        dp[3][4].set_color(ACCENT)
        pen = VGroup(TB("4 câu hỏi", size=40, color=GOOD),
                     T("viết ra giấy TRƯỚC khi code!", size=32, color=GOOD)).arrange(DOWN, buff=0.15)
        fit_stack(dp, pen, buff=0.8, max_scale=1.2)
        with self.voice("Điều em vừa làm có tên là quy hoạch động: chia bài toán thành các bài toán con cùng dạng "
                        "nhưng nhỏ hơn, giải mỗi bài toán con đúng một lần, lưu kết quả vào bảng và dùng lại khi cần."):
            self.play(FadeIn(dp, shift=UP * 0.3), run_time=1.0)
        with self.voice("Mọi lời giải quy hoạch động đều được xây từ bốn câu trả lời. Hãy tập thói quen "
                        "viết bốn câu trả lời này ra giấy trước khi viết dòng code đầu tiên."):
            self.play(Write(pen), run_time=1.2)

        qs = [
            ("1", "Trạng thái", "f(i) nghĩa là gì? Một câu rõ ràng.", "f(i) = số cách đi từ đá 0 tới đá i", BLUEC,
             "Câu một, trạng thái: f nghĩa là gì? Phải phát biểu thành một câu rõ ràng, đầy đủ. "
             "Ở đây: f của i là số cách đi từ đá 0 tới đá i."),
            ("2", "Cơ sở", "Trạng thái nhỏ nhất nào biết ngay?", "f(0)=1, f(âm)=0, f(đá trơn)=0", GOOD,
             "Câu hai, cơ sở: những trạng thái nhỏ nhất nào biết ngay đáp án mà không cần tính? "
             "Ở đây: f của 0 bằng 1, chỉ số âm và đá trơn bằng 0."),
            ("3", "Công thức chuyển", "Gợi ý: “Bước cuối cùng là gì?”", "f(i) = f(i−1) + f(i−2) + f(i−3)", ACCENT,
             "Câu ba, công thức chuyển: tính một trạng thái từ những trạng thái nhỏ hơn thế nào? "
             "Câu hỏi gợi ý tốt nhất là: bước cuối cùng là gì?"),
            ("4", "Đáp án & thứ tự tính", "Đáp án ở ô nào? Điền theo thứ tự nào?", "đáp án f(n); điền i tăng dần",
             ORANGE,
             "Câu bốn, đáp án và thứ tự tính: đáp án nằm ở ô nào, ở đây là f của n. Và điền bảng theo thứ tự nào "
             "để ô cần dùng luôn có sẵn, ở đây là i tăng dần."),
        ]
        cards = VGroup()
        for num, ttl, q, ans, col, _ in qs:
            badge = Circle(radius=0.4, fill_color=col, fill_opacity=1, stroke_width=0)
            bn = TB(num, size=36, color=BG).move_to(badge)
            txt = VGroup(TB(ttl, size=32, color=col), T(q, size=25, color=MUTED), T(ans, size=25))
            txt.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            row = VGroup(VGroup(badge, bn), txt).arrange(RIGHT, buff=0.3)
            c = panel(row, width=7.5, pad=0.24, stroke=col)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.24)
            cards.add(c)
        cards.arrange(DOWN, buff=0.28)
        pen_t = pen.copy()
        fit_stack(pen_t, cards, buff=0.5)
        self.play(FadeOut(dp), Transform(pen, pen_t), run_time=0.7)
        for c, q in zip(cards, qs):
            with self.voice(q[5]):
                self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao công thức đếm đúng?")

        def cond_card(title, l1, l2, col):
            g = VGroup(TB(title, size=36, color=col), T(l1, size=28), T(l2, size=28)).arrange(DOWN, aligned_edge=LEFT,
                                                                                                buff=0.15)
            c = panel(g, width=7.5, stroke=col)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.35)
            return c

        cond = VGroup(cond_card("✓ Không trùng", "Mỗi cách đi có đúng MỘT bước nhảy cuối", "→ rơi vào đúng một nhóm.",
                                GOOD),
                      cond_card("✓ Không sót", "Bước nhảy cuối chỉ dài 1, 2 hoặc 3", "→ cách nào cũng thuộc một nhóm.",
                                BLUEC)).arrange(DOWN, buff=0.35)
        left = VGroup(*[mini_path(p[:-1]) for _, p in WAYS_TO_5[:3]]).arrange(DOWN, buff=0.3)
        right = VGroup(*[mini_path(p) for _, p in WAYS_TO_5[:3]]).arrange(DOWN, buff=0.3)
        lr = VGroup(left, right).arrange(RIGHT, buff=1.1)
        arr = VGroup(*[Arrow(l.get_right(), r.get_left(), buff=0.1, color=ACCENT, stroke_width=5) for l, r in
                       zip(left, right)])
        lt = T("cách tới đá 4", size=26, color=MUTED).next_to(left, UP, buff=0.2)
        rt = T("cách tới 5 qua đá 4", size=26, color=MUTED).next_to(right, UP, buff=0.2)
        plus = T("ghép thêm bước nhảy 4 → 5: SONG ÁNH", size=28, color=ACCENT).next_to(lr, DOWN, buff=0.3)
        bij = VGroup(lt, rt, lr, arr, plus)
        fit_stack(cond, bij, buff=0.8, max_scale=1.2)
        with self.voice("Một công thức đếm bằng cách cộng các nhóm chỉ đúng khi hai điều kiện cùng thỏa mãn. "
                        "Thứ nhất, không trùng: mỗi cách đi có đúng một bước nhảy cuối, nên chỉ rơi vào đúng một nhóm."):
            self.play(FadeIn(cond[0], shift=UP * 0.2), run_time=0.8)
        with self.voice("Thứ hai, không sót: bước nhảy cuối chỉ có thể dài 1, 2 hoặc 3, nên cách nào cũng thuộc một nhóm."):
            self.play(FadeIn(cond[1], shift=UP * 0.2), run_time=0.8)
        with self.voice("Ngoài ra, mỗi cách tới đá i trừ d, ghép thêm bước nhảy d, luôn cho một cách hợp lệ tới đá i, "
                        "và ngược lại. Đó là một song ánh, nên nhóm thứ d có đúng f của i trừ d phần tử."):
            self.play(FadeIn(left), FadeIn(lt), run_time=0.8)
            self.play(Create(arr), FadeIn(plus), run_time=0.8)
            self.play(FadeIn(right), FadeIn(rt), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
FEES = [None, 2, 7, 3, -1, 1, 4]  # đá 1..6


def fee_stream():
    s = stream_with_stones(6, slippery=(4,), spacing=1.08)
    tags = VGroup()
    for i in range(1, 7):
        f = FEES[i]
        t = TB("trơn" if f < 0 else f"{f}đ", size=26, color=BAD if f < 0 else ACCENT)
        t.next_to(s.stones[i], UP, buff=0.6)
        tags.add(t)
    return VGroup(s, tags), s, tags


class B1_09_PhiQua(B1Scene):
    def construct(self):
        self.show_header("4. Từ đếm sang tối ưu: Bài toán PHIQUA")
        box = tag_box("BÀI TOÁN: PHIQUA", [
            "Vẫn dãy đá, mỗi bước nhảy 1, 2 hoặc 3 đá.",
            "Đặt chân lên đá i phải trả phí cᵢ",
            "(cᵢ = −1 nghĩa là đá trơn).",
            "Tìm TỔNG PHÍ NHỎ NHẤT từ đá 0 tới đá n",
            "(in −1 nếu không thể tới).",
        ], accent=BLUEC, width=7.4, size=28)
        st, s, tags = fee_stream()
        gt = VGroup(TB("Cách sai hấp dẫn: THAM LAM", size=34, color=ORANGE),
                    T("Mỗi bước nhảy tới đá rẻ nhất trong 3 đá phía trước", size=26, color=MUTED)).arrange(DOWN,
                                                                                                         buff=0.15)
        run_slot = TB("Tham lam: 2 + 3 + 1 + 4 = 10", size=32, color=ORANGE)
        best_txt = TB("Tối ưu: 3 + 4 = 7", size=32, color=GOOD)
        lesson = VGroup(T("Quyết định tốt ở hiện tại chưa chắc", size=30),
                        T("dẫn tới kết quả tốt nhất ở cuối!", size=30)).arrange(DOWN, buff=0.12)
        sc = fit_stack(box, st, gt, run_slot, best_txt, lesson, buff=0.45, max_scale=1.1)
        frog = make_frog(0.85 * sc).move_to(frog_on(s.stones[0], sc))
        with self.voice("Quy hoạch động không chỉ dùng để đếm. Hãy giữ nguyên dãy đá nhưng đổi câu hỏi. "
                        "Mỗi khi đặt chân lên đá i, em phải trả một khoản phí. Tìm tổng phí nhỏ nhất để qua suối."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Ví dụ: sáu hòn đá với phí lần lượt là 2, 7, 3, đá 4 trơn, rồi 1 và 4."):
            self.play(FadeIn(s), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.2) for t in tags], lag_ratio=0.15), FadeIn(frog),
                      run_time=1.2)
        with self.voice("Ý tưởng đầu tiên của nhiều bạn là tham lam: mỗi bước, nhảy tới hòn đá có phí rẻ nhất "
                        "trong ba hòn phía trước. Hãy thử xem."):
            self.play(FadeIn(gt), run_time=0.8)
        steps = [(0, 1, "Từ đá 0: chọn đá 1, phí 2, vì rẻ hơn 7 và 3."),
                 (1, 3, "Từ đá 1: đá 4 trơn, chọn đá 3, phí 3."),
                 (3, 5, "Từ đá 3: chọn đá 5, phí 1."),
                 (5, 6, "Từ đá 5: nhảy lên đá 6, phí 4.")]
        total, parts = 0, []
        run = TB("Tham lam: 0", size=32, color=ORANGE).scale(sc).move_to(run_slot)
        self.play(FadeIn(run), run_time=0.3)
        g_arcs = VGroup()
        for a, b, line in steps:
            total += FEES[b]
            parts.append(str(FEES[b]))
            with self.voice(line):
                arc = jump_arc(s.stones[a].get_top(), s.stones[b].get_top(), color=ORANGE)
                g_arcs.add(arc)
                self.play(Create(arc), frog_hop(frog, s.stones[b], sc), run_time=0.7)
                txt = "Tham lam: " + " + ".join(parts) + (f" = {total}" if len(parts) > 1 else "")
                self.play(Transform(run, TB(txt, size=32, color=ORANGE).scale(sc).move_to(run_slot)), run_time=0.4)
        with self.voice("Tham lam được tổng phí 10."):
            self.play(Indicate(run, color=ORANGE), run_time=0.8)
        with self.voice("Nhưng đi từ 0 nhảy thẳng tới 3, rồi từ 3 nhảy tới 6, chỉ tốn 3 cộng 4, bằng 7!"):
            self.play(g_arcs.animate.set_opacity(0.25), frog.animate.move_to(frog_on(s.stones[0], sc)), run_time=0.5)
            for a, b in [(0, 3), (3, 6)]:
                arc = jump_arc(s.stones[a].get_top(), s.stones[b].get_top(), color=GOOD, sw=8)
                self.play(Create(arc), frog_hop(frog, s.stones[b], sc), run_time=0.8)
            self.play(FadeIn(best_txt), run_time=0.5)
        with self.voice("Chính lựa chọn rẻ trước mắt buộc em phải đi thêm nhiều bước sau. Bài học: một quyết định tốt "
                        "ở hiện tại chưa chắc dẫn tới kết quả tốt nhất ở cuối. Quy hoạch động không đoán, "
                        "nó xét mọi khả năng một cách có hệ thống nhưng không lặp lại công việc."):
            self.play(FadeIn(lesson), run_time=1.0)

        self.clear_body()
        self.show_header("Bốn câu hỏi cho PHIQUA")
        lines = [
            ("1. Trạng thái", ["g(i) = tổng phí nhỏ nhất từ đá 0 tới đá i", "(bằng ∞ nếu không tới được)"], BLUEC),
            ("2. Cơ sở", ["g(0) = 0;  g(i) = ∞ nếu đá i trơn"], GOOD),
            ("3. Công thức chuyển", ["g(i) = min(g(i−1), g(i−2), g(i−3)) + cᵢ"], ACCENT),
            ("4. Đáp án", ["g(n), hoặc −1 nếu g(n) = ∞; điền i tăng dần"], ORANGE),
        ]
        rows = VGroup()
        for ttl, body, col in lines:
            rows.add(VGroup(TB(ttl, size=32, color=col), *[T(b, size=27) for b in body]).arrange(
                DOWN, aligned_edge=LEFT, buff=0.1))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        def cmp_card(t, f, d, col):
            return panel(VGroup(TB(t, size=30, color=col), M(f, size=26), T(d, size=24, color=MUTED)).arrange(
                DOWN, buff=0.12), width=3.65, stroke=col)

        cmpbox = VGroup(cmp_card("Bài ĐẾM", "f = f + f + f", "phép CỘNG", BLUEC),
                        cmp_card("Bài TỐI ƯU", "g = min(g,g,g)+c", "phép MIN", ACCENT)).arrange(RIGHT, buff=0.2)
        fit_stack(rows, cmpbox, buff=0.8, max_scale=1.2)
        spoken = [
            "Trạng thái: g của i là tổng phí nhỏ nhất để đi từ đá 0 tới đá i, bằng vô cùng nếu không tới được.",
            "Cơ sở: g của 0 bằng 0, và g bằng vô cùng tại đá trơn.",
            "Công thức: bước cuối tới đá i xuất phát từ i trừ 1, i trừ 2 hoặc i trừ 3. Lấy nhỏ nhất trong ba khả năng, "
            "rồi cộng phí của đá i.",
            "Đáp án là g của n, hoặc trừ 1 nếu bằng vô cùng. Điền i tăng dần.",
        ]
        for r, sp in zip(rows, spoken):
            with self.voice(sp):
                self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("So sánh với bài đếm: cấu trúc giống hệt, chỉ khác phép toán. Bài đếm dùng phép cộng "
                        "để gộp các nhóm, bài tối ưu dùng phép min để chọn nhóm tốt nhất."):
            self.play(FadeIn(cmpbox, shift=UP * 0.2), run_time=1.0)

        gvals = ["0", "2", "7", "3", "∞", "4", "7"]
        fees_row = array_row(["", 2, 7, 3, "−1", 1, 4], w=0.95, h=0.8, size=30, label="c")
        g_row = array_row([""] * 7, w=0.95, h=0.9, size=34, label="g", show_index=False)
        for k, c in enumerate(g_row.cells):
            c.move_to(fees_row.cells[k].get_center() + DOWN * 0.95)
        g_row.lab.next_to(g_row.cells, LEFT, buff=0.25)
        fees_row.cells[4][0].set_fill("#7F1D1D", 1)
        tables = VGroup(fees_row, g_row)
        eq_slot = placeholder(7.0, 0.8)
        cmp_t = cmpbox.copy()
        sc2 = fit_stack(cmp_t, tables, eq_slot, buff=0.7, max_scale=1.2)
        self.play(FadeOut(rows), Transform(cmpbox, cmp_t), run_time=0.6)
        self.play(FadeIn(tables), run_time=0.7)
        explain = {
            0: ("g của 0 bằng 0.", "g(0) = 0"),
            1: ("g của 1 bằng g của 0 cộng 2, bằng 2.", "g(1) = g(0) + 2 = 2"),
            2: ("g của 2 bằng min của 2 và 0, cộng 7, bằng 7.", "g(2) = min(2, 0) + 7 = 7"),
            3: ("g của 3 bằng min của 7, 2, 0, cộng 3, bằng 3.", "g(3) = min(7, 2, 0) + 3 = 3"),
            4: ("Đá 4 trơn: g của 4 bằng vô cùng.", "g(4) = ∞  (đá trơn)"),
            5: ("g của 5 bằng min của vô cùng, 3, 7, cộng 1, bằng 4.", "g(5) = min(∞, 3, 7) + 1 = 4"),
            6: ("g của 6 bằng min của 4, vô cùng, 3, cộng 4, bằng 7. Đáp án là 7!", "g(6) = min(4, ∞, 3) + 4 = 7"),
        }
        eq = None
        for i in range(7):
            sp, formula = explain[i]
            col = BAD if i == 4 else (GOOD if i == 6 else ACCENT)
            new_eq = M(formula, size=32, color=col).scale(sc2).move_to(eq_slot)
            with self.voice(sp):
                c = g_row.cells[i]
                srcs = [j for j in (i - 1, i - 2, i - 3) if j >= 0] if i not in (0, 4) else []
                hi = [g_row.cells[j][0].animate.set_stroke(GOOD, 6) for j in srcs]
                if eq is None:
                    eq = new_eq
                    self.play(FadeIn(eq), *hi, run_time=0.5)
                else:
                    self.play(Transform(eq, new_eq), *hi, run_time=0.5)
                self.play(c[0].animate.set_fill(col, 1), Transform(c[1], set_cell_value(c, gvals[i], color=BG)),
                          run_time=0.5)
                if srcs:
                    self.play(*[g_row.cells[j][0].animate.set_stroke(MUTED, 2) for j in srcs], run_time=0.3)

        self.clear_body()
        self.show_header("Vì sao lấy min là đúng?")
        s2 = stream_with_stones(6, slippery=(4,), spacing=1.08)
        jl = TB("j", size=34, color=GOOD).next_to(s2.stones[3], DOWN, buff=0.65)
        il = TB("i", size=34, color=ACCENT).next_to(s2.stones[6], DOWN, buff=0.65)
        proof = wrap_lines([
            "Đoạn đường 0 → j cũng phải là",
            "đường đi TỐT NHẤT tới j.",
            "Nếu có đường tới j rẻ hơn, thay vào",
            "rồi nhảy j → i ⇒ đường tới i rẻ hơn:",
            "MÂU THUẪN!",
        ], size=30)
        proof[4].set_color(BAD)
        key = tag_box("CẤU TRÚC CON TỐI ƯU", [
            "Lời giải tốt nhất của bài lớn chứa",
            "lời giải tốt nhất của bài con.",
            "Cấu trúc con tối ưu + bài toán con gối nhau",
            "⇒ dùng quy hoạch động cho bài tối ưu.",
        ], accent=GOOD, width=7.4, size=28)
        fit_stack(VGroup(s2, jl, il), proof, key, buff=0.6, max_scale=1.15)
        best_path = VGroup(jump_arc(s2.stones[0].get_top(), s2.stones[3].get_top(), color=GOOD, sw=8),
                           jump_arc(s2.stones[3].get_top(), s2.stones[6].get_top(), color=ACCENT, sw=8))
        with self.voice("Xét một đường đi tốt nhất tới đá i, và giả sử bước cuối nhảy từ đá j."):
            self.play(FadeIn(s2), run_time=0.6)
            self.play(Create(best_path), FadeIn(jl), FadeIn(il), run_time=1.0)
        with self.voice("Khi đó đoạn đường từ 0 tới j cũng phải là đường đi tốt nhất tới j. Thật vậy, nếu có đường khác "
                        "tới j rẻ hơn, ta thay đoạn đầu bằng đường rẻ hơn đó rồi nhảy từ j tới i, sẽ được đường tới i "
                        "rẻ hơn, mâu thuẫn với giả thiết tốt nhất."):
            self.play(FadeIn(proof[:2]), run_time=0.8)
            self.play(FadeIn(proof[2:4]), run_time=0.8)
            self.play(FadeIn(proof[4], scale=1.3), run_time=0.6)
        with self.voice("Tính chất lời giải tốt nhất của bài lớn chứa lời giải tốt nhất của bài con được gọi là "
                        "cấu trúc con tối ưu. Cấu trúc con tối ưu và bài toán con gối nhau là hai dấu hiệu "
                        "để dùng quy hoạch động cho bài tối ưu."):
            self.play(FadeIn(key, shift=UP * 0.3), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
FULL_CODE = """
const long long MOD = 1000000007LL;
...
vector<long long> ways(stoneCount + 1, 0);
ways[0] = 1;
for (int stone = 1; stone <= stoneCount; stone++) {
    if (isSlippery[stone]) continue;
    for (int jump = 1; jump <= 3; jump++) {
        if (stone - jump < 0) continue;
        ways[stone] = (ways[stone]
                     + ways[stone - jump]) % MOD;
    }
}
cout << ways[stoneCount] << '\\n';
"""


class B1_10_TongKet(B1Scene):
    def construct(self):
        self.show_header("5. Chương trình & chi tiết quan trọng")
        code = code_block(FULL_CODE, size=22)
        note_slot = placeholder(7.4, 1.3)
        sc = fit_stack(code, note_slot, buff=0.5)
        with self.voice("Đây là phần chính của chương trình NHAYDA hoàn chỉnh. Chú ý ba chi tiết."):
            self.play(FadeIn(code, shift=UP * 0.3), run_time=1.0)
        notes = [
            (2, ["Mảng ways có n + 1 phần tử:", "chỉ số 0..n đúng như công thức."],
             "Một, mảng ways có n cộng 1 phần tử, để dùng chỉ số từ 0 đến n đúng như công thức."),
            (8, ["Lấy dư NGAY sau mỗi phép cộng", "(f(100) đã có khoảng 26 chữ số!)."],
             "Hai, phép lấy dư được thực hiện ngay sau mỗi phép cộng. Nếu đợi cộng xong mới lấy dư, số sẽ tràn rất nhanh, "
             "vì f của 100 đã có khoảng hai mươi sáu chữ số."),
            (5, ["Đá trơn: continue", "⇒ ways[stone] giữ nguyên 0."],
             "Ba, đá trơn được bỏ qua bằng lệnh continue, nên ô đó giữ nguyên giá trị 0."),
        ]
        hl = note_mob = None
        for li, text, sp in notes:
            with self.voice(sp):
                nb = line_box(code, li, ACCENT)
                nm = wrap_lines(text, size=30, color=ACCENT, align=ORIGIN)
                nm.scale_to_fit_height(min(nm.height, note_slot.height)).move_to(note_slot)
                if hl is None:
                    hl, note_mob = nb, nm
                    self.play(FadeIn(hl), FadeIn(note_mob), run_time=0.6)
                else:
                    self.play(Transform(hl, nb), Transform(note_mob, nm), run_time=0.6)

        self.clear_body()
        self.show_header("6. Mở rộng")
        ext = [
            ("Tập bước nhảy tùy ý S", "f(i) = Σ f(i − s), s ∈ S  →  O(n·k)",
             "Mở rộng một: nếu mỗi bước được nhảy một độ dài thuộc tập S, công thức là tổng f của i trừ s với s thuộc S, "
             "độ phức tạp O của n nhân k."),
            ("Thứ tự có quan trọng?", "0→1→3 khác 0→2→3. Không kể thứ tự → Bài 4",
             "Mở rộng hai: ở bài này, các cách khác thứ tự được tính là khác nhau. Nếu đề không kể thứ tự, "
             "ta cần trạng thái khác, đó là bài cái túi ở Bài 4. Đọc kĩ đề là kĩ năng sống còn."),
            ("n khổng lồ (10¹⁸)", "Truy hồi tuyến tính → lũy thừa ma trận 3×3 (Bài 14)",
             "Mở rộng ba: nếu n lên tới mười mũ mười tám, ta dùng lũy thừa ma trận ba nhân ba, trình bày ở Bài 14."),
            ("Khi nào dùng đệ quy có nhớ?", "Khi thứ tự tính khó xác định (Bài 10, 12)",
             "Mở rộng bốn: đệ quy có nhớ hữu ích khi thứ tự tính khó xác định, hoặc chỉ một phần nhỏ trạng thái được dùng. "
             "Nhớ rằng độ sâu đệ quy từ khoảng mười mũ năm tầng đã có nguy cơ tràn ngăn xếp."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Chỉ số âm", "ways[stone − 3] khi stone < 3 → lỗi! Kiểm tra stone − jump ≥ 0",
             "Bẫy một: chỉ số âm. Truy cập ô stone trừ 3 khi stone nhỏ hơn 3 là lỗi truy cập ngoài mảng."),
            ("Quên / lấy dư muộn", "Tràn số, sai ngay từ n ≈ 70",
             "Bẫy hai: quên lấy dư hoặc lấy dư muộn, kết quả tràn số, sai ngay từ n khoảng 70."),
            ("Quên f(0) = 1", "Đặt f(0) = 0 ⇒ cả bảng bằng 0",
             "Bẫy ba: quên cơ sở f của 0 bằng 1. Nhiều bạn đặt bằng 0 vì chưa nhảy bước nào, và toàn bộ bảng bằng 0."),
            ("Cộng ∞ với phí", "Kiểm tra ô nguồn < INF trước khi cộng",
             "Bẫy bốn: ở bài tối ưu, cộng phí vào ô vô cùng có thể tràn số. Luôn kiểm tra ô nguồn trước khi cộng."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 1", [
            "• QHĐ = chia bài toán con + giải mỗi bài",
            "   một lần + lưu bảng",
            "• Dấu hiệu: bài toán con GỐI NHAU;",
            "   bài tối ưu thêm CẤU TRÚC CON TỐI ƯU",
            "• Đệ quy → có nhớ → điền bảng → vài ô",
            "• Câu hỏi then chốt:",
            "   “BƯỚC CUỐI CÙNG LÀ GÌ?”",
        ], accent=GOOD, width=7.4, size=30)
        mem[3][6].set_color(ACCENT)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: quy hoạch động bằng chia thành bài toán con, giải mỗi bài một lần, và lưu bảng. "
                        "Dấu hiệu là bài toán con gối nhau, với bài tối ưu thì thêm cấu trúc con tối ưu."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Con đường nâng cấp: đệ quy, có nhớ, điền bảng, giữ vài ô. Và câu hỏi then chốt để tìm công thức: "
                        "bước cuối cùng là gì?"):
            self.play(FadeIn(mem[3][4:]), run_time=1.0)
            self.play(Indicate(mem[3][6], color=ACCENT), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Tính f(6) của bài NHAYDA", "khi đá 2 và đá 4 trơn."], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.6)
        row = array_row([""] * 7, w=0.95, h=0.95, size=34, label="f")
        for k in (2, 4):
            row.cells[k][0].set_fill("#7F1D1D", 1)
        nxt = VGroup(TB("Tiếp theo: BÀI 2", size=42, color=ACCENT),
                     T("Quy hoạch động trên dãy", size=34)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, row, nxt, buff=0.7, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: tính f của 6 trong bài nhảy đá, khi đá 2 và đá 4 trơn. "
                        "Em hãy dừng video và thử tính nhé!"):
            self.play(FadeIn(q), FadeIn(row), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        vals = [1, 1, 0, 2, 0, 2, 4]
        with self.voice("Đáp án: bảng f lần lượt là 1, 1, 0, 2, 0, 2, 4. Vậy f của 6 bằng 4."):
            for k, v in enumerate(vals):
                c = row.cells[k]
                self.play(Transform(c[1], set_cell_value(c, v, color=INK if k in (2, 4) else BG)),
                          c[0].animate.set_fill(BAD if k in (2, 4) else (GOOD if k == 6 else ACCENT), 1), run_time=0.35)
            self.play(Circumscribe(row.cells[6], color=GOOD), run_time=0.8)
        with self.voice("Bài tiếp theo, chúng ta sẽ học quy hoạch động trên dãy. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)


SCENES = [B1_00_Intro, B1_01_KhoiDong, B1_02_LietKe, B1_03_DeQuy, B1_04_CayLoiGoi, B1_05_Memo,
          B1_06_DienBang, B1_07_TietKiem, B1_08_BonCauHoi, B1_09_PhiQua, B1_10_TongKet]
