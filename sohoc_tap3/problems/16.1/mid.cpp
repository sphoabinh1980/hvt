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
    for (ll i = 1; i <= n; i++)            // i là ước của floor(n/i) số
        ans = (ans + i % MOD * ((n / i) % MOD)) % MOD;
    printf("%lld\n", ans);
    return 0;
}
