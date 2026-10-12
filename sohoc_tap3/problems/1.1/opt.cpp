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
        long long x = t - 2 + k;        // |x| <= 10^18 + 6: vừa long long
        long long d = (x % 7 + 7) % 7;  // số dư không âm, 0..6
        printf("%lld\n", d + 2);
    }
    return 0;
}
