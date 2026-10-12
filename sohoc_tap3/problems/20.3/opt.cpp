#include <cstdio>
typedef long long ll;
typedef __int128 lll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }
ll ab(ll x) { return x < 0 ? -x : x; }

void print(lll x) {                       // x >= 0
    char buf[45]; int len = 0;
    do { buf[len++] = '0' + (int)(x % 10); x /= 10; } while (x > 0);
    while (len > 0) putchar(buf[--len]);
    putchar('\n');
}

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
        ll ux = x2 - x1, uy = y2 - y1;  // hiệu tới 2 * 10^18: vừa long long
        ll vx = x3 - x1, vy = y3 - y1;
        lll S2 = (lll)ux * vy - (lll)vx * uy;   // ép kiểu TRƯỚC khi nhân
        if (S2 < 0) S2 = -S2;             // 2S tới 8 * 10^36 < 1,7 * 10^38
        lll B = (lll)gcd(ab(ux), ab(uy)) + gcd(ab(vx), ab(vy))
              + gcd(ab(x3 - x2), ab(y3 - y2));        // B tới 6 * 10^18
        print((S2 - B + 2) / 2);          // định lí Pick
    }
    return 0;
}
