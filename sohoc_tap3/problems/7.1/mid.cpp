#include <cstdio>

int main() {
    if (fopen("SOUOC.INP", "r")) {
        freopen("SOUOC.INP", "r", stdin);
        freopen("SOUOC.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long n;
        scanf("%lld", &n);
        long long d = 0, s = 0;
        for (long long k = 1; k * k <= n; k++)
            if (n % k == 0) {
                d++; s += k;
                if (k * k != n) { d++; s += n / k; }    // ước cặp n / k
            }
        printf("%lld %lld\n", d, s);
    }
    return 0;
}
