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
        long long cnt = 0, r = 1;                // cnt = số ước của n
        for (long long d = 1; d * d <= n; d++)
            if (n % d == 0) {
                cnt += (d * d == n) ? 1 : 2; // cặp (d, n/d); √n chỉ 1 lần
                r = d;                           // ước lớn nhất <= √n
            }
        if (cnt - 2 <= 0) printf("0\n");         // n = 1 hoặc n nguyên tố
        else printf("%lld %lld %lld\n", cnt - 2, r, n / r);
    }
    return 0;
}
