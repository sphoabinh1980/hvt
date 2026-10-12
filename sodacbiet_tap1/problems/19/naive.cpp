#include <bits/stdc++.h>
using namespace std;

long long isqrt(long long x) {              // phần nguyên của căn x
    long long r = sqrtl((long double)x);
    while (r * r > x) r--;
    while ((r + 1) * (r + 1) <= x) r++;
    return r;
}

int main() {
    if (fopen("HAIBP.INP", "r")) {
        freopen("HAIBP.INP", "r", stdin);
        freopen("HAIBP.OUT", "w", stdout);
    }
    int Q;
    scanf("%d", &Q);
    while (Q--) {
        long long n;
        scanf("%lld", &n);
        int cnt = 0;
        for (long long a = 0; 2 * a * a <= n; a++) {   // a <= b
            long long b = isqrt(n - a * a);
            if (b * b == n - a * a) cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
