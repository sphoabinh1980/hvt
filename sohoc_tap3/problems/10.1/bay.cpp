#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

ll power(ll a, ll b) {
    a %= MOD; ll r = 1;
    while (b) { if (b & 1) r = r * a % MOD; a = a * a % MOD; b >>= 1; }
    return r;
}

int main() {
    if (fopen("XACSUAT.INP", "r")) {
        freopen("XACSUAT.INP", "r", stdin);
        freopen("XACSUAT.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    ll X = 1, Y = 1, Z = 1;                 // các tích, lấy dư sau mỗi bước
    for (int i = 0; i < n; i++) {
        ll x, y;
        scanf("%lld %lld", &x, &y);
        X = X * x % MOD;
        Y = Y * y % MOD;
        Z = Z * (x + y) % MOD;              // x + y <= 10^9 < MOD: khác 0
    }
    ll inv = power(Z, MOD - 2);             // nghịch đảo duy nhất cần dùng
    ll P1 = X * inv % MOD;
    ll P2 = (1 - Y * inv % MOD) % MOD;      // có thể âm!
    printf("%lld\n%lld\n", P1, P2);
    return 0;
}
