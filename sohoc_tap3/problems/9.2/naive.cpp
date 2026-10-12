#include <cstdio>
typedef long long ll;

ll power(ll a, ll b, ll m) {
    a %= m;
    ll r = 1 % m;
    while (b > 0) {
        if (b & 1) r = r * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

int main() {
    if (fopen("SOMULON.INP", "r")) {
        freopen("SOMULON.INP", "r", stdin);
        freopen("SOMULON.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, b, m;
        scanf("%lld %lld %lld", &a, &b, &m);  // b dài 10^5 chữ số: đọc sai!
        printf("%lld\n", power(a, b, m));
    }
    return 0;
}
