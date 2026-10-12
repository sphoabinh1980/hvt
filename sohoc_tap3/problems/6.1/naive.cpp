#include <cstdio>

bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int main() {
    if (fopen("DEMNGUYENTO.INP", "r")) {
        freopen("DEMNGUYENTO.INP", "r", stdin);
        freopen("DEMNGUYENTO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int t, x;
        scanf("%d %d", &t, &x);
        if (t == 1) {                       // đếm số nguyên tố <= x
            int c = 0;
            for (int v = 2; v <= x; v++) c += isPrime(v);
            printf("%d\n", c);
        } else {                            // số nguyên tố thứ x
            int c = 0, v = 1;
            while (c < x) { v++; if (isPrime(v)) c++; }
            printf("%d\n", v);
        }
    }
    return 0;
}
