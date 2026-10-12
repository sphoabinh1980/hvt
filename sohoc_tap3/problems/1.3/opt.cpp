#include <cstdio>

int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    long long n, m;
    scanf("%lld %lld", &n, &m);
    long long r = 0;
    long long nextPow = 10;             // số i đầu tiên có thêm một chữ số
    long long p = 10 % m;               // 10^(số chữ số của i) mod m
    for (long long i = 1; i <= n; i++) {
        if (i == nextPow) {             // i = 10, 100, 1000, ...
            p = p * 10 % m;
            nextPow *= 10;
        }
        r = (r * p + i % m) % m;        // r * p < 10^18: vừa long long
    }
    printf("%lld\n", r);
    return 0;
}
