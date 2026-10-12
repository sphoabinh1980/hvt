#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef __int128 lll;
const ll MOD = 1000000007;

int main() {
    if (fopen("TONGDU.INP", "r")) {
        freopen("TONGDU.INP", "r", stdin);
        freopen("TONGDU.OUT", "w", stdout);
    }
    ll n, k;
    scanf("%lld %lld", &n, &k);
    // S = n * k - sum_{i <= min(n,k)} i * floor(n / i)   (i > n góp 0)
    ll S = n % MOD * (k % MOD) % MOD;
    ll lim = k;                             // BẪY: khối chạy tới k
    for (ll i = 1, j; i <= lim; i = j + 1) {
        ll q = n / i;
        j = min(n / q, lim);                // i > n: q = 0, chia cho 0
        ll s = (ll)((lll)(i + j) * (j - i + 1) / 2 % MOD);
        S = (S - q % MOD * s % MOD + MOD) % MOD;
    }
    printf("%lld\n", S);
    return 0;
}
