#include <cstdio>

int main() {
    if (fopen("LUYTHUALON.INP", "r")) {
        freopen("LUYTHUALON.INP", "r", stdin);
        freopen("LUYTHUALON.OUT", "w", stdout);
    }
    long long a, b, r = 1;             // đúng khi a^b <= 10^18
    scanf("%lld %lld", &a, &b);
    for (long long i = 0; i < b; i++) r *= a;
    printf("%lld\n", r);
    return 0;
}
