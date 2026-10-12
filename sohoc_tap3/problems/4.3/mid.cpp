#include <cstdio>
typedef long long ll;
typedef long long LL;                   // "tiết kiệm": không dùng __int128

ll extgcd(ll a, ll b, ll& x, ll& y) {   // a*x + b*y = gcd(a, b)
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    if (fopen("DONGHO.INP", "r")) {
        freopen("DONGHO.INP", "r", stdin);
        freopen("DONGHO.OUT", "w", stdout);
    }
    int Q;
    scanf("%d", &Q);
    while (Q--) {
        ll m, p, a, q, b, T, u, v;
        scanf("%lld %lld %lld %lld %lld %lld", &m, &p, &a, &q, &b, &T);
        ll d = ((a - b) % m + m) % m;   // d * t ≡ e (mod m)
        ll e = ((q - p) % m + m) % m;
        ll g = extgcd(d, m, u, v);      // d*u + m*v = g; d = 0 cho g = m
        if (e % g != 0) { puts("-1 0"); continue; }
        ll M = m / g;                   // các nghiệm cách nhau M
        ll uu = ((u % M) + M) % M;      // nghịch đảo của d/g theo mô-đun M
        ll t0 = (ll)((LL)(e / g % M) * uu % M);
        ll cnt = (t0 > T) ? 0 : (T - t0) / M + 1;
        printf("%lld %lld\n", t0, cnt);
    }
    return 0;
}
