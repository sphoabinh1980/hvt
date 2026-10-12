#include <cstdio>
#include <cstdlib>
typedef long long ll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }

int main() {
    if (fopen("TRONGCAY.INP", "r")) {
        freopen("TRONGCAY.INP", "r", stdin);
        freopen("TRONGCAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    ll x0, y0;
    scanf("%lld %lld", &x0, &y0);
    ll ans = 1;                           // điểm P1
    for (int i = 1; i < n; i++) {
        ll x, y;
        scanf("%lld %lld", &x, &y);
        ll dx = llabs(x - x0), dy = llabs(y - y0);   // tới 2 * 10^9
        ans += dx + dy;                   // chỉ đúng khi dx = 0 hoặc dy = 0
        x0 = x; y0 = y;
    }
    printf("%lld\n", ans);
    return 0;
}
