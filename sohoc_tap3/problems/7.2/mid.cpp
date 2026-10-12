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
        if (n <= 20) {                      // subtask 1: tính thẳng n!
            unsigned long long f = 1;
            for (ll i = 2; i <= n; i++) f *= i;
            int c = 0;
            while (f % b == 0) { f /= b; c++; }
            printf("%d\n", c);
            continue;
        }
        printf("%lld\n", legendre(n, 5));  // b = 10: đếm thừa số 5
    }
    return 0;
}
