#include <cstdio>
typedef long long ll;
typedef __int128 LL;

int main() {
    if (fopen("TONGLT.INP", "r")) {
        freopen("TONGLT.INP", "r", stdin);
        freopen("TONGLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, n, m;
        scanf("%lld %lld %lld", &a, &n, &m);
        ll s = 0, p = 1 % m, x = a % m;          // p = a^i mod m
        for (ll i = 0; i <= n; i++) {           // n + 1 số hạng
            s = (s + p) % m;
            p = (LL)p * x % m;
        }
        printf("%lld\n", s);
    }
    return 0;
}
