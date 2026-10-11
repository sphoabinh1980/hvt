"""BÀI 9 — Quy hoạch động trạng thái tập con (bitmask): GHEPDOI, đường Hamilton, duyệt tập con."""

import math

from shared import *  # noqa: F401,F403

C = [[0, 4, 1, 3], [4, 0, 2, 5], [1, 2, 0, 6], [3, 5, 6, 0]]
N = 4
INF = None


def matching(c):
    n = len(c)
    best = [INF] * (1 << n)
    best[0] = 0
    pushes = []  # (mask, i, j, next, candidate)
    for mask in range((1 << n) - 1):
        if best[mask] is None:
            continue
        i = 0
        while mask >> i & 1:
            i += 1
        for j in range(i + 1, n):
            if mask >> j & 1:
                continue
            nxt = mask | 1 << i | 1 << j
            cand = best[mask] + c[i][j]
            pushes.append((mask, i, j, nxt, cand))
            if best[nxt] is None or cand < best[nxt]:
                best[nxt] = cand
    return best, pushes


BEST, PUSHES = matching(C)
assert BEST[15] == 5 and BEST[0b0011] == 4 and BEST[0b0101] == 1 and BEST[0b1001] == 3
_c2 = [r[:] for r in C]
_c2[1][2] = _c2[2][1] = 9
assert matching(_c2)[0][15] == 6

EDGES = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3), (2, 3)]  # đồ thị minh họa


def hamilton(n, edges):
    into = [[] for _ in range(n)]
    for u, v in edges:
        into[v].append(u)
    ways = [[0] * n for _ in range(1 << n)]
    ways[1][0] = 1
    for mask in range(1, 1 << n):
        if not mask & 1:
            continue
        for last in range(1, n):
            if not mask >> last & 1:
                continue
            before = mask ^ (1 << last)
            for u in into[last]:
                if before >> u & 1:
                    ways[mask][last] += ways[before][u]
    return ways


HAM = hamilton(4, EDGES)
assert HAM[15][3] == 2


def submasks(m):
    out, s = [], m
    while s:
        out.append(s)
        s = (s - 1) & m
    return out


assert [format(x, "04b") for x in submasks(0b1010)] == ["1010", "1000", "0010"]
assert int("10110", 2) == 22
DFACT = {n: math.prod(range(n - 1, 0, -2)) for n in (10, 16, 20, 24)}
assert DFACT[20] == 654729075


class B9Scene(NarratedScene):
    lesson_tag = "BÀI 9"
    lesson_title = "Quy hoạch động trạng thái tập con"


def bits_row(mask, n=4, w=0.9, on=GOOD, show_idx=True):
    """Dãy bit từ bit cao (trái) tới bit thấp (phải)."""
    cells = VGroup()
    for k in range(n - 1, -1, -1):
        b = mask >> k & 1
        c = cell(str(b), w=w, h=w, fill=on if b else PANEL_2, size=w * 44, color=BG if b else MUTED)
        cells.add(c)
    cells.arrange(RIGHT, buff=0)
    g = VGroup(cells)
    if show_idx:
        idx = VGroup(*[T(f"bit {k}", size=w * 22, color=MUTED).next_to(cells[n - 1 - k], UP, buff=0.08)
                       for k in range(n - 1, -1, -1)])
        g.add(idx)
    g.cells = cells
    return g


def mask_node(mask, val, n=4, color=BLUEC):
    box = RoundedRectangle(width=1.7, height=1.0, corner_radius=0.15, fill_color=PANEL_2, fill_opacity=1,
                           stroke_color=color, stroke_width=3)
    t1 = M(format(mask, f"0{n}b"), size=28).move_to(box.get_center() + UP * 0.2)
    t2 = TB(str(val) if val is not None else "∞", size=26, color=ACCENT).move_to(box.get_center() + DOWN * 0.22)
    return VGroup(box, t1, t2)


# ----------------------------------------------------------------------------
class B9_00_Intro(B9Scene):
    def construct(self):
        tag = TB("BÀI 9", size=80, color=ACCENT)
        ttl = VGroup(TB("Quy hoạch động", size=48), TB("trạng thái tập con (bitmask)", size=42)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Tập con = MỘT SỐ NGUYÊN (dãy bit)",
            "✓ Trạng thái “những phần tử nào đã dùng”",
            "✓ Ghép cặp tối ưu, đếm đường Hamilton",
            "✓ Duyệt tập con của tập con: O(3ⁿ)",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 9: Quy hoạch động trạng thái tập con, hay bitmask."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ biểu diễn một tập con bằng một số nguyên và thành thạo các phép toán bit, rồi dùng "
                        "tập con làm trạng thái khi lời giải phụ thuộc vào những phần tử nào đã được dùng."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ giải bài ghép cặp tối ưu, bài đếm đường đi qua mọi đỉnh, và biết duyệt mọi tập con của một tập con "
                        "trong tổng O của 3 mũ n."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B9_01_KhoiDong(B9Scene):
    def construct(self):
        self.show_header("Khởi động: Chia 20 bạn thành 10 cặp")
        dots = VGroup(*[Dot(radius=0.16, color=BLUEC) for _ in range(20)]).arrange_in_grid(rows=4, cols=5, buff=0.5)
        story = VGroup(T("Mỗi hai bạn có “độ không hợp”;", size=28),
                       T("chia thành 10 cặp với tổng nhỏ nhất.", size=28)).arrange(DOWN, buff=0.1)
        cnt = VGroup(T("Số cách: 19 · 17 · 15 · … · 3 · 1 =", size=28),
                     TB("654 729 075", size=44, color=BAD)).arrange(DOWN, buff=0.12)
        more = T("24 bạn: gấp thêm 21 · 23 = 483 lần…", size=27, color=ORANGE)
        key = VGroup(T("Điều duy nhất quan trọng cho phần còn lại:", size=28),
                     TB("NHỮNG BẠN NÀO đã được ghép", size=34, color=GOOD),
                     VGroup(T("chỉ có", size=28), TB("2²⁰ ≈ 10⁶", size=40, color=GOOD), T("tập khác nhau!", size=28)).arrange(
                         RIGHT, buff=0.2)).arrange(DOWN, buff=0.12)
        fit_stack(dots, story, cnt, more, key, buff=0.5, max_scale=1.2)
        with self.voice("Lớp em có 20 bạn, cần chia thành 10 cặp làm bài thí nghiệm. Thầy giáo có bảng điểm độ không hợp giữa từng "
                        "hai bạn, và muốn tổng độ không hợp của 10 cặp là nhỏ nhất."):
            self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.04), FadeIn(story), run_time=1.5)
        with self.voice("Số cách chia 20 bạn thành 10 cặp là 19 nhân 17 nhân 15, cho tới 3 nhân 1, bằng hơn sáu trăm năm mươi tư "
                        "triệu cách. Thử hết được không? Máy tính nhanh cũng mất nhiều giây. Còn 24 bạn thì gấp thêm 483 lần."):
            self.play(FadeIn(cnt), run_time=0.8)
            self.play(FadeIn(more), run_time=0.5)
        pairs = [(0, 1), (2, 3), (5, 6), (7, 8)]
        lines = VGroup(*[Line(dots[a].get_center(), dots[b].get_center(), color=GOOD, stroke_width=5) for a, b in pairs])
        with self.voice("Nhưng nhìn lại: khi đã ghép xong vài cặp, điều duy nhất quan trọng cho phần còn lại là những bạn nào đã được "
                        "ghép, chứ không phải ghép với ai. Có bao nhiêu tập các bạn đã ghép khác nhau? Chỉ 2 mũ 20, khoảng một triệu."):
            self.play(Create(lines), *[dots[k].animate.set_color(GOOD) for p in pairs for k in p], run_time=0.8)
            self.play(FadeIn(key), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B9_02_TapHop(B9Scene):
    def construct(self):
        self.show_header("1. Tập hợp là một số nguyên")
        rule = VGroup(T("n phần tử 0, 1, …, n−1. Tập S ⟷ số mask n bit:", size=28),
                      T("bit thứ i = 1  ⟺  phần tử i thuộc S", size=30, color=ACCENT)).arrange(DOWN, buff=0.12)
        br = bits_row(0b1011, w=1.1)
        eq = VGroup(TB("11 = 1011₂", size=40, color=GOOD), T("⟷", size=36), TB("{0, 1, 3}", size=40, color=GOOD)).arrange(
            RIGHT, buff=0.3)
        total = T("Có 2ⁿ tập con ⟷ các số từ 0 đến 2ⁿ − 1", size=28, color=MUTED)
        fit_stack(rule, br, eq, total, buff=0.6, max_scale=1.25)
        with self.voice("Với n phần tử đánh số từ 0, mỗi tập con S được biểu diễn bằng một số nguyên mask có n bit: bit thứ i bằng 1 "
                        "khi và chỉ khi phần tử i thuộc S."):
            self.play(FadeIn(rule), run_time=0.8)
        with self.voice("Ví dụ số 11, viết nhị phân là 1011. Bit 0, bit 1 và bit 3 bằng 1, nên nó biểu diễn tập 0, 1, 3."):
            self.play(FadeIn(br), run_time=0.8)
            for k in (3, 2, 1, 0):
                if 0b1011 >> k & 1:
                    self.play(Indicate(br.cells[3 - k], color=GOOD, scale_factor=1.2), run_time=0.3)
            self.play(FadeIn(eq), run_time=0.6)
        with self.voice("Có 2 mũ n tập con, ứng với các số từ 0 đến 2 mũ n trừ 1."):
            self.play(FadeIn(total), run_time=0.6)

        self.clear_body()
        self.show_header("Các phép toán bit cơ bản")
        rows = [("Phần tử i thuộc tập?", "(mask >> i) & 1", "i = 2: 0"),
                ("Thêm phần tử i", "mask | (1 << i)", "i = 2: 1111"),
                ("Bỏ phần tử i", "mask & ~(1 << i)", "i = 0: 1010"),
                ("Đổi phần tử i", "mask ^ (1 << i)", "i = 3: 0011"),
                ("Số phần tử", "__builtin_popcount(mask)", "3"),
                ("Tập đầy đủ n phần tử", "(1 << n) - 1", "n = 4: 1111"),
                ("Bit 1 thấp nhất", "mask & (-mask)", "0001")]
        colw = [2.6, 3.1, 1.8]
        table = VGroup()
        for r, rowd in enumerate([("Thao tác", "C++", "mask = 1011")] + rows):
            cells_ = VGroup()
            x = -sum(colw) / 2
            for ci, (txt, w) in enumerate(zip(rowd, colw)):
                fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
                rect = Rectangle(width=w, height=0.78, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
                rect.move_to([x + w / 2, 0, 0])
                col = BG if r == 0 else (INK if ci == 0 else (ACCENT if ci == 1 else GOOD))
                maker = TB if r == 0 else (M if ci == 1 else T)
                t = maker(txt, size=22, color=col, max_width=w - 0.15)
                cells_.add(VGroup(rect, t.move_to(rect)))
                x += w
            table.add(cells_)
        table.arrange(DOWN, buff=0)
        prop = tag_box("TÍNH CHẤT QUAN TRỌNG", [
            "T là tập con thực sự của S ⇒ số của T NHỎ HƠN",
            "Chuyển trạng thái chỉ THÊM phần tử",
            "⇒ điền bảng theo mask TĂNG DẦN.",
        ], accent=GOOD, width=7.5, size=27)
        fit_stack(table, prop, buff=0.6)
        with self.voice("Các phép toán bit cơ bản: kiểm tra phần tử i bằng dịch phải rồi AND 1. Thêm phần tử i bằng OR với 1 dịch trái i. "
                        "Bỏ phần tử i bằng AND với phủ định. Đổi trạng thái bằng XOR."):
            self.play(FadeIn(table[0]), run_time=0.4)
            for r in table[1:5]:
                self.play(FadeIn(r, shift=UP * 0.15), run_time=0.4)
        with self.voice("Đếm số phần tử bằng hàm popcount. Tập đầy đủ n phần tử là 1 dịch trái n, trừ 1. Bit 1 thấp nhất là mask AND "
                        "trừ mask."):
            for r in table[5:]:
                self.play(FadeIn(r, shift=UP * 0.15), run_time=0.4)
        with self.voice("Một tính chất quan trọng cho quy hoạch động: nếu T là tập con thực sự của S thì số biểu diễn T nhỏ hơn số "
                        "biểu diễn S. Vậy nếu mỗi bước chuyển trạng thái chỉ thêm phần tử, ta điền bảng theo mask tăng dần."):
            self.play(FadeIn(prop), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
def cost_matrix(c, w=0.85):
    n = len(c)
    cells = VGroup()
    for i in range(n):
        for j in range(n):
            cc = cell(c[i][j], w=w, h=w * 0.8, fill=PANEL if i == j else PANEL_2, size=30, color=MUTED if i == j else INK)
            cc.move_to([j * w, -i * w * 0.8, 0])
            cells.add(cc)
    top = VGroup(*[T(str(j), size=22, color=BLUEC).next_to(cells[j], UP, buff=0.08) for j in range(n)])
    left = VGroup(*[T(str(i), size=22, color=BLUEC).next_to(cells[i * n], LEFT, buff=0.12) for i in range(n)])
    g = VGroup(cells, top, left)
    g.cells = cells
    return g


def students(n=4, r=1.1):
    pos = [np.array([-r, r * 0.6, 0]), np.array([r, r * 0.6, 0]), np.array([-r, -r * 0.6, 0]), np.array([r, -r * 0.6, 0])]
    pts = VGroup(*[VGroup(Circle(radius=0.32, fill_color=BLUEC, fill_opacity=1, stroke_color=INK, stroke_width=2),
                          TB(str(k), size=26, color=BG)).move_to(pos[k]) for k in range(n)])
    for p in pts:
        p[1].move_to(p[0])
    return pts


class B9_03_GhepDoi(B9Scene):
    def construct(self):
        self.show_header("2. Bài toán GHEPDOI")
        box = tag_box("BÀI TOÁN: GHEPDOI", [
            "n học sinh (n chẵn), ghép i với j có độ",
            "không hợp cᵢⱼ. Chia thành n/2 cặp với",
            "tổng độ không hợp NHỎ NHẤT.   n ≤ 20",
        ], accent=BLUEC, width=7.5, size=29)
        mat = cost_matrix(C)
        st = students()
        res_slot = placeholder(7.4, 1.6)
        sc = fit_stack(box, VGroup(mat, st).arrange(RIGHT, buff=0.8), res_slot, buff=0.6, max_scale=1.2)
        with self.voice("Bài toán GHEPDOI: có n học sinh, n chẵn. Ghép học sinh i với học sinh j có độ không hợp c i j. Hãy chia "
                        "thành n chia 2 cặp sao cho tổng độ không hợp nhỏ nhất. n không quá 20."):
            self.play(FadeIn(box), run_time=0.8)
        with self.voice("Ví dụ bốn bạn với ma trận độ không hợp như sau."):
            self.play(FadeIn(mat), FadeIn(st), run_time=0.8)

        def edge(a, b, col):
            return Line(st[a].get_center(), st[b].get_center(), buff=0.32 * sc, color=col, stroke_width=7)

        with self.voice("Tham lam chọn cặp rẻ nhất trước: cặp 0, 2 chỉ tốn 1. Còn lại bắt buộc ghép 1 với 3, tốn 5. Tổng 6."):
            e1, e2 = edge(0, 2, ORANGE), edge(1, 3, ORANGE)
            self.play(Create(e1), Indicate(mat.cells[2], color=ORANGE), run_time=0.7)
            self.play(Create(e2), Indicate(mat.cells[7], color=ORANGE), run_time=0.7)
            g = TB("Tham lam: (0,2) + (1,3) = 1 + 5 = 6", size=30, color=ORANGE).scale(sc).move_to(res_slot).shift(UP * 0.35)
            self.play(FadeIn(g), run_time=0.4)
        with self.voice("Nhưng ghép 0 với 3, và 1 với 2, chỉ tốn 3 cộng 2, bằng 5!"):
            self.play(e1.animate.set_stroke(opacity=0.2), e2.animate.set_stroke(opacity=0.2), run_time=0.3)
            f1, f2 = edge(0, 3, GOOD), edge(1, 2, GOOD)
            self.play(Create(f1), Create(f2), run_time=0.8)
            b = TB("Tối ưu: (0,3) + (1,2) = 3 + 2 = 5", size=30, color=GOOD).scale(sc).next_to(g, DOWN, buff=0.15)
            self.play(FadeIn(b), run_time=0.4)

        self.clear_body()
        self.show_header("3. Ý tưởng ngây thơ và bế tắc")
        naive = VGroup(T("Lấy bạn có số NHỎ NHẤT chưa ghép,", size=29),
                       T("thử ghép với từng bạn còn lại; lặp lại.", size=29)).arrange(DOWN, buff=0.1)
        rows = VGroup(*[VGroup(T(f"n = {n}:", size=28), TB(f"{DFACT[n]:,}".replace(",", " ") + " cách", size=30,
                                                            color=BAD if n >= 20 else INK)).arrange(RIGHT, buff=0.25)
                        for n in (10, 16, 20, 24)]).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        lab = T("Số cách ghép = (n − 1)·(n − 3)·…·3·1 = (n − 1)!!", size=27, color=MUTED)
        stuck = tag_box("BẾ TẮC", [
            "“(0,1) rồi (2,3)” và “(0,2) rồi (1,3)” đều dẫn tới",
            "CÙNG tình huống: bốn bạn 0..3 đã có cặp.",
            "Quay lui giải lại phần còn lại cho từng cách!",
            "⇒ Nhớ theo TẬP CÁC BẠN ĐÃ GHÉP.",
        ], accent=BAD, width=7.5, size=28)
        stuck[3][3].set_color(GOOD)
        fit_stack(naive, lab, rows, stuck, buff=0.5, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: để không liệt kê trùng, mỗi bước lấy bạn có số thứ tự nhỏ nhất chưa được ghép, rồi thử ghép "
                        "bạn ấy với từng bạn còn lại."):
            self.play(FadeIn(naive), run_time=0.8)
        with self.voice("Số cách ghép là n trừ 1, nhân n trừ 3, cho tới 1. Với 10 bạn có 945 cách; 16 bạn hơn hai triệu; 20 bạn hơn "
                        "sáu trăm năm mươi triệu: quá giới hạn một giây."):
            self.play(FadeIn(lab), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.3), run_time=1.4)
        with self.voice("Bế tắc! Hai cách ghép khác nhau, 0 với 1 rồi 2 với 3, và 0 với 2 rồi 1 với 3, đều dẫn tới cùng một tình huống: "
                        "bốn bạn đầu đã có cặp, phần còn lại cần ghép tối ưu y như nhau. Làm sao nhớ theo tập các bạn đã ghép?"):
            self.play(FadeIn(stuck), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
MATCH_CODE = """
vector<long long> best(fullMask + 1, INF);
best[0] = 0;
for (int mask = 0; mask < fullMask; mask++) {
    if (best[mask] == INF) continue;
    int first = 0;
    while ((mask >> first) & 1) first++;
    for (int j = first + 1; j < n; j++) {
        if ((mask >> j) & 1) continue;
        int next = mask | (1 << first) | (1 << j);
        best[next] = min(best[next],
                         best[mask] + cost[first][j]);
    }
}
"""


class B9_04_TrangThai(B9Scene):
    def construct(self):
        self.show_header("4. Phá bế tắc: Trạng thái là tập đã ghép")
        defi = panel(VGroup(TB("best[mask] =", size=34, color=ACCENT),
                            T("tổng nhỏ nhất để ghép cặp ĐÚNG các bạn", size=28),
                            T("thuộc tập mask.  Đáp án: best[2ⁿ − 1]", size=28)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        formula = tag_box("CÔNG THỨC (ĐẨY VỀ PHÍA TRƯỚC)", [
            "i = bạn NHỎ NHẤT chưa thuộc mask;  j > i chưa thuộc",
            "best[mask ∪ {i, j}] ← min(…, best[mask] + cᵢⱼ)",
            "Cơ sở best[0] = 0, còn lại ∞.  Duyệt mask tăng dần.",
        ], width=7.5, size=27)
        formula[3][1].set_color(ACCENT)
        why = VGroup(T("Vì sao chỉ xét bạn i nhỏ nhất? Bạn i sớm muộn", size=27),
                     T("cũng phải có cặp: quyết định ngay không mất cách nào,", size=27),
                     T("lại tránh sinh một cách ghép theo nhiều thứ tự.", size=27, color=GOOD)).arrange(DOWN, buff=0.08)
        fit_stack(defi, formula, why, buff=0.6, max_scale=1.2)
        with self.voice("Bước một: đặt best của mask là tổng độ không hợp nhỏ nhất để ghép cặp đúng các bạn thuộc tập mask. Đáp án là "
                        "best của tập đầy đủ."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Bước hai: công thức kiểu đẩy về phía trước. Từ một trạng thái đã biết, đẩy kết quả sang các trạng thái sau. "
                        "Từ mask, gọi i là bạn có số nhỏ nhất chưa thuộc mask. Bạn i phải được ghép với một bạn j chưa thuộc mask: "
                        "cập nhật best của mask hợp i, j bằng best của mask cộng c i j."):
            self.play(FadeIn(formula), run_time=1.0)
        with self.voice("Vì sao chỉ cần xét bạn i nhỏ nhất chưa ghép? Vì bạn i dù sớm hay muộn cũng phải có cặp; quyết định cặp của i "
                        "ngay bây giờ không làm mất cách ghép nào, mà lại tránh được việc một cách ghép bị sinh ra theo nhiều thứ tự."):
            self.play(FadeIn(why), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 3: Chạy tay trên đồ thị trạng thái")
        n0 = mask_node(0, 0)
        mids = VGroup(*[mask_node(m, None) for m in (0b0011, 0b0101, 0b1001)]).arrange(RIGHT, buff=0.8)
        n_end = mask_node(15, None, color=GOOD)
        graph = VGroup(n0, mids, n_end).arrange(DOWN, buff=1.8)
        e_top = VGroup(*[Arrow(n0.get_bottom(), m.get_top(), buff=0.08, color=MUTED, stroke_width=4) for m in mids])
        e_bot = VGroup(*[Arrow(m.get_bottom(), n_end.get_top(), buff=0.08, color=MUTED, stroke_width=4) for m in mids])
        sides = [LEFT * 1.05, ORIGIN, RIGHT * 1.05]  # nhãn cạnh mũi tên chéo, nhãn giữa nằm trên mũi tên (có nền)

        def edge_label(text, e, d, prop):
            t = T(text, size=24, color=INK)
            bg = BackgroundRectangle(t, color=BG, fill_opacity=1, buff=0.06)
            return VGroup(bg, t).move_to(e.point_from_proportion(prop) + d)

        lab_top = VGroup(*[edge_label(t, e, d, 0.5)
                           for t, e, d in zip(["+(0,1): 4", "+(0,2): 1", "+(0,3): 3"], e_top, sides)])
        lab_bot = VGroup(*[edge_label(t, e, d, 0.5)
                           for t, e, d in zip(["+(2,3): 6", "+(1,3): 5", "+(1,2): 2"], e_bot, sides)])
        res_slot = placeholder(7.4, 1.0)
        sc = fit_stack(VGroup(graph, e_top, e_bot, lab_top, lab_bot), res_slot, buff=0.5, max_scale=1.15)
        self.play(FadeIn(n0), run_time=0.5)
        with self.voice("Từ best của 0000 bằng 0: bạn 0 là bạn nhỏ nhất chưa ghép, ghép với 1, 2 hoặc 3: best của 0011 bằng 4, "
                        "best của 0101 bằng 1, best của 1001 bằng 3."):
            for k, m in enumerate((0b0011, 0b0101, 0b1001)):
                new = mask_node(m, BEST[m]).scale(sc).move_to(mids[k])
                self.play(GrowArrow(e_top[k]), FadeIn(lab_top[k]), FadeIn(mids[k]), run_time=0.45)
                self.play(Transform(mids[k], new), run_time=0.3)
        self.play(FadeIn(n_end), run_time=0.3)
        cands = [10, 6, 5]
        sps = ["Từ 0011, bạn nhỏ nhất chưa ghép là 2, chỉ ghép được với 3: ứng viên 4 cộng 6 bằng 10 cho best của 1111.",
               "Từ 0101, bạn 0 và 2 đã ghép: ghép 1 với 3, ứng viên 1 cộng 5 bằng 6.",
               "Từ 1001, bạn 0 và 3 đã ghép: ghép 1 với 2, ứng viên 3 cộng 2 bằng 5."]
        best_so_far = None
        for k in range(3):
            with self.voice(sps[k]):
                best_so_far = cands[k] if best_so_far is None else min(best_so_far, cands[k])
                new = mask_node(15, best_so_far, color=GOOD).scale(sc).move_to(n_end)
                self.play(GrowArrow(e_bot[k]), FadeIn(lab_bot[k]), run_time=0.5)
                self.play(Transform(n_end, new), run_time=0.4)
        with self.voice("best của 1111 bằng min của 10, 6, 5, bằng 5. Đường tốt nhất: ghép 0 với 3, rồi 1 với 2."):
            self.play(e_top[2].animate.set_color(GOOD).set_stroke(width=8), e_bot[2].animate.set_color(GOOD).set_stroke(width=8),
                      mids[2][0].animate.set_stroke(GOOD, 5), run_time=0.8)
            res = TB("best[1111] = min(10, 6, 5) = 5", size=34, color=GOOD).scale(sc).move_to(res_slot)
            self.play(FadeIn(res), run_time=0.5)

        self.clear_body()
        self.show_header("Code và độ phức tạp O(2ⁿ · n)")
        code = code_block(MATCH_CODE, size=20)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "2ⁿ trạng thái × ≤ n bạn j  ⇒  O(2ⁿ · n)",
            "n = 20: ≈ 2·10⁷ phép, vài chục mili giây; 8 MB",
            "n tăng 2: QHĐ chậm ≈ 4 lần, quay lui chậm ≈ n lần",
        ], accent=GOOD, width=7.5, size=27)
        fit_stack(code, cx, buff=0.6)
        with self.voice("Code: duyệt mask tăng dần, bỏ qua trạng thái chưa tới được. Tìm bạn first nhỏ nhất chưa ghép bằng vòng while, "
                        "rồi thử mọi bạn j chưa ghép, đẩy kết quả sang trạng thái mới."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 5, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 8, GOOD)), run_time=0.4)
        with self.voice("Có 2 mũ n trạng thái, mỗi trạng thái thử tối đa n bạn: O của 2 mũ n nhân n. Với n bằng 20, khoảng hai mươi triệu "
                        "phép, chạy trong vài chục mili giây. Và quan trọng hơn: khi n tăng thêm 2, quy hoạch động chỉ chậm đi khoảng "
                        "4 lần, còn quay lui chậm đi khoảng n lần."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
HAM_CODE = """
ways[1][0] = 1;
for (int mask = 1; mask <= fullMask; mask++) {
    if (!(mask & 1)) continue;
    for (int last = 1; last < n; last++) {
        if (!((mask >> last) & 1)) continue;
        int before = mask ^ (1 << last);
        for (int from : into[last])
            if ((before >> from) & 1)
                ways[mask][last] += ways[before][from];
    }
}
"""


class B9_05_Hamilton(B9Scene):
    def construct(self):
        self.show_header("5. Đi qua mọi đỉnh: Đếm đường Hamilton")
        task = VGroup(T("Đồ thị có hướng n đỉnh (n ≤ 18). Đếm số đường", size=28),
                      T("từ đỉnh 0 tới đỉnh n−1 đi qua MỖI ĐỈNH ĐÚNG MỘT LẦN.", size=28, color=ACCENT)).arrange(DOWN, buff=0.1)
        need = VGroup(T("Biết tập đỉnh đã đi chưa đủ: để đi tiếp,", size=28),
                      T("cần biết ĐỈNH CUỐI (có cạnh nào đi ra).", size=28, color=GOOD)).arrange(DOWN, buff=0.1)
        formula = tag_box("CÔNG THỨC ĐƯỜNG HAMILTON", [
            "ways[mask][v] = số đường từ 0, đi qua ĐÚNG các",
            "đỉnh thuộc mask, kết thúc tại v",
            "ways[mask][v] = Σ ways[mask \\ {v}][u],  cạnh u → v",
            "Cơ sở ways[{0}][0] = 1.  Đáp án ways[2ⁿ−1][n−1]",
        ], width=7.5, size=26)
        formula[3][2].set_color(ACCENT)
        fit_stack(task, need, formula, buff=0.6, max_scale=1.2)
        with self.voice("Một dạng bitmask kinh điển khác cần nhớ thêm đang đứng ở đâu. Cho đồ thị có hướng n đỉnh, n không quá 18. "
                        "Đếm số đường đi từ đỉnh 0 tới đỉnh n trừ 1, đi qua mỗi đỉnh đúng một lần."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Chỉ biết tập các đỉnh đã đi qua là chưa đủ: để đi tiếp, ta cần biết đỉnh cuối cùng để biết có cạnh nào đi ra. "
                        "Vậy trạng thái gồm hai thành phần."):
            self.play(FadeIn(need), run_time=0.8)
        with self.voice("ways của mask, v là số đường đi xuất phát từ 0, đi qua đúng các đỉnh thuộc mask, và kết thúc tại v. Nó bằng tổng "
                        "ways của mask bỏ v, kết thúc tại u, với mọi cạnh từ u đến v. Cơ sở: tập chỉ có đỉnh 0 có một cách."):
            self.play(FadeIn(formula), run_time=1.0)

        self.clear_body()
        self.show_header("Minh họa: đồ thị 4 đỉnh")
        pos = {0: LEFT * 2.6, 1: UP * 1.3, 2: DOWN * 1.3, 3: RIGHT * 2.6}
        vs = VGroup(*[VGroup(Circle(radius=0.42, fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=4),
                             TB(str(k), size=30)).move_to(pos[k]) for k in range(4)])
        for v in vs:
            v[1].move_to(v[0])
        arrows = {}
        for u, v in EDGES:
            off = 0.12 if (v, u) in EDGES else 0
            d = pos[v] - pos[u]
            perp = np.array([-d[1], d[0], 0]) / np.linalg.norm(d) * off
            arrows[(u, v)] = Arrow(pos[u] + perp, pos[v] + perp, buff=0.45, color=MUTED, stroke_width=4,
                                   max_tip_length_to_length_ratio=0.12)
        graph = VGroup(*arrows.values(), vs)
        paths = VGroup(M("0 → 1 → 2 → 3", size=32, color=GOOD), M("0 → 2 → 1 → 3", size=32, color=ORANGE)).arrange(DOWN, buff=0.15)
        res = TB("ways[1111][3] = 2", size=36, color=ACCENT)
        tsp = VGroup(T("Đổi phép cộng thành MIN với độ dài cạnh:", size=27),
                     TB("bài toán NGƯỜI DU LỊCH (TSP)", size=30, color=PURPLE)).arrange(DOWN, buff=0.1)
        fit_stack(graph, paths, res, tsp, buff=0.5, max_scale=1.2)
        with self.voice("Minh họa với một đồ thị nhỏ bốn đỉnh và sáu cạnh có hướng."):
            self.play(FadeIn(vs), LaggedStart(*[GrowArrow(a) for a in arrows.values()], lag_ratio=0.1), run_time=1.2)
        for k, (seq, col) in enumerate([((0, 1, 2, 3), GOOD), ((0, 2, 1, 3), ORANGE)]):
            sp = ("Đường thứ nhất: 0, 1, 2, 3." if k == 0 else "Đường thứ hai: 0, 2, 1, 3. Không còn đường nào khác.")
            with self.voice(sp):
                for a, b in zip(seq, seq[1:]):
                    self.play(arrows[(a, b)].animate.set_color(col).set_stroke(width=7), vs[b][0].animate.set_stroke(col, 5),
                              run_time=0.35)
                self.play(FadeIn(paths[k]), run_time=0.4)
                if k == 0:
                    self.play(*[arrows[(a, b)].animate.set_color(MUTED).set_stroke(width=4) for a, b in zip(seq, seq[1:])],
                              *[v[0].animate.set_stroke(BLUEC, 4) for v in vs], run_time=0.3)
        with self.voice("Bảng quy hoạch động cho ways của tập đầy đủ, kết thúc tại đỉnh 3, bằng 2."):
            self.play(FadeIn(res), run_time=0.6)
        with self.voice("Có 2 mũ n nhân n trạng thái, mỗi trạng thái xét tối đa n cạnh vào: O của 2 mũ n nhân n bình phương. Đổi phép "
                        "cộng thành phép min với độ dài cạnh, ta được bài toán người du lịch, một trong những bài toán nổi tiếng nhất "
                        "của tin học."):
            self.play(FadeIn(tsp), run_time=0.8)

        self.clear_body()
        self.show_header("Code đếm đường Hamilton, O(2ⁿ · n²)")
        code = code_block(HAM_CODE, size=20)
        note = VGroup(T("into[last]: các đỉnh có cạnh đi VÀO last", size=27),
                      T("n = 18: ≈ 8,5·10⁷ phép; bảng 2¹⁸·18 ≈ 4,7·10⁶ ô", size=27, color=MUTED)).arrange(DOWN, buff=0.1)
        fit_stack(code, note, buff=0.7)
        with self.voice("Code: chỉ xét các mask chứa đỉnh 0. Với mỗi đỉnh cuối last thuộc mask, bỏ last ra được tập before, rồi cộng "
                        "dồn từ mọi đỉnh from có cạnh đi vào last. Với n bằng 18, khoảng tám mươi lăm triệu phép."):
            self.play(FadeIn(code), FadeIn(note), run_time=0.8)
            hl = line_box(code, 5, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 8, GOOD)), run_time=0.4)
        self.clear_body()


# ----------------------------------------------------------------------------
class B9_06_TapCon(B9Scene):
    def construct(self):
        self.show_header("6. Duyệt các tập con của một tập con")
        use = VGroup(T("Chia tập thành NHIỀU NHÓM (mỗi ngày làm một nhóm việc):", size=27),
                     M("f[mask] = min(f[mask^sub] + g[sub])", size=30, color=ACCENT), T("với mọi tập con sub ⊆ mask", size=26, color=MUTED)).arrange(DOWN, buff=0.12)
        code = code_block("""
for (int sub = mask; sub > 0;
         sub = (sub - 1) & mask)
    f[mask] = min(f[mask], f[mask ^ sub] + g[sub]);
""", size=24)
        demo_title = TB("Ví dụ mask = 1010:", size=30)
        base = bits_row(0b1010, w=0.85, on=BLUEC, show_idx=False)
        demo_slot = placeholder(7.0, 1.0)
        seq_slot = placeholder(7.0, 0.8)
        three = tag_box("VÌ SAO TỔNG LÀ 3ⁿ?", [
            "Mỗi phần tử ở 1 trong 3 trạng thái:",
            "thuộc sub · thuộc mask nhưng không thuộc sub ·",
            "không thuộc mask.  n = 15: ≈ 1,4·10⁷; n = 20: quá chậm",
        ], accent=PURPLE, width=7.5, size=26)
        sc = fit_stack(use, code, VGroup(demo_title, base).arrange(RIGHT, buff=0.4), demo_slot, seq_slot, three, buff=0.4)
        with self.voice("Có những bài cần chia một tập thành nhiều nhóm, ví dụ chia n công việc cho các ngày, mỗi ngày làm một nhóm việc "
                        "có chi phí cho trước. Công thức tự nhiên: f của mask bằng min theo mọi tập con khác rỗng sub của mask."):
            self.play(FadeIn(use), run_time=0.8)
        with self.voice("Mẹo duyệt mọi tập con của mask, từ lớn đến nhỏ, rất ngắn gọn: sub bằng sub trừ 1, AND mask."):
            self.play(FadeIn(code), run_time=0.6)
        shown = []
        cur = None
        with self.voice("Ví dụ mask bằng 1010. Lần lượt: 1010, rồi 1000, rồi 0010, rồi dừng khi sub bằng 0."):
            self.play(FadeIn(demo_title), FadeIn(base), run_time=0.5)
            for s in submasks(0b1010):
                r = bits_row(s, w=0.85, on=GOOD, show_idx=False).scale(sc).move_to(demo_slot)
                shown.append(format(s, "04b"))
                seq = M(" → ".join(shown), size=28, color=GOOD).scale(sc).move_to(seq_slot)
                if cur is None:
                    cur, cur_seq = r, seq
                    self.play(FadeIn(cur), FadeIn(cur_seq), run_time=0.5)
                else:
                    self.play(Transform(cur, r), Transform(cur_seq, seq), run_time=0.5)
                self.wait(0.3)
        with self.voice("Tổng số cặp mask và sub với sub là tập con của mask là 3 mũ n, vì mỗi phần tử ở một trong ba trạng thái. Với n "
                        "bằng 15, khoảng mười bốn triệu, vẫn rất nhanh; n bằng 20 thì hơn ba tỉ, quá chậm."):
            self.play(FadeIn(three), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B9_07_TongKet(B9Scene):
    def construct(self):
        self.show_header("7. Mở rộng")
        ext = [
            ("Lát gạch theo cột (“chân rết”)", "Trạng thái = dãy bit các ô cột sau đã bị chiếm",
             "Mở rộng một: đếm số cách lát bảng bằng gạch domino, với số hàng nhỏ: duyệt từng cột, trạng thái là dãy bit cho biết "
             "những ô nào của cột tiếp theo đã bị gạch nằm ngang chiếm. Đây là bitmask trên đường biên."),
            ("Khi nào nghĩ tới bitmask?", "n ≤ 20 (2ⁿ·n) hoặc n ≤ 15 (3ⁿ); phụ thuộc TẬP đã dùng",
             "Mở rộng hai: khi nào nghĩ tới bitmask? Khi giới hạn rất nhỏ, n không quá 20 hoặc không quá 15, và lời giải phụ thuộc "
             "vào tập các phần tử đã dùng, không phụ thuộc thứ tự dùng, hoặc chỉ phụ thuộc phần tử cuối."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Thứ tự ưu tiên toán tử", "mask & 1 << i == 0 bị hiểu sai: luôn ĐẶT NGOẶC",
             "Bẫy một: thứ tự ưu tiên toán tử. Phép so sánh bằng được thực hiện trước phép AND. Hãy luôn đặt ngoặc."),
            ("Tràn bit", "1 << 31 với int là tràn; n ≥ 31 dùng 1LL << i",
             "Bẫy hai: tràn bit. 1 dịch trái 31 với kiểu int là tràn số; phải dùng 1 LL."),
            ("Bộ nhớ", "2²⁰ × 20 ô long long = 160 MB: ước lượng trước",
             "Bẫy ba: bộ nhớ. 2 mũ 20 nhân 20 ô long long tốn một trăm sáu mươi megabyte. Ước lượng trước khi khai báo."),
            ("Duyệt tập con", "vòng (sub − 1) & mask dừng ở 0: tập rỗng xử lí riêng",
             "Bẫy bốn: duyệt tập con mà quên tập rỗng. Vòng lặp dừng khi sub bằng 0; nếu cần tập rỗng, xử lí riêng."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 9", [
            "• Tập con ⟷ số nguyên n bit; tập con thực sự",
            "   luôn có số nhỏ hơn ⇒ điền theo mask tăng.",
            "• best[mask]: “tập đã dùng”;",
            "   ways[mask][v]: “tập đã dùng + phần tử cuối”.",
            "• O(2ⁿ·n) hoặc O(2ⁿ·n²);",
            "   duyệt tập con của tập con: O(3ⁿ).",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: tập con tương ứng một số nguyên n bit; tập con thực sự luôn có số nhỏ hơn, nên điền bảng theo mask "
                        "tăng dần. best của mask cho tập đã dùng; ways của mask, v cho tập đã dùng và phần tử cuối."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Độ phức tạp O của 2 mũ n nhân n, hoặc nhân n bình phương; duyệt tập con của tập con là O của 3 mũ n."):
            self.play(FadeIn(mem[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Viết tập {1, 2, 4}", "dưới dạng số nguyên?"], size=40, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        br = bits_row(0b10110, n=5, w=0.95)
        ans = TB("10110₂ = 22", size=44, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: BÀI 10", size=42, color=ACCENT), T("Quy hoạch động chữ số", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, br, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: viết tập 1, 2, 4 dưới dạng số nguyên. Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Bật bit 1, bit 2 và bit 4: được 10110 nhị phân, bằng 2 cộng 4 cộng 16, bằng 22."):
            self.play(FadeIn(br), run_time=0.8)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Bài tiếp theo: quy hoạch động chữ số. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
