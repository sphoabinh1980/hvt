#include <cstdio>

int main() {
    if (fopen("MUAHANG.INP", "r")) {
        freopen("MUAHANG.INP", "r", stdin);
        freopen("MUAHANG.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long a, b, c, cnt = 0;
        scanf("%lld %lld %lld", &a, &b, &c);
        for (long long x = 0; a * x <= c; x++)  // x gói kẹo
            if ((c - a * x) % b == 0) cnt++;     // phần còn lại mua bánh
        printf("%lld\n", cnt);
    }
    return 0;
}
