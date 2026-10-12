#include <cstdio>
typedef long long ll;

int gcd(int a, int b) {
    while (b) { int r = a % b; a = b; b = r; }
    return a;
}

int main() {
    if (fopen("PHANSO.INP", "r")) {
        freopen("PHANSO.INP", "r", stdin);
        freopen("PHANSO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int L, R;
        scanf("%d %d", &L, &R);
        ll cnt = 0;
        for (int b = L; b <= R; b++)
            for (int a = 1; a < b; a++)         // 0 < a/b < 1
                if (gcd(a, b) == 1) cnt++;
        printf("%lld\n", cnt);
    }
    return 0;
}
