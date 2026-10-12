#include <cstdio>

int main() {
    if (fopen("CATGACH.INP", "r")) {
        freopen("CATGACH.INP", "r", stdin);
        freopen("CATGACH.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        long long s = a < b ? a : b;
        while (a % s != 0 || b % s != 0) s--; // cạnh lớn nhất chia hết
        printf("%lld %lld\n", s, (a / s) * (b / s));
    }
    return 0;
}
