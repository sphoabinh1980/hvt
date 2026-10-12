#include <cstdio>

int main() {
    if (fopen("TONGLON.INP", "r")) {
        freopen("TONGLON.INP", "r", stdin);
        freopen("TONGLON.OUT", "w", stdout);
    }
    long long a, b;                   // chỉ đúng khi |a|, |b| <= 10^18
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", a + b);
    return 0;
}
