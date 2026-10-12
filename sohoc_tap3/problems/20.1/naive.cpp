#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

bool mark[201][201];                 // điểm (x, y) lưu ở mark[x+100][y+100]

int main() {
    if (fopen("TRONGCAY.INP", "r")) {
        freopen("TRONGCAY.INP", "r", stdin);
        freopen("TRONGCAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    ll px[100005], py[100005];
    for (int i = 0; i < n; i++) scanf("%lld %lld", &px[i], &py[i]);
    for (int i = 0; i + 1 < n; i++) {
        ll x1 = px[i], y1 = py[i], x2 = px[i + 1], y2 = py[i + 1];
        for (ll x = min(x1, x2); x <= max(x1, x2); x++)
            for (ll y = min(y1, y2); y <= max(y1, y2); y++)
                // (x, y) thẳng hàng với hai đầu mút (tích chéo bằng 0)
                if ((x - x1) * (y2 - y1) == (y - y1) * (x2 - x1))
                    mark[x + 100][y + 100] = true;
    }
    int cnt = 0;
    for (int x = 0; x <= 200; x++)
        for (int y = 0; y <= 200; y++) cnt += mark[x][y];
    printf("%d\n", cnt);
    return 0;
}
