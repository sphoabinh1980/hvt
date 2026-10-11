"""BÀI 6 — Dãy con tăng dài nhất (LEODOI): O(n²) với truy vết, O(n log n) với mảng d."""

import bisect

from shared import *  # noqa: F401,F403

A = [4, 7, 2, 5, 3, 8, 6, 9]


def lis_quadratic(a):
    f, par = [], []
    for i in range(len(a)):
        f.append(1)
        par.append(-1)
        for j in range(i):
            if a[j] < a[i] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1
                par[i] = j
    return f, par


def lis_steps(a):
    """Các bước của thuật toán mảng d: (x, k, appended, d sau bước)."""
    d, idx, par, steps = [], [], [-1] * len(a), []
    for i, x in enumerate(a):
        k = bisect.bisect_left(d, x)
        if k > 0:
            par[i] = idx[k - 1]
        if k == len(d):
            d.append(x)
            idx.append(i)
            steps.append((x, k, True, d[:]))
        else:
            d[k] = x
            idx[k] = i
            steps.append((x, k, False, d[:]))
    seq, i = [], idx[-1]
    while i != -1:
        seq.append(a[i])
        i = par[i]
    return steps, seq[::-1]


F, PAR = lis_quadratic(A)
assert F == [1, 2, 1, 2, 2, 3, 3, 4]
_tr, _i = [], 7
while _i != -1:
    _tr.append(A[_i])
    _i = PAR[_i]
TRACE_Q = _tr[::-1]
assert TRACE_Q == [4, 7, 8, 9]
STEPS, SEQ = lis_steps(A)
assert SEQ == [2, 3, 6, 9] and STEPS[-1][3] == [2, 3, 6, 9]
assert lis_steps([1, 5, 6, 2])[0][-1][3] == [1, 2, 6]
assert len(lis_steps([10, 9, 2, 5, 3, 7, 101, 18])[0][-1][3]) == 4


def piles_of(a):
    piles = []
    for x in a:
        for p in piles:
            if p[-1] > x:
                p.append(x)
                break
        else:
            piles.append([x])
    return piles


PILES = piles_of(A)
assert len(PILES) == 4 and [p[-1] for p in PILES] == [2, 3, 6, 9]


class B6Scene(NarratedScene):
    lesson_tag = "BÀI 6"
    lesson_title = "Dãy con tăng dài nhất"


def hills(heights, unit=0.42, base_w=0.9):
    """Dãy ngọn đồi hình tam giác, đáy chung tại y = 0."""
    g = VGroup()
    for k, h in enumerate(heights):
        x = k * base_w * 0.95
        tri = Polygon([x - base_w / 2, 0, 0], [x, h * unit, 0], [x + base_w / 2, 0, 0],
                      fill_color="#3F6212", fill_opacity=1, stroke_color="#A3E635", stroke_width=2)
        snow = Polygon([x - 0.12, h * unit - 0.2, 0], [x, h * unit, 0], [x + 0.12, h * unit - 0.2, 0],
                       fill_color=WHITE, fill_opacity=0.9, stroke_width=0)
        lab = TB(str(h), size=26).next_to(tri, DOWN, buff=0.1)
        g.add(VGroup(tri, snow, lab))
    g.peaks = [np.array([k * base_w * 0.95, h * unit, 0]) for k, h in enumerate(heights)]
    return g


def flag(at, color=ACCENT, s=1.0):
    pole = Line(at, at + UP * 0.55 * s, color=INK, stroke_width=3)
    cloth = Polygon(pole.get_end(), pole.get_end() + DOWN * 0.22 * s + RIGHT * 0.32 * s, pole.get_end() + DOWN * 0.44 * s,
                    fill_color=color, fill_opacity=1, stroke_width=0)
    return VGroup(pole, cloth)


# ----------------------------------------------------------------------------
class B6_00_Intro(B6Scene):
    def construct(self):
        tag = TB("BÀI 6", size=80, color=ACCENT)
        ttl = TB("Dãy con tăng dài nhất", size=50)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Quy hoạch động O(n²): “kết thúc tại i”",
            "    và truy vết bằng mảng cha",
            "✓ Nâng cấp O(n log n): mảng d TĂNG DẦN",
            "    + tìm kiếm nhị phân",
            "✓ Biến thể: không giảm, giảm, phủ bằng",
            "    ít dãy giảm nhất",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 6: Dãy con tăng dài nhất."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ giải bài dãy con tăng dài nhất bằng quy hoạch động O của n bình phương, "
                        "với trạng thái kết thúc tại i, và truy vết bằng mảng cha."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Rồi nâng cấp lên O của n log n nhờ mảng d tăng dần và tìm kiếm nhị phân, hiểu vì sao mảng d luôn tăng. "
                        "Cuối cùng là các biến thể: không giảm, giảm dần, và phủ dãy bằng ít dãy giảm nhất."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B6_01_KhoiDong(B6Scene):
    def construct(self):
        self.show_header("Khởi động: Cắm cờ trên các ngọn đồi")
        h = hills(A)
        story = VGroup(T("Tám ngọn đồi cao 4, 7, 2, 5, 3, 8, 6, 9 (trăm mét).", size=27),
                       T("Cắm cờ sao cho ngọn sau CAO HƠN HẲN ngọn trước;", size=27),
                       T("giữ thứ tự, được bỏ qua bất kì ngọn nào.", size=27)).arrange(DOWN, buff=0.1)
        q = TB("Cắm được nhiều nhất bao nhiêu lá cờ?", size=34, color=ACCENT)
        res_slot = placeholder(7.4, 1.0)
        sky = placeholder(1, 0.7).next_to(h, UP, buff=0)  # chừa chỗ cho lá cờ trên đỉnh
        sc = fit_stack(VGroup(sky, h), story, q, res_slot, buff=0.6, max_scale=1.2)
        with self.voice("Một đoàn leo núi đi qua tám ngọn đồi lần lượt cao 4, 7, 2, 5, 3, 8, 6, 9 trăm mét."):
            self.play(LaggedStart(*[GrowFromEdge(x, DOWN) for x in h], lag_ratio=0.12), run_time=1.6)
        with self.voice("Trưởng đoàn muốn chọn ra một số ngọn đồi để cắm cờ, sao cho đi tới đâu cờ cắm càng cao hơn: ngọn sau phải "
                        "cao hơn hẳn ngọn trước. Thứ tự các ngọn đồi giữ nguyên, nhưng được bỏ qua bất kì ngọn nào."):
            self.play(FadeIn(story), run_time=0.8)
        with self.voice("Cắm được nhiều nhất bao nhiêu lá cờ?"):
            self.play(Write(q), run_time=0.8)
        peaks = [h[k][0].get_vertices()[1] for k in range(len(A))]
        with self.voice("Câu trả lời là 4. Ví dụ cắm ở các ngọn cao 2, 3, 6, 9."):
            for k in (2, 4, 6, 7):
                self.play(FadeIn(flag(peaks[k], s=sc), shift=DOWN * 0.2), h[k][0].animate.set_fill("#A16207", 1),
                          run_time=0.5)
            ans = TB("4 lá cờ: 2 → 3 → 6 → 9", size=36, color=GOOD).scale(sc).move_to(res_slot)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Một đáp án khác là 4, 7, 8, 9, hay 4, 5, 6, 9. Cũng đều dài 4."):
            self.play(Indicate(ans, color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán LEODOI")
        box = tag_box("BÀI TOÁN: LEODOI", [
            "Cho dãy n số nguyên a₁, …, aₙ. DÃY CON là dãy thu",
            "được bằng cách XÓA đi một số phần tử",
            "(giữ nguyên thứ tự phần tử còn lại).",
            "Tìm dãy con TĂNG NGẶT dài nhất, in độ dài",
            "và một dãy con như vậy.    n ≤ 2·10⁵",
        ], accent=BLUEC, width=7.5, size=28)
        diff = VGroup(
            panel(VGroup(TB("DÃY CON", size=28, color=GOOD), T("được bỏ phần tử", size=24), T("(bài này)", size=22, color=MUTED))
                  .arrange(DOWN, buff=0.08), width=3.65, stroke=GOOD),
            panel(VGroup(TB("ĐOẠN CON", size=28, color=ORANGE), T("phần tử liên tiếp", size=24),
                         T("(Kadane, Bài 2)", size=22, color=MUTED)).arrange(DOWN, buff=0.08), width=3.65, stroke=ORANGE),
        ).arrange(RIGHT, buff=0.2)
        fit_stack(box, diff, buff=0.8, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán LEODOI: cho dãy n số nguyên. Một dãy con là dãy thu được bằng cách xóa "
                        "đi một số phần tử, giữ nguyên thứ tự các phần tử còn lại. Hãy tìm dãy con tăng ngặt dài nhất. "
                        "n lên tới hai trăm nghìn."):
            self.play(FadeIn(box), run_time=0.8)
        with self.voice("Lưu ý sự khác nhau giữa dãy con, được bỏ phần tử như bài này, và đoạn con, các phần tử liên tiếp, như bài "
                        "Kadane ở Bài 2."):
            self.play(FadeIn(diff), run_time=0.8)

        self.clear_body()
        self.show_header("2. Ý tưởng ngây thơ: Thử mọi dãy con")
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Mỗi phần tử giữ hoặc bỏ ⇒ 2ⁿ dãy con,",
            "mỗi dãy kiểm tra O(n): tổng O(2ⁿ · n).",
            "n = 20: ≈ 2·10⁷ phép — chạy kịp",
            "n = 40: ≈ 4·10¹³ phép — không thể!",
        ], accent=ORANGE, width=7.5, size=30)
        cnt[3][3].set_color(BAD)
        stuck = tag_box("BẾ TẮC", [
            "Dãy con tăng rất “có cấu trúc”: được xây bằng",
            "cách NỐI DẦN từng phần tử vào CUỐI.",
            "Biết các dãy tăng kết thúc ở vị trí trước,",
            "liệu có nối được ngay mà không liệt kê lại?",
        ], accent=BAD, width=7.5, size=29)
        fit_stack(cnt, stuck, buff=0.8, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: mỗi phần tử được giữ hoặc bỏ, nên có 2 mũ n dãy con. Với mỗi dãy con, kiểm tra nó có "
                        "tăng ngặt không. Tổng O của 2 mũ n nhân n. n bằng 20 thì chạy kịp, n bằng 40 thì không thể."):
            self.play(FadeIn(cnt), run_time=0.8)
        with self.voice("Bế tắc! Nhưng dãy con tăng thật ra rất có cấu trúc: nó được xây bằng cách nối dần từng phần tử vào cuối. "
                        "Nếu ta biết các dãy tăng kết thúc ở những vị trí trước, liệu có nối được ngay mà không cần liệt kê lại?"):
            self.play(FadeIn(stuck), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
QUAD_CODE = """
for (int i = 0; i < n; i++) {
    length[i] = 1;
    parent[i] = -1;
    for (int j = 0; j < i; j++)
        if (a[j] < a[i] && length[j] + 1 > length[i]) {
            length[i] = length[j] + 1;
            parent[i] = j;
        }
}
"""


class B6_02_On2(B6Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc lần 1: Quy hoạch động O(n²)")
        why = VGroup(T("Như bài Kadane: trạng thái “kết thúc tại i”,", size=30),
                     T("vì muốn nối thêm phần tử vào cuối", size=30),
                     T("thì phải biết PHẦN TỬ CUỐI.", size=30, color=ACCENT)).arrange(DOWN, buff=0.1)
        formula = tag_box("CÔNG THỨC", [
            "f(i) = độ dài dãy con tăng dài nhất",
            "         kết thúc ĐÚNG tại aᵢ",
            "f(i) = 1 + max{ f(j) : j < i, aⱼ < aᵢ }",
            "(không có j nào thì f(i) = 1)",
            "Đáp án: max của MỌI f(i)",
        ], accent=ACCENT, width=7.5, size=29)
        formula[3][2].set_color(ACCENT)
        fit_stack(why, formula, buff=0.8, max_scale=1.25)
        with self.voice("Rút kinh nghiệm từ bài Kadane, ta dùng trạng thái kết thúc tại i, vì để nối thêm một phần tử vào cuối, "
                        "ta cần biết phần tử cuối của dãy hiện tại."):
            self.play(FadeIn(why), run_time=0.8)
        with self.voice("Đặt f của i là độ dài dãy con tăng dài nhất kết thúc đúng tại a i. Phần tử đứng ngay trước a i trong dãy "
                        "là một a j nào đó với j nhỏ hơn i và a j nhỏ hơn a i, hoặc a i đứng một mình."):
            self.play(FadeIn(formula[0:3]), FadeIn(formula[3][0:2]), run_time=0.8)
        with self.voice("Vậy f của i bằng 1 cộng max các f của j thỏa mãn. Đáp án là max của mọi f của i, vì dãy tốt nhất có thể "
                        "kết thúc ở bất kì đâu."):
            self.play(FadeIn(formula[3][2:]), run_time=0.8)

        self.clear_body()
        self.show_header("Chạy tay: bảng f và mảng cha")
        a_row = array_row(A, w=0.85, h=0.8, size=30, index_from=1, label="a")
        f_row = array_row([""] * 8, w=0.85, h=0.85, size=30, label="f", show_index=False)
        for k, c in enumerate(f_row.cells):
            c.move_to(a_row.cells[k].get_center() + DOWN * 1.0)
        f_row.lab.next_to(f_row.cells, LEFT, buff=0.25)
        tables = VGroup(a_row, f_row)
        arc_space = placeholder(7.0, 1.6)
        eq_slot = placeholder(7.2, 1.0)
        sc = fit_stack(arc_space, tables, eq_slot, buff=0.3, max_scale=1.25)
        self.play(FadeIn(tables), run_time=0.8)
        eq = None
        parents = VGroup()
        for i in range(8):
            cands = [j for j in range(i) if A[j] < A[i]]
            if cands:
                best = max(F[j] for j in cands)
                f_text = f"f({i + 1}) = 1 + max{{{', '.join(str(F[j]) for j in cands)}}} = {F[i]}"
            else:
                f_text = f"f({i + 1}) = 1  (không có phần tử nhỏ hơn đứng trước)"
            if i == 0:
                sp = "f của 1 bằng 1: phần tử 4 đứng một mình."
            elif i == 5:
                sp = ("Tính f của 6, với a 6 bằng 8: mọi phần tử đứng trước đều nhỏ hơn 8. Trong số đó, f lớn nhất là 2, "
                      "nên f của 6 bằng 3.")
            elif i == 7:
                sp = "Cuối cùng f của 8, với a 8 bằng 9: f lớn nhất phía trước là 3, nên f của 8 bằng 4."
            elif not cands:
                sp = f"f của {i + 1}: a bằng {A[i]}, không có phần tử nào nhỏ hơn đứng trước, nên bằng 1."
            else:
                sp = f"f của {i + 1}, với a bằng {A[i]}: các phần tử nhỏ hơn đứng trước có f lớn nhất là {best}, nên bằng {F[i]}."
            new_eq = M(f_text, size=28).scale(sc)
            if new_eq.width > 7.3:
                new_eq.scale_to_fit_width(7.3)
            new_eq.move_to(eq_slot)
            with self.voice(sp):
                hi = [a_row.cells[j][0].animate.set_fill(BLUEC, 1) for j in cands]
                a_row.cells[i][0].set_fill(PANEL_2, 1)
                anims = hi + [a_row.cells[i][0].animate.set_stroke(ACCENT, 6)]
                if eq is None:
                    eq = new_eq
                    anims.append(FadeIn(eq))
                else:
                    anims.append(Transform(eq, new_eq))
                self.play(*anims, run_time=0.6)
                c = f_row.cells[i]
                post = [c[0].animate.set_fill(ACCENT, 1), Transform(c[1], set_cell_value(c, F[i], color=BG))]
                if PAR[i] != -1:
                    arc = CurvedArrow(a_row.cells[PAR[i]].get_top() + UP * 0.05, a_row.cells[i].get_top() + UP * 0.05,
                                      angle=-PI / 2.5, color=GOOD, stroke_width=3, tip_length=0.16)
                    parents.add(arc)
                    post.append(Create(arc))
                self.play(*post, run_time=0.5)
                self.play(*[a_row.cells[j][0].animate.set_fill(PANEL_2, 1) for j in range(8)],
                          a_row.cells[i][0].animate.set_stroke(MUTED, 2), run_time=0.3)
        with self.voice("Bảng đầy đủ: f bằng 1, 2, 1, 2, 2, 3, 3, 4. Đáp án là 4. Các mũi tên xanh là mảng cha: parent của i là chỉ "
                        "số j đạt max."):
            self.play(Circumscribe(f_row.cells[7], color=ACCENT), run_time=0.8)
        path_ids = []
        k = 7
        while k != -1:
            path_ids.append(k)
            k = PAR[k]
        with self.voice("Truy vết: từ vị trí có f lớn nhất là vị trí 8, lần theo parent về đầu dãy: 9 về 8, 8 về 7, 7 về 4. "
                        "Đảo ngược ta được dãy 4, 7, 8, 9."):
            self.play(*[f_row.cells[j][0].animate.set_fill(GOOD, 1) for j in path_ids],
                      *[a_row.cells[j][0].animate.set_fill(GOOD, 1) for j in path_ids],
                      *[a_row.cells[j][1].animate.set_color(BG) for j in path_ids], run_time=0.8)
            res = TB("Truy vết: 4 → 7 → 8 → 9", size=34, color=GOOD).scale(sc).move_to(eq_slot)
            self.play(Transform(eq, res), run_time=0.6)

        self.clear_body()
        self.show_header("Code O(n²) và bế tắc lần 2")
        code = code_block(QUAD_CODE, size=22)
        cx = VGroup(T("Hai vòng lồng nhau ≈ n²/2 phép:", size=28), TB("O(n²)", size=40, color=ORANGE)).arrange(RIGHT, buff=0.2)
        cx2 = T("n = 5000: tốt;  n = 2·10⁵: 2·10¹⁰ phép — quá chậm!", size=27, color=MUTED)
        stuck = tag_box("BẾ TẮC LẦN 2", [
            "Tính f(i) phải quét MỌI j < i để tìm f(j) lớn",
            "nhất trong các aⱼ < aᵢ. Phần lớn là thừa.",
            "Trả lời “trong các phần tử nhỏ hơn aᵢ, dãy tăng",
            "dài nhất kết thúc ở chúng dài bao nhiêu?”",
            "mà KHÔNG quét lại từ đầu?",
        ], accent=BAD, width=7.5, size=28)
        fit_stack(code, VGroup(cx, cx2).arrange(DOWN, buff=0.12), stuck, buff=0.6)
        with self.voice("Code O của n bình phương: với mỗi i, quét mọi j phía trước. Nếu a j nhỏ hơn a i và nối vào được dãy dài "
                        "hơn, cập nhật độ dài và lưu parent bằng j."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 4, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
            self.play(Transform(hl, line_box(code, 6, GOOD)), run_time=0.4)
        with self.voice("Hai vòng lặp lồng nhau, tổng khoảng n bình phương chia 2 phép. Với n bằng năm nghìn chạy tốt; với n bằng hai "
                        "trăm nghìn cần hai mươi tỉ phép, quá chậm."):
            self.play(FadeOut(hl), FadeIn(cx), FadeIn(cx2), run_time=0.8)
        with self.voice("Bế tắc lần 2: để tính f của i, ta quét mọi j để tìm f lớn nhất trong số các a j nhỏ hơn a i. Phần lớn các "
                        "phép so sánh đó là thừa. Có cách nào trả lời câu hỏi này mà không quét lại từ đầu?"):
            self.play(FadeIn(stuck), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
NLOGN_CODE = """
for (int i = 0; i < n; i++) {
    int length = lower_bound(tailValue.begin(), tailValue.end(),
                             height[i]) - tailValue.begin();
    if (length > 0) parent[i] = tailIndex[length - 1];
    if (length == (int)tailValue.size()) {
        tailValue.push_back(height[i]);
        tailIndex.push_back(i);
    } else {
        tailValue[length] = height[i];
        tailIndex[length] = i;
    }
}
"""


class B6_03_MangD(B6Scene):
    def construct(self):
        self.show_header("4. Phá bế tắc lần 2: Mảng d, O(n log n)")
        q = TB("Hai dãy tăng cùng dài 2: dãy nào “có tương lai” hơn?", size=28)
        seqs = VGroup()
        for vals, col, lab in [([4, 7], ORANGE, "kết thúc bằng 7"), ([2, 5], GOOD, "kết thúc bằng 5")]:
            r = VGroup(*[cell(v, w=0.85, h=0.8, size=32) for v in vals]).arrange(RIGHT, buff=0)
            for c in r:
                c[0].set_fill(col, 1)
                c[1].set_color(BG)
            plus = VGroup(T("+", size=34), cell(6, w=0.85, h=0.8, size=32)).arrange(RIGHT, buff=0.2)
            seqs.add(VGroup(r, plus, T(lab, size=24, color=col)).arrange(RIGHT, buff=0.3))
        seqs.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        verdict = VGroup(T("Mọi số nối được sau 7 thì cũng nối được sau 5,", size=27),
                         T("nhưng 6 chỉ nối được sau 5!", size=27, color=GOOD)).arrange(DOWN, buff=0.1)
        defi = panel(VGroup(TB("d[k] =", size=34, color=ACCENT), T("phần tử CUỐI NHỎ NHẤT của một", size=28),
                            T("dãy con tăng dài k (trong phần đã duyệt)", size=28)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        fit_stack(q, seqs, verdict, defi, buff=0.6, max_scale=1.25)
        with self.voice("Bước một: đổi câu hỏi. Giả sử đã có hai dãy tăng cùng độ dài 2: dãy 4, 7 và dãy 2, 5. Dãy nào có tương lai "
                        "hơn?"):
            self.play(FadeIn(q), FadeIn(seqs[0][0]), FadeIn(seqs[0][2]), FadeIn(seqs[1][0]), FadeIn(seqs[1][2]), run_time=1.0)
        with self.voice("Chắc chắn là dãy kết thúc bằng 5: mọi số nối được vào sau 7 thì cũng nối được vào sau 5, nhưng số 6 chỉ "
                        "nối được vào sau 5."):
            self.play(FadeIn(seqs[1][1]), run_time=0.5)
            cross = Cross(seqs[0][1], stroke_color=BAD, stroke_width=6)
            self.play(FadeIn(seqs[0][1]), run_time=0.4)
            self.play(Create(cross), FadeIn(verdict), run_time=0.8)
        with self.voice("Vậy với mỗi độ dài k, ta chỉ cần nhớ phần tử cuối nhỏ nhất có thể. Gọi d của k là phần tử cuối nhỏ nhất "
                        "của một dãy con tăng dài k, trong các phần tử đã duyệt."):
            self.play(FadeIn(defi), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 2: Mảng d luôn TĂNG DẦN")
        proof = tag_box("VÌ SAO d[1] < d[2] < d[3] < …?", [
            "Lấy dãy tăng dài k+1 có phần tử cuối d[k+1].",
            "Bỏ phần tử cuối ⇒ dãy tăng dài k có phần tử",
            "cuối NHỎ HƠN d[k+1].",
            "d[k] là phần tử cuối nhỏ nhất của mọi dãy dài k",
            "⇒ d[k] ≤ (phần tử đó) < d[k+1].",
        ], accent=GOOD, width=7.5, size=28)
        rule = tag_box("BƯỚC 3: THÊM PHẦN TỬ x", [
            "k = số ô của d có giá trị < x",
            "   = lower_bound(d, x)  (tìm kiếm nhị phân!)",
            "• k = độ dài d: NỐI THÊM x vào cuối d",
            "• ngược lại: THAY d[k+1] bằng x",
            "  (cuối nhỏ hơn hoặc bằng ⇒ tương lai tốt hơn)",
        ], accent=ACCENT, width=7.5, size=28)
        fit_stack(proof, rule, buff=0.8, max_scale=1.2)
        with self.voice("Bước hai: mảng d luôn tăng dần. Vì sao? Lấy dãy tăng dài k cộng 1 có phần tử cuối d của k cộng 1. Bỏ phần "
                        "tử cuối đi, ta được một dãy tăng dài k có phần tử cuối nhỏ hơn. Vì d của k là phần tử cuối nhỏ nhất của "
                        "mọi dãy dài k, nên d của k nhỏ hơn d của k cộng 1."):
            self.play(FadeIn(proof), run_time=1.0)
        with self.voice("Bước ba: thêm phần tử x. x nối được vào sau mọi dãy có phần tử cuối nhỏ hơn x. Vì d tăng dần, các ô nhỏ hơn "
                        "x nằm liền nhau ở đầu mảng, nên số ô đó tìm được bằng tìm kiếm nhị phân, chính là lower bound."):
            self.play(FadeIn(rule[0:3]), FadeIn(rule[3][0:2]), run_time=1.0)
        with self.voice("Nếu số ô đó bằng độ dài mảng d, ta nối thêm x vào cuối. Ngược lại, ta thay ô ngay sau bằng x: phần tử cuối "
                        "nhỏ hơn hoặc bằng, có tương lai tốt hơn. Mỗi bước chỉ đổi một ô, và d vẫn tăng dần."):
            self.play(FadeIn(rule[3][2:]), run_time=0.8)

        self.clear_body()
        self.show_header("Chạy tay: mảng d qua từng phần tử")
        a_row = array_row(A, w=0.85, h=0.8, size=30, index_from=1, label="a")
        d_slots = VGroup(*[cell("", w=1.2, h=1.0, size=40) for _ in range(4)]).arrange(RIGHT, buff=0)
        d_idx = VGroup(*[T(f"d[{k + 1}]", size=24, color=MUTED).next_to(c, UP, buff=0.1) for k, c in enumerate(d_slots)])
        d_lab = TB("d", size=34, color=ACCENT).next_to(d_slots, LEFT, buff=0.3)
        d_grp = VGroup(d_slots, d_idx, d_lab)
        for c in d_slots:
            c[0].set_stroke(opacity=0.25)
        eq_slot = placeholder(7.3, 1.1)
        sc = fit_stack(a_row, d_grp, eq_slot, buff=0.8, max_scale=1.25)
        self.play(FadeIn(a_row), FadeIn(d_grp), run_time=0.8)
        eq = None
        filled = 0
        lines = {
            0: "x bằng 4: d đang rỗng, nối thêm. d bằng 4.",
            1: "x bằng 7: lớn hơn mọi ô, nối thêm. d bằng 4, 7.",
            2: "x bằng 2: không ô nào nhỏ hơn 2, thay d 1 bằng 2. d bằng 2, 7.",
            3: "x bằng 5: một ô nhỏ hơn 5, thay d 2 bằng 5. d bằng 2, 5.",
            4: "x bằng 3: thay d 2 bằng 3. d bằng 2, 3.",
            5: "x bằng 8: lớn hơn mọi ô, nối thêm. d bằng 2, 3, 8.",
            6: "x bằng 6: thay d 3 bằng 6. d bằng 2, 3, 6.",
            7: "x bằng 9: nối thêm. d bằng 2, 3, 6, 9. Độ dài 4!",
        }
        for i, (x, k, app, d_after) in enumerate(STEPS):
            txt = f"x = {x}: lower_bound = {k}  →  " + ("NỐI THÊM" if app else f"THAY d[{k + 1}]")
            new_eq = TB(txt, size=30, color=GOOD if app else ORANGE).scale(sc)
            if new_eq.width > 7.3:
                new_eq.scale_to_fit_width(7.3)
            new_eq.move_to(eq_slot)
            with self.voice(lines[i]):
                anims = [a_row.cells[i][0].animate.set_fill(ACCENT, 1), a_row.cells[i][1].animate.set_color(BG)]
                if eq is None:
                    eq = new_eq
                    anims.append(FadeIn(eq))
                else:
                    anims.append(Transform(eq, new_eq))
                # vùng tìm kiếm nhị phân
                if filled:
                    region = SurroundingRectangle(VGroup(*d_slots[:filled]), color=BLUEC, buff=0.04, stroke_width=4)
                    anims.append(Create(region))
                self.play(*anims, run_time=0.5)
                c = d_slots[k]
                mover = a_row.cells[i][1].copy()
                self.play(mover.animate.move_to(c[0]).scale(1.2), c[0].animate.set_stroke(opacity=1), run_time=0.5)
                self.play(FadeOut(mover), Transform(c[1], set_cell_value(c, x, color=BG)),
                          c[0].animate.set_fill(GOOD if app else ORANGE, 1), run_time=0.35)
                if filled:
                    self.play(FadeOut(region), run_time=0.15)
                self.play(c[0].animate.set_fill(BLUEC, 1), a_row.cells[i][0].animate.set_fill(PANEL_2, 1),
                          a_row.cells[i][1].animate.set_color(INK), run_time=0.25)
                filled = len(d_after)
        with self.voice("Độ dài dãy con tăng dài nhất chính là độ dài của mảng d sau khi duyệt hết: 4."):
            self.play(Circumscribe(d_slots, color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("Cảnh báo: mảng d KHÔNG phải đáp án")
        warn_row = array_row([1, 5, 6, 2], w=0.9, h=0.85, size=32, index_from=1, label="a")
        d_row = array_row([1, 2, 6], w=0.9, h=0.85, size=32, label="d", show_index=False)
        for c in d_row.cells:
            c[0].set_fill(BLUEC, 1)
            c[1].set_color(BG)
        warn = tag_box("CẢNH BÁO", [
            "Dãy 1, 5, 6, 2 ⇒ d cuối là 1, 2, 6.",
            "Nhưng “2, 6” KHÔNG phải dãy con (6 đứng trước 2)!",
            "Muốn in dãy con phải TRUY VẾT: khi đặt aᵢ vào",
            "ô k+1, ghi parent[i] = chỉ số đang giữ ô d[k].",
        ], accent=BAD, width=7.5, size=28)
        res = VGroup(T("Ví dụ chính, truy vết cho:", size=28), TB("2, 3, 6, 9", size=36, color=GOOD)).arrange(RIGHT, buff=0.25)
        fit_stack(warn_row, d_row, warn, res, buff=0.6, max_scale=1.2)
        with self.voice("Cảnh báo: mảng d không phải là đáp án. Ở ví dụ, d cuối cùng là 2, 3, 6, 9, và tình cờ lại là một dãy con "
                        "tăng. Nhưng thử dãy 1, 5, 6, 2: mảng d cuối là 1, 2, 6."):
            self.play(FadeIn(warn_row), FadeIn(d_row), run_time=0.8)
        with self.voice("Trong khi 2, 6 không phải dãy con, vì 6 đứng trước 2. Muốn in dãy con, ta phải truy vết: khi thêm a i vào "
                        "ô k cộng 1, ghi parent của i bằng chỉ số của phần tử đang giữ ô d của k lúc đó."):
            self.play(FadeIn(warn), Indicate(d_row.cells[1], color=BAD), run_time=1.0)
        with self.voice("Với ví dụ chính, truy vết cho dãy 2, 3, 6, 9."):
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("Code O(n log n) và độ phức tạp")
        code = code_block(NLOGN_CODE, size=19)
        note = VGroup(T("tailValue = mảng d,  tailIndex = chỉ số đang giữ mỗi ô", size=26),
                      T("lower_bound: vị trí đầu tiên ≥ x = số ô nhỏ hơn x", size=26)).arrange(DOWN, buff=0.1)
        cx = VGroup(TB("O(n log n)", size=44, color=GOOD), T("n = 2·10⁵: ≈ 2·10⁵ · 18 ≈ 3,6·10⁶ phép so sánh", size=26)).arrange(
            DOWN, buff=0.12)
        fit_stack(code, note, cx, buff=0.6)
        with self.voice("Chương trình giữ song song hai mảng: tail value, chính là d, và tail index, chỉ số của phần tử đang giữ mỗi ô. "
                        "Hàm lower bound trả về vị trí đầu tiên có giá trị lớn hơn hoặc bằng x, đúng bằng số ô nhỏ hơn x."):
            self.play(FadeIn(code), FadeIn(note), run_time=0.8)
            hl = line_box(code, 1, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
            self.play(Transform(hl, line_box(code, 3, GOOD)), run_time=0.4)
        with self.voice("Mỗi phần tử thực hiện một lần tìm kiếm nhị phân: O của log n. Tổng cộng O của n log n: với n bằng hai trăm "
                        "nghìn, chỉ khoảng ba triệu sáu trăm nghìn phép so sánh."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B6_04_TongKet(B6Scene):
    def construct(self):
        self.show_header("5. Mở rộng: không giảm, giảm dần")
        ext = list_cards([
            ("Dãy KHÔNG GIẢM (cho phép bằng)", "Thay lower_bound bằng upper_bound"),
            ("Dãy GIẢM ngặt", "Đổi dấu mọi phần tử (aᵢ ← −aᵢ) rồi tìm dãy tăng"),
        ])
        fit_stack(ext, max_scale=1.3)
        with self.voice("Mở rộng một: dãy không giảm, cho phép bằng nhau, thì thay lower bound bằng upper bound, vì x được nối sau "
                        "cả những dãy có phần tử cuối bằng x."):
            self.play(FadeIn(ext[0], shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Dãy giảm ngặt: đổi dấu mọi phần tử rồi tìm dãy tăng ngặt."):
            self.play(FadeIn(ext[1], shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Mở rộng 2: Phủ dãy bằng ít dãy giảm nhất")
        story = VGroup(T("Xếp các toa tàu (theo thứ tự đến) vào các đoàn,", size=27),
                       T("mỗi đoàn có số hiệu GIẢM DẦN. Ít nhất bao nhiêu đoàn?", size=27),
                       T("Tham lam: xếp vào đoàn ĐẦU TIÊN có toa cuối lớn hơn.", size=27, color=ACCENT)).arrange(DOWN, buff=0.1)
        incoming = VGroup(*[cell(v, w=0.75, h=0.7, size=28) for v in A]).arrange(RIGHT, buff=0.08)
        track_lines = VGroup(*[Line(LEFT * 3.4, RIGHT * 3.4, color=MUTED, stroke_width=2).shift(DOWN * k * 0.95)
                               for k in range(4)])
        tlabs = VGroup(*[T(f"đoàn {k + 1}", size=22, color=MUTED).next_to(track_lines[k], LEFT, buff=0.1).shift(UP * 0.35)
                         for k in range(4)])
        tracks = VGroup(track_lines, tlabs)
        concl = VGroup(TB("Số đoàn ít nhất = độ dài dãy tăng dài nhất = 4", size=28, color=GOOD),
                       T("toa cuối các đoàn 2, 3, 6, 9 chính là mảng d (định lí Dilworth)", size=25, color=MUTED)).arrange(
            DOWN, buff=0.1)
        sc = fit_stack(story, incoming, tracks, concl, buff=0.6, max_scale=1.2)
        with self.voice("Mở rộng hai, một bài toán nghe rất khác: xếp các toa tàu theo thứ tự đến vào các đoàn, mỗi đoàn phải có số "
                        "hiệu giảm dần. Cần ít nhất bao nhiêu đoàn? Cách xếp tham lam: mỗi toa xếp vào đoàn đầu tiên có toa cuối "
                        "lớn hơn nó, nếu không có thì mở đoàn mới."):
            self.play(FadeIn(story), FadeIn(incoming), FadeIn(tracks), run_time=1.0)
        piles = []
        counts = []
        with self.voice("Thử với dãy 4, 7, 2, 5, 3, 8, 6, 9: toa 4 mở đoàn 1, toa 7 mở đoàn 2, toa 2 vào đoàn 1, toa 5 vào đoàn 2, "
                        "toa 3 vào đoàn 2, toa 8 mở đoàn 3, toa 6 vào đoàn 3, toa 9 mở đoàn 4."):
            for i, x in enumerate(A):
                for k, p in enumerate(piles):
                    if p[-1] > x:
                        p.append(x)
                        break
                else:
                    piles.append([x])
                    counts.append(0)
                    k = len(piles) - 1
                pos = track_lines[k].get_left() + RIGHT * (0.5 + counts[k] * 0.85) * sc + UP * 0.35 * sc
                counts[k] += 1
                self.play(incoming[i].animate.move_to(pos), run_time=0.45)
        with self.voice("Cần đúng 4 đoàn. Số đoàn ít nhất đúng bằng độ dài dãy con tăng dài nhất. Hai toa thuộc một dãy tăng không "
                        "thể chung đoàn, nên cần ít nhất L đoàn; và cách xếp tham lam đạt đúng L, vì toa cuối các đoàn chính là "
                        "mảng d. Đây là một trường hợp của định lí Dilworth."):
            self.play(FadeIn(concl), run_time=0.8)

        self.clear_body()
        self.show_header("Mở rộng 3, 4")
        ext = list_cards([
            ("Hình lồng nhau (hai chiều)", "Sắp w tăng, cùng w thì h GIẢM"),
            ("Đếm số dãy / tổng lớn nhất", "f(i) = 1 + max f(j) + cây Fenwick"),
        ])
        fit_stack(ext, max_scale=1.3)
        with self.voice("Mở rộng ba: cho các hình chữ nhật, tìm dãy dài nhất mà mỗi hình lồng vừa vào hình sau. Sắp xếp theo chiều "
                        "rộng tăng dần, cùng chiều rộng thì chiều cao giảm dần, rồi tìm dãy con tăng ngặt trên chiều cao. Thứ tự "
                        "sắp xếp phụ chính là mấu chốt."):
            self.play(FadeIn(ext[0], shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Mở rộng bốn: khi cần đếm số dãy con tăng dài nhất, hay dãy tăng có tổng lớn nhất, mảng d không còn đủ. "
                        "Quay lại công thức f của i và dùng cây Fenwick, trình bày ở Bài 14."):
            self.play(FadeIn(ext[1], shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Nhầm dãy con với đoạn con", "Dãy con được bỏ phần tử", "Bẫy một: nhầm dãy con với đoạn con."),
            ("Sai lower_bound / upper_bound", "Tăng ngặt: lower_bound; không giảm: upper_bound",
             "Bẫy hai: dùng sai lower bound và upper bound."),
            ("In mảng d làm đáp án", "Sai! Phải truy vết", "Bẫy ba: in mảng d làm đáp án. Sai, phải truy vết."),
            ("Lấy f(n) làm đáp án", "Cách O(n²): phải lấy max mọi f(i)",
             "Bẫy bốn: lấy f của n làm đáp án trong cách O của n bình phương. Phải lấy max mọi f của i."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 6", [
            "• “Kết thúc tại i”: f(i) = 1 + max f(j),",
            "   j < i, aⱼ < aᵢ.  O(n²).",
            "• d[k] = phần tử cuối nhỏ nhất của dãy",
            "   tăng dài k; d tăng dần; mỗi phần tử:",
            "   lower_bound rồi nối/thay.  O(n log n).",
            "• Độ dài dãy tăng dài nhất = số dãy giảm",
            "   ít nhất phủ được dãy.",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: trạng thái kết thúc tại i, f của i bằng 1 cộng max f của j, với j nhỏ hơn i và a j nhỏ hơn a i, "
                        "độ phức tạp O của n bình phương."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:2]), run_time=1.0)
        with self.voice("d của k là phần tử cuối nhỏ nhất của dãy tăng dài k; d tăng dần; mỗi phần tử tìm lower bound rồi nối hoặc "
                        "thay, O của n log n. Và độ dài dãy tăng dài nhất bằng số dãy giảm ít nhất phủ được dãy."):
            self.play(FadeIn(mem[3][2:]), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Độ dài dãy con tăng ngặt dài nhất:", "10, 9, 2, 5, 3, 7, 101, 18"], size=36, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        steps, _ = lis_steps([10, 9, 2, 5, 3, 7, 101, 18])
        d_final = steps[-1][3]
        row = array_row(d_final, w=1.2, h=1.0, size=36, label="d", show_index=False)
        for c in row.cells:
            c[0].set_fill(GOOD, 1)
            c[1].set_color(BG)
        ans = T("Đáp án 4, ví dụ 2, 3, 7, 18", size=32, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: BÀI 7", size=42, color=ACCENT), T("Quy hoạch động trên hai xâu", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, row, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: tìm độ dài dãy con tăng ngặt dài nhất của 10, 9, 2, 5, 3, 7, 101, 18. "
                        "Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Mảng d cuối cùng là 2, 3, 7, 18, độ dài 4. Một dãy con tăng dài nhất là 2, 3, 7, 18."):
            self.play(LaggedStart(*[FadeIn(c, scale=0.6) for c in row.cells], lag_ratio=0.2), FadeIn(row.lab), run_time=1.0)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Bài tiếp theo: quy hoạch động trên hai xâu. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
