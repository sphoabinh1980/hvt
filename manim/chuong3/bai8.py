"""BÀI 8 — Quy hoạch động trên đoạn (BOCXU — bỏ một đầu, NHANMATRAN — chọn điểm chia)."""

from shared import *  # noqa: F401,F403

COINS = [3, 9, 1, 2]
P = [10, 30, 5, 60, 10]


def lead_table(a):
    n = len(a)
    D = [[None] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        D[i][i] = a[i - 1]
    for ln in range(2, n + 1):
        for l in range(1, n - ln + 2):
            r = l + ln - 1
            D[l][r] = max(a[l - 1] - D[l + 1][r], a[r - 1] - D[l][r - 1])
    return D


def chain(p):
    n = len(p) - 1
    C = [[0] * (n + 1) for _ in range(n + 1)]
    K = [[0] * (n + 1) for _ in range(n + 1)]
    for ln in range(2, n + 1):
        for l in range(1, n - ln + 2):
            r = l + ln - 1
            C[l][r] = None
            for k in range(l, r):
                c = C[l][k] + C[k + 1][r] + p[l - 1] * p[k] * p[r]
                if C[l][r] is None or c < C[l][r]:
                    C[l][r], K[l][r] = c, k
    return C, K


def brackets(K, l, r):
    return f"A{l}" if l == r else "(" + brackets(K, l, K[l][r]) + brackets(K, K[l][r] + 1, r) + ")"


def all_par(p, l, r):
    if l == r:
        return [(f"A{l}", 0)]
    out = []
    for k in range(l, r):
        for x, cx in all_par(p, l, k):
            for y, cy in all_par(p, k + 1, r):
                out.append(("(" + x + y + ")", cx + cy + p[l - 1] * p[k] * p[r]))
    return out


LEAD = lead_table(COINS)
ANS = (sum(COINS) + LEAD[1][4]) // 2
COST, SPLIT = chain(P)
PARS = sorted(all_par(P, 1, 4), key=lambda z: z[1])
assert LEAD[1][4] == 7 and ANS == 11 and LEAD[1][3] == -5
assert COST[1][4] == 5000 and brackets(SPLIT, 1, 4) == "((A1A2)(A3A4))" and PARS[-1][1] == 33000
_q = lead_table([2, 7, 3])
assert (12 + _q[1][3]) // 2 == 5


class B8Scene(NarratedScene):
    lesson_tag = "BÀI 8"
    lesson_title = "Quy hoạch động trên đoạn"


def coin(v, r=0.5):
    c = Circle(radius=r, fill_color="#CA8A04", fill_opacity=1, stroke_color="#FDE68A", stroke_width=4)
    inner = Circle(radius=r * 0.78, stroke_color="#FDE68A", stroke_width=1.5, stroke_opacity=0.7).move_to(c)
    return VGroup(c, inner, TB(str(v), size=r * 70, color=BG).move_to(c))


# ----------------------------------------------------------------------------
class B8_00_Intro(B8Scene):
    def construct(self):
        chap = TB("CHƯƠNG 3", size=44, color=ACCENT)
        title = VGroup(TB("QUY HOẠCH ĐỘNG", size=60), TB("NÂNG CAO", size=60)).arrange(DOWN, buff=0.2)
        bar = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        cover = VGroup(chap, title, bar).arrange(DOWN, buff=0.35)
        kinds = VGroup(*[panel(T(t, size=28), pad=0.18, stroke=c) for t, c in
                         [("một ĐOẠN [l, r]", BLUEC), ("một TẬP HỢP (dãy bit)", GOOD), ("tiền tố CHỮ SỐ", ORANGE),
                          ("một CÂY CON", PURPLE)]])
        kinds.arrange_in_grid(rows=2, cols=2, buff=0.25)
        key = VGroup(T("Câu hỏi then chốt:", size=30, color=MUTED),
                     TB("“Để đi tiếp, ta cần nhớ gì về quá khứ?”", size=32, color=GOOD)).arrange(DOWN, buff=0.15)
        fit_stack(cover, kinds, key, buff=0.8, max_scale=1.15)
        with self.voice("Chào các em! Chúng ta bước sang Chương 3: Quy hoạch động nâng cao."):
            self.play(FadeIn(chap, shift=DOWN * 0.3), Write(title), run_time=1.8)
            self.play(GrowFromCenter(bar), run_time=0.5)
        with self.voice("Đến đây, trạng thái của em mới chỉ là i phần tử đầu, hay ô i, j trên lưới. Chương này mở rộng trí tưởng tượng "
                        "về trạng thái: trạng thái có thể là một đoạn, một tập hợp được mã hóa bằng dãy bit, một tiền tố của chữ số, "
                        "hay một cây con."):
            self.play(LaggedStart(*[FadeIn(k, scale=0.8) for k in kinds], lag_ratio=0.3), run_time=1.6)
        with self.voice("Câu hỏi then chốt vẫn không đổi: để đi tiếp, ta cần nhớ gì về quá khứ? Trả lời đúng câu hỏi ấy là chìa khóa "
                        "của các bài khó nhất trong đề thi."):
            self.play(FadeIn(key), run_time=1.0)

        self.clear_body()
        heading = TB("TRONG CHƯƠNG NÀY", size=42, color=ACCENT)
        items = [("Bài 8", "Quy hoạch động trên đoạn"), ("Bài 9", "Trạng thái tập con (bitmask)"),
                 ("Bài 10", "Quy hoạch động chữ số"), ("Bài 11", "Quy hoạch động trên cây"),
                 ("Bài 12", "Đếm, đồ thị, xác suất, kì vọng")]
        cards = VGroup()
        for tag, ttl in items:
            pill = RoundedRectangle(width=1.5, height=0.7, corner_radius=0.35, fill_color=ACCENT, fill_opacity=1,
                                    stroke_width=0)
            row = VGroup(VGroup(pill, TB(tag, size=28, color=BG).move_to(pill)), TB(ttl, size=29)).arrange(RIGHT, buff=0.3)
            c = panel(row, width=7.5, pad=0.22)
            c[1].align_to(c[0], LEFT).shift(RIGHT * 0.22)
            cards.add(c)
        cards.arrange(DOWN, buff=0.25)
        fit_stack(heading, cards, buff=0.6, max_scale=1.2)
        with self.voice("Chương này gồm năm bài: quy hoạch động trên đoạn, trạng thái tập con, quy hoạch động chữ số, trên cây, và "
                        "cuối cùng là đếm, đồ thị có hướng, xác suất và kì vọng."):
            self.play(FadeIn(heading), run_time=0.5)
            for c in cards:
                self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.5)

        self.clear_body()
        tag = TB("BÀI 8", size=80, color=ACCENT)
        ttl = TB("Quy hoạch động trên đoạn", size=48)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Trạng thái là một ĐOẠN [l, r]",
            "✓ Điền bảng theo ĐỘ DÀI đoạn tăng dần",
            "✓ “Bỏ một đầu” O(n²) và “chọn điểm chia” O(n³)",
            "✓ Truy vết điểm chia để in cách đặt ngoặc",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Bài 8: Quy hoạch động trên đoạn."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.4)
        with self.voice("Học xong bài này, em sẽ nhận ra các bài có trạng thái là một đoạn của dãy: trò chơi lấy hai đầu, ghép hoặc "
                        "chia đoạn; và điền bảng theo độ dài đoạn tăng dần, vì đoạn dài luôn được tính từ các đoạn ngắn hơn."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ phân biệt hai dạng chuyển trạng thái: bỏ một đầu, O của n bình phương, và chọn điểm chia, O của n mũ "
                        "ba; cùng cách truy vết điểm chia để in ra cách đặt ngoặc."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B8_01_BocXu(B8Scene):
    def construct(self):
        self.show_header("Khởi động: Trò chơi bốc xu hai đầu")
        row = VGroup(*[coin(v) for v in COINS]).arrange(RIGHT, buff=0.35)
        rule = VGroup(T("An đi trước, hai bạn lần lượt lấy;", size=28),
                      T("mỗi lượt chỉ lấy đồng xu ở MỘT TRONG HAI ĐẦU.", size=28, color=ACCENT),
                      T("Ai có tổng lớn hơn thì thắng.", size=28)).arrange(DOWN, buff=0.1)
        players = VGroup(
            VGroup(TB("An", size=32, color=BLUEC), placeholder(3.0, 0.9)).arrange(DOWN, buff=0.15),
            VGroup(TB("Bình", size=32, color=ORANGE), placeholder(3.0, 0.9)).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=0.8)
        res_slot = placeholder(7.3, 1.0)
        sc = fit_stack(rule, row, players, res_slot, buff=0.6, max_scale=1.15)
        with self.voice("An và Bình chơi một trò chơi với bốn đồng xu xếp thành hàng, mệnh giá 3, 9, 1, 2. Hai bạn lần lượt lấy, "
                        "An đi trước; mỗi lượt chỉ được lấy đồng xu ở một trong hai đầu hàng. Ai có tổng lớn hơn thì thắng."):
            self.play(FadeIn(rule), run_time=0.8)
            self.play(LaggedStart(*[GrowFromCenter(c) for c in row], lag_ratio=0.2), FadeIn(players[0][0]),
                      FadeIn(players[1][0]), run_time=1.2)

        def play_game(order, label):
            """order: danh sách (người, chỉ số đồng xu)."""
            copies = row.copy()
            self.add(copies)
            row.set_opacity(0)
            slots = {0: players[0][1].get_left() + RIGHT * 0.45 * sc, 1: players[1][1].get_left() + RIGHT * 0.45 * sc}
            tot = {0: 0, 1: 0}
            for who, idx in order:
                tot[who] += COINS[idx]
                self.play(copies[idx].animate.scale(0.75).move_to(slots[who]), run_time=0.55)
                slots[who] = slots[who] + RIGHT * 0.85 * sc
            return copies, tot

        with self.voice("An nghĩ: đầu trái là 3, đầu phải là 2, lấy 3 thôi! Nếu cả hai cứ lấy đầu lớn hơn: An lấy 3, Bình lấy 9, "
                        "An lấy 2, Bình lấy 1. An chỉ được 5."):
            copies, tot = play_game([(0, 0), (1, 1), (0, 3), (1, 2)], "tham lam")
            g = TB(f"Lấy đầu lớn hơn: An được {tot[0]}, thua!", size=32, color=BAD).scale(sc).move_to(res_slot)
            self.play(FadeIn(g), run_time=0.5)
        self.play(FadeOut(copies), FadeOut(g), run_time=0.4)
        row.set_opacity(1)
        with self.voice("Lấy đồng 3 trước làm lộ đồng 9 cho Bình. Nước đi tốt là lấy đồng 2, nhỏ hơn! Sau lượt của Bình, dù Bình lấy "
                        "3 hay lấy 1, đồng 9 vẫn nằm ở một đầu cho An. An được 2 cộng 9, bằng 11."):
            copies, tot = play_game([(0, 3), (1, 0), (0, 1), (1, 2)], "tối ưu")
            b = TB(f"Chơi tối ưu: An được {tot[0]}!", size=34, color=GOOD).scale(sc).move_to(res_slot)
            self.play(FadeIn(b), run_time=0.5)
        with self.voice("Trò chơi đối kháng đòi hỏi ta nghĩ trước nhiều nước, và tham lam lại thất bại."):
            self.play(Indicate(b, color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán BOCXU")
        box = tag_box("BÀI TOÁN: BOCXU", [
            "n đồng xu xếp thành hàng, đồng i mệnh giá aᵢ.",
            "Hai người lần lượt lấy một đồng ở đầu trái",
            "hoặc đầu phải. Cả hai chơi TỐI ƯU.",
            "Người đi trước được tổng bao nhiêu?",
            "n ≤ 2000",
        ], width=7.5, size=29)
        box[3][4].set_color(ORANGE)
        ex = VGroup(M("3 9 1 2", size=36), TB("→ 11", size=40, color=GOOD)).arrange(RIGHT, buff=0.4)
        fit_stack(box, ex, buff=0.8, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán BOCXU: n đồng xu xếp thành hàng. Hai người chơi lần lượt, mỗi lượt lấy "
                        "một đồng xu ở đầu trái hoặc đầu phải. Cả hai đều chơi tối ưu, luôn cố gắng làm tổng của mình lớn nhất. "
                        "Hỏi người đi trước được tổng bao nhiêu? n lên tới hai nghìn."):
            self.play(FadeIn(box), run_time=1.0)
            self.play(FadeIn(ex), run_time=0.5)
        self.clear_body()


# ----------------------------------------------------------------------------
class B8_02_HieuSo(B8Scene):
    def construct(self):
        self.show_header("2. Mẹo hiệu số và cây lời gọi")
        trick = VGroup(T("Thay vì theo dõi tổng của từng người,", size=29),
                       T("hãy theo dõi HIỆU SỐ của người đang đến lượt.", size=29, color=ACCENT)).arrange(DOWN, buff=0.1)
        defi = panel(VGroup(TB("hơn(l, r) =", size=34, color=ACCENT),
                            T("số điểm người ĐANG ĐẾN LƯỢT hơn được", size=27),
                            T("đối thủ khi còn các đồng xu l..r", size=27)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        moves = VGroup(
            panel(VGroup(TB("Lấy aₗ", size=30, color=BLUEC), T("đối thủ thành người đi", size=22),
                         M("aₗ − hơn(l+1, r)", size=26, color=BLUEC)).arrange(DOWN, buff=0.08), width=3.65, stroke=BLUEC),
            panel(VGroup(TB("Lấy aᵣ", size=30, color=GOOD), T("đối thủ thành người đi", size=22),
                         M("aᵣ − hơn(l, r−1)", size=26, color=GOOD)).arrange(DOWN, buff=0.08), width=3.65, stroke=GOOD),
        ).arrange(RIGHT, buff=0.2)
        pick = T("Người chơi tối ưu chọn nước có hiệu số LỚN HƠN.", size=28, color=GOOD)
        fit_stack(trick, defi, moves, pick, buff=0.6, max_scale=1.2)
        with self.voice("Một mẹo giúp bài toán gọn hơn hẳn: thay vì theo dõi tổng của từng người, hãy theo dõi hiệu số."):
            self.play(FadeIn(trick), run_time=0.8)
        with self.voice("Đặt hơn của l, r là số điểm mà người đang đến lượt hơn được đối thủ, khi trên bàn còn các đồng xu từ l đến r, "
                        "nếu cả hai chơi tối ưu."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Nếu người đang đến lượt lấy đồng a l, đối thủ trở thành người đang đến lượt với đoạn l cộng 1 đến r, và hơn "
                        "được hơn của l cộng 1, r. Vậy hiệu số của người đang đi là a l trừ hơn của l cộng 1, r. Tương tự nếu lấy a r."):
            self.play(FadeIn(moves[0]), run_time=0.6)
            self.play(FadeIn(moves[1]), run_time=0.6)
        with self.voice("Người chơi tối ưu chọn nước có hiệu số lớn hơn."):
            self.play(FadeIn(pick), run_time=0.6)

        self.clear_body()
        self.show_header("Cây lời gọi của hơn(1, 4)")
        nodes, edges = {}, []

        def build(l, r, depth, key):
            nodes[key] = (l, r, depth)
            if l < r:
                build(l + 1, r, depth + 1, key + "L")
                build(l, r - 1, depth + 1, key + "R")
                edges.append((key, key + "L"))
                edges.append((key, key + "R"))

        build(1, 4, 0, "")
        leaves = sorted([k for k, v in nodes.items() if v[0] == v[1]])
        xs = {}
        order = []

        def place(key):
            l, r, d = nodes[key]
            if l == r:
                xs[key] = len(order)
                order.append(key)
            else:
                place(key + "L")
                place(key + "R")
                xs[key] = (xs[key + "L"] + xs[key + "R"]) / 2

        place("")
        nleaf = len(order)
        mobs = {}
        for key, (l, r, d) in nodes.items():
            box = RoundedRectangle(width=0.82, height=0.6, corner_radius=0.1, fill_color=PANEL_2, fill_opacity=1,
                                   stroke_color=BLUEC, stroke_width=2.5)
            t = TB(f"[{l},{r}]", size=22).move_to(box)
            mobs[key] = VGroup(box, t).move_to([xs[key] * 7.4 / (nleaf - 1), -d * 1.5, 0])
        emobs = VGroup(*[Line(mobs[a].get_bottom(), mobs[b].get_top(), color=MUTED, stroke_width=2) for a, b in edges])
        tree = VGroup(emobs, *mobs.values())
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Mỗi đoạn dài ≥ 2 sinh 2 lời gọi con",
            "⇒ khoảng 2ⁿ nút: n = 30 ≈ 10⁹; n = 2000: không thể",
            "Nhưng chỉ có ≈ n²/2 ĐOẠN khác nhau (2·10⁶)!",
        ], accent=ORANGE, width=7.5, size=27)
        cnt[3][2].set_color(GOOD)
        fit_stack(tree, cnt, buff=0.8, max_scale=1.2)
        with self.voice("Vẽ cây lời gọi của hơn của 1, 4: mỗi đoạn dài ít nhất 2 sinh ra hai lời gọi con, với đoạn ngắn hơn đúng một "
                        "phần tử."):
            self.play(FadeIn(mobs[""]), run_time=0.4)
            for d in range(1, 4):
                anims = []
                for (a, b), e in zip(edges, emobs):
                    if nodes[b][2] == d:
                        anims += [Create(e), FadeIn(mobs[b])]
                self.play(*anims, run_time=0.8)
        dup = [k for k, v in nodes.items() if (v[0], v[1]) == (2, 3)]
        with self.voice("Đoạn 2, 3 bị tính hai lần. Với n lớn, mỗi đoạn bị tính lại số lần khổng lồ."):
            self.play(*[mobs[k][0].animate.set_fill(ACCENT, 1) for k in dup], *[mobs[k][1].animate.set_color(BG) for k in dup],
                      run_time=0.6)
            self.play(*[Indicate(mobs[k], color=ACCENT, scale_factor=1.25) for k in dup], run_time=0.8)
        with self.voice("Cây lời gọi có khoảng 2 mũ n nút. Nhưng trạng thái chỉ là một đoạn l, r: chỉ có khoảng n bình phương chia 2 "
                        "đoạn, tức hai triệu đoạn với n bằng hai nghìn. Bế tắc được phá bằng một bảng theo đoạn!"):
            self.play(FadeIn(cnt), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
BOC_CODE = """
for (int i = 1; i <= n; i++) lead[i][i] = a[i];
for (int len = 2; len <= n; len++)
  for (int l = 1; l + len - 1 <= n; l++) {
    int r = l + len - 1;
    lead[l][r] = max(a[l] - lead[l + 1][r],
                     a[r] - lead[l][r - 1]);
  }
cout << (total + lead[1][n]) / 2;
"""

LEN_COLORS = {1: "#334155", 2: "#1E3A8A", 3: "#6D28D9", 4: "#A16207"}


class B8_03_BangDoan(B8Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Điền bảng theo độ dài")
        formula = tag_box("CÔNG THỨC", [
            "hơn(l, r) = max( aₗ − hơn(l+1, r), aᵣ − hơn(l, r−1) )",
            "• Cơ sở: hơn(i, i) = aᵢ (còn một đồng, lấy nó)",
            "• S = tổng mọi đồng, D = hơn(1, n):",
            "  x − (S − x) = D  ⇒  người đi trước được (S + D)/2",
        ], width=7.5, size=27)
        formula[3][0].set_color(ACCENT)
        order = VGroup(T("Ô (l, r) cần (l+1, r) và (l, r−1): đoạn NGẮN HƠN 1.", size=27),
                       T("Điền theo l tăng dần là SAI (ô hàng dưới chưa có)!", size=27, color=BAD),
                       T("Đúng: độ dài 1, rồi 2, rồi 3… = từng ĐƯỜNG CHÉO.", size=27, color=GOOD)).arrange(DOWN, buff=0.1)
        fit_stack(formula, order, buff=0.8, max_scale=1.25)
        with self.voice("Công thức: hơn của l, r bằng max của a l trừ hơn của l cộng 1, r, và a r trừ hơn của l, r trừ 1. Cơ sở: "
                        "hơn của i, i bằng a i, còn một đồng thì lấy nó."):
            self.play(FadeIn(formula[0:3]), FadeIn(formula[3][0:2]), run_time=1.0)
        with self.voice("Đáp án: gọi S là tổng mọi đồng xu và D bằng hơn của 1, n. Người đi trước được x, người đi sau được S trừ x, "
                        "và hiệu bằng D, nên x bằng S cộng D, chia 2."):
            self.play(FadeIn(formula[3][2:]), run_time=0.8)
        with self.voice("Thứ tự điền là điểm mới của bài này. Ô l, r cần hai đoạn ngắn hơn đúng 1. Điền theo hàng từ trên xuống, l tăng "
                        "dần, sẽ sai, vì ô l cộng 1, r ở hàng dưới chưa có. Thứ tự đúng: điền tất cả các đoạn độ dài 1, rồi độ dài 2, "
                        "rồi độ dài 3. Trên bảng, đó là điền từng đường chéo."):
            for o in order:
                self.play(FadeIn(o), run_time=0.5)

        self.clear_body()
        self.show_header("Chạy tay với dãy 3, 9, 1, 2")
        coins = VGroup(*[coin(v, 0.4) for v in COINS]).arrange(RIGHT, buff=0.25)
        tbl = Table2D(4, 4, w=1.15, h=0.9, row_labels=["l=1", "l=2", "l=3", "l=4"], col_title="r")
        # nhãn cột 1..4 thay vì 0..3
        for k, lab in enumerate(tbl.labels[0]):
            lab.become(T(str(k + 1), size=22, color=MUTED).move_to(lab))
        for l in range(4):
            for r in range(l):
                tbl.cells[(l, r)][0].set_fill(BG, 1).set_stroke(opacity=0.2)
        eq_slot = placeholder(7.4, 1.1)
        res_slot = placeholder(7.4, 1.0)
        sc = fit_stack(coins, tbl, eq_slot, res_slot, buff=0.5, max_scale=1.3)
        eq = [None]

        def say(text, color=INK):
            new = M(text, size=28, color=color).scale(sc)
            if new.width > 7.4:
                new.scale_to_fit_width(7.4)
            new.move_to(eq_slot)
            if eq[0] is None:
                eq[0] = new
                return FadeIn(new)
            return Transform(eq[0], new)

        self.play(FadeIn(coins), FadeIn(tbl), run_time=0.8)

        def fill(l, r):
            v = LEAD[l][r]
            return AnimationGroup(*tbl.fill(l - 1, r - 1, v, fill=LEN_COLORS[r - l + 1]))

        with self.voice("Độ dài 1, đường chéo chính: hơn của i, i bằng a i: 3, 9, 1, 2."):
            self.play(say("hơn(i, i) = aᵢ"), LaggedStart(*[fill(i, i) for i in range(1, 5)], lag_ratio=0.25), run_time=1.2)
        with self.voice("Độ dài 2: hơn của 1, 2 bằng max của 3 trừ 9 và 9 trừ 3, bằng 6. hơn của 2, 3 bằng max của 9 trừ 1 và 1 trừ 9, "
                        "bằng 8. hơn của 3, 4 bằng max của 1 trừ 2 và 2 trừ 1, bằng 1."):
            self.play(say("hơn(1,2) = 6;  hơn(2,3) = 8;  hơn(3,4) = 1"),
                      LaggedStart(*[fill(i, i + 1) for i in range(1, 4)], lag_ratio=0.3), run_time=1.4)
        with self.voice("Độ dài 3: hơn của 1, 3 bằng max của 3 trừ 8 và 1 trừ 6, bằng trừ 5: ai đi trước với 3, 9, 1 sẽ thua 5 điểm. "
                        "hơn của 2, 4 bằng max của 9 trừ 1 và 2 trừ 8, bằng 8."):
            self.play(say("hơn(1,3) = max(3−8, 1−6) = −5;  hơn(2,4) = 8"),
                      LaggedStart(fill(1, 3), fill(2, 4), lag_ratio=0.4), run_time=1.2)
        with self.voice("Độ dài 4: hơn của 1, 4 bằng max của 3 trừ 8, và 2 trừ trừ 5. Bằng 7, đạt được khi lấy đồng 2!"):
            self.play(say("hơn(1,4) = max(3 − 8, 2 − (−5)) = 7", GOOD), fill(1, 4), run_time=1.0)
            self.play(Circumscribe(tbl.cells[(0, 3)], color=ACCENT), Indicate(coins[3], color=GOOD), run_time=0.8)
        res = TB("S = 15  ⇒  An được (15 + 7) / 2 = 11", size=34, color=GOOD).scale(sc).move_to(res_slot)
        with self.voice("Tổng S bằng 15, nên An được 15 cộng 7, chia 2, bằng 11."):
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("Code và độ phức tạp")
        code = code_block(BOC_CODE, size=20)
        note = VGroup(T("Vòng ngoài: len (độ dài đoạn); vòng trong: l;", size=27),
                      T("r suy ra. Khuôn mẫu của MỌI bài QHĐ trên đoạn.", size=27, color=ACCENT)).arrange(DOWN, buff=0.1)
        cx = VGroup(TB("O(n²)", size=44, color=GOOD), T("n = 2000: 4·10⁶ ô long long ≈ 32 MB", size=26)).arrange(DOWN, buff=0.1)
        mem = tag_box("CHỈ CẦN O(n) BỘ NHỚ", [
            "Độ dài k chỉ dùng độ dài k − 1: lưu lead[l] cho",
            "độ dài hiện tại, duyệt l tăng dần ⇒ mảng một chiều.",
        ], accent=PURPLE, width=7.5, size=26)
        fit_stack(code, note, cx, mem, buff=0.5)
        with self.voice("Code: vòng lặp ngoài là len, độ dài đoạn; vòng trong là l; r được suy ra từ hai biến này. Đó là "
                        "khuôn mẫu của mọi bài quy hoạch động trên đoạn."):
            self.play(FadeIn(code), FadeIn(note), run_time=0.8)
            hl = line_box(code, 1, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 2, ACCENT)), run_time=0.3)
        with self.voice("Bảng có khoảng n bình phương chia 2 ô có ích, mỗi ô O của 1: O của n bình phương thời gian và bộ nhớ."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.6)
        with self.voice("Thật ra chỉ cần O của n bộ nhớ: các đoạn độ dài k chỉ dùng các đoạn độ dài k trừ 1, nên lưu một mảng một chiều "
                        "theo điểm đầu l là đủ."):
            self.play(FadeIn(mem), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
MAT_CODE = """
for (int len = 2; len <= n; len++)
  for (int l = 1; l + len - 1 <= n; l++) {
    int r = l + len - 1;
    cost[l][r] = INF;
    for (int k = l; k < r; k++) {
      long long c = cost[l][k] + cost[k + 1][r]
                  + p[l - 1] * p[k] * p[r];
      if (c < cost[l][r]) {
        cost[l][r] = c;  split[l][r] = k;
      }
    }
  }
"""


def matrix_icon(name, rows, cols, unit=0.03):
    h = max(0.5, min(rows * unit * 1.1, 2.0))
    w = max(0.5, min(cols * unit * 1.1, 2.0))
    r = Rectangle(width=w, height=h, fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=3)
    t = VGroup(TB(name, size=26, color=ACCENT), T(f"{rows}×{cols}", size=20, color=MUTED)).arrange(DOWN, buff=0.04)
    t.move_to(r)
    if t.width > w:
        t.next_to(r, DOWN, buff=0.08)
    return VGroup(r, t)


class B8_04_NhanMaTran(B8Scene):
    def construct(self):
        self.show_header("4. Chọn điểm chia: Bài NHANMATRAN")
        box = tag_box("BÀI TOÁN: NHANMATRAN", [
            "Tính A₁·A₂·…·Aₙ, Aᵢ cỡ pᵢ₋₁ × pᵢ.",
            "Nhân (x × y)·(y × z) tốn x·y·z phép nhân số.",
            "Được tùy ý ĐẶT NGOẶC (tính kết hợp):",
            "đặt sao cho tổng số phép nhân ÍT NHẤT.  n ≤ 300",
        ], accent=BLUEC, width=7.5, size=28)
        mats = VGroup(*[matrix_icon(f"A{k + 1}", P[k], P[k + 1]) for k in range(4)]).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        p_lab = M("p = 10 30 5 60 10", size=30, color=MUTED)
        maxc = PARS[-1][1]
        bars = VGroup()
        for name, c in PARS:
            bw = 4.4 * c / maxc
            bar = Rectangle(width=max(bw, 0.1), height=0.5, fill_color=GOOD if c == PARS[0][1] else ORANGE, fill_opacity=0.9,
                            stroke_width=0)
            lab = M(name, size=22)
            val = TB(f"{c}", size=24)
            r = VGroup(lab, bar, val).arrange(RIGHT, buff=0.2)
            bars.add(r)
        for r in bars:
            r[1].align_to(bars[0][1], LEFT)
            r[2].next_to(r[1], RIGHT, buff=0.15)
        bars.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        for r in bars:
            r[0].align_to(bars, LEFT)
        for r in bars:
            r[1].next_to(r[0], RIGHT, buff=0.2).align_to(bars[0][1], LEFT)
            r[2].next_to(r[1], RIGHT, buff=0.15)
        fit_stack(box, VGroup(mats, p_lab).arrange(DOWN, buff=0.2), bars, buff=0.5, max_scale=1.2)
        with self.voice("Ở bài bốc xu, đoạn chỉ co lại một đầu. Dạng phổ biến hơn của quy hoạch động trên đoạn là chia đoạn thành hai "
                        "phần tại một điểm k. Bài toán NHANMATRAN: cần tính tích n ma trận. Nhân ma trận cỡ x nhân y với ma trận cỡ y "
                        "nhân z tốn x nhân y nhân z phép nhân số. Phép nhân có tính kết hợp, nên ta được tùy ý đặt ngoặc."):
            self.play(FadeIn(box), run_time=1.0)
        with self.voice("Ví dụ bốn ma trận với p bằng 10, 30, 5, 60, 10."):
            self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in mats], lag_ratio=0.2), FadeIn(p_lab), run_time=1.0)
        with self.voice("Có năm cách đặt ngoặc, tốn từ năm nghìn đến ba mươi ba nghìn phép nhân. Cách tốt nhất rẻ hơn cách tệ nhất "
                        "gần 7 lần!"):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in bars], lag_ratio=0.2), run_time=1.5)
            self.play(Indicate(bars[0], color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("Phép nhân CUỐI CÙNG chia đoạn tại k")
        naive = VGroup(T("Thử mọi cách đặt ngoặc: số Catalan, tăng ≈ 4ⁿ", size=28),
                       T("n = 20: 1,77·10⁹ cách;  n = 300: không tưởng", size=28, color=BAD)).arrange(DOWN, buff=0.1)
        split = VGroup(T("(Aₗ … Aₖ)", size=36, color=BLUEC), T("·", size=40),
                       T("(Aₖ₊₁ … Aᵣ)", size=36, color=GOOD)).arrange(RIGHT, buff=0.2)
        dims = VGroup(T("pₗ₋₁ × pₖ", size=26, color=BLUEC), T("pₖ × pᵣ", size=26, color=GOOD)).arrange(RIGHT, buff=1.6)
        joint = T("phép nhân cuối tốn  pₗ₋₁ · pₖ · pᵣ", size=28, color=ACCENT)
        formula = tag_box("CÔNG THỨC CHỌN ĐIỂM CHIA", [
            "cost(l, r) = min over l ≤ k < r of",
            "  cost(l, k) + cost(k+1, r) + pₗ₋₁·pₖ·pᵣ",
            "Cơ sở cost(i, i) = 0. Điền theo độ dài.",
        ], width=7.5, size=28)
        formula[3][1].set_color(ACCENT)
        fit_stack(naive, VGroup(split, dims, joint).arrange(DOWN, buff=0.2), formula, buff=0.6, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: thử mọi cách đặt ngoặc. Số cách là số Catalan, tăng khoảng 4 mũ n. Với n bằng 20 đã có gần "
                        "hai tỉ cách; n bằng 300 là không tưởng."):
            self.play(FadeIn(naive), run_time=0.8)
        with self.voice("Phá bế tắc: trong mọi cách đặt ngoặc, có đúng một phép nhân được thực hiện sau cùng. Nó nhân kết quả của đoạn "
                        "l đến k với kết quả của đoạn k cộng 1 đến r, với một k nào đó."):
            self.play(FadeIn(split), run_time=0.8)
        with self.voice("Hai kết quả có kích thước p l trừ 1 nhân p k, và p k nhân p r, nên phép nhân cuối tốn p l trừ 1, nhân p k, "
                        "nhân p r."):
            self.play(FadeIn(dims), FadeIn(joint), run_time=0.8)
        with self.voice("Công thức chọn điểm chia: cost của l, r bằng min theo k của cost hai đoạn con, cộng chi phí phép nhân cuối. "
                        "Cơ sở cost của i, i bằng 0. Điền theo độ dài tăng dần."):
            self.play(FadeIn(formula), run_time=0.8)

        self.clear_body()
        self.show_header("Chạy tay bảng cost và truy vết")
        tbl = Table2D(4, 4, w=1.55, h=0.85, row_labels=["l=1", "l=2", "l=3", "l=4"], col_title="r")
        for k, lab in enumerate(tbl.labels[0]):
            lab.become(T(str(k + 1), size=22, color=MUTED).move_to(lab))
        for l in range(4):
            for r in range(l):
                tbl.cells[(l, r)][0].set_fill(BG, 1).set_stroke(opacity=0.2)
        eq_slot = placeholder(7.4, 1.4)
        res_slot = placeholder(7.4, 1.0)
        sc = fit_stack(tbl, eq_slot, res_slot, buff=0.5, max_scale=1.25)
        eq = [None]

        def say(lines, color=INK):
            new = VGroup(*[M(t, size=26, color=color) for t in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.1).scale(sc)
            if new.width > 7.4:
                new.scale_to_fit_width(7.4)
            new.move_to(eq_slot)
            if eq[0] is None:
                eq[0] = new
                return FadeIn(new)
            return Transform(eq[0], new)

        def fill(l, r):
            return AnimationGroup(*tbl.fill(l - 1, r - 1, COST[l][r], fill=LEN_COLORS[r - l + 1]))

        self.play(FadeIn(tbl), run_time=0.6)
        with self.voice("Độ dài 1: cost bằng 0. Độ dài 2: cost của 1, 2 bằng 10 nhân 30 nhân 5, bằng 1500; cost của 2, 3 bằng 9000; "
                        "cost của 3, 4 bằng 3000."):
            self.play(LaggedStart(*[fill(i, i) for i in range(1, 5)], lag_ratio=0.2), run_time=0.8)
            self.play(say(["cost(1,2) = 10·30·5 = 1500", "cost(2,3) = 30·5·60 = 9000", "cost(3,4) = 5·60·10 = 3000"]),
                      LaggedStart(*[fill(i, i + 1) for i in range(1, 4)], lag_ratio=0.3), run_time=1.2)
        with self.voice("Độ dài 3: cost của 1, 3 bằng min của 27000 và 4500, bằng 4500. cost của 2, 4 cũng bằng 4500."):
            self.play(say(["cost(1,3) = min(0+9000+18000, 1500+0+3000) = 4500",
                           "cost(2,4) = min(0+3000+1500, 9000+0+18000) = 4500"]),
                      LaggedStart(fill(1, 3), fill(2, 4), lag_ratio=0.4), run_time=1.2)
        with self.voice("Độ dài 4, thử ba điểm chia: k bằng 1 được 7500, k bằng 2 được 5000, k bằng 3 được 10500. Nhỏ nhất là 5000, "
                        "đạt tại k bằng 2."):
            self.play(say(["k=1: 0 + 4500 + 3000 = 7500", "k=2: 1500 + 3000 + 500 = 5000  ← min",
                           "k=3: 4500 + 0 + 6000 = 10500"], ACCENT), fill(1, 4), run_time=1.2)
            self.play(Circumscribe(tbl.cells[(0, 3)], color=ACCENT), run_time=0.8)
        res = VGroup(T("split[1][4] = 2  ⇒", size=28),
                     M(brackets(SPLIT, 1, 4), size=36, color=GOOD)).arrange(DOWN, buff=0.12).scale(sc).move_to(res_slot)
        with self.voice("Truy vết: lưu split là k đạt min. Cách đặt ngoặc của đoạn l, r là mở ngoặc, cách đặt ngoặc đoạn trái, cách "
                        "đặt ngoặc đoạn phải, đóng ngoặc, viết bằng một hàm đệ quy ngắn. Ta được A1 A2 trong ngoặc, nhân với A3 A4 "
                        "trong ngoặc."):
            self.play(FadeIn(res), run_time=0.8)

        self.clear_body()
        self.show_header("Code và độ phức tạp O(n³)")
        code = code_block(MAT_CODE, size=20)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "≈ n²/2 đoạn, mỗi đoạn thử ≤ n điểm chia ⇒ ≈ n³/6",
            "n = 300: 4,5·10⁶ phép — rất nhanh",
            "n = 2000: 1,3·10⁹ — quá chậm (cần tối ưu Knuth)",
        ], accent=ORANGE, width=7.5, size=27)
        fit_stack(code, cx, buff=0.7)
        with self.voice("Code: ba vòng lặp lồng nhau, độ dài, điểm đầu, và điểm chia k. Mỗi khi tìm được chi phí nhỏ hơn, lưu cả điểm chia."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 4, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 8, GOOD)), run_time=0.4)
        with self.voice("Có khoảng n bình phương chia 2 đoạn, mỗi đoạn thử tối đa n điểm chia: khoảng n mũ 3 chia 6 phép. Với n bằng "
                        "300 rất nhanh; với n bằng hai nghìn thì quá chậm, cần các kĩ thuật tối ưu nằm ngoài phạm vi sách."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B8_05_TongKet(B8Scene):
    def construct(self):
        self.show_header("5. Khi nào nghĩ tới QHĐ trên đoạn?")
        heads = ["Dấu hiệu", "Ví dụ"]
        data = [["Thao tác ở HAI ĐẦU dãy", "lấy hai đầu, xóa thành đối xứng"],
                ["GHÉP phần tử kề nhau", "ghép sỏi, nhân ma trận, nổ bóng"],
                ["CHIA dãy thành phần", "cắt gỗ, tách xâu đối xứng"],
                ["Cấu trúc LỒNG NHAU", "dãy ngoặc, biểu thức"]]
        colw = [3.2, 4.3]
        table = VGroup()
        for r, rowd in enumerate([heads] + data):
            cells_ = VGroup()
            x = -sum(colw) / 2
            for ci, (txt, w) in enumerate(zip(rowd, colw)):
                fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
                rect = Rectangle(width=w, height=0.9, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
                rect.move_to([x + w / 2, 0, 0])
                col = BG if r == 0 else (ACCENT if ci == 0 else INK)
                t = (TB if r == 0 or ci == 0 else T)(txt, size=24, color=col, max_width=w - 0.2)
                cells_.add(VGroup(rect, t.move_to(rect)))
                x += w
            table.add(cells_)
        table.arrange(DOWN, buff=0)
        ask = VGroup(T("Luôn tự hỏi: thao tác CUỐI CÙNG (hoặc ĐẦU TIÊN)", size=28),
                     T("chia đoạn [l, r] thành những đoạn con nào?", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        fit_stack(table, ask, buff=0.8, max_scale=1.2)
        with self.voice("Khi nào nghĩ tới quy hoạch động trên đoạn? Khi có thao tác ở hai đầu dãy; khi ghép các phần tử kề nhau thành "
                        "một; khi chia dãy thành các phần; hoặc khi có cấu trúc lồng nhau như dãy ngoặc."):
            for r in table:
                self.play(FadeIn(r, shift=UP * 0.15), run_time=0.45)
        with self.voice("Trong mọi trường hợp, hãy tự hỏi: thao tác cuối cùng, hoặc đầu tiên, chia đoạn l, r thành những đoạn con nào?"):
            self.play(FadeIn(ask), run_time=0.8)

        self.clear_body()
        self.show_header("6. Mở rộng")
        ext = [
            ("Dãy xếp vòng tròn", "NHÂN ĐÔI dãy, xét các đoạn [i, i + n − 1]",
             "Mở rộng một: nếu các phần tử xếp thành vòng tròn, mẹo kinh điển là nhân đôi dãy, rồi giải trên dãy dài 2 n, "
             "đáp án là tốt nhất trong các đoạn dài n."),
            ("Xâu đối xứng", "pal(l, r) = (sₗ = sᵣ) và pal(l+1, r−1)",
             "Mở rộng hai: bảng xâu đối xứng, pal của l, r đúng khi hai đầu bằng nhau và phần bên trong đối xứng. Đây là nền tảng "
             "của nhiều bài đếm và tách xâu."),
            ("Nghĩ ngược: phần tử xử lí CUỐI CÙNG", "Nổ bóng: bóng nổ cuối ⇒ hai phía độc lập",
             "Mở rộng ba: ở bài nổ bóng bay, nghĩ bóng nào nổ đầu tiên thì rất rối; nghĩ bóng nào nổ cuối cùng thì hai phần trái "
             "phải độc lập. Khi một hướng nghĩ làm các đoạn con phụ thuộc nhau, hãy thử hướng ngược lại."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Sai thứ tự điền", "Điền theo l tăng dần khi cần ô (l+1, r): hãy điền theo ĐỘ DÀI",
             "Bẫy một: sai thứ tự điền. Hãy luôn điền theo độ dài."),
            ("Nhầm biên điểm chia", "k chạy từ l đến r − 1 (hai phần khác rỗng)",
             "Bẫy hai: nhầm biên điểm chia. k chạy từ l đến r trừ 1."),
            ("Tràn số", "pₗ₋₁·pₖ·pᵣ tới 10⁹, cộng nhiều lần vượt int",
             "Bẫy ba: tràn số, tích ba kích thước tới một tỉ, cộng nhiều lần có thể vượt int."),
            ("Quên dữ liệu vòng tròn", "Cần nhân đôi dãy", "Bẫy bốn: quên rằng dữ liệu vòng tròn cần nhân đôi dãy."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 8", [
            "• Trạng thái là đoạn [l, r];",
            "   điền theo ĐỘ DÀI đoạn tăng dần.",
            "• “Bỏ một đầu”: O(n²);",
            "   “chọn điểm chia k”: O(n³).",
            "• Trò chơi đối kháng: dùng HIỆU SỐ;",
            "   đổi lượt thì hiệu số đổi dấu.",
            "• Truy vết bằng mảng điểm chia + đệ quy.",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: trạng thái là đoạn l, r, điền bảng theo độ dài đoạn tăng dần. Dạng bỏ một đầu là O của n bình phương; "
                        "dạng chọn điểm chia k là O của n mũ 3."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Trò chơi đối kháng: dùng hiệu số của người đang đến lượt; khi đổi lượt, hiệu số đổi dấu. Và truy vết bằng mảng "
                        "điểm chia cùng một hàm đệ quy in ngoặc."):
            self.play(FadeIn(mem[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Dãy xu 2, 7, 3:", "người đi trước được bao nhiêu?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        row = VGroup(*[coin(v, 0.5) for v in (2, 7, 3)]).arrange(RIGHT, buff=0.4)
        ans = VGroup(TB("Đáp án 5", size=40, color=GOOD),
                     T("lấy 2 hay 3 thì đối thủ đều lấy 7; hơn(1,3) = −2, (12 − 2)/2 = 5", size=24)).arrange(DOWN, buff=0.12)
        nxt = VGroup(TB("Tiếp theo: BÀI 9", size=42, color=ACCENT), T("Trạng thái tập con (bitmask)", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, row, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: với dãy xu 2, 7, 3, người đi trước được bao nhiêu? Dừng video và thử nhé!"):
            self.play(FadeIn(q), FadeIn(row), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp án 5. Lấy 2 thì đối thủ lấy 7; lấy 3 thì đối thủ cũng lấy 7. hơn của 1, 3 bằng trừ 2, tổng 12, nên người "
                        "đi trước được 12 trừ 2, chia 2, bằng 5."):
            self.play(Indicate(row[1], color=BAD), FadeIn(ans), run_time=0.8)
        with self.voice("Bài tiếp theo: quy hoạch động trạng thái tập con, bitmask. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
