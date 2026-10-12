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
        ll ans = -1;                        // -1: chưa có giá trị
        for (ll p = 2; p * p <= b; p++)     // phân tích b bằng thử chia
            if (b % p == 0) {
                int k = 0;
                while (b % p == 0) { b /= p; k++; }
                ll t = legendre(n, p) / k;  // số lần b "lấy được" p^k
                if (ans < 0 || t < ans) ans = t;
            }
        if (b > 1) {                      // ước nguyên tố lớn còn lại, mũ 1
            ll t = legendre(n, b);
            if (ans < 0 || t < ans) ans = t;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
