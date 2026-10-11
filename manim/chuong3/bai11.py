"""BÀI 11 — Quy hoạch động trên cây: DATIEC (mời / không mời), duyệt BFS ngược, đổi gốc KHOANGCACH."""

from itertools import combinations

from shared import *  # noqa: F401,F403

# ---------------------------------------------------------------- DATIEC
JOY = {1: 5, 2: 3, 3: 9, 4: 4, 5: 2, 6: 1, 7: 7}
BOSS = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}
KIDS = {v: [c for c in sorted(BOSS) if BOSS[c] == v] for v in JOY}
ORDER = [1]
for _v in ORDER:
    ORDER.extend(KIDS[_v])
assert ORDER == [1, 2, 3, 4, 5, 6, 7]


def party(joy):
    moi, khong = {}, {}
    for v in reversed(ORDER):
        moi[v] = joy[v] + sum(khong[c] for c in KIDS[v])
        khong[v] = sum(max(moi[c], khong[c]) for c in KIDS[v])
    return moi, khong


MOI, KHONG = party(JOY)
assert (MOI[2], KHONG[2]) == (3, 6) and (MOI[3], KHONG[3]) == (9, 8) and (MOI[1], KHONG[1]) == (19, 15)
assert max(MOI[1], KHONG[1]) == 19


def ok(s):
    return all(not (v in s and BOSS[v] in s) for v in BOSS)


BEST = max(sum(JOY[v] for v in s) for r in range(8) for s in combinations(JOY, r) if ok(set(s)))
assert BEST == 19 and ok({1, 4, 5, 6, 7}) and sum(JOY[v] for v in (1, 4, 5, 6, 7)) == 19
# tham lam: mời người vui nhất (3) trước
GREEDY = max(sum(JOY[v] for v in s) for r in range(8) for s in combinations(JOY, r) if ok(set(s)) and 3 in s)
assert GREEDY == 15
_m, _k = party({**JOY, 1: 1})
assert max(_m[1], _k[1]) == 15 and _m[1] == 15 and _k[1] == 15

# ---------------------------------------------------------------- KHOANGCACH
DN = 6
DEDGES = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
DPAR = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3}
DORDER = [1, 2, 3, 4, 5, 6]
DEPTH = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}
SIZE = {v: 1 for v in range(1, 7)}
for _v in reversed(DORDER[1:]):
    SIZE[DPAR[_v]] += SIZE[_v]
assert SIZE == {1: 6, 2: 3, 3: 2, 4: 1, 5: 1, 6: 1}
ANS = {1: sum(DEPTH.values())}
for _v in DORDER[1:]:
    ANS[_v] = ANS[DPAR[_v]] - SIZE[_v] + (DN - SIZE[_v])


def _bfs_sum(s):
    adj = {v: [] for v in range(1, 7)}
    for a, b in DEDGES:
        adj[a].append(b)
        adj[b].append(a)
    d, q = {s: 0}, [s]
    for x in q:
        for y in adj[x]:
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return sum(d.values())


assert [ANS[v] for v in range(1, 7)] == [8, 8, 10, 12, 12, 14] == [_bfs_sum(v) for v in range(1, 7)]

DATIEC_CODE = """
vector<int> order = {1};
for (int k = 0; k < order.size(); k++)
  for (int c : children[order[k]])
    order.push_back(c);
for (int k = n - 1; k >= 0; k--) {
  int v = order[k];
  invited[v] = joy[v];
  absent[v] = 0;
  for (int c : children[v]) {
    invited[v] += absent[c];
    absent[v] += max(invited[c], absent[c]);
  }
}
cout << max(invited[1], absent[1]);
"""

REROOT_CODE = """
// pass 1: BFS from 1 -> parent, depth
for (int k = n - 1; k > 0; k--) {
  int v = order[k];
  sz[parent[v]] += sz[v];
}
for (int v = 1; v <= n; v++)
  ans[1] += depth[v];
// pass 2: forward BFS order
for (int k = 1; k < n; k++) {
  int v = order[k];
  ans[v] = ans[parent[v]]
         - sz[v] + (n - sz[v]);
}
"""


class B11Scene(NarratedScene):
    lesson_tag = "BÀI 11"
    lesson_title = "Quy hoạch động trên cây"


TPOS = {1: (0, 2.2), 2: (-2.1, 0.6), 3: (2.1, 0.6), 4: (-3.1, -1.1), 5: (-1.1, -1.1), 6: (1.1, -1.1), 7: (3.1, -1.1)}


def person(v, h=None, r=0.42, color=BLUEC):
    c = Circle(radius=r, fill_color=PANEL_2, fill_opacity=1, stroke_color=color, stroke_width=4)
    t = TB(str(v), size=30).move_to(c)
    g = VGroup(c, t)
    if h is not None:
        tag = TB(f"♥{h}", size=24, color=ACCENT).next_to(c, UR, buff=-0.08)
        g.add(tag)
    return g


def company(pos=TPOS, joy=JOY, boss=BOSS, r=0.42):
    nodes = {v: person(v, joy.get(v) if joy else None, r=r).move_to([x, y, 0]) for v, (x, y) in pos.items()}
    edges = {v: Line(nodes[p][0].get_bottom(), nodes[v][0].get_top(), color=MUTED, stroke_width=3)
             for v, p in boss.items()}
    g = VGroup(*edges.values(), *nodes.values())
    g.nodes, g.edges = nodes, edges
    return g


def invite(node, color=GOOD):
    return [node[0].animate.set_fill(color, 1).set_stroke(color), node[1].animate.set_color(BG)]


def pair_tag(a, b, size=24):
    t = VGroup(M(f"({a}, {b})", size=size, color=INK))
    p = panel(t, pad=0.08, radius=0.1, stroke=ACCENT)
    return p


# ----------------------------------------------------------------------------
class B11_00_Intro(B11Scene):
    def construct(self):
        tag = TB("BÀI 11", size=80, color=ACCENT)
        ttl = VGroup(TB("Quy hoạch động", size=50), TB("TRÊN CÂY", size=56, color=GOOD)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Bài toán con = CÂY CON",
            "✓ Trạng thái “được chọn hay không”",
            "✓ Duyệt KHÔNG đệ quy: BFS ngược",
            "✓ Đổi gốc: đáp án cho MỌI gốc, O(n)",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 11: Quy hoạch động trên cây."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ dùng cây con làm bài toán con: kết quả tại một đỉnh được ghép từ kết quả tại "
                        "các con của nó. Em sẽ thêm trạng thái được chọn hay không để xử lí ràng buộc giữa cha và con."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em sẽ duyệt cây không đệ quy theo thứ tự BFS ngược, tránh tràn ngăn xếp khi cây sâu hai trăm nghìn "
                        "tầng; và học kĩ thuật đổi gốc, tính đáp án cho mọi đỉnh làm gốc chỉ trong O của n."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B11_01_KhoiDong(B11Scene):
    def construct(self):
        self.show_header("Khởi động: Dạ tiệc cuối năm")
        story = VGroup(T("Mỗi nhân viên có một “độ vui” ♥ khi dự tiệc.", size=28),
                       T("Luật ngầm: KHÔNG ai muốn dự cùng", size=28),
                       T("SẾP TRỰC TIẾP của mình!", size=30, color=BAD)).arrange(DOWN, buff=0.1)
        tree = company()
        role = VGroup(T("giám đốc ở gốc, mỗi người có đúng một sếp", size=24, color=MUTED))
        ask = TB("Mời những ai để tổng ♥ lớn nhất?", size=34, color=ACCENT)
        fit_stack(story, tree, role, ask, buff=0.6, max_scale=1.2)
        with self.voice("Công ty tổ chức dạ tiệc cuối năm. Mỗi nhân viên có một độ vui khi tham gia. Nhưng có một luật ngầm: "
                        "không ai muốn dự tiệc cùng sếp trực tiếp của mình, vì sẽ mất vui."):
            self.play(FadeIn(story), run_time=1.0)
        with self.voice("Sơ đồ công ty là một cây: giám đốc, người số 1, ở gốc; mỗi người khác có đúng một sếp trực tiếp. "
                        "Con số màu vàng là độ vui."):
            self.play(LaggedStart(*[Create(e) for e in tree.edges.values()], lag_ratio=0.1),
                      LaggedStart(*[FadeIn(n, scale=0.6) for n in tree.nodes.values()], lag_ratio=0.1), run_time=1.6)
            self.play(FadeIn(role), run_time=0.4)
        with self.voice("Mời những ai để tổng độ vui lớn nhất?"):
            self.play(FadeIn(ask), run_time=0.6)

        # tham lam
        greedy = T("Tham lam: mời người vui nhất (3, ♥9) trước…", size=28, color=ORANGE)
        greedy.move_to(ask)
        n = tree.nodes
        with self.voice("Thử cách tham lam: mời ngay người vui nhất, người số 3 với độ vui 9. Khi đó sếp 1 và hai nhân viên 6, "
                        "7 đều không được mời."):
            self.play(FadeOut(ask), FadeIn(greedy), run_time=0.5)
            self.play(*invite(n[3], ORANGE), run_time=0.6)
            self.play(*[n[v][0].animate.set_stroke(BAD, 4).set_fill(BG, 1) for v in (1, 6, 7)],
                      *[n[v][1].animate.set_color(MUTED) for v in (1, 6, 7)], run_time=0.6)
        res1 = TB("9 + 4 + 2 = 15", size=34, color=ORANGE).move_to(greedy)
        with self.voice("Tốt nhất phần còn lại là mời 4 và 5. Tổng chỉ được 15."):
            self.play(*invite(n[4], ORANGE), *invite(n[5], ORANGE), run_time=0.6)
            self.play(Transform(greedy, res1), run_time=0.5)
        self.play(*[n[v][0].animate.set_fill(PANEL_2, 1).set_stroke(BLUEC, 4) for v in JOY],
                  *[n[v][1].animate.set_color(INK) for v in JOY], run_time=0.5)
        res2 = TB("5 + 4 + 2 + 1 + 7 = 19  ✓", size=34, color=GOOD).move_to(greedy)
        with self.voice("Cách tốt nhất lại không mời người 3: mời giám đốc 1, cùng 4, 5, 6 và 7. Tổng 5 cộng 4 cộng 2 cộng 1 "
                        "cộng 7 bằng 19."):
            self.play(*[a for v in (1, 4, 5, 6, 7) for a in invite(n[v])], run_time=0.8)
            self.play(Transform(greedy, res2), run_time=0.5)

        self.clear_body()
        self.show_header("1. Bài toán DATIEC")
        task = tag_box("BÀI TOÁN: DATIEC", [
            "n người (n ≤ 2·10⁵), người 1 là giám đốc;",
            "người v ≥ 2 có sếp trực tiếp p_v < v, độ vui h_v.",
            "Chọn tập người để mời: KHÔNG có cặp (sếp trực",
            "tiếp, nhân viên) nào cùng được mời; tổng ♥ max.",
        ], width=7.5, size=27)
        ex = VGroup(M("7", size=28, color=BLUEC), M("5 3 9 4 2 1 7", size=28, color=BLUEC), M("1 1 2 2 3 3", size=28, color=BLUEC)
                    ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        exr = VGroup(T("→", size=34), TB("19", size=44, color=GOOD)).arrange(RIGHT, buff=0.3)
        exg = VGroup(ex, exr).arrange(RIGHT, buff=0.6)
        link = VGroup(T("Giống bài HÁI NẤM (Bài 2): không chọn hai phần tử", size=27),
                      T("kề nhau — nhưng “kề” giờ là quan hệ CHA–CON", size=27, color=ACCENT),
                      T("trên CÂY thay vì trên dãy.", size=27)).arrange(DOWN, buff=0.08)
        fit_stack(task, exg, link, buff=0.7, max_scale=1.2)
        with self.voice("Bài toán DATIEC: công ty có n người, tới hai trăm nghìn. Người 1 là giám đốc, mỗi người v khác có sếp "
                        "trực tiếp p v nhỏ hơn v, và độ vui h v. Chọn một tập người để mời, không có cặp sếp trực tiếp và nhân "
                        "viên nào cùng được mời, sao cho tổng độ vui lớn nhất."):
            self.play(FadeIn(task), run_time=1.0)
        with self.voice("Ví dụ: bảy người, dòng hai là độ vui, dòng ba là sếp của người 2 đến 7. Đáp án 19."):
            self.play(FadeIn(exg), run_time=0.8)
        with self.voice("Bài này giống bài hái nấm ở Bài 2: không chọn hai phần tử kề nhau. Nhưng kề nhau giờ là quan hệ cha "
                        "con trên cây, thay vì trên dãy."):
            self.play(FadeIn(link), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B11_02_NgayTho(B11Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: Thử mọi tập người")
        flow = VGroup()
        for txt, col in [("Duyệt mọi tập con S (2ⁿ tập)", BLUEC), ("Kiểm tra n − 1 cặp sếp – nhân viên", ORANGE),
                         ("Hợp lệ? Cập nhật tổng lớn nhất", GOOD)]:
            flow.add(panel(T(txt, size=28), stroke=col, width=7.0))
        flow.arrange(DOWN, buff=0.45)
        arrows = VGroup(*[Arrow(flow[k].get_bottom(), flow[k + 1].get_top(), buff=0.05, color=MUTED, stroke_width=4)
                          for k in range(2)])
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "2ⁿ tập con × (n − 1) cặp: O(2ⁿ · n)",
            "Chỉ chạy được với n ≤ 20  (n = 2·10⁵: không tưởng)",
        ], accent=BLUEC, width=7.5, size=27)
        fit_stack(VGroup(flow, arrows), cnt, buff=0.8, max_scale=1.2)
        with self.voice("Cách ngây thơ: thử mọi tập người được mời. Có 2 mũ n tập con; với mỗi tập, kiểm tra n trừ 1 cặp sếp và "
                        "nhân viên; nếu hợp lệ thì cập nhật tổng lớn nhất."):
            self.play(LaggedStart(FadeIn(flow[0]), GrowArrow(arrows[0]), FadeIn(flow[1]), GrowArrow(arrows[1]), FadeIn(flow[2]),
                                  lag_ratio=0.4), run_time=2.0)
        with self.voice("Độ phức tạp O của 2 mũ n nhân n: chỉ chạy được với n không quá 20."):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Bế tắc: Bỏ qua cấu trúc độc lập")
        tree = company()
        n = tree.nodes
        left = SurroundingRectangle(VGroup(n[2], n[4], n[5]), color=BLUEC, buff=0.2, corner_radius=0.2)
        right = SurroundingRectangle(VGroup(n[3], n[6], n[7]), color=PURPLE, buff=0.2, corner_radius=0.2)
        ll = T("nhóm của 2", size=24, color=BLUEC).next_to(left, DOWN, buff=0.12)
        rl = T("nhóm của 3", size=24, color=PURPLE).next_to(right, DOWN, buff=0.12)
        cases = VGroup(
            VGroup(TB("1 KHÔNG được mời:", size=28, color=GOOD), T("hai nhánh hoàn toàn tự do", size=28)).arrange(RIGHT, buff=0.2),
            VGroup(TB("1 được mời:", size=28, color=ORANGE), T("chỉ cấm đúng người 2 và 3", size=28)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        key = VGroup(T("Hai nhánh “gặp nhau” chỉ ở người 1 ⇒", size=28),
                     TB("tách thành các bài toán CÂY CON!", size=32, color=ACCENT)).arrange(DOWN, buff=0.1)
        fit_stack(VGroup(tree, left, right, ll, rl), cases, key, buff=0.7, max_scale=1.2)
        self.play(FadeIn(tree), run_time=0.6)
        with self.voice("Bế tắc nằm ở đâu? Quyết định ở nhánh trái, mời ai trong nhóm của người 2, và ở nhánh phải, nhóm của "
                        "người 3, gần như độc lập với nhau."):
            self.play(Create(left), Create(right), FadeIn(ll), FadeIn(rl), run_time=1.0)
        with self.voice("Chúng chỉ gặp nhau ở người 1. Nếu người 1 không được mời, hai nhánh hoàn toàn tự do. Nếu người 1 được "
                        "mời, chỉ có người 2 và 3 bị cấm."):
            self.play(FadeIn(cases[0]), run_time=0.6)
            self.play(FadeIn(cases[1]), Indicate(VGroup(n[2], n[3]), color=ORANGE), run_time=0.8)
        with self.voice("Duyệt mọi tập con là bỏ qua cấu trúc độc lập ấy. Ta sẽ tách thành các bài toán trên cây con."):
            self.play(FadeIn(key), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B11_03_HaiTrangThai(B11Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Hai trạng thái tại mỗi đỉnh")
        sub = VGroup(T("Bước 1: CÂY CON GỐC v = v và mọi cấp dưới của v.", size=27),
                     T("Đáp án của nó chỉ cần đáp án các cây con của con,", size=27),
                     T("cộng MỘT thông tin: v có được mời hay không.", size=27, color=ACCENT)).arrange(DOWN, buff=0.1)
        box = tag_box("CÔNG THỨC (THÊM CHIỀU “MỜI HAY KHÔNG”)", [
            "• moi(v): ♥ max cây con gốc v, v ĐƯỢC mời",
            "• khong(v): ♥ max cây con gốc v, v KHÔNG mời",
            "moi(v)   = h_v + Σ khong(c)",
            "khong(v) = Σ max(moi(c), khong(c))",
            "Cơ sở: lá có (h_v, 0)",
            "Đáp án: max(moi(1), khong(1))",
        ], width=7.5, size=27)
        box[3][2].set_color(GOOD)
        box[3][3].set_color(BLUEC)
        same = VGroup(T("= kĩ thuật THÊM CHIỀU ở Bài 2:", size=27, color=MUTED),
                      T("“phần tử trước được chọn?” → “đỉnh cha được chọn?”", size=26, color=MUTED)).arrange(DOWN, buff=0.08)
        fit_stack(sub, box, same, buff=0.7, max_scale=1.2)
        with self.voice("Bước một: cây con là bài toán con. Với mỗi người v, xét cây con gốc v, gồm v và mọi cấp dưới của v. "
                        "Đáp án cho cây con này chỉ phụ thuộc vào đáp án cho các cây con của các nhân viên trực tiếp, cộng thêm "
                        "một thông tin: v có được mời hay không, vì điều đó quyết định các con của v có được mời không."):
            self.play(FadeIn(sub), run_time=1.0)
        with self.voice("Vậy ta lưu hai giá trị. moi của v là tổng vui lớn nhất trong cây con gốc v khi v được mời; khong của v "
                        "là khi v không được mời."):
            self.play(FadeIn(box[0:3]), FadeIn(box[3][0:2]), run_time=1.0)
        with self.voice("Nếu v được mời, mọi con c phải vắng mặt: moi của v bằng h v cộng tổng khong của các con."):
            self.play(FadeIn(box[3][2]), run_time=0.6)
        with self.voice("Nếu v không được mời, mỗi con được tự do chọn cách tốt hơn: khong của v bằng tổng max của moi c và "
                        "khong c."):
            self.play(FadeIn(box[3][3]), run_time=0.6)
        with self.voice("Cơ sở: lá có moi bằng độ vui, khong bằng 0. Đáp án là max của moi 1 và khong 1. Đây đúng là kĩ thuật "
                        "thêm chiều trạng thái ở Bài 2."):
            self.play(FadeIn(box[3][4:]), FadeIn(same), run_time=0.8)

        self.clear_body()
        self.show_header("Bước 2: Chạy tay từ lá lên gốc")
        tree = company()
        n = tree.nodes
        tags_slot = {v: placeholder(1.5, 0.5).next_to(n[v][0], DOWN, buff=0.12) for v in JOY}
        tags_slot[1].next_to(n[1][0], LEFT, buff=0.15)
        tags_slot[2].next_to(n[2][0], RIGHT, buff=0.12)
        tags_slot[3].next_to(n[3][0], LEFT, buff=0.12)
        legend = VGroup(M("(moi, khong)", size=28, color=ACCENT), T("tại mỗi người", size=26, color=MUTED)).arrange(RIGHT, buff=0.2)
        calc_slot = placeholder(7.4, 1.6)
        ans_slot = placeholder(7.0, 0.8)
        sc = fit_stack(legend, VGroup(tree, *tags_slot.values()), calc_slot, ans_slot, buff=0.5, max_scale=1.15)
        self.play(FadeIn(tree), FadeIn(legend), run_time=0.6)

        def ptag(v):
            return pair_tag(MOI[v], KHONG[v], size=24).scale(sc).move_to(tags_slot[v])

        def calc(lines, col=INK):
            g = VGroup(*[M(l, size=24, color=col) for l in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            g.scale_to_fit_width(min(g.width * sc, 7.4)).move_to(calc_slot)
            return g

        with self.voice("Bắt đầu từ bốn lá: người 4, 5, 6, 7. Mỗi lá có moi bằng độ vui, khong bằng 0: bốn cặp 4 0, 2 0, 1 0 "
                        "và 7 0."):
            self.play(*[n[v][0].animate.set_stroke(GOOD, 5) for v in (4, 5, 6, 7)], run_time=0.4)
            self.play(LaggedStart(*[FadeIn(ptag(v), shift=UP * 0.1) for v in (4, 5, 6, 7)], lag_ratio=0.2), run_time=1.0)
        cur = calc(["moi(2)   = 3 + 0 + 0 = 3",
                    "khong(2) = max(4,0) + max(2,0) = 6"])
        with self.voice("Người 2, độ vui 3: moi bằng 3 cộng khong của 4 và 5, đều bằng 0, được 3. khong bằng max của 4 và 0, "
                        "cộng max của 2 và 0, được 6."):
            self.play(n[2][0].animate.set_stroke(ACCENT, 5), FadeIn(cur), run_time=0.6)
            t2 = ptag(2)
            self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.5)
        new = calc(["moi(3)   = 9 + 0 + 0 = 9",
                    "khong(3) = max(1,0) + max(7,0) = 8"])
        with self.voice("Người 3, độ vui 9: moi bằng 9, khong bằng 1 cộng 7 bằng 8."):
            self.play(n[3][0].animate.set_stroke(ACCENT, 5), Transform(cur, new), run_time=0.6)
            self.play(FadeIn(ptag(3), shift=UP * 0.1), run_time=0.5)
        new = calc(["moi(1)   = 5 + khong(2) + khong(3)",
                    "moi(1)   = 5 + 6 + 8 = 19",
                    "khong(1) = max(3,6) + max(9,8) = 15"])
        with self.voice("Người 1, độ vui 5: moi bằng 5 cộng khong của 2 cộng khong của 3, bằng 5 cộng 6 cộng 8, bằng 19. "
                        "khong bằng max của 3 và 6, cộng max của 9 và 8, bằng 15."):
            self.play(n[1][0].animate.set_stroke(ACCENT, 5), Transform(cur, new), run_time=0.6)
            self.play(FadeIn(ptag(1), shift=UP * 0.1), run_time=0.5)
        ans = TB("Đáp án max(19, 15) = 19", size=36, color=GOOD).scale(sc).move_to(ans_slot)
        with self.voice("Đáp án là max của 19 và 15, bằng 19. Truy ngược lại: 1 được mời, nên 2 và 3 vắng; khi 2 vắng, 4 và 5 "
                        "chọn được mời; khi 3 vắng, 6 và 7 chọn được mời."):
            self.play(FadeIn(ans), run_time=0.6)
            self.play(*[a for v in (1, 4, 5, 6, 7) for a in invite(n[v])], run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
class B11_04_KhongDeQuy(B11Scene):
    def construct(self):
        self.show_header("Bước 3: Duyệt cây KHÔNG đệ quy")
        chain = VGroup(*[person(v, r=0.3) for v in ("1", "2", "3", "⋮", "n")]).arrange(DOWN, buff=0.35)
        chain[3][0].set_opacity(0)
        chain_edges = VGroup(*[Line(chain[k][0].get_bottom(), chain[k + 1][0].get_top(), color=MUTED, stroke_width=3)
                               for k in range(4)])
        warn = VGroup(T("Cây “đường thẳng” 2·10⁵ đỉnh:", size=28),
                      T("đệ quy sâu 2·10⁵ tầng", size=28),
                      TB("⇒ nguy cơ TRÀN NGĂN XẾP!", size=30, color=BAD)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        top = VGroup(VGroup(chain, chain_edges), warn).arrange(RIGHT, buff=0.8)
        steps = VGroup(T("1. Liệt kê đỉnh theo thứ tự BFS từ gốc", size=28),
                       T("    (cha luôn đứng trước con)", size=26, color=MUTED),
                       T("2. Duyệt danh sách TỪ CUỐI LÊN ĐẦU:", size=28),
                       T("    mọi con đã xử lí xong trước cha", size=26, color=GOOD)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        order = array_row(ORDER, w=0.85, h=0.85, size=34, show_index=False, label="order")
        back = placeholder(6.0, 0.7)
        sc = fit_stack(top, steps, VGroup(order, back).arrange(DOWN, buff=0.15), buff=0.6, max_scale=1.2)
        with self.voice("Cách viết tự nhiên là một hàm DFS đệ quy. Nhưng cây có thể là một đường thẳng dài hai trăm nghìn đỉnh, "
                        "mỗi người chỉ có một nhân viên. Đệ quy sẽ sâu hai trăm nghìn tầng, có nguy cơ tràn ngăn xếp."):
            self.play(FadeIn(chain), Create(chain_edges), run_time=0.8)
            self.play(FadeIn(warn), run_time=0.6)
        with self.voice("Cách an toàn: liệt kê các đỉnh theo thứ tự BFS từ gốc, cha luôn đứng trước con. Với cây của ta: 1, rồi "
                        "2, 3, rồi 4, 5, 6, 7."):
            self.play(FadeIn(steps[0:2]), run_time=0.6)
            self.play(FadeIn(order), run_time=0.8)
        arr = Arrow(order.cells[-1].get_bottom() + DOWN * 0.15, order.cells[0].get_bottom() + DOWN * 0.15, buff=0,
                    color=GOOD, stroke_width=6).move_to(back)
        with self.voice("Rồi duyệt danh sách từ cuối lên đầu: 7, 6, 5, 4, rồi 3, 2, và cuối cùng là 1. Khi xử lí một đỉnh, mọi "
                        "con của nó đã được xử lí xong."):
            self.play(FadeIn(steps[2:]), GrowArrow(arr), run_time=0.8)
            for k in range(6, -1, -1):
                self.play(order.cells[k][0].animate.set_fill(GOOD, 1), order.cells[k][1].animate.set_color(BG), run_time=0.25)

        self.clear_body()
        self.show_header("DATIEC.CPP: Quy hoạch động trên cây, O(n)")
        code = code_block(DATIEC_CODE, size=21)
        note = VGroup(T("order vừa là HÀNG ĐỢI BFS (chỉ số k chạy dần),", size=27),
                      T("vừa là thứ tự kết quả. Mỗi đỉnh, mỗi cạnh xét 1 lần:", size=27),
                      TB("O(n) thời gian và bộ nhớ", size=30, color=GOOD)).arrange(DOWN, buff=0.1)
        fit_stack(code, note, buff=0.7, max_scale=1.2)
        with self.voice("Code: danh sách order bắt đầu bằng đỉnh 1. Duyệt nó bằng chỉ số k chạy dần, thêm các con vào cuối: "
                        "order vừa là hàng đợi BFS, vừa là thứ tự kết quả."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 0, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 3, ACCENT)), run_time=0.4)
        with self.voice("Rồi duyệt k từ n trừ 1 về 0. invited là moi, absent là khong; cộng dồn từ mọi con."):
            self.play(Transform(hl, line_box(code, 4, GOOD)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 9, GOOD)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 10, BLUEC)), run_time=0.4)
        with self.voice("Mỗi đỉnh xuất hiện một lần, mỗi cạnh được xét một lần: O của n thời gian và bộ nhớ."):
            self.play(FadeOut(hl), FadeIn(note), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao đúng?")
        why = tag_box("VÌ SAO ĐÚNG?", [
            "• v được mời ⇒ mọi con c vắng mặt; các cây con",
            "   khác nhau KHÔNG có cặp sếp – nhân viên chung",
            "   ⇒ tối ưu độc lập: h_v + Σ khong(c)",
            "• v không được mời ⇒ mỗi con tự do:",
            "   max(moi(c), khong(c)), cây con lại độc lập",
            "⇒ không bỏ sót, không vi phạm ràng buộc",
        ], accent=PURPLE, width=7.5, size=28)
        why[3][5].set_color(GOOD)
        fit_stack(why, max_scale=1.25)
        with self.voice("Vì sao công thức đúng? Nếu v được mời thì mọi con c đều không được mời, và các cây con của các con khác "
                        "nhau không có cặp sếp và nhân viên nào chung, nên có thể tối ưu độc lập."):
            self.play(FadeIn(why[0:3]), FadeIn(why[3][0:3]), run_time=1.0)
        with self.voice("Nếu v không được mời, mỗi con c được tự do, tốt nhất là max của moi c và khong c, và các cây con lại "
                        "độc lập. Vì vậy công thức không bỏ sót và không vi phạm ràng buộc."):
            self.play(FadeIn(why[3][3:]), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
DTPOS = {1: (0, 2.0), 2: (-1.9, 0.3), 3: (1.9, 0.3), 4: (-3.0, -1.4), 5: (-0.8, -1.4), 6: (1.9, -1.4)}


class B11_05_DoiGoc(B11Scene):
    def construct(self):
        self.show_header("4. Đổi gốc: Bài toán KHOANGCACH")
        task = tag_box("BÀI TOÁN: KHOANGCACH", [
            "Cây n đỉnh (n ≤ 2·10⁵), các cạnh dài 1. Với MỖI đỉnh v,",
            "tính tổng khoảng cách từ v tới mọi đỉnh khác.",
        ], width=7.5, size=27)
        tree = company(DTPOS, joy=None, boss=DPAR)
        ans = VGroup(T("Kết quả:", size=30), M("8 8 10 12 12 14", size=32, color=GOOD)).arrange(RIGHT, buff=0.25)
        naive = VGroup(T("Làm lại quy hoạch động cho từng gốc: O(n²)", size=28, color=BAD),
                       TB("Đổi gốc: chỉ HAI lần duyệt, O(n)", size=32, color=GOOD)).arrange(DOWN, buff=0.12)
        fit_stack(task, tree, ans, naive, buff=0.6, max_scale=1.2)
        with self.voice("Có những bài hỏi đáp án cho mọi đỉnh khi coi đỉnh đó là gốc. Bài KHOANGCACH: cho cây n đỉnh, mỗi cạnh "
                        "dài 1. Với mỗi đỉnh v, tính tổng khoảng cách từ v tới mọi đỉnh khác."):
            self.play(FadeIn(task), run_time=0.8)
            self.play(FadeIn(tree), run_time=0.8)
        with self.voice("Ví dụ cây sáu đỉnh này cho kết quả 8, 8, 10, 12, 12, 14. Chẳng hạn từ đỉnh 1: 1 cộng 1 cộng 2 cộng 2 "
                        "cộng 2 bằng 8."):
            self.play(FadeIn(ans), run_time=0.6)
        with self.voice("Làm lại quy hoạch động cho từng gốc tốn O của n bình phương. Kĩ thuật đổi gốc chỉ cần hai lần duyệt."):
            self.play(FadeIn(naive), run_time=0.8)

        self.clear_body()
        self.show_header("Lần duyệt 1: độ sâu và kích thước cây con")
        tree = company(DTPOS, joy=None, boss=DPAR)
        n = tree.nodes
        side = {1: RIGHT, 2: LEFT, 3: RIGHT, 4: DOWN, 5: DOWN, 6: DOWN}
        info_slot = {v: placeholder(0.8, 0.7).next_to(n[v][0], side[v], buff=0.12) for v in DTPOS}
        f1 = VGroup(T("BFS từ gốc 1: depth(v), size(v)", size=28),
                    M("kq(1) = Σ depth = 0+1+1+2+2+2 = 8", size=26, color=ACCENT)).arrange(DOWN, buff=0.12)
        sc = fit_stack(VGroup(tree, *info_slot.values()), f1, buff=0.7, max_scale=1.2)
        self.play(FadeIn(tree), run_time=0.5)
        with self.voice("Lần duyệt thứ nhất, từ gốc 1: BFS để tính độ sâu mọi đỉnh, rồi duyệt ngược để tính kích thước cây con "
                        "size của mỗi đỉnh: lá có size 1, đỉnh 3 có size 2, đỉnh 2 có size 3, gốc có size 6."):
            tags = {}
            for v in reversed(DORDER):
                t = VGroup(M(f"d={DEPTH[v]}", size=20, color=BLUEC), M(f"s={SIZE[v]}", size=20, color=GOOD)
                           ).arrange(DOWN, aligned_edge=LEFT, buff=0.05).scale(sc).move_to(info_slot[v])
                tags[v] = t
                self.play(FadeIn(t, shift=UP * 0.1), run_time=0.3)
        with self.voice("Khi đó kq của 1 bằng tổng các độ sâu, bằng 8."):
            self.play(FadeIn(f1), run_time=0.6)

        self.clear_body(keep=[tree, *tags.values()])
        self.show_header("Lần duyệt 2: chuyển gốc từ v sang con c")
        rule = VGroup(VGroup(TB("size(c)", size=28, color=GOOD), T("đỉnh trong cây con c: GẦN THÊM 1", size=28)).arrange(RIGHT, buff=0.2),
                      VGroup(TB("n − size(c)", size=28, color=BAD), T("đỉnh còn lại: XA THÊM 1", size=28)).arrange(RIGHT, buff=0.2)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        form = panel(M("kq(c) = kq(v) − size(c) + (n − size(c))", size=27, color=ACCENT), stroke=ACCENT)
        calc_slot = placeholder(7.4, 0.7)
        res = VGroup(*[M(str(ANS[v]), size=30) for v in range(1, 7)])
        g = VGroup(tree, *tags.values())
        target = VGroup(g.copy(), rule.copy(), form.copy(), calc_slot.copy())
        sc2 = fit_stack(*target, buff=0.7, max_scale=1.0)
        self.play(g.animate.become(target[0]), run_time=0.6)
        rule.match_width(target[1]).move_to(target[1])
        form.match_width(target[2]).move_to(target[2])
        calc_slot.move_to(target[3])
        n = {v: g[0].nodes[v] for v in DTPOS}
        kq_tags = {}
        with self.voice("Lần duyệt thứ hai đi từ gốc xuống. Giả sử đã biết kq của v, tính kq của c là con của v. Khi đi từ v "
                        "sang c, size c đỉnh nằm trong cây con của c gần thêm 1; n trừ size c đỉnh còn lại xa thêm 1."):
            self.play(FadeIn(rule), run_time=0.8)
        with self.voice("Công thức đổi gốc: kq của c bằng kq của v, trừ size c, cộng n trừ size c."):
            self.play(FadeIn(form), run_time=0.6)

        def kq_tag(v):
            t = TB(f"kq={ANS[v]}", size=24, color=ACCENT).scale(sc * sc2)
            if v in (4, 5, 6):
                t.next_to(tags[v], DOWN, buff=0.06)
            else:
                t.next_to(n[v][0], UL if v == 2 else LEFT, buff=0.08)
            return t

        kq_tags[1] = kq_tag(1)
        self.play(FadeIn(kq_tags[1]), run_time=0.4)
        steps = [
            (2, [2, 4, 5], "kq(2) = 8 − 3 + 3 = 8",
             "Từ 1 sang 2: ba đỉnh 2, 4, 5 gần thêm 1, ba đỉnh còn lại xa thêm 1. kq của 2 bằng 8 trừ 3 cộng 3, bằng 8."),
            (3, [3, 6], "kq(3) = 8 − 2 + 4 = 10",
             "Từ 1 sang 3: hai đỉnh gần thêm, bốn đỉnh xa thêm. kq của 3 bằng 8 trừ 2 cộng 4, bằng 10."),
            (4, [4], "kq(4) = 8 − 1 + 5 = 12", "Từ 2 sang 4: kq của 4 bằng 8 trừ 1 cộng 5, bằng 12. Tương tự kq của 5 cũng bằng 12."),
            (6, [6], "kq(6) = 10 − 1 + 5 = 14", "Từ 3 sang 6: kq của 6 bằng 10 trừ 1 cộng 5, bằng 14."),
        ]
        cur = None
        for c, inside, txt, sp in steps:
            outside = [v for v in DTPOS if v not in inside]
            line = M(txt, size=28, color=INK).scale(sc2).move_to(calc_slot)
            with self.voice(sp):
                self.play(*[n[v][0].animate.set_fill(GOOD, 0.8) for v in inside],
                          *[n[v][0].animate.set_fill(BAD, 0.6) for v in outside], run_time=0.5)
                if cur is None:
                    cur = line
                    self.play(FadeIn(cur), run_time=0.4)
                else:
                    self.play(Transform(cur, line), run_time=0.4)
                kq_tags[c] = kq_tag(c)
                extra = []
                if c == 4:
                    kq_tags[5] = kq_tag(5)
                    extra = [FadeIn(kq_tags[5])]
                self.play(FadeIn(kq_tags[c]), *extra, run_time=0.4)
                self.wait(0.3)
                self.play(*[n[v][0].animate.set_fill(PANEL_2, 1) for v in DTPOS], run_time=0.3)

        self.clear_body()
        self.show_header("KHOANGCACH.CPP: Đổi gốc, O(n)")
        code = code_block(REROOT_CODE, size=21)
        note = VGroup(T("Lần 1 (size): BFS NGƯỢC — con trước cha", size=28, color=BLUEC),
                      T("Lần 2 (kq): BFS XUÔI — cha trước con", size=28, color=GOOD),
                      T("Tổng khoảng cách tới ≈ n²/2 ≈ 2·10¹⁰ ⇒ long long", size=27, color=ORANGE)).arrange(DOWN, buff=0.12)
        fit_stack(code, note, buff=0.7, max_scale=1.2)
        with self.voice("Code: lần một duyệt BFS từ gốc 1 để có cha, độ sâu và thứ tự; rồi duyệt ngược để cộng dồn size lên cha. "
                        "kq của 1 bằng tổng độ sâu."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 3, BLUEC)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 6, BLUEC)), run_time=0.4)
        with self.voice("Lần hai đi theo thứ tự BFS xuôi, cha trước con, ngược với lần tính size. Mỗi đỉnh một công thức O của 1."):
            self.play(Transform(hl, line_box(code, 10, GOOD)), run_time=0.4)
            self.play(FadeIn(note[0:2]), run_time=0.6)
        with self.voice("Tổng khoảng cách có thể tới cỡ n bình phương chia 2, khoảng hai mươi tỉ, nên phải dùng long long."):
            self.play(FadeOut(hl), FadeIn(note[2]), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B11_06_TongKet(B11Scene):
    def construct(self):
        self.show_header("5. Mở rộng")
        ext = [
            ("Cái túi trên cây: O(n²)", "k đỉnh liên thông chứa gốc; ghép con như túi",
             "Mở rộng một: cái túi trên cây. Chọn đúng k đỉnh liên thông chứa gốc với tổng trọng số lớn nhất. f của v, j là tổng "
             "lớn nhất khi chọn j đỉnh trong cây con gốc v. Ghép các con lần lượt như cái túi theo nhóm; nếu giới hạn j theo "
             "kích thước cây con đã ghép, tổng chỉ là O của n bình phương, không phải n lập phương."),
            ("Ba trạng thái: đặt camera", "có camera · được con canh · chờ cha canh",
             "Mở rộng hai: bài đặt camera. Mỗi đỉnh phải có camera hoặc kề một đỉnh có camera. Mỗi đỉnh có ba trạng thái: có "
             "camera; không có nhưng được một con canh; hoặc chưa được canh, phải nhờ cha."),
            ("Đường kính cây", "down(v); ghép HAI nhánh xuống dài nhất qua v",
             "Mở rộng ba: đường kính cây. Đường dài nhất đi qua một đỉnh cao nhất v rồi xuống hai nhánh khác nhau. Lưu down của "
             "v là đường xuống dài nhất, rồi ghép hai nhánh dài nhất tại mỗi đỉnh."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Đệ quy sâu", "cây đường thẳng: tràn ngăn xếp ⇒ BFS ngược",
             "Bẫy một: đệ quy sâu với cây dạng đường thẳng gây tràn ngăn xếp. Dùng thứ tự BFS ngược."),
            ("Cạnh vô hướng", "tìm cha bằng BFS, tránh đi ngược lên cha",
             "Bẫy hai: cây cho dưới dạng danh sách cạnh vô hướng. Phải tìm cha bằng BFS, và tránh đi ngược lên cha."),
            ("Gốc không phải đỉnh 1", "đọc kĩ đề",
             "Bẫy ba: gốc không phải đỉnh 1. Đọc kĩ đề."),
            ("Quên trường hợp n = 1", "không có cạnh nào",
             "Bẫy bốn: quên trường hợp n bằng 1, không có cạnh nào."),
            ("Tràn số", "cộng dồn trên cây lớn: dùng long long",
             "Bẫy năm: tràn số khi cộng dồn trên cây lớn."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 11", [
            "• Bài toán con = cây con; ghép kết quả",
            "   các con tại cha",
            "• Ràng buộc cha – con: thêm chiều trạng thái",
            "   (chọn hay không, hoặc nhiều hơn)",
            "• Thứ tự an toàn: BFS từ gốc, xử lí ngược",
            "• Đổi gốc: tính cho gốc 1, rồi chuyển gốc",
            "   sang con bằng công thức O(1) mỗi cạnh",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: bài toán con là cây con, ghép kết quả các con tại cha. Ràng buộc cha con thì thêm chiều trạng "
                        "thái: chọn hay không, hoặc nhiều hơn."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Thứ tự an toàn: BFS từ gốc, xử lí ngược. Đổi gốc: tính cho gốc 1, rồi chuyển gốc sang con bằng công "
                        "thức O của 1 mỗi cạnh."):
            self.play(FadeIn(mem[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Ví dụ DATIEC, nếu người 1 có", "độ vui 1 thì đáp án là bao nhiêu?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        work = VGroup(M("moi(1)   = 1 + 6 + 8 = 15", size=30, color=GOOD),
                      M("khong(1) = 6 + 9     = 15", size=30, color=BLUEC)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        ans = TB("Đáp số: 15 (hai cách bằng nhau)", size=38, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: BÀI 12", size=42, color=ACCENT),
                     T("Đếm, đồ thị có hướng, xác suất và kì vọng", size=30)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, work, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: với ví dụ DATIEC, nếu người 1 chỉ có độ vui 1 thì đáp án là bao nhiêu? Dừng video "
                        "và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Các cặp ở người 2 và 3 không đổi. moi của 1 bằng 1 cộng 6 cộng 8 bằng 15; khong của 1 bằng 6 cộng 9 "
                        "cũng bằng 15. Đáp số 15, hai cách bằng nhau."):
            self.play(FadeIn(work), run_time=0.8)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Bài tiếp theo: đếm, đồ thị có hướng, xác suất và kì vọng. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
