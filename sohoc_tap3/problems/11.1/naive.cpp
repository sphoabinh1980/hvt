#include <cstdio>
typedef long long ll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }

int main() {
    if (fopen("PHI.INP", "r")) {
        freopen("PHI.INP", "r", stdin);
        freopen("PHI.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n, cnt = 0;
        scanf("%lld", &n);
        for (ll k = 1; k <= n; k++)
            if (gcd(k, n) == 1) cnt++;      // kim đi qua đủ n vạch
        printf("%lld\n", cnt);
    }
    return 0;
}
