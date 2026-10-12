#include <cstdio>

int main() {
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        long long a, b;                 // chỉ đúng khi a, b vừa long long
        scanf("%lld %lld", &a, &b);
        long long d = a % 10, r = 1;    // chỉ giữ chữ số cuối
        for (long long i = 0; i < b; i++)
            r = r * d % 10;
        printf("%lld\n", r);
    }
    return 0;
}
