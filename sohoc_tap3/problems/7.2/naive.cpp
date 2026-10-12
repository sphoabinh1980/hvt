#include <cstdio>
typedef unsigned long long ull;

int main() {
    if (fopen("CHUSO0.INP", "r")) {
        freopen("CHUSO0.INP", "r", stdin);
        freopen("CHUSO0.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ull n, b;
        scanf("%llu %llu", &n, &b);
        ull f = 1;
        for (ull i = 2; i <= n; i++) f *= i;    // 20! ≈ 2,4·10^18: vừa ull
        int cnt = 0;
        while (f % b == 0) { f /= b; cnt++; }
        printf("%d\n", cnt);
    }
    return 0;
}
