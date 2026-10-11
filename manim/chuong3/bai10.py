"""BÀI 10 — Quy hoạch động chữ số: SOMAYMAN (tổng chữ số chia hết cho K), cờ tight, khuôn mẫu STATE."""

from functools import lru_cache

from shared import *  # noqa: F401,F403


def count_upto(n, k):
    """count(N): số các x trong [0, N] có tổng chữ số chia hết cho k (quy hoạch động chữ số)."""
    if n < 0:
        return 0
    d = list(map(int, str(n)))

    @lru_cache(None)
    def go(pos, rem, tight):
        if pos == len(d):
            return 1 if rem == 0 else 0
        lim = d[pos] if tight else 9
        return sum(go(pos + 1, (rem + x) % k, tight and x == lim) for x in range(lim + 1))

    return go(0, 0, True)


def brute(lo, hi, k):
    return [x for x in range(lo, hi + 1) if sum(map(int, str(x))) % k == 0]


LUCKY30 = brute(1, 30, 5)
assert LUCKY30 == [5, 14, 19, 23, 28]
assert count_upto(30, 5) == 6 and count_upto(0, 5) == 1
assert count_upto(30, 5) - count_upto(0, 5) == 5
BIG = count_upto(10 ** 18, 7) - count_upto(0, 7)
assert BIG == 142857142856594041
assert brute(1, 100, 10) == [19, 28, 37, 46, 55, 64, 73, 82, 91]
# "1 _ _" và "6 _ _" với K = 5: cùng một tập đuôi hợp lệ
TAILS1 = [(a, b) for a in range(10) for b in range(10) if (1 + a + b) % 5 == 0]
TAILS6 = [(a, b) for a in range(10) for b in range(10) if (6 + a + b) % 5 == 0]
assert TAILS1 == TAILS6 and len(TAILS1) == 20
# chạy tay N = 30: mỗi nhánh tự do d ∈ {0,1,2} có đúng 2 chữ số cuối hợp lệ
HAND = {d: [e for e in range(10) if (d + e) % 5 == 0] for d in range(3)}
assert HAND == {0: [0, 5], 1: [4, 9], 2: [3, 8]}
assert (3 + 0) % 5 != 0  # nhánh bị chặn "3 0" không cho số nào

NAIVE_CODE = """
long long answer = 0;
for (long long x = L; x <= R; x++) {
    int s = 0;
    for (long long y = x; y > 0; y /= 10)
        s += y % 10;
    if (s % K == 0) answer++;
}
"""

DIGIT_CODE = """
long long countFrom(int pos, int rem,
                    bool tight) {
  if (pos == len) return rem == 0 ? 1 : 0;
  if (!tight && memo[pos][rem] != -1)
    return memo[pos][rem];
  int limit = tight ? digits[pos] - '0' : 9;
  long long total = 0;
  for (int d = 0; d <= limit; d++)
    total += countFrom(pos + 1,
        (rem + d) % K, tight && d == limit);
  if (!tight) memo[pos][rem] = total;
  return total;
}
"""

UPTO_CODE = """
long long countUpTo(long long n) {
  if (n < 0) return 0;
  digits = to_string(n);
  len = digits.size();
  memo.assign(len, vector<long long>(K, -1));
  return countFrom(0, 0, true);
}
"""

TEMPLATE_CODE = """
long long countFrom(int pos, STATE st,
                    bool tight) {
  if (pos == len) return isGood(st) ? 1 : 0;
  if (!tight && memo[pos][st] known)
    return memo[pos][st];
  int limit = tight ? digits[pos] : 9;
  long long total = 0;
  for (int d = 0; d <= limit; d++)
    total += countFrom(pos + 1,
        update(st, d), tight && d == limit);
  if (!tight) memo[pos][st] = total;
  return total;
}
"""


class B10Scene(NarratedScene):
    lesson_tag = "BÀI 10"
    lesson_title = "Quy hoạch động chữ số"


def dnode(label, color=MUTED, r=0.3, size=26, fill=PANEL_2):
    c = Circle(radius=r, fill_color=fill, fill_opacity=1, stroke_color=color, stroke_width=4)
    t = TB(str(label), size=size, color=INK).move_to(c)
    return VGroup(c, t)


def edge(a, b, color=MUTED, sw=3):
    return Line(a[0].get_bottom(), b[0].get_top(), color=color, stroke_width=sw, buff=0.03)


def digit_slots(chars, w=0.9, colors=None, size=40):
    cells = VGroup()
    for k, ch in enumerate(chars):
        col = colors[k] if colors else INK
        cells.add(cell(ch, w=w, h=w * 1.1, size=size, color=col))
    return cells.arrange(RIGHT, buff=0.08)


# ----------------------------------------------------------------------------
class B10_00_Intro(B10Scene):
    def construct(self):
        tag = TB("BÀI 10", size=80, color=ACCENT)
        ttl = VGroup(TB("Quy hoạch động", size=50), TB("CHỮ SỐ", size=56, color=GOOD)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Đếm trên đoạn [L, R] tới 10¹⁸:",
            "    count(R) − count(L − 1)",
            "✓ Xây số từng chữ số, cờ “bị chặn” (tight)",
            "✓ Đệ quy có nhớ, chỉ nhớ trạng thái tự do",
            "✓ Thêm thông tin vào trạng thái (STATE)",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        goals[1].set_color(ACCENT)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 10: Quy hoạch động chữ số. Đây là công cụ để đếm những con số "
                        "khổng lồ, tới 10 mũ 18, mà không cần duyệt từng số."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ đếm các số trong đoạn L đến R thỏa mãn một tính chất về chữ số, bằng cách "
                        "đưa về hiệu count của R trừ count của L trừ 1."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ xây số từng chữ số từ trái sang phải, với cờ cho biết số đang bị chặn bởi N hay đã tự do; "
                        "cài đặt bằng đệ quy có nhớ, và chỉ ghi nhớ các trạng thái tự do."):
            self.play(FadeIn(goals[2:4], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Cuối cùng, em sẽ biết thêm thông tin cần thiết vào trạng thái: số dư, chữ số trước, hay cờ đã bắt đầu."):
            self.play(FadeIn(goals[4], shift=RIGHT * 0.3), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_01_KhoiDong(B10Scene):
    def construct(self):
        self.show_header("Khởi động: Số may mắn bậc 5")
        q = VGroup(T("Số may mắn bậc 5: tổng các chữ số", size=30),
                   T("chia hết cho 5. Từ 1 đến 30 có những số nào?", size=30)).arrange(DOWN, buff=0.1)
        grid = VGroup()
        for x in range(1, 31):
            grid.add(cell(str(x), w=1.15, h=0.8, size=30))
        grid.arrange_in_grid(rows=6, cols=5, buff=0.08)
        sums_slot = placeholder(7.0, 0.8)
        res = TB("5 · 14 · 19 · 23 · 28  →  5 số", size=36, color=GOOD)
        big = VGroup(T("Còn từ 1 đến 10¹⁸ thì sao?", size=32, color=ACCENT),
                     T("10⁹ số mỗi giây ⇒ 10⁹ giây ≈ hơn 30 năm!", size=30, color=BAD)).arrange(DOWN, buff=0.12)
        sc = fit_stack(q, grid, sums_slot, res, big, buff=0.45, max_scale=1.2)
        with self.voice("Một số được gọi là số may mắn bậc 5 nếu tổng các chữ số của nó chia hết cho 5. Trong các số từ 1 "
                        "đến 30, có những số may mắn nào?"):
            self.play(FadeIn(q), LaggedStart(*[FadeIn(c) for c in grid], lag_ratio=0.03), run_time=1.6)
        notes = []
        with self.voice("Cộng các chữ số từng số: 5 có tổng 5; 14 có 1 cộng 4 bằng 5; 19 có tổng 10; 23 có tổng 5; 28 "
                        "có tổng 10. Tất cả đều chia hết cho 5."):
            for x in LUCKY30:
                c = grid[x - 1]
                s = sum(map(int, str(x)))
                lab = T(f"{'+'.join(str(x))}={s}" if x >= 10 else f"{s}", size=20, color=BG).scale(sc)
                lab.move_to(c[0].get_bottom() + UP * 0.17 * sc)
                self.play(c[0].animate.set_fill(GOOD, 1), c[1].animate.set_color(BG).shift(UP * 0.1 * sc),
                          FadeIn(lab), run_time=0.5)
                notes.append(lab)
        with self.voice("Vậy có đúng năm số: 5, 14, 19, 23 và 28."):
            self.play(FadeIn(res, scale=1.2), run_time=0.6)
        with self.voice("Còn từ 1 đến 10 mũ 18 thì sao? Duyệt từng số là không thể: máy tính nhanh nhất cũng chỉ duyệt được "
                        "khoảng 10 mũ 9 số mỗi giây, nghĩa là cần 10 mũ 9 giây, hơn 30 năm!"):
            self.play(FadeIn(big), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán SOMAYMAN")
        task = tag_box("BÀI TOÁN: SOMAYMAN", [
            "Đếm số các số nguyên x thuộc đoạn [L, R]",
            "có tổng các chữ số chia hết cho K.",
            "1 ≤ L ≤ R ≤ 10¹⁸,  1 ≤ K ≤ 200",
        ], width=7.5, size=28)
        task[3][2].set_color(ACCENT)
        ex1 = VGroup(M("1 30 5", size=32, color=BLUEC), T("→", size=32), TB("5", size=36, color=GOOD),
                     T("(5, 14, 19, 23, 28)", size=26, color=MUTED)).arrange(RIGHT, buff=0.25)
        ex2a = VGroup(M("1 10¹⁸ 7", size=32, color=BLUEC), T("→", size=32)).arrange(RIGHT, buff=0.25)
        ex2b = TB("142 857 142 856 594 041", size=36, color=GOOD)
        ex2 = VGroup(ex2a, ex2b).arrange(DOWN, buff=0.15)
        note = VGroup(T("10¹⁸ / 7 = 142 857 142 857 142 857,…", size=26, color=MUTED),
                      T("gần đúng 1/7 số, nhưng KHÔNG chính xác bằng!", size=27, color=ORANGE)).arrange(DOWN, buff=0.1)
        fit_stack(task, ex1, ex2, note, buff=0.6, max_scale=1.2)
        with self.voice("Bài toán SOMAYMAN: đếm số các số nguyên x thuộc đoạn L đến R có tổng các chữ số chia hết cho K. "
                        "L và R tới 10 mũ 18, K không quá 200."):
            self.play(FadeIn(task), run_time=1.0)
        with self.voice("Ví dụ một: từ 1 đến 30, K bằng 5, đáp án 5, đúng như em vừa đếm."):
            self.play(FadeIn(ex1), run_time=0.6)
        with self.voice("Ví dụ hai: từ 1 đến 10 mũ 18, K bằng 7, đáp án là một số mười tám chữ số."):
            self.play(FadeIn(ex2), run_time=0.8)
        with self.voice("Để ý: nó gần bằng một phần bảy của 10 mũ 18, nhưng không bằng chính xác. Không có công thức chia "
                        "đơn giản nào ở đây; ta cần một cách đếm thật sự."):
            self.play(FadeIn(note), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_02_NgayTho(B10Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: Duyệt từng số")
        code = code_block(NAIVE_CODE, size=24)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "R − L + 1 số, mỗi số tới 19 phép chia: O((R − L)·19)",
            "R − L = 10⁷:  ≈ 2·10⁸ phép  ✓ vừa kịp",
            "R − L = 10¹⁸:  KHÔNG THỂ  ✗",
        ], accent=BLUEC, width=7.5, size=27)
        cnt[3][1].set_color(GOOD)
        cnt[3][2].set_color(BAD)
        fit_stack(code, cnt, buff=0.8, max_scale=1.2)
        with self.voice("Cách ngây thơ: duyệt từng số x từ L đến R, tách từng chữ số bằng phép chia lấy dư cho 10 để tính "
                        "tổng, rồi kiểm tra tổng có chia hết cho K không."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 1, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 3, BLUEC)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 5, GOOD)), run_time=0.4)
        with self.voice("Một số có tới 19 chữ số, nên độ phức tạp là O của R trừ L nhân 19. Với R trừ L bằng 10 mũ 7, khoảng "
                        "hai trăm triệu phép, vừa kịp. Nhưng với 10 mũ 18 thì không thể."):
            self.play(FadeOut(hl), FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Bế tắc: Đếm từng số một")
        dead = VGroup(T("Tính chất chỉ phụ thuộc vào CÁC CHỮ SỐ,", size=29),
                      T("và rất nhiều số giống nhau ở phần đuôi.", size=29)).arrange(DOWN, buff=0.1)
        a = digit_slots("1__", colors=[ACCENT, MUTED, MUTED])
        b = digit_slots("6__", colors=[ORANGE, MUTED, MUTED])
        ca = T("cần a + b ≡ 4 (mod 5)", size=28, color=ACCENT)
        cb = T("cần a + b ≡ 4 (mod 5)", size=28, color=ORANGE)
        rowa = VGroup(a, ca).arrange(RIGHT, buff=0.4)
        rowb = VGroup(b, cb).arrange(RIGHT, buff=0.4)
        same = VGroup(T("1 và 6 cùng số dư khi chia cho 5", size=28),
                      TB("⇒ CÙNG 20 cách điền đuôi:", size=30, color=GOOD)).arrange(DOWN, buff=0.1)
        tails = VGroup(*[M(f"{x}{y}", size=24, color=INK) for x, y in TAILS1]).arrange_in_grid(rows=2, cols=10, buff=(0.22, 0.15))
        ask = TB("Đếm theo NHÓM thay vì từng số?", size=34, color=ACCENT)
        fit_stack(dead, VGroup(rowa, rowb).arrange(DOWN, buff=0.35), same, tails, ask, buff=0.55, max_scale=1.2)
        with self.voice("Bế tắc nằm ở đâu? Ta đang xử lí từng số một. Nhưng tính chất cần kiểm tra chỉ phụ thuộc vào các chữ "
                        "số, và rất nhiều số có phần đuôi giống nhau."):
            self.play(FadeIn(dead), run_time=0.8)
        with self.voice("Ví dụ với K bằng 5, xét các số ba chữ số dạng 1 gạch gạch. Hai chữ số cuối a và b phải có tổng chia "
                        "5 dư 4, để cộng với 1 thành bội của 5."):
            self.play(FadeIn(rowa), run_time=0.8)
        with self.voice("Còn với dạng 6 gạch gạch: vì 6 chia 5 cũng dư 1, nên điều kiện cho a và b y hệt."):
            self.play(FadeIn(rowb), run_time=0.8)
        with self.voice("Vậy hai nhóm có chung đúng 20 cách điền phần đuôi. Chỉ cần đếm một lần, dùng lại cho cả hai."):
            self.play(FadeIn(same), LaggedStart(*[FadeIn(t) for t in tails], lag_ratio=0.03), run_time=1.5)
        with self.voice("Câu hỏi là: làm sao đếm theo nhóm như vậy một cách có hệ thống, thay vì đếm từng số?"):
            self.play(FadeIn(ask, scale=1.1), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_03_ChanTren(B10Scene):
    def construct(self):
        self.show_header("Bước 1: Đưa về đếm trên đoạn [0, N]")
        ax = NumberLine(x_range=[0, 30, 5], length=7.0, include_numbers=False, color=MUTED, stroke_width=3)
        nums = VGroup(*[T(str(v), size=22, color=MUTED).next_to(ax.n2p(v), DOWN, buff=0.15) for v in range(0, 31, 5)])
        line_g = VGroup(ax, nums)
        bar_r = placeholder(7.0, 0.5)
        bar_l = placeholder(7.0, 0.5)
        bar_d = placeholder(7.0, 0.5)
        f = VGroup(T("Đáp án trên [L, R] =", size=32),
                   TB("count(R) − count(L − 1)", size=40, color=ACCENT)).arrange(DOWN, buff=0.15)
        ex = VGroup(M("count(30) = 6   (00 05 14 19 23 28)", size=25, color=GOOD),
                    M("count(0)  = 1   (số 00)", size=25, color=BAD),
                    TB("6 − 1 = 5  ✓", size=34, color=ACCENT)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        like = T("Giống mảng cộng dồn: tổng đoạn = hiệu hai tiền tố", size=27, color=MUTED)
        sc = fit_stack(VGroup(bar_r, bar_l, line_g, bar_d).arrange(DOWN, buff=0.25), f, ex, like, buff=0.6, max_scale=1.1)

        def seg(a, b, color, slot, text):
            r = Rectangle(width=ax.n2p(b)[0] - ax.n2p(a)[0], height=0.42 * sc, fill_color=color, fill_opacity=0.85,
                          stroke_width=0)
            r.move_to([(ax.n2p(a)[0] + ax.n2p(b)[0]) / 2, slot.get_center()[1], 0])
            t = TB(text, size=24, color=BG).scale(sc).move_to(r)
            return VGroup(r, t)

        r_bar = seg(0, 30, GOOD, bar_r, "count(R): [0, R]")
        l_bar = seg(0, 1, BAD, bar_l, "")
        l_lab = TB("count(L−1)", size=22, color=BAD).scale(sc).next_to(l_bar, RIGHT, buff=0.15)
        d_bar = seg(1, 30, ACCENT, bar_d, "[L, R]")
        with self.voice("Bước một: đưa về bài đếm từ 0. Đặt count của N là số các số x từ 0 đến N thỏa mãn tính chất."):
            self.play(Create(ax), FadeIn(nums), run_time=0.8)
            self.play(FadeIn(r_bar), run_time=0.6)
        with self.voice("Các số trong đoạn L đến R chính là các số từ 0 đến R, bỏ đi các số từ 0 đến L trừ 1."):
            self.play(FadeIn(l_bar), FadeIn(l_lab), run_time=0.6)
            self.play(FadeIn(d_bar), run_time=0.6)
            self.play(FadeIn(f), run_time=0.6)
        with self.voice("Với ví dụ: count của 30 bằng 6, gồm cả số 0, viết là 00. Count của 0 bằng 1, vì số 0 có tổng chữ số "
                        "bằng 0, chia hết cho 5. Đáp án 6 trừ 1 bằng 5, khớp với ví dụ."):
            self.play(LaggedStart(*[FadeIn(e) for e in ex], lag_ratio=0.5), run_time=1.5)
        with self.voice("Kĩ thuật này giống hệt mảng cộng dồn: tổng trên một đoạn bằng hiệu hai tổng tiền tố. Từ nay ta chỉ "
                        "cần giải bài đếm từ 0 đến N."):
            self.play(FadeIn(like), run_time=0.6)

        self.clear_body()
        self.show_header("Bước 2: Xây số từng chữ số, cờ “bị chặn”")
        nrow = VGroup(T("N =", size=34), digit_slots("274", colors=[ACCENT] * 3)).arrange(RIGHT, buff=0.3)
        pad = VGroup(T("Viết đủ 3 chữ số: 5 →", size=28), M("005", size=32, color=BLUEC),
                     T("(tổng chữ số không đổi)", size=24, color=MUTED)).arrange(RIGHT, buff=0.2)
        # cây các số ≤ 274
        root = dnode("", color=ACCENT, r=0.22)
        root.move_to(UP * 2.4)
        l1 = {d: dnode(d, color=BLUEC if d < 2 else ACCENT) for d in range(3)}
        l1[0].move_to([-3.3, 1.0, 0])
        l1[1].move_to([-2.3, 1.0, 0])
        l1[2].move_to([0.5, 1.0, 0])
        l2 = {d: dnode(d, color=BLUEC if d < 7 else ACCENT, r=0.26, size=24) for d in range(8)}
        for d in range(8):
            l2[d].move_to([-1.6 + d * 0.6, -0.5, 0])
        l3 = {d: dnode(d, color=ACCENT, r=0.23, size=22) for d in range(5)}
        for d in range(5):
            l3[d].move_to([1.5 + d * 0.56, -2.6, 0])

        def tri(node, w=0.7, h=0.9, label="00..99"):
            t = Polygon(node[0].get_bottom() + DOWN * 0.08, node[0].get_bottom() + DOWN * (0.08 + h) + LEFT * w / 2,
                        node[0].get_bottom() + DOWN * (0.08 + h) + RIGHT * w / 2, color=BLUEC, fill_color=BLUEC,
                        fill_opacity=0.25, stroke_width=2)
            lab = T(label, size=18, color=BLUEC).next_to(t, DOWN, buff=0.08)
            return VGroup(t, lab)

        tri0, tri1 = tri(l1[0]), tri(l1[1])
        tris2 = VGroup(*[tri(l2[d], w=0.42, h=0.55, label="0..9") for d in range(7)])
        for k in range(7):
            tris2[k][1].set_opacity(0)
        tris2_lab = VGroup(T("mỗi nhánh xanh:", size=20, color=BLUEC), T("chữ số cuối 0..9 tự do", size=20, color=BLUEC)
                           ).arrange(DOWN, aligned_edge=LEFT, buff=0.06).next_to(tris2, DOWN, buff=0.15)
        tris2_lab.align_to(tris2, LEFT)
        e1 = VGroup(*[edge(root, l1[d], BLUEC if d < 2 else ACCENT, 4 if d == 2 else 3) for d in range(3)])
        e2 = VGroup(*[edge(l1[2], l2[d], BLUEC if d < 7 else ACCENT, 4 if d == 7 else 3) for d in range(8)])
        e3 = VGroup(*[edge(l2[7], l3[d], ACCENT, 3) for d in range(5)])
        tree = VGroup(root, *l1.values(), *l2.values(), *l3.values(), tri0, tri1, tris2, tris2_lab, e1, e2, e3)
        legend = VGroup(VGroup(Dot(color=ACCENT, radius=0.12), T("bị chặn (bằng hệt N tới giờ)", size=26)).arrange(RIGHT, buff=0.2),
                        VGroup(Dot(color=BLUEC, radius=0.12), T("tự do (đã nhỏ hơn N)", size=26)).arrange(RIGHT, buff=0.2)
                        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        key = VGroup(T("Mỗi vị trí: TỐI ĐA MỘT nhánh bị chặn.", size=28, color=ACCENT),
                     T("Nhánh tự do chỉ phụ thuộc: số chữ số còn lại", size=27),
                     T("+ điều cần nhớ (tổng chữ số mod K).", size=27)).arrange(DOWN, buff=0.1)
        fit_stack(nrow, pad, tree, legend, key, buff=0.45, max_scale=1.2)
        with self.voice("Bước hai, ý tưởng cốt lõi. Viết mọi số từ 0 đến N với cùng số chữ số như N, thêm các số 0 ở đầu. Ví "
                        "dụ với N bằng 274, số 5 viết thành 005. Số 0 ở đầu không làm thay đổi tổng chữ số."):
            self.play(FadeIn(nrow), run_time=0.6)
            self.play(FadeIn(pad), run_time=0.6)
        with self.voice("Ta điền các chữ số từ trái sang phải. Chữ số hàng trăm chỉ được chọn 0, 1 hoặc 2, vì nếu lớn hơn 2 thì "
                        "số vượt quá 274."):
            self.play(FadeIn(root), *[Create(e) for e in e1], *[FadeIn(l1[d]) for d in range(3)], run_time=1.0)
        with self.voice("Nếu chọn 0 hoặc 1, số đã chắc chắn nhỏ hơn N. Hai chữ số sau được tự do từ 0 đến 9, bất kể điền gì. "
                        "Ta nói nhánh đó tự do, tô màu xanh."):
            self.play(FadeIn(tri0), FadeIn(tri1), run_time=0.8)
        with self.voice("Còn nếu chọn 2, bằng đúng chữ số đầu của N, số vẫn bị chặn: chữ số hàng chục chỉ được từ 0 đến 7."):
            self.play(*[Create(e) for e in e2], *[FadeIn(l2[d]) for d in range(8)], run_time=1.0)
        with self.voice("Các nhánh 20 đến 26 lại tự do, chữ số cuối từ 0 đến 9. Chỉ nhánh 27 vẫn bị chặn, chữ số cuối chỉ từ 0 "
                        "đến 4."):
            self.play(FadeIn(tris2), FadeIn(tris2_lab), run_time=0.8)
            self.play(*[Create(e) for e in e3], *[FadeIn(l3[d]) for d in range(5)], run_time=0.8)
        with self.voice("Quan sát: đường màu vàng bị chặn đi đúng theo các chữ số của N, và chỉ có một đường như thế."):
            self.play(FadeIn(legend), Indicate(VGroup(root, l1[2], l2[7], l3[4]), color=ACCENT, scale_factor=1.3), run_time=1.2)
        with self.voice("Mọi nhánh khác đều tự do, và kết quả của một nhánh tự do chỉ phụ thuộc vào số chữ số còn phải điền, "
                        "cùng điều ta cần nhớ về phần đã điền. Ở đây, đó là tổng chữ số chia lấy dư cho K. Không cần biết "
                        "chính các chữ số đã điền là gì."):
            self.play(FadeIn(key), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_04_CongThuc(B10Scene):
    def construct(self):
        self.show_header("Bước 3: Trạng thái và công thức")
        st = tag_box("TRẠNG THÁI", [
            "countFrom(pos, rem, tight) = số cách điền các",
            "chữ số từ vị trí pos đến hết, biết rằng:",
            "• rem = tổng chữ số đã điền, mod K",
            "• tight = phần đã điền BẰNG HỆT phần đầu của N",
        ], width=7.5, size=27)
        st[3][2].set_color(GOOD)
        st[3][3].set_color(ACCENT)
        rng = VGroup(T("Chữ số d chạy từ 0 đến", size=28),
                     M("tight ? N[pos] : 9", size=30, color=ACCENT)).arrange(RIGHT, buff=0.2)
        form = panel(VGroup(M("countFrom(pos, rem, tight) =", size=28),
                            M("  Σ countFrom(pos + 1,", size=28, color=GOOD),
                            M("      (rem + d) mod K,", size=28, color=GOOD),
                            M("      tight && d == N[pos])", size=28, color=ACCENT)).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
                     stroke=ACCENT, width=7.5)
        base = VGroup(T("Cơ sở: hết chữ số ⇒ trả 1 nếu rem = 0, ngược lại 0", size=26),
                      TB("Đáp án: count(N) = countFrom(0, 0, true)", size=28, color=ACCENT)).arrange(DOWN, buff=0.12)
        fit_stack(st, rng, form, base, buff=0.5, max_scale=1.2)
        with self.voice("Bước ba: viết thành trạng thái. countFrom của pos, rem, tight là số cách điền các chữ số từ vị trí pos "
                        "đến hết. Trong đó rem là tổng các chữ số đã điền, chia lấy dư cho K."):
            self.play(FadeIn(st[0:3]), FadeIn(st[3][0:3]), run_time=1.0)
        with self.voice("Và tight là cờ bị chặn: đúng nếu phần đã điền bằng hệt phần đầu của N."):
            self.play(FadeIn(st[3][3]), run_time=0.5)
        with self.voice("Tại vị trí pos, chữ số d chạy từ 0 đến chữ số của N nếu đang bị chặn, hoặc đến 9 nếu đã tự do."):
            self.play(FadeIn(rng), run_time=0.6)
        with self.voice("Công thức: cộng dồn countFrom tại vị trí kế tiếp, số dư mới là rem cộng d, mod K. Cờ tight mới chỉ "
                        "đúng khi đang bị chặn và d bằng đúng chữ số của N; chỉ cần chọn nhỏ hơn một lần là tự do mãi mãi."):
            self.play(FadeIn(form[0]), FadeIn(form[1][0:3]), run_time=0.8)
            self.play(Indicate(form[1][3], color=ACCENT, scale_factor=1.05), run_time=0.8)
        with self.voice("Cơ sở: khi đã điền hết, trả về 1 nếu rem bằng 0, ngược lại trả về 0. Đáp án count của N là "
                        "countFrom của 0, 0, đúng: bắt đầu ở vị trí đầu, tổng 0, và đang bị chặn."):
            self.play(FadeIn(base), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao không bỏ sót, không đếm trùng?")
        why = tag_box("VÌ SAO ĐÚNG?", [
            "• Mỗi số x ∈ [0, N] (viết đủ chữ số) ⟷ đúng",
            "   MỘT đường đi đầy đủ từ gốc trong cây",
            "• countFrom chỉ GỘP các nhánh CÙNG trạng thái,",
            "   mà cùng trạng thái ⇒ cùng số cách điền tiếp",
            "⇒ đếm theo nhóm = đếm từng số",
        ], accent=PURPLE, width=7.5, size=28)
        why[3][4].set_color(GOOD)
        ex = VGroup(T("Với N = 274, K = 5: nhánh “1 _ _” và “0 _ _”", size=27),
                    T("là hai trạng thái khác nhau:", size=27),
                    M("(pos=1, rem=1, tự do)  ≠  (pos=1, rem=0, tự do)", size=23, color=BLUEC),
                    T("“1 _ _” trùng trạng thái với “6 _ _” (nếu có)", size=27, color=GOOD)).arrange(DOWN, buff=0.12)
        fit_stack(why, ex, buff=0.8, max_scale=1.2)
        with self.voice("Vì sao cách đếm này đúng? Mỗi số x từ 0 đến N, viết đủ số chữ số, ứng với đúng một đường đi đầy đủ từ "
                        "gốc trong cây, và ngược lại."):
            self.play(FadeIn(why[0:3]), FadeIn(why[3][0:2]), run_time=1.0)
        with self.voice("Hàm countFrom chỉ gộp các nhánh có cùng trạng thái, mà các nhánh cùng trạng thái thì có cùng số cách "
                        "điền tiếp. Vì thế đếm theo nhóm cho đúng kết quả của đếm từng số."):
            self.play(FadeIn(why[3][2:]), run_time=1.0)
        with self.voice("Ví dụ: nhánh 1 gạch gạch có trạng thái vị trí 1, số dư 1, tự do; khác với nhánh 0 gạch gạch có số dư 0. "
                        "Nhưng nếu N đủ lớn, nhánh 6 gạch gạch sẽ có đúng cùng trạng thái với nhánh 1 gạch gạch, và được dùng "
                        "lại."):
            self.play(FadeIn(ex), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_05_ChayTay(B10Scene):
    def construct(self):
        self.show_header("Bước 4: Chạy tay với N = 30, K = 5")
        nrow = VGroup(T("N =", size=34), digit_slots("30", colors=[ACCENT] * 2)).arrange(RIGHT, buff=0.3)
        rows = VGroup()
        for d in range(4):
            free = d < 3
            lab = panel(VGroup(M(f"{d} _", size=30, color=BLUEC if free else ACCENT)), pad=0.15,
                        stroke=BLUEC if free else ACCENT)
            st = M(f"rem={d}" + (" tự do" if free else " chặn"), size=20, color=MUTED)
            left = VGroup(lab, st).arrange(DOWN, buff=0.08)
            lim = 9 if free else 0
            cells = VGroup(*[cell(str(e), w=0.48, h=0.55, size=22, color=INK if e <= lim else MUTED,
                                  fill=PANEL_2 if e <= lim else BG) for e in range(10)]).arrange(RIGHT, buff=0.03)
            cnt = placeholder(0.8, 0.6)
            r = VGroup(left, cells, cnt).arrange(RIGHT, buff=0.25)
            r.cells, r.cnt = cells, cnt
            rows.add(r)
        rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        total = VGroup(TB("count(30) = 2 + 2 + 2 + 0 = 6", size=34, color=GOOD),
                       M("00 05 14 19 23 28", size=30, color=GOOD)).arrange(DOWN, buff=0.12)
        ans = VGroup(T("count(0) = 1  (số 0 có tổng 0 ⋮ 5)", size=28),
                     TB("Đáp án = 6 − 1 = 5  ✓", size=38, color=ACCENT)).arrange(DOWN, buff=0.15)
        sc = fit_stack(nrow, rows, total, ans, buff=0.55, max_scale=1.2)
        with self.voice("Bước bốn: chạy tay với N bằng 30, K bằng 5. Chữ số hàng chục được chọn từ 0 đến 3."):
            self.play(FadeIn(nrow), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(r[0]) for r in rows], lag_ratio=0.25), run_time=1.0)
        with self.voice("Chọn 0, 1 hoặc 2: nhỏ hơn 3, nên chữ số cuối tự do từ 0 đến 9. Chọn 3: bằng chữ số của N, vẫn bị "
                        "chặn, chữ số cuối chỉ được là 0."):
            self.play(*[FadeIn(r[1]) for r in rows], run_time=0.8)
        texts = [
            "Nhánh 0 gạch: số dư đang là 0, chữ số cuối phải chia hết cho 5: chọn 0 hoặc 5. Hai cách: 00 và 05.",
            "Nhánh 1 gạch: số dư 1, chữ số cuối phải là 4 hoặc 9. Hai cách: 14 và 19.",
            "Nhánh 2 gạch: số dư 2, chữ số cuối là 3 hoặc 8. Hai cách: 23 và 28.",
            "Nhánh 3 gạch bị chặn: chỉ được số 30, tổng chữ số 3, không chia hết cho 5. Không cách nào.",
        ]
        for d, r in enumerate(rows):
            ok = HAND.get(d, [])
            with self.voice(texts[d]):
                anims = [r.cells[e][0].animate.set_fill(GOOD, 1) for e in ok]
                if d == 3:
                    anims = [r.cells[0][0].animate.set_fill(BAD, 1)]
                self.play(*anims, run_time=0.6)
                n = TB(str(len(ok)), size=40, color=GOOD if ok else BAD).scale(sc).move_to(r.cnt)
                self.play(FadeIn(n, scale=1.4), run_time=0.4)
        with self.voice("Ba nhánh tự do, mỗi nhánh 2 cách; nhánh bị chặn không cho số nào. Vậy count của 30 bằng 6, gồm 00, 05, "
                        "14, 19, 23 và 28."):
            self.play(FadeIn(total), run_time=0.8)
        with self.voice("Số 0 có tổng chữ số bằng 0, chia hết cho 5, nên count của 0 bằng 1. Đáp án 6 trừ 1 bằng 5, khớp với "
                        "ví dụ."):
            self.play(FadeIn(ans), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_06_Code(B10Scene):
    def construct(self):
        self.show_header("Bước 5: Đệ quy có nhớ, chỉ nhớ trạng thái tự do")
        why = VGroup(T("Trạng thái tight = đúng chỉ xuất hiện MỘT LẦN", size=28),
                     T("ở mỗi vị trí (trên đường vàng duy nhất)", size=28),
                     T("⇒ ghi nhớ nó vô ích. Chỉ nhớ memo[pos][rem].", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        code = code_block(DIGIT_CODE, size=21)
        fit_stack(why, code, buff=0.6)
        with self.voice("Bước năm: cài đặt. Thứ tự tính ở đây là vị trí lớn trước, rất hợp với đệ quy có nhớ. Và ta chỉ cần "
                        "ghi nhớ các trạng thái tự do: trạng thái bị chặn chỉ xuất hiện đúng một lần ở mỗi vị trí, trên "
                        "đường vàng duy nhất, nên nhớ nó chẳng có ích gì."):
            self.play(FadeIn(why), run_time=1.0)
        with self.voice("Hàm countFrom: hết chữ số thì trả về 1 nếu số dư bằng 0."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 2, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
        with self.voice("Nếu đang tự do và trạng thái đã tính, trả luôn kết quả đã nhớ."):
            self.play(Transform(hl, line_box(code, 3, BLUEC)), run_time=0.4)
        with self.voice("Giới hạn chữ số: bằng chữ số của N nếu bị chặn, ngược lại là 9. Thử mọi chữ số d, cập nhật số dư và "
                        "cờ tight."):
            self.play(Transform(hl, line_box(code, 5, ACCENT)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 8, GOOD)), run_time=0.4)
        with self.voice("Cuối cùng, chỉ ghi nhớ khi trạng thái tự do."):
            self.play(Transform(hl, line_box(code, 10, BLUEC)), run_time=0.4)

        self.clear_body()
        self.show_header("Hàm count và độ phức tạp")
        code2 = code_block(UPTO_CODE, size=22)
        main = VGroup(T("Trong main:", size=28),
                      M("countUpTo(R) - countUpTo(L - 1)", size=28, color=ACCENT)).arrange(DOWN, buff=0.12)
        reset = VGroup(T("memo được KHỞI TẠO LẠI mỗi lần gọi: giá trị của", size=26),
                       T("(pos, rem) phụ thuộc số chữ số còn lại, tức độ dài N", size=26)).arrange(DOWN, buff=0.08)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "19 vị trí × K số dư × 10 chữ số: O(19·K·10)",
            "K = 200: chỉ ≈ 38 000 phép!",
            "Đáp án tới ≈ 10¹⁸: vẫn vừa long long",
        ], accent=GOOD, width=7.5, size=28)
        cx[3][1].set_color(GOOD)
        fit_stack(code2, main, reset, cx, buff=0.5, max_scale=1.2)
        with self.voice("Hàm countUpTo: nếu n âm thì trả về 0, để xử lí trường hợp L bằng 1 thì L trừ 1 bằng 0 vẫn đúng. "
                        "Đổi n thành xâu chữ số, khởi tạo bảng memo toàn trừ 1, rồi gọi countFrom từ vị trí 0."):
            self.play(FadeIn(code2), run_time=0.8)
        with self.voice("Trong hàm main, in ra countUpTo của R trừ countUpTo của L trừ 1."):
            self.play(FadeIn(main), run_time=0.6)
        with self.voice("Chú ý: mỗi lần gọi countUpTo, bảng memo phải được khởi tạo lại, vì giá trị của một trạng thái tự do "
                        "phụ thuộc vào số chữ số còn lại, tức là phụ thuộc vào độ dài của N."):
            self.play(FadeIn(reset), run_time=0.8)
        with self.voice("Độ phức tạp: 19 vị trí nhân K số dư, mỗi trạng thái thử 10 chữ số. Với K bằng 200, chỉ khoảng ba "
                        "mươi tám nghìn phép. Từ hơn 30 năm xuống còn chưa tới một mili giây!"):
            self.play(FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_07_KhuonMau(B10Scene):
    def construct(self):
        self.show_header("4. Khuôn mẫu chung")
        code = code_block(TEMPLATE_CODE, size=21)
        ask = VGroup(T("Việc của em chỉ là trả lời:", size=28),
                     TB("“Để kiểm tra tính chất ở cuối, ta cần", size=30, color=ACCENT),
                     TB("nhớ gì về các chữ số đã điền?”", size=30, color=ACCENT),
                     T("Đó chính là STATE.", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        fit_stack(code, ask, buff=0.7, max_scale=1.2)
        with self.voice("Hầu hết các bài quy hoạch động chữ số đều có chung một khuôn. Chỉ khác ở trạng thái STATE, hàm update "
                        "cập nhật trạng thái khi thêm chữ số d, và hàm isGood kiểm tra ở cuối."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 0, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 2, BLUEC)), run_time=0.4)
        with self.voice("Việc của em chỉ là trả lời một câu hỏi: để kiểm tra tính chất ở cuối, ta cần nhớ gì về các chữ số "
                        "đã điền? Đó chính là STATE."):
            self.play(FadeOut(hl), FadeIn(ask), run_time=0.8)

        self.clear_body()
        self.show_header("Tính chất → STATE cần nhớ")
        rows = [
            ("Tổng chữ số chia hết cho K", "tổng chữ số mod K"),
            ("Không chứa chữ số 4", "không cần gì (cấm chọn d = 4)"),
            ("Không có 2 chữ số kề nhau bằng nhau", "chữ số trước + cờ “đã bắt đầu”"),
            ("Số chia hết cho K", "giá trị mod K: (rem·10 + d) mod K"),
            ("Chứa xâu “13”", "đã thấy “13” chưa + chữ số trước là 1?"),
        ]
        speech = [
            "Tính chất tổng chữ số chia hết cho K: nhớ tổng chữ số mod K, như bài vừa học.",
            "Không chứa chữ số 4: không cần nhớ gì cả, chỉ cần cấm chọn d bằng 4 trong vòng lặp.",
            "Không có hai chữ số kề nhau bằng nhau: nhớ chữ số trước, cùng cờ đã bắt đầu để bỏ qua các số 0 ở đầu.",
            "Bản thân số chia hết cho K: nhớ giá trị phần đã điền mod K, cập nhật bằng rem nhân 10 cộng d.",
            "Chứa xâu 13: nhớ đã thấy 13 chưa, và chữ số trước có phải là 1 không.",
        ]
        cards = VGroup()
        for a, b in rows:
            g = VGroup(TB(a, size=28, color=ACCENT), VGroup(T("STATE:", size=25, color=MUTED), T(b, size=26, color=GOOD)
                                                           ).arrange(RIGHT, buff=0.2)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            c = panel(g, width=7.5, pad=0.25)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.25)
            cards.add(c)
        cards.arrange(DOWN, buff=0.25)
        fit_stack(cards, max_scale=1.3)
        for c, s in zip(cards, speech):
            with self.voice(s):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B10_08_TongKet(B10Scene):
    def construct(self):
        self.show_header("5. Mở rộng")
        ext = [
            ("Số 0 đứng đầu", "7 viết thành 007 có hai số 0 kề nhau! Thêm cờ started",
             "Mở rộng một: số 0 đứng đầu. Với tổng chữ số thì không sao, nhưng với tính chất không có hai chữ số kề nhau "
             "bằng nhau, số 7 viết thành 007 lại có hai số 0 kề nhau! Cần thêm cờ started: chưa bắt đầu thì các số 0 không "
             "tính là chữ số trước."),
            ("Chia hết cho tổng chữ số của chính nó", "Cố định tổng mục tiêu s = 1..162, đếm từng s rồi cộng",
             "Mở rộng hai: đếm các số chia hết cho tổng chữ số của chính nó. Tổng chưa biết trước, nhưng chỉ từ 1 đến 162. "
             "Ta cố định tổng mục tiêu s, đếm các số có tổng chữ số bằng s và chia hết cho s, rồi cộng lại."),
            ("Tìm số may mắn thứ k", "Thử d từ nhỏ đến lớn, dùng hàm đếm để chốt từng chữ số",
             "Mở rộng ba: tìm số may mắn thứ k. Đi từ trái sang phải, thử chữ số d từ nhỏ đến lớn, dùng hàm đếm để biết có "
             "bao nhiêu số nếu chọn d. Ít hơn k thì trừ đi và thử d tiếp; không thì chốt d. Đây là truy vết bằng hàm đếm."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Tính count(L) thay vì count(L − 1)", "lệch đúng một số khi L thỏa mãn",
             "Bẫy một: tính count của L thay vì count của L trừ 1, sẽ lệch đúng một số khi chính L thỏa mãn."),
            ("L = 1 ⇒ count(0)", "số 0 có thể được tính: xử lí đúng",
             "Bẫy hai: L bằng 1 thì phải tính count của 0, và số 0 có thể được tính."),
            ("Ghi nhớ chung cả trạng thái tight", "không tách chiều tight trong memo ⇒ sai",
             "Bẫy ba: ghi nhớ trạng thái bị chặn chung với trạng thái tự do. Nếu muốn nhớ cả hai, memo phải có thêm chiều "
             "tight."),
            ("Quên khởi tạo lại memo", "giữa hai lần gọi count với độ dài khác nhau",
             "Bẫy bốn: không khởi tạo lại memo giữa hai lần gọi count với hai số có độ dài khác nhau."),
            ("Số 0 đứng đầu", "với tính chất về chữ số kề nhau, số lượng chữ số",
             "Bẫy năm: quên số 0 đứng đầu, với các tính chất liên quan tới chữ số kề nhau hoặc số lượng chữ số."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 10", [
            "• Đáp án trên [L, R] = count(R) − count(L − 1)",
            "• Xây số từ trái sang phải; cờ tight cho biết",
            "   còn bị chặn bởi N không",
            "• STATE = điều cần nhớ về phần đã điền",
            "   để kiểm tra tính chất cuối cùng",
            "• Chỉ nhớ trạng thái tự do:",
            "   O(số chữ số × số STATE × 10)",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: đáp án trên đoạn L đến R bằng count của R trừ count của L trừ 1. Xây số từ trái sang phải, "
                        "cờ tight cho biết còn bị chặn bởi N không."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:3]), run_time=1.0)
        with self.voice("STATE là những gì cần nhớ về phần đã điền để kiểm tra tính chất cuối cùng. Chỉ ghi nhớ trạng thái tự "
                        "do; độ phức tạp là số chữ số nhân số STATE nhân 10."):
            self.play(FadeIn(mem[3][3:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Từ 1 đến 100, bao nhiêu số có", "tổng chữ số chia hết cho 10?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        nums = VGroup(*[cell(str(x), w=0.78, h=0.7, size=26, fill=GOOD, color=BG) for x in brute(1, 100, 10)]).arrange(RIGHT, buff=0.04)
        ans = TB("Đáp số: 9 số", size=44, color=GOOD)
        hint = T("(số 100 có tổng 1; mỗi chữ số hàng chục 1..9 ghép đúng một chữ số cuối)", size=22, color=MUTED)
        nxt = VGroup(TB("Tiếp theo: BÀI 11", size=42, color=ACCENT), T("Quy hoạch động trên cây", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, nums, ans, hint, nxt, buff=0.55, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: từ 1 đến 100, có bao nhiêu số có tổng chữ số chia hết cho 10? Dừng video và thử "
                        "nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp số: 9 số, gồm 19, 28, 37, 46, 55, 64, 73, 82 và 91. Mỗi chữ số hàng chục từ 1 đến 9 ghép với đúng "
                        "một chữ số cuối; số 100 có tổng chữ số bằng 1."):
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in nums], lag_ratio=0.15), run_time=1.2)
            self.play(FadeIn(ans), FadeIn(hint), run_time=0.6)
        with self.voice("Bài tiếp theo: quy hoạch động trên cây. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
