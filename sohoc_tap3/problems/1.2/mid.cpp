#include <cstdio>

int main() {
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        long long d = a % 10, r = 1;
        while (b > 0) {                 // lũy thừa nhanh theo mô-đun 10
            if (b & 1) r = r * d % 10;
            d = d * d % 10;
            b >>= 1;
        }
        printf("%lld\n", r);
    }
    return 0;
}
