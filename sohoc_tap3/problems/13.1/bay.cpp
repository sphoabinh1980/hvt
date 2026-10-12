#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;
const int N = 1000000;                      // "n <= 10^6 thì bảng tới 10^6"
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

int main() {
    if (fopen("CHIAKEO.INP", "r")) {
        freopen("CHIAKEO.INP", "r", stdin);
        freopen("CHIAKEO.OUT", "w", stdout);
    }
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    ifact[N] = power(fact[N], MOD - 2);     // một lần lũy thừa
    for (int i = N; i > 0; i--) ifact[i - 1] = ifact[i] * i % MOD;
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n, k, t;
        scanf("%lld %lld %lld", &n, &k, &t);
        if (k * t > n) { printf("0\n"); continue; }     // k·t tới 10^12
        ll m = n - k * t;                   // còn lại sau khi phát trước
        printf("%lld\n", C(m + k - 1, k - 1));
    }
    return 0;
}
