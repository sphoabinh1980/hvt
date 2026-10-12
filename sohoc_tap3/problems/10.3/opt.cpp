#include <cstdio>
typedef long long ll;
typedef __int128 LL;

ll extgcd(ll a, ll b, ll& x, ll& y) {   // a*x + b*y = gcd(a, b)
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
ll md(ll x, ll m) { x %= m; return x < 0 ? x + m : x; }    // dư không âm

int main() {
    if (fopen("PTDONGDU.INP", "r")) {
        freopen("PTDONGDU.INP", "r", stdin);
        freopen("PTDONGDU.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a, c, m, L, R, u, v;
        scanf("%lld %lld %lld %lld %lld", &a, &c, &m, &L, &R);
        a = md(a, m); c = md(c, m);
        ll g = extgcd(a, m, u, v);      // a = 0 cho g = m
        if (c % g != 0) { printf("0\n"); continue; }
        ll M = m / g;                   // nghiệm: x ≡ x0 (mod M)
        ll x0 = (ll)((LL)(c / g % M) * md(u, M) % M);
        ll first = L + md(x0 - L, M);   // nghiệm nhỏ nhất >= L
        if (first > R) { printf("0\n"); continue; }
        printf("%lld %lld\n", (R - first) / M + 1, first);
    }
    return 0;
}
