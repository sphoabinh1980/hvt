#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
typedef __int128 LL;
const ll MOD = 1000000007;
const int MX = 1000000;
int spf[MX + 1], best[MX + 1];              // best[p]: số mũ lớn nhất của p

ll extgcd(ll a, ll b, ll& x, ll& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - (a / b) * y1;
    return g;
}
ll md(ll x, ll m) { x %= m; return x < 0 ? x + m : x; }

int main() {
    if (fopen("CANCHI.INP", "r")) {
        freopen("CANCHI.INP", "r", stdin);
        freopen("CANCHI.OUT", "w", stdout);
    }
    for (int p = 2; p <= MX; p++)
        if (!spf[p])
            for (int j = p; j <= MX; j += p) if (!spf[j]) spf[j] = p;
    int k, Q;
    scanf("%d %d", &k, &Q);
    vector<ll> m(k);
    for (auto& x : m) {
        scanf("%lld", &x);
        for (int v = x; v > 1; ) {          // phân tích m_i bằng spf
            int p = spf[v], e = 0;
            while (v % p == 0) { v /= p; e++; }
            if (e > best[p]) best[p] = e;
        }
    }
    ll Lc = 1;                              // lcm thật, rồi mới lấy dư
    for (ll x : m) { ll u, v, g = extgcd(Lc, x, u, v); Lc = Lc / g * x; }
    ll names = Lc % MOD;                    // tràn khi lcm > 9,2·10^18
    printf("%lld\n", names);
    while (Q--) {
        vector<ll> c(k);
        ll L, R;
        for (auto& x : c) scanf("%lld", &x);
        scanf("%lld %lld", &L, &R);
        LL r = 0, M = 1;                    // x ≡ r (mod M)
        bool ok = true;
        for (int i = 0; i < k && ok; i++) {
            ll u, v, Mi = (ll)M;            // M <= R <= 10^18
            ll g = extgcd(Mi % m[i], m[i], u, v);
            ll diff = md(c[i] - (ll)(r % m[i]), m[i]);
            if (diff % g != 0) { ok = false; break; }
            ll mg = m[i] / g;
            ll t = (ll)((LL)(diff / g) * md(u, mg) % mg);
            r += M * t;                     // < lcm mới, tới 10^24
            M = M / g * m[i];
        }
        if (!ok) { printf("0\n"); continue; }
        ll Mm = (ll)M, rr = (ll)r;
        ll first = L + md(rr - L, Mm);
        if (first > R) printf("0\n");
        else printf("%lld %lld\n", (R - first) / Mm + 1, first);
    }
    return 0;
}
