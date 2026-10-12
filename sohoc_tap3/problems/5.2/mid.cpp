#include <cstdio>

bool isPrime(long long x) {
    if (x < 2) return false;
    if (x < 4) return true;
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (long long i = 5; i * i <= x; i += 6)
        if (x % i == 0 || x % (i + 2) == 0) return false;
    return true;
}

int main() {
    if (fopen("GOLDBACH.INP", "r")) {
        freopen("GOLDBACH.INP", "r", stdin);
        freopen("GOLDBACH.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long n, ans = -1;
        scanf("%lld", &n);
        // n lẻ và n - 2 hợp số: vòng lặp chạy tới tận n/2!
        for (long long p = 2; p <= n / 2; p++)
            if (isPrime(p) && isPrime(n - p)) { ans = p; break; }
        if (ans < 0) printf("-1\n");
        else printf("%lld %lld\n", ans, n - ans);
    }
    return 0;
}
