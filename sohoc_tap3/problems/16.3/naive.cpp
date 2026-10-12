#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("HAITHUONG.INP", "r")) {
        freopen("HAITHUONG.INP", "r", stdin);
        freopen("HAITHUONG.OUT", "w", stdout);
    }
    ll n, m, S = 0;
    scanf("%lld %lld", &n, &m);
    for (ll i = 1; i <= min(n, m); i++)
        S = (S + (n % i) % MOD * ((m % i) % MOD)) % MOD;
    printf("%lld\n", S);
    return 0;
}
