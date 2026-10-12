#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("NTCN.INP", "r")) {
        freopen("NTCN.INP", "r", stdin);
        freopen("NTCN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n, N;
        scanf("%lld %lld", &n, &N);
        vector<ll> ps;                      // ước nguyên tố phân biệt của n
        for (ll p = 2; p * p <= n; p++) {   // thử mọi d, kể cả hợp số
            if (n % p == 0) {
                ps.push_back(p);
                while (n % p == 0) n /= p;
            }
        }
        if (n > 1) ps.push_back(n);         // ước nguyên tố lớn còn lại
        int k = ps.size();                  // k <= 11 với n <= 10^12
        ll ans = 0;
        for (int mask = 0; mask < (1 << k); mask++) {
            ll prod = 1; int bits = 0;
            for (int j = 0; j < k; j++)
                if (mask >> j & 1) { prod *= ps[j]; bits++; }   // prod <= n
            ans += (bits % 2 ? -1 : 1) * (N / prod);
        }
        printf("%lld\n", ans);
    }
    return 0;
}
