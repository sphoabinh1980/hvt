#include <cstdio>

const int N = 10000000;
char comp[N + 3];                           // sàng tới N + 2
int t[N + 1];                      // t[x] = số p <= x mà p, p + 2 nguyên tố

int main() {
    if (fopen("SINHDOI.INP", "r")) {
        freopen("SINHDOI.INP", "r", stdin);
        freopen("SINHDOI.OUT", "w", stdout);
    }
    comp[0] = comp[1] = 1;
    for (long long p = 2; p * p <= N + 2; p++)
        if (!comp[p])
            for (long long j = p * p; j <= N + 2; j += p) comp[j] = 1;
    for (int x = 1; x <= N; x++)            // "ghi danh" cặp tại số nhỏ p
        t[x] = t[x - 1] + (!comp[x] && !comp[x + 2]);
    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (b - 2 < a) printf("0\n");       // đoạn có ít hơn 3 số
        else printf("%d\n", t[b - 2] - t[a - 1]);
    }
    return 0;
}
