#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("TONGSIGMA.INP", "r")) {
        freopen("TONGSIGMA.INP", "r", stdin);
        freopen("TONGSIGMA.OUT", "w", stdout);
    }
    ll n, ans = 0;
    scanf("%lld", &n);
    for (ll x = 1; x <= n; x++) {
        ll s = 0;                          // s = sigma(x)
        for (ll d = 1; d * d <= x; d++)
            if (x % d == 0) {
                s += d;
                if (d != x / d) s += x / d;
            }
        ans = (ans + s) % MOD;
    }
    printf("%lld\n", ans);
    return 0;
}
