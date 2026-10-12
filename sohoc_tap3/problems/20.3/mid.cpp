#include <cstdio>
#include <cstdlib>
typedef long long ll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }

int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin);
        freopen("TAMGIAC.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll x1, y1, x2, y2, x3, y3;
        scanf("%lld %lld %lld %lld", &x1, &y1, &x2, &y2);
        scanf("%lld %lld", &x3, &y3);
        ll ux = x2 - x1, uy = y2 - y1, vx = x3 - x1, vy = y3 - y1;
        ll S2 = llabs(ux * vy - vx * uy);  // tràn khi tọa độ > ~10^9
        ll B = gcd(llabs(ux), llabs(uy)) + gcd(llabs(vx), llabs(vy))
             + gcd(llabs(x3 - x2), llabs(y3 - y2));
        printf("%lld\n", (S2 - B + 2) / 2);
    }
    return 0;
}
