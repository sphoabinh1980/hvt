#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

ll cr(ll ax, ll ay, ll bx, ll by, ll px, ll py) {   // tích chéo AB x AP
    return (bx - ax) * (py - ay) - (by - ay) * (px - ax);
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
        ll cnt = 0;
        for (ll x = min({x1, x2, x3}); x <= max({x1, x2, x3}); x++)
            for (ll y = min({y1, y2, y3}); y <= max({y1, y2, y3}); y++) {
                ll a = cr(x1, y1, x2, y2, x, y);
                ll b = cr(x2, y2, x3, y3, x, y);
                ll c = cr(x3, y3, x1, y1, x, y);
                // nằm hẳn bên trong: ba tích chéo cùng dấu, khác 0
                if ((a > 0 && b > 0 && c > 0) || (a < 0 && b < 0 && c < 0))
                    cnt++;
            }
        printf("%lld\n", cnt);
    }
    return 0;
}
