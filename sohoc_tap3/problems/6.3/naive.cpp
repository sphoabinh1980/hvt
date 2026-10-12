#include <cstdio>

int main() {
    if (fopen("BAUOC.INP", "r")) {
        freopen("BAUOC.INP", "r", stdin);
        freopen("BAUOC.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    while (n--) {
        long long a;
        scanf("%lld", &a);
        int cnt = 0;
        for (long long p = 2; p * p <= a; p++)      // thử chia tới √a
            if (a % p == 0) {
                int e = 0;
                while (a % p == 0) { a /= p; e++; }
                if (e >= 2) cnt++;                // p² | a: p² là số ba ước
            }
        printf("%d\n", cnt);                       // phần còn lại > 1: mũ 1
    }
    return 0;
}
