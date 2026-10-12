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
    if (fopen("HAIDEN.INP", "r")) {
        freopen("HAIDEN.INP", "r", stdin);
        freopen("HAIDEN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a1, p1, a2, p2, u, v;
        scanf("%lld %lld %lld %lld", &a1, &p1, &a2, &p2);
        ll r1 = a1 % p1, r2 = a2 % p2;
        ll g = extgcd(p1, p2, u, v);            // p1·u + p2·v = g
        if ((r2 - r1) % g != 0) { printf("-1\n"); continue; }
        ll m2 = p2 / g;
        // r1 + p1·t ≡ r2 (mod p2)  <=>  (p1/g)·t ≡ (r2 − r1)/g (mod m2)
        ll t = (ll)((LL)md((r2 - r1) / g, m2) * md(u, m2) % m2);
        ll L = p1 / g * p2;                     // lcm <= 10^18
        ll r = r1 + p1 * t;                     // 0 <= r < L
        ll A = a1 > a2 ? a1 : a2;               // cả hai đèn đã bật
        printf("%lld\n", A + md(r - A, L));     // < 2·10^18
    }
    return 0;
}
