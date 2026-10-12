#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;
const int N = 2000000;                      // m + n <= 2·10^6
ll fact[N + 1], ifact[N + 1];

ll power(ll a, ll b) {
    ll r = 1; a %= MOD;
    while (b) { if (b & 1) r = r * a % MOD; a = a * a % MOD; b >>= 1; }
    return r;
}
ll C(ll a, ll b) {
    if (b < 0 || b > a) return 0;
    return fact[a] * ifact[b] % MOD * ifact[a - b] % MOD;
}
ll paths(ll x1, ll y1, ll x2, ll y2) {    // số đường từ (x1,y1) tới (x2,y2)
    if (x2 < x1 || y2 < y1) return 0;       // không tới được
    return C((x2 - x1) + (y2 - y1), x2 - x1);
}

int main() {
    if (fopen("DUONGLUOI.INP", "r")) {
        freopen("DUONGLUOI.INP", "r", stdin);
        freopen("DUONGLUOI.OUT", "w", stdout);
    }
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    ifact[N] = power(fact[N], MOD - 2);
    for (int i = N; i > 0; i--) ifact[i - 1] = ifact[i] * i % MOD;
    ll m, n; int K;
    scanf("%lld %lld %d", &m, &n, &K);
    ll x[2], y[2];
    for (int i = 0; i < K; i++) scanf("%lld %lld", &x[i], &y[i]);
    ll ans = paths(0, 0, m, n);
    for (int i = 0; i < K; i++)             // trừ các đường qua từng ô cấm
        ans -= paths(0, 0, x[i], y[i]) * paths(x[i], y[i], m, n) % MOD;
    if (K == 2) {                           // cộng lại đường qua cả hai ô
        ans += paths(0, 0, x[0], y[0]) * paths(x[0], y[0], x[1], y[1]) % MOD
               * paths(x[1], y[1], m, n) % MOD;    // chỉ xét ô 0 đi trước
    }
    printf("%lld\n", ((ans % MOD) + MOD) % MOD);
    return 0;
}
