#include <cstdio>

typedef unsigned long long ull;
typedef unsigned __int128 u128;

ull gcd(ull a, ull b) {
    while (b != 0) {
        ull r = a % b;
        a = b;
        b = r;
    }
    return a;
}

void print128(u128 x) {                 // in số 128 bit không dấu
    char buf[45];
    int len = 0;
    do {
        buf[len++] = '0' + (int)(x % 10);
        x /= 10;
    } while (x > 0);
    while (len > 0) putchar(buf[--len]);
}

int main() {
    if (fopen("CATGACH.INP", "r")) {
        freopen("CATGACH.INP", "r", stdin);
        freopen("CATGACH.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ull a, b;
        scanf("%llu %llu", &a, &b);
        ull g = gcd(a, b);
        u128 cnt = (u128)(a / g) * (b / g);     // chia trước, nhân sau
        printf("%llu ", g);
        print128(cnt);
        putchar('\n');
    }
    return 0;
}
