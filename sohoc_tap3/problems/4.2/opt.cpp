#include <cstdio>
typedef long long ll;

ll extgcd(ll a, ll b, ll& x, ll& y) {   // a*x + b*y = gcd(a, b)
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    if (fopen("MUAHANG.INP", "r")) {
        freopen("MUAHANG.INP", "r", stdin);
        freopen("MUAHANG.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a, b, c, u, v;
        scanf("%lld %lld %lld", &a, &b, &c);
        ll g = extgcd(a, b, u, v);      // a*u + b*v = g
        if (c % g != 0) { puts("0"); continue; }
        ll A = a / g, B = b / g, C = c / g;
        // A*x ≡ C (mod B)  =>  x ≡ C * u (mod B), vì A*u ≡ 1 (mod B)
        ll x = (ll)((__int128)(C % B) * (((u % B) + B) % B) % B);
        if (A * x > C) { puts("0"); continue; }   // A*x < A*B <= 10^18
        printf("%lld\n", (C - A * x) / (A * B) + 1);
    }
    return 0;
}
