#include <cstdio>
typedef long long ll;
typedef __int128 lll;
const ll MOD = 1000000007;

int main() {
    if (fopen("TONGSIGMA.INP", "r")) {
        freopen("TONGSIGMA.INP", "r", stdin);
        freopen("TONGSIGMA.OUT", "w", stdout);
    }
    ll n, ans = 0;
    scanf("%lld", &n);
    for (ll i = 1, j; i <= n; i = j + 1) {
        ll q = n / i;
        j = n / q;                          // khối [i, j] cùng thương q
        // i + (i+1) + ... + j, tính đúng bằng __int128 rồi mới lấy dư
        ll s = (ll)((lll)(i + j) * (j - i + 1) / 2 % MOD);
        ans = (ans + q % MOD * s) % MOD;
    }
    printf("%lld\n", ans);
    return 0;
}
