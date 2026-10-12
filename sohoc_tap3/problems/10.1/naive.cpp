#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }
ll power(ll a, ll b) {
    a %= MOD; ll r = 1;
    while (b) { if (b & 1) r = r * a % MOD; a = a * a % MOD; b >>= 1; }
    return r;
}
ll frac(ll p, ll q) {                       // in phân số p/q theo mô-đun
    ll g = gcd(p, q);
    p /= g; q /= g;
    return p % MOD * power(q % MOD, MOD - 2) % MOD;
}

int main() {
    if (fopen("XACSUAT.INP", "r")) {
        freopen("XACSUAT.INP", "r", stdin);
        freopen("XACSUAT.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    ll X = 1, Y = 1, Z = 1;                 // tích x, tích y, tích (x + y)
    for (int i = 0; i < n; i++) {
        ll x, y;
        scanf("%lld %lld", &x, &y);
        X *= x; Y *= y; Z *= x + y;         // giá trị thật: tràn khi lớn
    }
    printf("%lld\n%lld\n", frac(X, Z), frac(Z - Y, Z));
    return 0;
}
