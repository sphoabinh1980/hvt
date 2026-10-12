#include <cstdio>

int main() {
    if (fopen("SOUOC.INP", "r")) {
        freopen("SOUOC.INP", "r", stdin);
        freopen("SOUOC.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d", &n);
        long long d = 0, s = 0;
        for (int k = 1; k <= n; k++)
            if (n % k == 0) { d++; s += k; }
        printf("%lld %lld\n", d, s);
    }
    return 0;
}
