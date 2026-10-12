#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("KHOANGCACH.INP", "r")) {
        freopen("KHOANGCACH.INP", "r", stdin);
        freopen("KHOANGCACH.OUT", "w", stdout);
    }
    ll L, R;
    scanf("%lld %lld", &L, &R);
    const int S = 1000000;
    vector<char> comp(S + 1, 0);
    vector<int> pr;
    for (int i = 2; i <= S; i++)
        if (!comp[i]) {
            pr.push_back(i);
            for (ll j = (ll)i * i; j <= S; j += i) comp[j] = 1;
        }
    vector<char> mark(R - L + 1, 0);        // 10^7 ô char = 10 MB
    for (int p : pr) {
        if ((ll)p * p > R) break;
        ll st = (L + p - 1) / p * p;
        if (st < (ll)p * p) st = (ll)p * p;
        for (ll j = st; j <= R; j += p) mark[j - L] = 1;
    }
    if (L == 1) mark[0] = 1;
    ll prev = -1, bmax = -1, pmax = 0, bmin = -1, pmin = 0;
    for (ll x = L; x <= R; x++) {
        if (mark[x - L]) continue;
        if (prev > 0) {                     // cặp liên tiếp (prev, x)
            ll g = x - prev;
            // so sánh chặt (>, <) để khi hòa giữ cặp có p nhỏ nhất
            if (bmax < 0 || g > bmax) { bmax = g; pmax = prev; }
            if (bmin < 0 || g < bmin) { bmin = g; pmin = prev; }
        }
        prev = x;
    }
    if (bmax < 0) printf("-1\n");
    else {
        printf("%lld %lld\n", pmax, pmax + bmax);
        printf("%lld %lld\n", pmin, pmin + bmin);
    }
    return 0;
}
