#include <cstdio>

bool isPrime(long long x) {             // thử mọi i từ 2 tới √x
    if (x < 2) return false;
    for (long long i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
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
