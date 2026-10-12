#include <cstdio>

long long gcd(long long a, long long b) {
    while (b) { long long r = a % b; a = b; b = r; }
    return a;
}

int main() {
    if (fopen("MUAHANG.INP", "r")) {
        freopen("MUAHANG.INP", "r", stdin);
        freopen("MUAHANG.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        long long g = gcd(a, b), B = b / g, ans = 0;
        // các x của nghiệm cách nhau B: tìm x nhỏ nhất trong [0, B)
        for (long long x = 0; x < B && a * x <= c; x++)
            if ((c - a * x) % b == 0) {
                ans = (c - a * x) / (a * B) + 1;   // x, x + B, x + 2B, ...
                break;
            }
        printf("%lld\n", ans);
    }
    return 0;
}
