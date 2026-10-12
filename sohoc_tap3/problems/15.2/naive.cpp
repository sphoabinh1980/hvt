#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("TRIBO.INP", "r")) {
        freopen("TRIBO.INP", "r", stdin);
        freopen("TRIBO.OUT", "w", stdout);
    }
    ll n; int K;
    scanf("%lld %d", &n, &K);
    vector<char> bad(n + 1, 0);          // n = 10^18: không cấp phát nổi
    for (int i = 0; i < K; i++) { ll b; scanf("%lld", &b); bad[b] = 1; }
    vector<ll> f(n + 1, 0);
    f[0] = 1;
    for (ll x = 1; x <= n; x++) {
        if (bad[x]) continue;             // bậc hỏng: f[x] = 0
        for (int s = 1; s <= 3; s++)
            if (x - s >= 0) f[x] += f[x - s];
        f[x] %= MOD;
    }
    printf("%lld\n", f[n]);
    return 0;
}
