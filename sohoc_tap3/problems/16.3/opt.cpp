#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef __int128 lll;
const ll MOD = 1000000007;

ll S1(ll r) { return (ll)((lll)r * (r + 1) / 2 % MOD); }          // 1+...+r
ll S2(ll r) { return (ll)((lll)r * (r + 1) * (2 * r + 1) / 6 % MOD); } // 1^2+...+r^2

int main() {
    if (fopen("HAITHUONG.INP", "r")) {
        freopen("HAITHUONG.INP", "r", stdin);
        freopen("HAITHUONG.OUT", "w", stdout);
    }
    ll n, m;
    scanf("%lld %lld", &n, &m);
    ll L = min(n, m), S = 0;
    ll nm = n % MOD * (m % MOD) % MOD;
    for (ll i = 1, j; i <= L; i = j + 1) {
        ll a = n / i, b = m / i;
        j = min(n / a, m / b);              // khối chung: a, b không đổi
        // (n - a i)(m - b i) = nm - (n b + m a) i + a b i^2
        ll cnt = (j - i + 1) % MOD;
        ll si = (S1(j) - S1(i - 1) + MOD) % MOD;
        ll sq = (S2(j) - S2(i - 1) + MOD) % MOD;
        ll am = a % MOD, bm = b % MOD;
        ll lin = (n % MOD * bm + m % MOD * am) % MOD;
        ll term = (nm * cnt % MOD - lin * si % MOD + MOD) % MOD;
        term = (term + am * bm % MOD * sq) % MOD;
        S = (S + term) % MOD;
    }
    printf("%lld\n", S);
    return 0;
}
