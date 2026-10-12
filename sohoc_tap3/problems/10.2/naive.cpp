#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("NGHICHDAO.INP", "r")) {
        freopen("NGHICHDAO.INP", "r", stdin);
        freopen("NGHICHDAO.OUT", "w", stdout);
    }
    ll n, p;
    scanf("%lld %lld", &n, &p);
    ll H = 0, X = 0;
    for (ll i = 1; i <= n; i++) {
        ll x = 1;
        while (i * x % p != 1) x++;    // thử x = 1, 2, ... (tới p − 1 bước)
        H = (H + x) % p;
        X ^= x;
    }
    printf("%lld\n%lld\n", H, X);
    return 0;
}
