#include <cstdio>
typedef long long ll;
typedef __int128 LL;

ll extgcd(ll a, ll b, ll& x, ll& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - (a / b) * y1;
    return g;
}
ll md(ll x, ll m) { x %= m; return x < 0 ? x + m : x; }

int main() {
    if (fopen("DIEMBINH.INP", "r")) {
        freopen("DIEMBINH.INP", "r", stdin);
        freopen("DIEMBINH.OUT", "w", stdout);
    }
    int k; ll L;
    scanf("%d %lld", &k, &L);
    ll r = 0, M = 1;                            // x ≡ r (mod M), 0 <= r < M
    for (int i = 0; i < k; i++) {
        ll m, a, u, v;
        scanf("%lld %lld", &m, &a);
        // x = r + M·t, cần M·t ≡ a − r (mod m); gcd(M, m) = 1
        extgcd(M % m, m, u, v);                 // u = M^(-1) mod m
        ll t = (ll)((LL)md(a - r, m) * md(u, m) % m);
        r = r + M * t;                          // < M·m <= 10^18
        M = M * m;
    }
    ll x = L + md(r - L, M);                  // số đầu tiên >= L, < 2·10^18
    printf("%lld\n", x);
    return 0;
}
