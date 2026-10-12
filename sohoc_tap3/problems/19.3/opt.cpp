#include <cstdio>
typedef long long ll;

int a[405][405], b[405], pre[405];
int cnt[1000005];                         // cnt[d]: số tiền tố có số dư d

int main() {
    if (fopen("HCNCHIAHET.INP", "r")) {
        freopen("HCNCHIAHET.INP", "r", stdin);
        freopen("HCNCHIAHET.OUT", "w", stdout);
    }
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            ll x;
            scanf("%lld", &x);
            a[i][j] = (int)((x % k + k) % k); // số dư không âm ngay khi đọc
        }
    ll ans = 0;
    for (int i1 = 1; i1 <= m; i1++) {
        for (int j = 1; j <= n; j++) b[j] = 0;
        for (int i2 = i1; i2 <= m; i2++) {
            for (int j = 1; j <= n; j++) {  // b[j]: tổng cột j, hàng i1..i2
                b[j] += a[i2][j];
                if (b[j] >= k) b[j] -= k;
            }
            // đếm đoạn con của b có tổng chia hết cho k
            pre[0] = 0; cnt[0] = 1;
            for (int j = 1; j <= n; j++) {
                pre[j] = pre[j - 1] + b[j];
                if (pre[j] >= k) pre[j] -= k;
                ans += cnt[pre[j]];
                cnt[pre[j]]++;
            }
            for (int j = 0; j <= n; j++) cnt[pre[j]] = 0; // chỉ xóa ô đã dùng
        }
    }
    printf("%lld\n", ans);
    return 0;
}
