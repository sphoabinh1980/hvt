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
        int d = t - 2;                  // thứ Hai = 0, ..., Chủ nhật = 6
        if (k >= 0) {
            for (long long i = 0; i < k; i++) {    // tiến từng ngày
                d++;
                if (d == 7) d = 0;
            }
        } else {
            for (long long i = 0; i < -k; i++) {   // lùi từng ngày
                d--;
                if (d < 0) d = 6;
            }
        }
        printf("%d\n", d + 2);
    }
    return 0;
}
