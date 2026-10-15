"""BÀI 13 — Tăng tốc bằng mảng cộng dồn (DEMCACHNHAY) và hàng đợi đơn điệu (NHAYXA)."""

from collections import deque

from shared import *  # noqa: F401,F403


def count_jumps(n, lo, hi):
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        if i - lo >= 0:
            f[i] = sum(f[j] for j in range(max(0, i - hi), i - lo + 1))
    return f


F7 = count_jumps(7, 2, 3)
assert F7 == [1, 0, 1, 1, 1, 2, 2, 3]
S7 = [0]
for _x in F7:
    S7.append(S7[-1] + _x)
assert S7 == [0, 1, 1, 2, 3, 4, 6, 8, 11]
assert F7[7] == S7[7 - 2 + 1] - S7[max(0, 7 - 3)] == 3
for _i in range(1, 8):
    if _i - 2 >= 0:
        assert F7[_i] == S7[_i - 2 + 1] - S7[max(0, _i - 3)]
assert count_jumps(10, 3, 5)[10] == 4


def seqs(n, lo, hi):
    if n == 0:
        return [[]]
    return [[d] + r for d in range(lo, hi + 1) if d <= n for r in seqs(n - d, lo, hi)]


assert sorted(seqs(7, 2, 3)) == [[2, 2, 3], [2, 3, 2], [3, 2, 2]]

SCORE = [0, 2, -5, -1, 4, -8, -2, 3, 1]
K = 3


def far_jump(score, k):
    n = len(score) - 1
    best = [0] * (n + 1)
    win = deque([0])
    log = []
    for i in range(1, n + 1):
        popped_front = []
        while win[0] < i - k:
            popped_front.append(win.popleft())
        head = win[0]
        best[i] = best[head] + score[i]
        popped_back = []
        while win and best[win[-1]] <= best[i]:
            popped_back.append(win.pop())
        win.append(i)
        log.append((i, popped_front, head, popped_back, list(win)))
    return best, log


BEST, QLOG = far_jump(SCORE, K)
assert BEST == [0, 2, -3, 1, 6, -2, 4, 9, 10]
assert [w for *_, w in QLOG] == [[1], [1, 2], [1, 3], [4], [4, 5], [4, 6], [7], [8]]
assert far_jump(SCORE, 2)[0][-1] == 7
assert 2 + 4 + 3 + 1 == BEST[8]

PREFIX_CODE = """
ways[0] = 1;
prefix[1] = 1;
for (int i = 1; i <= n; i++) {
  int from = i - R, to = i - L;
  if (to >= 0) {
    if (from < 0) from = 0;
    ways[i] = (prefix[to + 1] - prefix[from]
               + MOD) % MOD;
  }
  prefix[i + 1] = (prefix[i] + ways[i]) % MOD;
}
"""

DEQUE_CODE = """
deque<int> window;
window.push_back(0);
for (int i = 1; i <= n; i++) {
  while (window.front() < i - k)
    window.pop_front();
  best[i] = best[window.front()] + score[i];
  while (!window.empty() &&
         best[window.back()] <= best[i])
    window.pop_back();
  window.push_back(i);
}
"""


class B13Scene(NarratedScene):
    lesson_tag = "BÀI 13"
    lesson_title = "Mảng cộng dồn và hàng đợi đơn điệu"


def ghost_row(n, **kw):
    """array_row với chữ ẩn trong mỗi ô (để Transform điền số hoạt động)."""
    r = array_row(["0"] * n, **kw)
    for c in r.cells:
        c[1].set_opacity(0)
    return r


def setv(c, v, col=INK):
    return Transform(c[1], set_cell_value(c, v, color=col))


def stone_row(n, w=0.82, labels=None, colors=None):
    g = VGroup()
    for i in range(n + 1):
        c = Circle(radius=w * 0.42, fill_color=STONE if 0 < i < n else "#6B8E4E", fill_opacity=1,
                   stroke_color="#CBD5E1", stroke_width=3)
        t = TB(str(labels[i] if labels else i), size=w * 30, color=BG)
        if colors and colors[i]:
            c.set_fill(colors[i], 1)
        g.add(VGroup(c, t.move_to(c)))
    return g.arrange(RIGHT, buff=w * 0.2)


def arc(a, b, color=ACCENT, sw=5):
    return ArcBetweenPoints(a[0].get_top() + UP * 0.05, b[0].get_top() + UP * 0.05, angle=-PI * 0.6, color=color,
                            stroke_width=sw)


# ----------------------------------------------------------------------------
class B13_00_Intro(B13Scene):
    def construct(self):
        chap = TB("CHƯƠNG 4", size=44, color=ACCENT)
        title = VGroup(TB("TỐI ƯU HÓA", size=60), TB("QUY HOẠCH ĐỘNG", size=60)).arrange(DOWN, buff=0.2)
        bar = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        cover = VGroup(chap, title, bar).arrange(DOWN, buff=0.35)
        prob = VGroup(T("Công thức ĐÚNG nhưng vẫn quá thời gian:", size=29),
                      T("10⁶ ô, mỗi ô lại duyệt 10⁶ ô khác…", size=29, color=BAD),
                      TB("Giữ nguyên công thức — đổi CÁCH TÍNH", size=32, color=GOOD)).arrange(DOWN, buff=0.15)
        tools = VGroup(*[panel(T(t, size=27), pad=0.18, stroke=c) for t, c in
                         [("mảng cộng dồn", BLUEC), ("hàng đợi đơn điệu", GOOD), ("cây Fenwick", ORANGE),
                          ("lũy thừa ma trận", PURPLE)]]).arrange_in_grid(rows=2, cols=2, buff=0.25)
        fit_stack(cover, prob, tools, buff=0.8, max_scale=1.15)
        with self.voice("Chào các em! Chúng ta bước sang chương cuối, Chương 4: Tối ưu hóa quy hoạch động."):
            self.play(FadeIn(chap, shift=DOWN * 0.3), Write(title), run_time=1.8)
            self.play(GrowFromCenter(bar), run_time=0.5)
        with self.voice("Có những bài em đã tìm ra công thức đúng, nhưng chương trình vẫn chạy quá thời gian: bảng có một triệu ô, "
                        "mỗi ô lại phải duyệt một triệu ô khác. Lúc này công thức không cần thay đổi; thứ cần thay đổi là cách "
                        "tính từng ô."):
            self.play(FadeIn(prob), run_time=1.0)
        with self.voice("Chương này giới thiệu bốn công cụ tăng tốc quan trọng nhất: mảng cộng dồn, hàng đợi đơn điệu, cây Fenwick "
                        "và lũy thừa ma trận. Mỗi công cụ trả lời nhanh một loại câu hỏi nằm bên trong công thức chuyển."):
            self.play(LaggedStart(*[FadeIn(t, scale=0.8) for t in tools], lag_ratio=0.3), run_time=1.6)

        self.clear_body()
        tag = TB("BÀI 13", size=80, color=ACCENT)
        ttl = VGroup(TB("Tăng tốc bằng", size=46), TB("mảng cộng dồn", size=50, color=BLUEC),
                     TB("và hàng đợi đơn điệu", size=50, color=GOOD)).arrange(DOWN, buff=0.15)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Tổng trên ĐOẠN LIÊN TIẾP:",
            "    mảng cộng dồn, O(1)",
            "✓ Max/min trên CỬA SỔ TRƯỢT:",
            "    hàng đợi đơn điệu, O(1) trung bình",
            "✓ Từ O(n·k) xuống O(n)",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Bài 13: Tăng tốc bằng mảng cộng dồn và hàng đợi đơn điệu."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ nhận ra khi công thức chuyển là tổng trên một đoạn liên tiếp các ô trước đó, và "
                        "tính nó trong O của 1 bằng mảng cộng dồn."):
            self.play(FadeIn(goals[0:2]), run_time=0.6)
        with self.voice("Em cũng nhận ra khi công thức là max hoặc min trên một cửa sổ trượt, và tính nó bằng hàng đợi đơn điệu. "
                        "Kết quả: giảm độ phức tạp từ O của n nhân k xuống O của n."):
            self.play(FadeIn(goals[2:]), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_01_KhoiDong(B13Scene):
    def construct(self):
        self.show_header("Khởi động: Ếch nhảy xa hơn")
        recall = VGroup(T("Bài 1: mỗi bước nhảy 1, 2 hoặc 3 đá", size=29),
                        M("f(i) = f(i−1) + f(i−2) + f(i−3)", size=28, color=MUTED)).arrange(DOWN, buff=0.12)
        frog = make_frog(1.6)
        now = VGroup(T("Giờ được nhảy BẤT KÌ độ dài nào", size=30),
                     TB("từ 2 đến 300 000!", size=36, color=ORANGE)).arrange(DOWN, buff=0.1)
        cost = VGroup(T("≈ 300 000 số hạng mỗi ô × 10⁶ ô", size=29),
                      TB("≈ 3·10¹¹ phép cộng", size=34, color=BAD)).arrange(DOWN, buff=0.1)
        hint = VGroup(T("Nhưng các số hạng là các ô LIÊN TIẾP nhau;", size=28, color=GOOD),
                      T("ô sau dùng gần như đúng các ô ấy, chỉ dịch 1…", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        fit_stack(recall, frog, now, cost, hint, buff=0.55, max_scale=1.2)
        with self.voice("Ở Bài 1, chú ếch mỗi bước chỉ nhảy 1, 2 hoặc 3 đá, nên công thức có ba số hạng."):
            self.play(FadeIn(recall), FadeIn(frog, shift=UP * 0.3), run_time=0.8)
        with self.voice("Nếu được nhảy bất kì độ dài nào từ 2 đến ba trăm nghìn, công thức có tới gần ba trăm nghìn số hạng cho mỗi "
                        "ô."):
            self.play(FadeIn(now), frog.animate.shift(UP * 0.3), run_time=0.6)
            self.play(frog.animate.shift(DOWN * 0.3), run_time=0.3)
        with self.voice("Một triệu ô cần khoảng 3 nhân 10 mũ 11 phép cộng: quá chậm."):
            self.play(FadeIn(cost), run_time=0.6)
        with self.voice("Nhưng hãy để ý: các số hạng ấy là các ô liên tiếp nhau trong bảng. Ô tiếp theo dùng gần như đúng các ô ấy, "
                        "chỉ dịch đi một vị trí."):
            self.play(FadeIn(hint), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán DEMCACHNHAY")
        task = tag_box("BÀI TOÁN: DEMCACHNHAY", [
            "Các đá 0, 1, …, n. Từ đá i nhảy tới đá i + d với",
            "L ≤ d ≤ R. Đếm số cách đi từ đá 0 tới đá n,",
            "lấy dư cho 10⁹ + 7.   (1 ≤ L ≤ R ≤ n ≤ 10⁶)",
        ], width=7.5, size=28)
        ex = VGroup(M("7 2 3", size=32, color=BLUEC), T("→", size=32), TB("3 cách", size=36, color=GOOD)).arrange(RIGHT, buff=0.3)
        row = stone_row(7)
        arcs_slot = placeholder(7.0, 1.2)
        seq_slot = placeholder(7.0, 0.7)
        sc = fit_stack(task, ex, VGroup(arcs_slot, row).arrange(DOWN, buff=0.05), seq_slot, buff=0.55, max_scale=1.2)
        with self.voice("Bài toán DEMCACHNHAY: các đá đánh số từ 0 đến n. Từ đá i được nhảy tới đá i cộng d, với d từ L đến R. "
                        "Đếm số cách đi từ đá 0 tới đá n, lấy dư cho 10 mũ 9 cộng 7. n tới một triệu."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Ví dụ: n bằng 7, mỗi bước nhảy 2 hoặc 3 đá. Có 3 cách."):
            self.play(FadeIn(ex), FadeIn(row), run_time=0.8)
        cols = [GOOD, ORANGE, PURPLE]
        cur_arcs, cur_seq = None, None
        for (steps, col) in zip([[2, 2, 3], [2, 3, 2], [3, 2, 2]], cols):
            pos = [0]
            for d in steps:
                pos.append(pos[-1] + d)
            arcs = VGroup(*[arc(row[a], row[b], col) for a, b in zip(pos, pos[1:])])
            seq = M(" + ".join(map(str, steps)) + " = 7", size=32, color=col).scale(sc).move_to(seq_slot)
            with self.voice(f"Cách: {', '.join(map(str, steps))}."):
                if cur_arcs is None:
                    self.play(Create(arcs), FadeIn(seq), run_time=0.8)
                    cur_arcs, cur_seq = arcs, seq
                else:
                    self.play(Transform(cur_arcs, arcs), Transform(cur_seq, seq), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_02_NgayTho(B13Scene):
    def construct(self):
        self.show_header("2. Ngây thơ: Cộng đủ R − L + 1 số hạng")
        why = VGroup(T("Lập luận “bước cuối cùng” của Bài 1:", size=28),
                     T("bước cuối dài d ∈ [L, R]", size=28, color=MUTED)).arrange(DOWN, buff=0.08)
        f = panel(VGroup(M("f(i) = f(i−R) + … + f(i−L)", size=30, color=ACCENT),
                         M("f(0) = 1  (bỏ chỉ số âm)", size=26, color=MUTED)).arrange(DOWN, buff=0.12), stroke=ACCENT)
        arr = ghost_row(8, w=0.85, h=0.85, size=34, label="f")
        win_slot = placeholder(7.0, 0.6)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Mỗi ô cộng R − L + 1 số hạng, n ô: O(n·(R − L + 1))",
            "n = 10⁶, L = 1, R = 5·10⁵:  ≈ 5·10¹¹ phép",
        ], accent=BLUEC, width=7.5, size=27)
        cnt[3][1].set_color(BAD)
        sc = fit_stack(why, f, VGroup(arr, win_slot).arrange(DOWN, buff=0.1), cnt, buff=0.6, max_scale=1.2)
        with self.voice("Theo đúng lập luận bước cuối cùng của Bài 1: bước cuối có độ dài d từ L đến R, nên f của i bằng tổng f "
                        "từ i trừ R đến i trừ L. f của 0 bằng 1, bỏ qua các chỉ số âm."):
            self.play(FadeIn(why), FadeIn(f), run_time=1.0)
            self.play(FadeIn(arr), run_time=0.6)
        with self.voice("Với L bằng 2, R bằng 3: điền lần lượt. f của 1 bằng 0, vì không bước nào dài 1."):
            self.play(setv(arr.cells[0], 1, GOOD), run_time=0.4)
            self.play(setv(arr.cells[1], 0), run_time=0.4)
        box = None
        for i in range(2, 8):
            lo, hi = max(0, i - 3), i - 2
            r = SurroundingRectangle(VGroup(*arr.cells[lo:hi + 1]), color=ACCENT, buff=0.04, stroke_width=4)
            txt = M(f"f({i}) = " + " + ".join(f"f({j})" for j in range(lo, hi + 1)) + f" = {F7[i]}", size=26,
                    color=ACCENT).scale(sc).move_to(win_slot)
            sp = (f"f của {i} bằng tổng của đoạn từ {lo} đến {hi}, bằng {F7[i]}." if i < 7 else
                  "f của 7 bằng f của 4 cộng f của 5, bằng 3. Đúng ba cách.")
            with self.voice(sp, min_duration=1.6):
                if box is None:
                    box, line = r, txt
                    self.play(Create(box), FadeIn(line), run_time=0.4)
                else:
                    self.play(Transform(box, r), Transform(line, txt), run_time=0.4)
                c = arr.cells[i]
                self.play(setv(c, F7[i], GOOD if i == 7 else INK), run_time=0.4)
        with self.voice("Mỗi ô cộng R trừ L cộng 1 số hạng. Với n bằng một triệu, L bằng 1, R bằng năm trăm nghìn: khoảng 5 nhân "
                        "10 mũ 11 phép."):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Bế tắc: Cộng lại gần như cùng các số")
        n = 12
        cells = VGroup(*[Square(0.6, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED, stroke_width=2)
                         for _ in range(n)]).arrange(RIGHT, buff=0)
        idx = VGroup()
        w1 = SurroundingRectangle(VGroup(*cells[1:9]), color=BLUEC, buff=0.03, stroke_width=5)
        w2 = SurroundingRectangle(VGroup(*cells[2:10]), color=ORANGE, buff=0.12, stroke_width=5)
        l1 = T("đoạn của f(i)", size=28, color=BLUEC).next_to(w1, UP, buff=0.2)
        l2 = T("đoạn của f(i + 1)", size=28, color=ORANGE).next_to(w2, DOWN, buff=0.2)
        strip = VGroup(cells, idx, w1, w2, l1, l2)
        dead = VGroup(T("[i − R, i − L] và [i − R + 1, i − L + 1]", size=28),
                      TB("gần như TRÙNG NHAU!", size=34, color=BAD),
                      T("Mỗi lần lại cộng từ đầu gần như cùng các số ấy.", size=28)).arrange(DOWN, buff=0.15)
        diff = VGroup(T("Chỉ khác: bỏ 1 ô ở đầu, thêm 1 ô ở cuối", size=28, color=GOOD)).arrange(DOWN)
        fit_stack(strip, dead, diff, buff=0.8, max_scale=1.2)
        self.play(FadeIn(cells), FadeIn(idx), run_time=0.5)
        with self.voice("Bế tắc nằm ở đâu? f của i và f của i cộng 1 là tổng của hai đoạn gần như trùng nhau."):
            self.play(Create(w1), FadeIn(l1), run_time=0.6)
            self.play(Create(w2), FadeIn(l2), run_time=0.6)
            self.play(FadeIn(dead[0:2]), run_time=0.6)
        with self.voice("Mỗi lần ta lại cộng lại từ đầu gần như cùng các số ấy. Chúng chỉ khác nhau ở một ô đầu và một ô cuối."):
            self.play(FadeIn(dead[2]), run_time=0.5)
            self.play(cells[1].animate.set_fill(BAD, 0.8), cells[9].animate.set_fill(GOOD, 0.8), FadeIn(diff), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_03_CongDon(B13Scene):
    def construct(self):
        self.show_header("3. Mảng cộng dồn chạy song song với bảng")
        d = VGroup(M("S[i] = f(0) + f(1) + … + f(i−1)", size=28, color=BLUEC), M("S[0] = 0", size=26, color=MUTED)
                   ).arrange(DOWN, buff=0.1)
        f = panel(VGroup(M("f(i) = S[i−L+1] − S[max(0, i−R)]", size=29, color=ACCENT),
                         T("(khi i − L ≥ 0)", size=24, color=MUTED)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        fr = ghost_row(8, w=0.82, h=0.8, size=32, label="f")
        sr = ghost_row(9, w=0.82, h=0.8, size=32, label="S")
        # S[k] nằm giữa ô f(k−1) và f(k): dịch nửa ô sang trái
        rows = VGroup(fr, sr).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        sr.shift(LEFT * 0.41)
        calc_slot = placeholder(7.2, 0.7)
        key = VGroup(T("Tính xong f(i) ⇒ cập nhật ngay S[i + 1] = S[i] + f(i)", size=27, color=GOOD),
                     T("Mọi S cần dùng (chỉ số ≤ i − L + 1 ≤ i) đều đã có", size=26, color=MUTED)).arrange(DOWN, buff=0.08)
        sc = fit_stack(d, f, rows, calc_slot, key, buff=0.5, max_scale=1.15)
        with self.voice("Phá bế tắc: gọi S của i là tổng f của 0 đến f của i trừ 1, với S của 0 bằng 0. Tổng của một đoạn bất kì "
                        "là hiệu của hai giá trị S."):
            self.play(FadeIn(d), run_time=0.8)
        with self.voice("Vậy f của i bằng S của i trừ L cộng 1, trừ S của max của 0 và i trừ R."):
            self.play(FadeIn(f), run_time=0.8)
        with self.voice("Điểm mấu chốt: mảng S được xây đồng thời với bảng f. Tính xong f của i, ta cập nhật ngay S của i cộng 1."):
            self.play(FadeIn(fr), FadeIn(sr), FadeIn(key[0]), run_time=0.8)

        with self.voice("Ban đầu f của 0 bằng 1, S của 0 bằng 0 và S của 1 bằng 1."):
            self.play(setv(fr.cells[0], 1, GOOD), setv(sr.cells[0], 0, BLUEC), run_time=0.4)
            self.play(setv(sr.cells[1], 1, BLUEC), run_time=0.4)
        cur = None
        for i in range(1, 8):
            to, frm = i - 2, max(0, i - 3)
            if to >= 0:
                txt = f"f({i}) = S[{to + 1}] − S[{frm}] = {S7[to + 1]} − {S7[frm]} = {F7[i]}"
                sp = f"f của {i} bằng S của {to + 1} trừ S của {frm}, bằng {S7[to + 1]} trừ {S7[frm]}, bằng {F7[i]}."
            else:
                txt = f"f({i}) = 0  (i − L < 0)"
                sp = "f của 1 bằng 0, vì i trừ L âm."
            if i == 7:
                sp += " Chỉ một phép trừ, thay vì cộng cả đoạn!"
            line = M(txt, size=26, color=ACCENT).scale(sc).move_to(calc_slot)
            with self.voice(sp, min_duration=1.8):
                hl = []
                if to >= 0:
                    hl = [sr.cells[to + 1][0].animate.set_fill(GOOD, 0.7), sr.cells[frm][0].animate.set_fill(BAD, 0.7)]
                self.play(FadeIn(line) if cur is None else Transform(cur, line), *hl, run_time=0.5)
                if cur is None:
                    cur = line
                self.play(setv(fr.cells[i], F7[i], GOOD if i == 7 else INK), run_time=0.4)
                self.play(setv(sr.cells[i + 1], S7[i + 1], BLUEC),
                          *[sr.cells[k][0].animate.set_fill(PANEL_2, 1) for k in range(9)], run_time=0.4)
        with self.voice("Khi tính f của i, mọi giá trị S cần dùng, với chỉ số tới i trừ L cộng 1, không vượt quá i, đều đã có sẵn."):
            self.play(FadeIn(key[1]), run_time=0.6)

        self.clear_body()
        self.show_header("DEMCACHNHAY.CPP: O(n)")
        code = code_block(PREFIX_CODE, size=22)
        trap = tag_box("CHÚ Ý: TRỪ TRONG ĐỒNG DƯ", [
            "S[6] mod p có thể NHỎ HƠN S[4] mod p ⇒ hiệu âm!",
            "Luôn viết: (prefix[to+1] − prefix[from] + MOD) % MOD",
        ], accent=BAD, width=7.5, size=26)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "Mỗi ô O(1): tổng O(n). n = 10⁶: vài triệu phép,",
            "nhanh hơn cách ngây thơ khoảng 10⁵ lần",
        ], accent=GOOD, width=7.5, size=27)
        fit_stack(code, trap, cx, buff=0.55, max_scale=1.2)
        with self.voice("Code: mảng ways là f, mảng prefix là S. Với mỗi i, tính đoạn from đến to; nếu to không âm thì f bằng hiệu "
                        "hai giá trị prefix; cuối cùng cập nhật prefix của i cộng 1."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 3, BLUEC)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 6, ACCENT)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.4)
        with self.voice("Chú ý: phép trừ trong số học đồng dư có thể cho kết quả âm, vì S của 6 lấy dư có thể nhỏ hơn S của 4 lấy "
                        "dư. Ta cộng thêm MOD trước khi lấy dư. Đây là lỗi kinh điển khi kết hợp cộng dồn với lấy dư."):
            self.play(Transform(hl, line_box(code, 7, BAD)), FadeIn(trap), run_time=0.8)
        with self.voice("Mỗi ô O của 1, tổng O của n: với n bằng một triệu, chỉ vài triệu phép, nhanh hơn cách ngây thơ khoảng 10 "
                        "mũ 5 lần."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_04_NhayXa(B13Scene):
    def construct(self):
        self.show_header("4. Bài toán NHAYXA: Max trên cửa sổ trượt")
        intro = VGroup(T("Đổi “đếm” thành “tối ưu”: tổng trở thành MAX.", size=28),
                       T("Không có phép “trừ” cho max ⇒ cộng dồn bó tay!", size=28, color=BAD)).arrange(DOWN, buff=0.1)
        task = tag_box("BÀI TOÁN: NHAYXA", [
            "Đá 0..n, đá i có điểm a_i (có thể âm). Từ đá 0,",
            "mỗi bước nhảy tới trước 1..k đá, dừng đúng ở đá n.",
            "Tìm TỔNG ĐIỂM các đá đặt chân LỚN NHẤT.",
            "1 ≤ k ≤ n ≤ 10⁶",
        ], width=7.5, size=27)
        row = stone_row(8, labels=["0"] + [f"{v}" for v in SCORE[1:]])
        for i in range(1, 9):
            row[i][0].set_fill(GOOD if SCORE[i] > 0 else BAD, 1)
        idx = VGroup(*[T(f"đá {i}" if i == 0 else str(i), size=20, color=MUTED).next_to(row[i], DOWN, buff=0.1)
                       for i in range(9)])
        arcs_slot = placeholder(7.0, 1.0)
        res = VGroup(M("0 → 1 → 4 → 7 → 8", size=30, color=ACCENT), TB("2 + 4 + 3 + 1 = 10", size=34, color=GOOD)
                     ).arrange(DOWN, buff=0.12)
        sc = fit_stack(intro, task, VGroup(arcs_slot, row, idx).arrange(DOWN, buff=0.08), res, buff=0.5, max_scale=1.2)
        with self.voice("Đổi câu hỏi từ đếm sang tối ưu, và tổng trở thành max. Mảng cộng dồn không giúp được nữa, vì không có "
                        "phép trừ cho max."):
            self.play(FadeIn(intro), run_time=0.8)
        with self.voice("Bài toán NHAYXA: các đá từ 0 đến n, đá i có điểm a i, có thể âm. Đứng ở đá 0, mỗi bước nhảy tới trước "
                        "từ 1 đến k đá, phải dừng đúng ở đá n. Tìm tổng điểm lớn nhất của các đá đặt chân."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Ví dụ: tám đá với điểm 2, âm 5, âm 1, 4, âm 8, âm 2, 3, 1; k bằng 3."):
            self.play(FadeIn(row), FadeIn(idx), run_time=0.8)
        path = [0, 1, 4, 7, 8]
        arcs = VGroup(*[arc(row[a], row[b], ACCENT) for a, b in zip(path, path[1:])])
        with self.voice("Cách tốt nhất: 0, 1, 4, 7, 8, né các đá điểm âm bằng các bước nhảy xa. Tổng 2 cộng 4 cộng 3 cộng 1 bằng 10."):
            self.play(Create(arcs), run_time=1.2)
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("Công thức và chi phí")
        f = panel(VGroup(M("best(i) = a_i + max best(j)", size=30, color=ACCENT),
                         M("với i − k ≤ j ≤ i − 1;  best(0) = 0", size=26, color=MUTED)).arrange(DOWN, buff=0.12), stroke=ACCENT)
        n = 14
        cells = VGroup(*[Square(0.48, fill_color=PANEL_2, fill_opacity=1, stroke_color=MUTED, stroke_width=2)
                         for _ in range(n)]).arrange(RIGHT, buff=0)
        win = SurroundingRectangle(VGroup(*cells[3:8]), color=GOOD, buff=0.04, stroke_width=5)
        cur = cells[8].copy().set_fill(ACCENT, 0.8)
        wl = T("cửa sổ k ô ngay trước i", size=24, color=GOOD).next_to(win, UP, buff=0.12)
        strip = VGroup(cells, win, cur, wl)
        cost = VGroup(T("Tính thẳng: O(n·k)", size=30),
                      T("n = k = 10⁶ ⇒ 10¹² phép", size=30, color=BAD)).arrange(DOWN, buff=0.1)
        q = TB("Lấy max của cửa sổ TRƯỢT nhanh thế nào?", size=32, color=ACCENT)
        fit_stack(f, strip, cost, q, buff=0.8, max_scale=1.2)
        with self.voice("Công thức: best của i bằng a i cộng max của best j, với j trong cửa sổ k ô ngay trước i. best của 0 bằng 0."):
            self.play(FadeIn(f), run_time=0.8)
            self.play(FadeIn(cells), FadeIn(cur), Create(win), FadeIn(wl), run_time=0.8)
        with self.voice("Mỗi bước cửa sổ trượt sang phải một ô."):
            for _ in range(3):
                self.play(win.animate.shift(RIGHT * 0.48), cur.animate.shift(RIGHT * 0.48), wl.animate.shift(RIGHT * 0.48),
                          run_time=0.4)
        with self.voice("Tính thẳng tốn O của n nhân k; với n và k bằng một triệu là 10 mũ 12 phép. Làm sao lấy max của cửa sổ "
                        "trượt thật nhanh?"):
            self.play(FadeIn(cost), run_time=0.6)
            self.play(FadeIn(q), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_05_HangDoi(B13Scene):
    def construct(self):
        self.show_header("5. Phá bế tắc: Hàng đợi đơn điệu")
        s1 = VGroup(TB("Bước 1: Ứng viên nào VÔ DỤNG?", size=30, color=ACCENT),
                    T("j < j′ cùng trong cửa sổ và best(j) ≤ best(j′):", size=28)).arrange(DOWN, buff=0.12)
        # minh họa hai cột
        bj = VGroup(Rectangle(width=0.8, height=1.2, fill_color=BLUEC, fill_opacity=0.9, stroke_width=0),
                    T("j", size=28)).arrange(DOWN, buff=0.1)
        bj2 = VGroup(Rectangle(width=0.8, height=2.0, fill_color=GOOD, fill_opacity=0.9, stroke_width=0),
                     T("j′", size=28)).arrange(DOWN, buff=0.1)
        pair = VGroup(bj, bj2).arrange(RIGHT, buff=1.2, aligned_edge=DOWN)
        reasons = VGroup(T("• j RỜI cửa sổ TRƯỚC j′", size=28),
                         T("• Khi cả hai còn trong cửa sổ, j′ tốt bằng/hơn j", size=28),
                         TB("⇒ j không bao giờ là đáp án nữa: VỨT ĐI!", size=30, color=BAD)).arrange(DOWN, aligned_edge=LEFT,
                                                                                                    buff=0.12)
        s2 = VGroup(TB("Bước 2: Hàng đợi hai đầu (deque)", size=30, color=ACCENT),
                    T("Vị trí TĂNG dần, best GIẢM dần", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        steps = VGroup(T("1. Bỏ ĐẦU hàng các j đã ra khỏi cửa sổ (j < i − k)", size=26),
                       T("2. best(i) = best(đầu hàng) + a_i", size=26, color=ACCENT),
                       T("3. Bỏ CUỐI hàng các j có best ≤ best(i); thêm i", size=26)).arrange(DOWN, aligned_edge=LEFT,
                                                                                            buff=0.1)
        fit_stack(s1, pair, reasons, s2, steps, buff=0.45, max_scale=1.15)
        with self.voice("Bước một: ứng viên nào không bao giờ còn hữu ích? Giả sử j nhỏ hơn j phẩy, cả hai đều trong cửa sổ, và best "
                        "của j không lớn hơn best của j phẩy."):
            self.play(FadeIn(s1), FadeIn(pair), run_time=0.8)
        with self.voice("Khi cửa sổ trượt sang phải, j sẽ rời cửa sổ trước j phẩy. Trong lúc cả hai còn trong cửa sổ, j phẩy luôn "
                        "tốt bằng hoặc hơn j. Vậy j không bao giờ là đáp án nữa: vứt nó đi được!"):
            self.play(FadeIn(reasons[0:2]), run_time=0.8)
            self.play(FadeIn(reasons[2]), bj.animate.set_opacity(0.25), run_time=0.6)
        with self.voice("Bước hai: sau khi vứt hết ứng viên vô dụng, các vị trí còn lại xếp tăng dần có best giảm dần. Ta giữ chúng "
                        "trong một hàng đợi hai đầu."):
            self.play(FadeIn(s2), run_time=0.6)
        with self.voice("Mỗi bước: bỏ đầu hàng các vị trí đã ra khỏi cửa sổ; đầu hàng chính là vị trí có best lớn nhất, nên best "
                        "của i bằng best đầu hàng cộng a i; rồi bỏ cuối hàng các vị trí có best không lớn hơn best của i, và "
                        "thêm i vào cuối."):
            self.play(LaggedStart(*[FadeIn(s) for s in steps], lag_ratio=0.5), run_time=1.5)

        # -------- chạy tay
        self.clear_body()
        self.show_header("Chạy tay với k = 3")
        a_row = array_row([str(v) for v in SCORE], w=0.78, h=0.7, size=26, label="a")
        a_row.cells[0][1].set_opacity(0)
        b_row = ghost_row(9, w=0.78, h=0.8, size=28, show_index=False, label="best")
        rows = VGroup(a_row, b_row).arrange(DOWN, buff=0.25, aligned_edge=RIGHT)
        dq_lab = TB("deque:", size=30, color=ACCENT)
        dq_slot = placeholder(5.6, 1.3)
        dq = VGroup(dq_lab, dq_slot).arrange(RIGHT, buff=0.3)
        info_slot = placeholder(7.2, 1.3)
        sc = fit_stack(rows, dq, info_slot, buff=0.9, max_scale=1.15)
        self.play(FadeIn(rows), FadeIn(dq_lab), run_time=0.6)

        def dq_mob(items):
            boxes = VGroup()
            for j in items:
                b = VGroup(RoundedRectangle(width=1.3, height=1.25, corner_radius=0.14, fill_color=PANEL_2, fill_opacity=1,
                                            stroke_color=GOOD, stroke_width=3),
                           VGroup(TB(str(j), size=36), T(f"best {BEST[j]}", size=22, color=ACCENT)).arrange(DOWN, buff=0.06))
                b[1].move_to(b[0])
                boxes.add(b)
            boxes.arrange(RIGHT, buff=0.12)
            boxes.scale(sc)
            boxes.next_to(dq_lab, RIGHT, buff=0.3)
            return boxes

        def info(lines):
            g = VGroup(*[T(l, size=30, color=c) for l, c in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.08).scale(sc)
            if g.width > info_slot.width:
                g.scale_to_fit_width(info_slot.width)
            return g.move_to(info_slot)

        with self.voice("Ban đầu best của 0 bằng 0, hàng đợi chỉ có vị trí 0. Mỗi ô trong hàng đợi ghi vị trí và best của nó."):
            self.play(setv(b_row.cells[0], 0), run_time=0.3)
            cur_dq = dq_mob([0])
            self.play(FadeIn(cur_dq), run_time=0.4)
        cur_info = None
        texts = {
            1: "i bằng 1: đầu hàng là 0, best của 1 bằng 0 cộng 2 bằng 2. Vị trí 0 có best 0, không lớn hơn 2, bị bỏ.",
            2: "i bằng 2: đầu hàng là 1, best bằng 2 trừ 5 bằng âm 3. Thêm 2 vào cuối; hàng đợi vẫn giảm dần.",
            3: "i bằng 3: cửa sổ là 0, 1, 2; đầu hàng là 1, best của 3 bằng 2 trừ 1 bằng 1. Vị trí 2 có best âm 3 bị bỏ.",
            4: "i bằng 4: đầu hàng vẫn là 1, best của 4 bằng 2 cộng 4 bằng 6. Vị trí 1 và 3 đều bị bỏ vì best không lớn hơn 6.",
            5: "i bằng 5: best bằng 6 trừ 8 bằng âm 2, thêm vào cuối.",
            6: "i bằng 6: best bằng 6 trừ 2 bằng 4; vị trí 5 bị bỏ.",
            7: "i bằng 7: vị trí 4 vẫn trong cửa sổ, best bằng 6 cộng 3 bằng 9; mọi vị trí khác bị bỏ.",
            8: "i bằng 8: best bằng 9 cộng 1 bằng 10. Đáp án 10!",
        }
        prev = [0]
        for (i, pf, head, pb, win) in QLOG:
            lines = []
            if pf:
                lines.append((f"bỏ đầu: {', '.join(map(str, pf))} (ra khỏi cửa sổ)", BAD))
            lines.append((f"best({i}) = best({head}) + a_{i} = {BEST[head]} + ({SCORE[i]}) = {BEST[i]}", ACCENT))
            if pb:
                lines.append((f"bỏ cuối: {', '.join(map(str, pb))} (best ≤ {BEST[i]}); thêm {i}", ORANGE))
            else:
                lines.append((f"thêm {i} vào cuối", GOOD))
            with self.voice(texts[i]):
                win_rect = SurroundingRectangle(VGroup(*b_row.cells[max(0, i - K):i]), color=GOOD, buff=0.04, stroke_width=4)
                new_info = info(lines)
                self.play(Create(win_rect), FadeIn(new_info) if cur_info is None else Transform(cur_info, new_info),
                          b_row.cells[i][0].animate.set_stroke(ACCENT, 4), run_time=0.5)
                if cur_info is None:
                    cur_info = new_info
                if pf:
                    mid = dq_mob([j for j in prev if j not in pf])
                    self.play(Transform(cur_dq, mid), run_time=0.4)
                self.play(Indicate(cur_dq[0], color=ACCENT), setv(b_row.cells[i], BEST[i], GOOD if i == 8 else INK),
                          run_time=0.5)
                self.play(Transform(cur_dq, dq_mob(win)), run_time=0.5)
                self.play(FadeOut(win_rect), b_row.cells[i][0].animate.set_stroke(MUTED, 2), run_time=0.3)
            prev = win

        self.clear_body()
        self.show_header("NHAYXA.CPP: O(n)")
        code = code_block(DEQUE_CODE, size=22)
        why = tag_box("VÌ SAO LÀ O(n)?", [
            "Hai vòng while, nhưng MỖI VỊ TRÍ được thêm vào",
            "hàng đợi đúng 1 lần và lấy ra tối đa 1 lần",
            "⇒ cả chương trình: ≤ 2n lần chạy while ⇒ O(n)",
            "Đánh giá tổng chi phí như vậy: PHÂN TÍCH KHẤU HAO",
        ], accent=PURPLE, width=7.5, size=27)
        why[3][3].set_color(GOOD)
        fit_stack(code, why, buff=0.7, max_scale=1.2)
        with self.voice("Code: hàng đợi window bắt đầu bằng vị trí 0. Với mỗi i: bỏ đầu hàng các vị trí ra khỏi cửa sổ, lấy best "
                        "từ đầu hàng, bỏ cuối hàng các vị trí không tốt hơn, rồi thêm i."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 3, BAD)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 5, ACCENT)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 7, ORANGE)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.4)
        with self.voice("Vì sao là O của n? Trong vòng lặp có hai vòng while, nhưng mỗi vị trí được thêm vào hàng đợi đúng một lần "
                        "và bị lấy ra tối đa một lần. Tổng số lần chạy của cả hai vòng while không vượt quá 2n."):
            self.play(FadeOut(hl), FadeIn(why[0:3]), FadeIn(why[3][0:3]), run_time=1.0)
        with self.voice("Một bước riêng lẻ có thể tốn nhiều thao tác, nhưng tổng vẫn là O của n. Kiểu đánh giá tổng chi phí trên "
                        "toàn bộ thuật toán này gọi là phân tích khấu hao."):
            self.play(FadeIn(why[3][3]), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B13_06_TongKet(B13Scene):
    def construct(self):
        self.show_header("6. Mở rộng: Nhận dạng kiểu tăng tốc")
        rows = [
            ("Tổng (xor) trên đoạn liên tiếp", "Mảng cộng dồn", "phép toán có “phép ngược”", BLUEC),
            ("Max/min, đoạn có HAI ĐẦU cùng tăng", "Hàng đợi đơn điệu", "cửa sổ chỉ trượt sang phải", GOOD),
            ("Max/min/tổng theo GIÁ TRỊ", "Cây Fenwick (Bài 14)", "truy vấn tiền tố", ORANGE),
        ]
        cards = VGroup()
        for a, b, c, col in rows:
            g = VGroup(T(a, size=27), VGroup(T("→", size=28), TB(b, size=29, color=col)).arrange(RIGHT, buff=0.2),
                       T("điều kiện: " + c, size=24, color=MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            p = panel(g, width=7.5, stroke=col, pad=0.25)
            p[1].align_to(p[0], LEFT).shift(RIGHT * 0.25)
            cards.add(p)
        cards.arrange(DOWN, buff=0.3)
        fit_stack(cards, max_scale=1.3)
        speech = [
            "Mở rộng một: nhận dạng kiểu tăng tốc. Công thức chứa tổng, hoặc xor, trên một đoạn liên tiếp: dùng mảng cộng dồn, "
            "với điều kiện phép toán có phép ngược, như phép trừ.",
            "Công thức chứa max hoặc min trên một đoạn có hai đầu cùng tăng: dùng hàng đợi đơn điệu, vì cửa sổ chỉ trượt sang "
            "phải.",
            "Còn max, min hay tổng theo giá trị, trên đoạn bất kì: dùng cây Fenwick, sẽ học ở Bài 14.",
        ]
        for c, s in zip(cards, speech):
            with self.voice(s):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Mở rộng: hai ứng dụng nữa")
        ext = [
            ("Cái túi giới hạn số lượng: O(n·W)", "chia sức chứa theo c mod w ⇒ max cửa sổ dài q + 1",
             "Mở rộng hai: cái túi giới hạn số lượng ở Bài 5. Với loại hàng có q món, chia các sức chứa theo số dư khi chia "
             "cho w. Trong mỗi lớp, công thức trở thành max trên một cửa sổ trượt độ dài q cộng 1, tính bằng hàng đợi đơn "
             "điệu: cả bài chỉ O của n nhân W."),
            ("Chia kẹo có giới hạn", "ways(i, s) = Σ ways(i−1, s−t), t = 0..c_i: cộng dồn hàng",
             "Mở rộng ba: đếm số cách chia K viên kẹo cho n bạn, bạn thứ i nhận từ 0 đến c i viên. Công thức là tổng trên "
             "đoạn liên tiếp của hàng trước, tính bằng mảng cộng dồn: O của n nhân K."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Trừ trong đồng dư", "quên cộng thêm MOD ⇒ kết quả âm",
             "Bẫy một: trừ trong đồng dư mà không cộng thêm MOD, kết quả âm."),
            ("Lệch chỉ số mảng cộng dồn", "S[i] là tổng tới i − 1 hay tới i? Viết rõ!",
             "Bẫy hai: lệch chỉ số mảng cộng dồn. S của i là tổng tới i trừ 1 hay tới i? Viết rõ định nghĩa và thử trên ví dụ "
             "nhỏ."),
            ("Bỏ đầu hàng sai điều kiện", "j hợp lệ khi j ≥ i − k; bỏ khi j < i − k",
             "Bẫy ba: bỏ đầu hàng sai điều kiện. Vị trí j hợp lệ khi j lớn hơn hoặc bằng i trừ k."),
            ("< hay ≤ khi bỏ cuối hàng", "đều đúng cho bài max; ≤ giữ hàng ngắn hơn",
             "Bẫy bốn: so sánh nhỏ hơn hay nhỏ hơn hoặc bằng khi bỏ cuối hàng. Cả hai đều đúng cho bài max, nhưng nhỏ hơn hoặc "
             "bằng giữ hàng đợi ngắn hơn."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 13", [
            "• Tổng trên đoạn liên tiếp các ô trước:",
            "   mảng cộng dồn xây SONG SONG với bảng",
            "• Max/min trên cửa sổ trượt: hàng đợi đơn điệu;",
            "   mỗi phần tử vào 1 lần, ra 1 lần",
            "• Công thức không đổi, chỉ CÁCH TÍNH đổi:",
            "   O(n·k) thành O(n)",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: tổng trên đoạn liên tiếp các ô trước thì dùng mảng cộng dồn, xây song song với bảng. Max hoặc min "
                        "trên cửa sổ trượt thì dùng hàng đợi đơn điệu; mỗi phần tử vào một lần, ra một lần."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Công thức không đổi, chỉ cách tính đổi: O của n nhân k thành O của n."):
            self.play(FadeIn(mem[3][4:]), run_time=0.6)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["DEMCACHNHAY với n = 10,", "L = 3, R = 5: có bao nhiêu cách?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        ans = VGroup(M("5 + 5", size=32, color=GOOD), M("3 + 3 + 4,  3 + 4 + 3,  4 + 3 + 3", size=30, color=GOOD),
                     TB("Đáp số: 4 cách", size=42, color=GOOD)).arrange(DOWN, buff=0.15)
        nxt = VGroup(TB("Tiếp theo: BÀI 14", size=42, color=ACCENT),
                     T("Cây Fenwick và lũy thừa ma trận", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: với n bằng 10, L bằng 3, R bằng 5, có bao nhiêu cách? Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp số: 4 cách, gồm 5 cộng 5, và ba cách sắp xếp của 3, 3, 4."):
            self.play(FadeIn(ans), run_time=0.8)
        with self.voice("Bài tiếp theo, bài cuối cùng: quy hoạch động với cây Fenwick và lũy thừa ma trận. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
