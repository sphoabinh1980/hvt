#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10000000;
int spf[MAXN + 1];                          // ước nguyên tố nhỏ nhất

int main() {
    if (fopen("HAIBP.INP", "r")) {
        freopen("HAIBP.INP", "r", stdin);
        freopen("HAIBP.OUT", "w", stdout);
    }
    for (int i = 2; i <= MAXN; i++)
        if (spf[i] == 0)
            for (int j = i; j <= MAXN; j += i)
                if (spf[j] == 0) spf[j] = i;
    int Q;
    scanf("%d", &Q);
    while (Q--) {
        int n;
        scanf("%d", &n);
        long long B = 1;                    // tích (e + 1), p = 4k + 1
        bool ok = true;
        for (int m = n; m > 1;) {
            int p = spf[m], e = 0;
            while (m % p == 0) m /= p, e++;
            if (p % 4 == 1) B *= e + 1;
            else if (p % 4 == 3 && e % 2 == 1) ok = false;
        }
        if (!ok) { printf("0\n"); continue; }
        int r = sqrt((double)n);
        while (r * r > n) r--;
        while ((r + 1) * (r + 1) <= n) r++;
        int z = (r * r == n);               // n = 0^2 + r^2
        int h = sqrt((double)(n / 2));
        while (h * h > n / 2) h--;
        while ((h + 1) * (h + 1) <= n / 2) h++;
        int e2 = (n % 2 == 0 && h * h == n / 2);   // n = h^2 + h^2
        printf("%lld\n", (B + z + e2) / 2);
    }
    return 0;
}
