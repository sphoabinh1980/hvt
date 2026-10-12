#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

ll power(ll a, ll b) {
    ll r = 1; a %= MOD;
    for (; b > 0; b >>= 1, a = a * a % MOD)
        if (b & 1) r = r * a % MOD;
    return r;
}

int main() {
    if (fopen("TANGQUA.INP", "r")) {
        freopen("TANGQUA.INP", "r", stdin);
        freopen("TANGQUA.OUT", "w", stdout);
    }
    ll n, m;
    scanf("%lld %lld", &n, &m);
    ll k = n - m;                       // số người không may mắn, k <= 10^7
    // C(n, k) = n (n-1) ... (n-k+1) / k!
    ll num = 1, kf = 1;
    for (ll i = 0; i < k; i++) {
        num = num * ((n - i) % MOD) % MOD;  // lấy dư thừa số trước khi nhân
        kf = kf * ((i + 1) % MOD) % MOD;
    }
    ll C = num * power(kf, MOD - 2) % MOD;  // k < MOD nên k! khả nghịch
    // D(i) = (i - 1) (D(i-1) + D(i-2)),  D(0) = 1, D(1) = 0
    ll d0 = 1, d1 = 0;                   // D(0), D(1)
    for (ll i = 2; i <= k; i++) {
        ll d2 = (i - 1) % MOD * ((d0 + d1) % MOD) % MOD;
        d0 = d1; d1 = d2;
    }
    ll Dk = (k == 0 ? d0 : d1);
    printf("%lld\n", C * Dk % MOD);
    return 0;
}
