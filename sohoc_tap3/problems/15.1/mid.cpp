#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("LATGACH.INP", "r")) {
        freopen("LATGACH.INP", "r", stdin);
        freopen("LATGACH.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    vector<ll> ns(q);
    for (ll &n : ns) scanf("%lld", &n);
    ll mx = *max_element(ns.begin(), ns.end());
    vector<ll> T(mx + 1);            // n = 10^18 thì không cấp phát nổi
    T[0] = 1; T[1] = 1;
    for (ll i = 2; i <= mx; i++) T[i] = (T[i - 1] + T[i - 2]) % MOD;
    for (ll n : ns) printf("%lld\n", T[n]);
    return 0;
}
