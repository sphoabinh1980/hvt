#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll CAP = 2000000000LL;                // > mọi φ(m) với m <= 10^9

int k;
vector<ll> a, cap;                      // cap[i] = min(tháp a[i..k-1], CAP)

ll power(ll b, ll e, ll m) {                // b^e mod m
    b %= m; ll r = 1 % m;
    while (e) { if (e & 1) r = r * b % m; b = b * b % m; e >>= 1; }
    return r;
}
ll capPow(ll b, ll e) {                    // min(b^e, CAP), quy ước 0^0 = 1
    if (e == 0) return 1;
    if (b <= 1) return b;
    ll r = 1;
    for (ll i = 0; i < e; i++) {            // b >= 2: tối đa 31 vòng
        r *= b;
        if (r >= CAP) return CAP;
    }
    return r;
}
ll phi(ll n) {
    ll res = n;
    for (ll p = 2; p * p <= n; p++)
        if (n % p == 0) { res -= res / p; while (n % p == 0) n /= p; }
    if (n > 1) res -= res / n;
    return res;
}
ll solve(int i, ll m) {                     // tháp a[i..k-1] mod m
    if (m == 1) return 0;
    if (i == k - 1) return a[i] % m;
    ll E = cap[i + 1];                      // giá trị (chặn) của số mũ
    ll ph = phi(m);
    if (E < ph) return power(a[i], E, m);   // số mũ thật nhỏ: dùng thẳng
    return power(a[i], solve(i + 1, ph) + ph, m);   // Euler mở rộng
}

int main() {
    if (fopen("THAPLT.INP", "r")) {
        freopen("THAPLT.INP", "r", stdin);
        freopen("THAPLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll m;
        scanf("%d %lld", &k, &m);
        a.assign(k, 0); cap.assign(k, 0);
        for (auto& x : a) scanf("%lld", &x);
        cap[k - 1] = a[k - 1] < CAP ? a[k - 1] : CAP;
        for (int i = k - 2; i >= 0; i--) cap[i] = capPow(a[i], cap[i + 1]);
        printf("%lld\n", solve(0, m));
    }
    return 0;
}
