#include <cstdio>

const int N = 10000000;
char comp[N + 1];                    // comp[x] = 1: x là hợp số (hoặc 0, 1)
int cnt[N + 1];                             // cnt[x] = π(x)

int main() {
    if (fopen("DEMNGUYENTO.INP", "r")) {
        freopen("DEMNGUYENTO.INP", "r", stdin);
        freopen("DEMNGUYENTO.OUT", "w", stdout);
    }
    comp[0] = comp[1] = 1;
    for (long long p = 2; p * p <= N; p++)  // sàng Eratosthenes
        if (!comp[p])
            for (long long j = p * p; j <= N; j += p) comp[j] = 1;
    for (int x = 1; x <= N; x++) cnt[x] = cnt[x - 1] + !comp[x];
    int q;
    scanf("%d", &q);
    while (q--) {
        int t, x;
        scanf("%d %d", &t, &x);
        if (t == 1) printf("%d\n", cnt[x]);
        else {                           // duyệt sàng tìm số thứ x: O(10^7)
            int v = 1;
            while (cnt[v] < x) v++;
            printf("%d\n", v);
        }
    }
    return 0;
}
