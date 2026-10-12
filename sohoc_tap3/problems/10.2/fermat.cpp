#include <cstdio>
typedef long long ll;

ll power(ll a, ll b, ll m) {
    ll r = 1; a %= m;
    while (b) { if (b & 1) r = r * a % m; a = a * a % m; b >>= 1; }
    return r;
}

int main() {
    if (fopen("NGHICHDAO.INP", "r")) {
        freopen("NGHICHDAO.INP", "r", stdin);
        freopen("NGHICHDAO.OUT", "w", stdout);
    }
    ll n, p;
    scanf("%lld %lld", &n, &p);
    ll H = 0, X = 0;
    for (ll i = 1; i <= n; i++) {
        ll x = power(i, p - 2, p);          // Fermat: khoảng 60 phép nhân
        H = (H + x) % p;
        X ^= x;
    }
    printf("%lld\n%lld\n", H, X);
    return 0;
}
