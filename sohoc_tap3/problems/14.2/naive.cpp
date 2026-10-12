#include <cstdio>
typedef long long ll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }

int main() {
    if (fopen("NTCN.INP", "r")) {
        freopen("NTCN.INP", "r", stdin);
        freopen("NTCN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n, N, cnt = 0;
        scanf("%lld %lld", &n, &N);
        for (ll x = 1; x <= N; x++)
            if (gcd(x, n) == 1) cnt++;
        printf("%lld\n", cnt);
    }
    return 0;
}
