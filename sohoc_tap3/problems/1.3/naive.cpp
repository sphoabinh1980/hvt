#include <cstdio>

int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    long long n, m;
    scanf("%lld %lld", &n, &m);
    long long x = 0;                    // số bé Na viết, giữ nguyên giá trị
    for (long long i = 1; i <= n; i++) {
        long long p = 1;
        while (p <= i) p *= 10;         // 10^(số chữ số của i)
        x = x * p + i;                  // tràn số khi x có quá 18 chữ số
    }
    printf("%lld\n", x % m);
    return 0;
}
