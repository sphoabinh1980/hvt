#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("LUYTHUAQ.INP", "r")) {
        freopen("LUYTHUAQ.INP", "r", stdin);
        freopen("LUYTHUAQ.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a, b;
        scanf("%lld %lld", &a, &b);
        ll r = 1 % MOD, x = a % MOD;
        for (ll i = 0; i < b; i++) r = r * x % MOD;     // b lần nhân
        printf("%lld\n", r);
    }
    return 0;
}
