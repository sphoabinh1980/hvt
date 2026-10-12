#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

ll power(ll a, ll b) {                  // a^b mod MOD, O(log b)
    a %= MOD;                           // a tới 10^18: lấy dư trước!
    ll r = 1;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;   // bit 1: nhân lũy thừa hiện tại vào r
        a = a * a % MOD;                // a^1, a^2, a^4, a^8, ...
        b >>= 1;
    }
    return r;
}

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
        printf("%lld\n", power(a, b));
    }
    return 0;
}
