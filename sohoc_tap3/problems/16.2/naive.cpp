#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("TONGDU.INP", "r")) {
        freopen("TONGDU.INP", "r", stdin);
        freopen("TONGDU.OUT", "w", stdout);
    }
    ll n, k, S = 0;
    scanf("%lld %lld", &n, &k);
    for (ll i = 1; i <= k; i++) S = (S + n % i) % MOD;
    printf("%lld\n", S);
    return 0;
}
