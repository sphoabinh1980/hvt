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
    if (fopen("TONGLT.INP", "r")) {
        freopen("TONGLT.INP", "r", stdin);
        freopen("TONGLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, n, m;
        scanf("%lld %lld %lld", &a, &n, &m);
        // S = (a^(n+1) - 1) / (a - 1): chia bằng nghịch đảo Fermat
        // chỉ đúng khi m nguyên tố và (a - 1) không chia hết cho m
        ll t = (power(a, n + 1, m) - 1 + m) % m;
        ll inv = power((a % m - 1 + m) % m, m - 2, m);
        printf("%lld\n", t * inv % m);
    }
    return 0;
}
