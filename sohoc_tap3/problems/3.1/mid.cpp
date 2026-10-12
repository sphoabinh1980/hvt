#include <cstdio>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    if (fopen("CATGACH.INP", "r")) {
        freopen("CATGACH.INP", "r", stdin);
        freopen("CATGACH.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        long long g = gcd(a, b);
        printf("%lld %lld\n", g, (a / g) * (b / g)); // tràn khi > 9,2·10^18
    }
    return 0;
}
