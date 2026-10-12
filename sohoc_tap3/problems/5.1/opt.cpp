#include <cstdio>

bool isPrime(long long x) {
    if (x < 2) return false;
    if (x < 4) return true;                 // 2 và 3
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (long long i = 5; i * i <= x; i += 6)   // chỉ thử 6k - 1 và 6k + 1
        if (x % i == 0 || x % (i + 2) == 0) return false;
    return true;
}

int main() {
    if (fopen("NTGANNHAT.INP", "r")) {
        freopen("NTGANNHAT.INP", "r", stdin);
        freopen("NTGANNHAT.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long n;
        scanf("%lld", &n);
        for (long long d = 0; ; d++) {      // loang ra hai phía
            if (isPrime(n - d)) { printf("%lld\n", n - d); break; }
            if (isPrime(n + d)) { printf("%lld\n", n + d); break; }
        }
    }
    return 0;
}
