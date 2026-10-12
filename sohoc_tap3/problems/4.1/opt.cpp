#include <cstdio>

long long gcd(long long a, long long b) {
    while (b) { long long r = a % b; a = b; b = r; }
    return a;
}

int main() {
    if (fopen("DONGNUOC.INP", "r")) {
        freopen("DONGNUOC.INP", "r", stdin);
        freopen("DONGNUOC.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    long long g = 0;                    // gcd(0, x) = x
    for (int i = 0; i < n; i++) {
        long long x;
        scanf("%lld", &x);
        g = gcd(g, x);
    }
    printf("%lld\n", g);                // lượng dương nhỏ nhất đong được
    while (q--) {
        long long c;
        scanf("%lld", &c);
        puts(c % g == 0 ? "CO" : "KHONG");     // c = 0 luôn đong được
    }
    return 0;
}
