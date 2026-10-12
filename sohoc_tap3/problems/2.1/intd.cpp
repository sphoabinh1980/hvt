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
        long long cnt = 0, r = 1;
        for (int d = 1; d * d <= n; d++)       // d * d tính bằng int: tràn!
            if (n % d == 0) {
                cnt += (d * d == n) ? 1 : 2;
                r = d;
            }
        if (cnt - 2 <= 0) printf("0\n");
        else printf("%lld %lld %lld\n", cnt - 2, r, n / r);
    }
    return 0;
}
