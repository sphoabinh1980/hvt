#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

ll T(ll n) {                         // số cách lát hành lang 2 x n
    if (n <= 1) return 1;            // T(0) = T(1) = 1
    return (T(n - 1) + T(n - 2)) % MOD;
}

int main() {
    if (fopen("LATGACH.INP", "r")) {
        freopen("LATGACH.INP", "r", stdin);
        freopen("LATGACH.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n;
        scanf("%lld", &n);
        printf("%lld\n", T(n));
    }
    return 0;
}
