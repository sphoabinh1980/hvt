#include <cstdio>

int main() {
    if (fopen("XEPHANG.INP", "r")) {
        freopen("XEPHANG.INP", "r", stdin);
        freopen("XEPHANG.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        long long n;
        scanf("%lld", &n);
        long long k = 0, r = 0;
        for (long long d = 1; d <= n; d++)
            if (n % d == 0) {
                if (d >= 2 && d <= n / 2) k++;   // d hàng, mỗi hàng n/d bạn
                if (d * d <= n) r = d;       // ước lớn nhất không vượt √n
            }
        if (k == 0) printf("0\n");
        else printf("%lld %lld %lld\n", k, r, n / r);
    }
    return 0;
}
