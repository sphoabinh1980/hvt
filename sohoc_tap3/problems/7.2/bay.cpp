#include <cstdio>
typedef long long ll;

ll legendre(ll n, ll p) {                   // số mũ của p trong n!
    ll s = 0;
    while (n > 0) { n /= p; s += n; }       // ⌊n/p⌋ + ⌊n/p²⌋ + ...
    return s;
}

int main() {
    if (fopen("CHUSO0.INP", "r")) {
        freopen("CHUSO0.INP", "r", stdin);
        freopen("CHUSO0.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll n, b;
        scanf("%lld %lld", &n, &b);
        ll ans = 0, P = 0, K = 0;          // chỉ nhớ ước nguyên tố lớn nhất
        for (ll p = 2; p * p <= b; p++)
            if (b % p == 0) {
                int k = 0;
                while (b % p == 0) { b /= p; k++; }
                P = p; K = k;
            }
        if (b > 1) { P = b; K = 1; }
        ans = legendre(n, P) / K;         // SAI: số khác có thể "thiếu" hơn
        printf("%lld\n", ans);
    }
    return 0;
}
