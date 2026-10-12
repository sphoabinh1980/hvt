#include <cstdio>
typedef long long ll;
typedef __int128 LL;
ll a, m;

ll mul(ll x, ll y) { return (LL)x * y % m; }   // m tới 10^18

// trả về S(k) = 1 + a + ... + a^(k-1) (k số hạng), gán p = a^k
ll S(ll k, ll& p) {
    if (k == 0) { p = 1 % m; return 0; }
    if (k & 1) {                        // S(k) = 1 + a · S(k - 1)
        ll q, s = S(k - 1, q);
        p = mul(q, a);
        return (1 + mul(a, s)) % m;
    }
    ll q, s = S(k / 2, q);              // S(2h) = S(h) · (1 + a^h)
    p = mul(q, q);
    return mul(s, (1 + q) % m);
}

int main() {
    if (fopen("TONGLT.INP", "r")) {
        freopen("TONGLT.INP", "r", stdin);
        freopen("TONGLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll n, p;
        scanf("%lld %lld %lld", &a, &n, &m);
        a %= m;
        printf("%lld\n", S(n + 1, p));  // n + 1 số hạng a^0..a^n
    }
    return 0;
}
