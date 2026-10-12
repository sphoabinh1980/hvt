#include <cstdio>

int main() {
    if (fopen("NGAYTHU.INP", "r")) {
        freopen("NGAYTHU.INP", "r", stdin);
        freopen("NGAYTHU.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long t, k;
        scanf("%lld %lld", &t, &k);
        printf("%lld\n", (t - 2 + k) % 7 + 2);   // sai khi t - 2 + k < 0
    }
    return 0;
}
