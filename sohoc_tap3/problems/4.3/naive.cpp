#include <cstdio>

int main() {
    if (fopen("DONGHO.INP", "r")) {
        freopen("DONGHO.INP", "r", stdin);
        freopen("DONGHO.OUT", "w", stdout);
    }
    int Q;
    scanf("%d", &Q);
    while (Q--) {
        long long m, p, a, q, b, T;
        scanf("%lld %lld %lld %lld %lld %lld", &m, &p, &a, &q, &b, &T);
        long long first = -1, cnt = 0, A = p, B = q;    // vị trí hai kim
        long long lim = (T + 1 > m) ? T + 1 : m;   // sau m giây thì lặp lại
        for (long long t = 0; t < lim; t++) {
            if (A == B) {
                if (first < 0) first = t;
                if (t <= T) cnt++;
            }
            A = (A + a) % m;
            B = (B + b) % m;
        }
        printf("%lld %lld\n", first, cnt);
    }
    return 0;
}
