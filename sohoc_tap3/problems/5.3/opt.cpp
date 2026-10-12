#include <cstdio>
typedef unsigned long long ull;
typedef unsigned __int128 u128;

ull mulmod(ull a, ull b, ull m) { return (u128)a * b % m; }

ull power(ull a, ull e, ull m) {        // a^e mod m, lũy thừa nhanh
    ull r = 1;
    a %= m;
    while (e > 0) {
        if (e & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        e >>= 1;
    }
    return r;
}

bool isPrime(ull n) {
    if (n < 2) return false;
    static const ull B[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (ull p : B)                   // n chia hết cho một cơ số
        if (n % p == 0) return n == p;
    ull d = n - 1; int s = 0;
    while ((d & 1) == 0) { d >>= 1; s++; }      // n - 1 = d * 2^s, d lẻ
    for (ull a : B) {
        ull x = power(a, d, n);
        if (x == 1 || x == n - 1) continue;     // a "cho qua"
        bool pass = false;
        for (int r = 1; r < s && !pass; r++) {
            x = mulmod(x, x, n);
            if (x == n - 1) pass = true;
        }
        if (!pass) return false;        // a là "nhân chứng": n hợp số
    }
    return true;
}

int main() {
    if (fopen("NT64.INP", "r")) {
        freopen("NT64.INP", "r", stdin);
        freopen("NT64.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ull n;
        scanf("%llu", &n);
        puts(isPrime(n) ? "YES" : "NO");
    }
    return 0;
}
