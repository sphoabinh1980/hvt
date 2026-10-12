#include <cstdio>
typedef long long ll;

ll P[405][405];                   // P[i][j]: tổng hình chữ nhật (1,1)-(i,j)

int main() {
    if (fopen("HCNCHIAHET.INP", "r")) {
        freopen("HCNCHIAHET.INP", "r", stdin);
        freopen("HCNCHIAHET.OUT", "w", stdout);
    }
    int m, n; ll k;
    scanf("%d %d %lld", &m, &n, &k);
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            ll x;
            scanf("%lld", &x);
            P[i][j] = x + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1];
        }
    ll cnt = 0;
    for (int i1 = 1; i1 <= m; i1++)
        for (int i2 = i1; i2 <= m; i2++)
            for (int j1 = 1; j1 <= n; j1++)
                for (int j2 = j1; j2 <= n; j2++) {
                    ll s = P[i2][j2] - P[i1 - 1][j2] - P[i2][j1 - 1]
                         + P[i1 - 1][j1 - 1];
                    if (s % k == 0) cnt++;
                }
    printf("%lld\n", cnt);
    return 0;
}
