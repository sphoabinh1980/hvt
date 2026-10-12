#include <cstdio>

const int N = 10000000;
int spf[N + 1];                             // ước nguyên tố nhỏ nhất, 40 MB

int main() {
    if (fopen("SOUOC.INP", "r")) {
        freopen("SOUOC.INP", "r", stdin);
        freopen("SOUOC.OUT", "w", stdout);
    }
    for (long long p = 2; p <= N; p++)
        if (spf[p] == 0) {                  // p nguyên tố
            spf[p] = p;
            for (long long j = p * p; j <= N; j += p)
                if (spf[j] == 0) spf[j] = p;    // lần gạch đầu tiên
        }
    int q;
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d", &n);
        long long d = 1, s = 1;
        while (n > 1) {
            int p = spf[n];
            long long pk = 1, sum = 1;      // sum = 1 + p + ... + p^e
            int e = 0;
            while (n % p == 0) {
                n /= p; e++;
                pk *= p; sum += pk;
            }
            d *= (e + 1);
            s *= sum;
        }
        printf("%lld %lld\n", d, s);
    }
    return 0;
}
