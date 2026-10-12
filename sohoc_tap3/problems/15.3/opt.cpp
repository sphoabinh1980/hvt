#include <cstdio>
#include <cstring>
typedef long long ll;
typedef unsigned long long ull;
const ull MOD = 1000000007, M2 = MOD * MOD;   // M2 ~ 10^18
const int N = 50, LG = 60;                    // 2^60 > 10^18

int n;
ull P[LG][N][N];                              // P[i] = A^(2^i)

// c = a * b; tổng tích giữ dưới 2 * M2 < 1,8 * 10^19
void mulMat(ull a[N][N], ull b[N][N], ull c[N][N]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            ull s = 0;
            for (int t = 0; t < n; t++) {
                s += a[i][t] * b[t][j];
                if (s >= M2) s -= M2;
            }
            c[i][j] = s % MOD;
        }
}

int main() {
    if (fopen("DUONGK.INP", "r")) {
        freopen("DUONGK.INP", "r", stdin);
        freopen("DUONGK.OUT", "w", stdout);
    }
    int m, q;
    scanf("%d %d %d", &n, &m, &q);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        P[0][u - 1][v - 1] = 1;
    }
    for (int i = 1; i < LG; i++) mulMat(P[i - 1], P[i - 1], P[i]);
    while (q--) {
        int s, t; ll K;
        scanf("%d %d %lld", &s, &t, &K);
        ull v[N] = {0}, w[N];
        v[s - 1] = 1;                         // vectơ hàng e_s
        for (int i = 0; i < LG; i++)
            if (K >> i & 1) {                 // v <- v * A^(2^i)
                for (int j = 0; j < n; j++) {
                    ull acc = 0;
                    for (int u = 0; u < n; u++) {
                        acc += v[u] * P[i][u][j];
                        if (acc >= M2) acc -= M2;
                    }
                    w[j] = acc % MOD;
                }
                memcpy(v, w, sizeof(ull) * n);
            }
        printf("%llu\n", v[t - 1]);
    }
    return 0;
}
