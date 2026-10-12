#include <cstdio>

bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int main() {
    if (fopen("SINHDOI.INP", "r")) {
        freopen("SINHDOI.INP", "r", stdin);
        freopen("SINHDOI.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b, c = 0;
        scanf("%d %d", &a, &b);
        for (int p = a; p + 2 <= b; p++) // (p, p + 2) nằm trọn trong [a, b]
            if (isPrime(p) && isPrime(p + 2)) c++;
        printf("%d\n", c);
    }
    return 0;
}
