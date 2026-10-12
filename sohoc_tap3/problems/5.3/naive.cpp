#include <cstdio>
typedef unsigned long long ull;

bool isPrime(ull n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (ull i = 5; i * i <= n; i += 6)     // tới √n: 4,3 tỉ với n ≈ 2^64
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}

int main() {
    if (fopen("NT64.INP", "r")) {
        freopen("NT64.INP", "r", stdin);
        freopen("NT64.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ull n;
        scanf("%llu", &n);
        puts(isPrime(n) ? "YES" : "NO");
    }
    return 0;
}
