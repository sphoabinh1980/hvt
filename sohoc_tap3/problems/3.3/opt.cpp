#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll LIM = 1000000000000000000LL, INF = LIM + 1;    // INF: "vượt 10^18"

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }
ll lcm(ll a, ll b) {                    // BCNN, chặn trên bởi INF
    if (a == INF || b == INF) return INF;
    ll x = a / gcd(a, b);
    if (x > LIM / b) return INF;
    return x * b;
}

int main() {
    if (fopen("DENNHAY.INP", "r")) {
        freopen("DENNHAY.INP", "r", stdin);
        freopen("DENNHAY.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<ll> t(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &t[i]);
    vector<vector<pair<int, int>>> byR(n + 1);  // (l, số thứ tự) theo r
    for (int j = 0; j < q; j++) {
        int l, r;
        scanf("%d %d", &l, &r);
        byR[r].push_back({l, j});
    }
    vector<ll> ans(q);
    // seg: các cặp (giá trị, lo), lo giảm dần: với lo <= l < lo của cặp
    // đứng trước, lcm(t[l..r]) = giá trị. Tối đa khoảng 62 cặp.
    vector<pair<ll, int>> seg, nseg;
    for (int r = 1; r <= n; r++) {
        nseg.clear();
        nseg.push_back({t[r], r});
        for (auto& s : seg) {
            ll v = lcm(s.first, t[r]);         // cùng giá trị thì gộp
            if (v == nseg.back().first) nseg.back().second = s.second;
            else nseg.push_back({v, s.second});     // giá trị mới
        }
        swap(seg, nseg);
        for (auto& qq : byR[r]) {
            int l = qq.first;
            size_t k = 0;
            while (seg[k].second > l) k++;      // cặp đầu tiên có lo <= l
            ans[qq.second] = seg[k].first == INF ? -1 : seg[k].first;
        }
    }
    for (int j = 0; j < q; j++) printf("%lld\n", ans[j]);
    return 0;
}
