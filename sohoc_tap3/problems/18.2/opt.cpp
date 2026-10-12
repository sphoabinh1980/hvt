#include <cstdio>
typedef long long ll;
typedef unsigned __int128 u128;

// f(n) = popcount(0) + popcount(1) + ... + popcount(n), n >= -1
u128 f(ll n) {
    u128 s = 0;
    for (int k = 0; k <= 60; k++) {
        ll half = 1LL << k, period = half << 1;   // cột k: chu kì 2^(k+1)
        ll q = (n + 1) / period, r = (n + 1) % period;
        s += (u128)q * half + (r > half ? r - half : 0);
    }
    return s;
}

void print(u128 x) {                     // printf không in được __int128
    char buf[45]; int len = 0;
    do { buf[len++] = '0' + (int)(x % 10); x /= 10; } while (x > 0);
    while (len > 0) putchar(buf[--len]);
    putchar('\n');
}

int main() {
    if (fopen("BITDOAN.INP", "r")) {
        freopen("BITDOAN.INP", "r", stdin);
        freopen("BITDOAN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll L, R;
        scanf("%lld %lld", &L, &R);
        print(f(R) - f(L - 1));
    }
    return 0;
}
