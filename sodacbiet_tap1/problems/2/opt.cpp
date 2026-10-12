#include <bits/stdc++.h>
using namespace std;

long long powMod(long long a, long long b, long long m) {
    long long r = 1 % m;
    a %= m;
    for (; b > 0; b >>= 1, a = a * a % m)
        if (b & 1) r = r * a % m;
    return r;
}

int main() {
    if (fopen("DAUCUOI.INP", "r")) {
        freopen("DAUCUOI.INP", "r", stdin);
        freopen("DAUCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        long long a, b;
        cin >> a >> b;
       // a^b = 10^x với x = b * log10(a);  10^(phần lẻ của x) thuộc [1, 10)
        long double x = (long double)b * log10l((long double)a);
        long double frac = x - floorl(x);
        long long first = (long long)floorl(powl(10.0L, frac + 2));
        long long last = powMod(a, b, 1000);      // 3 chữ số cuối
        printf("%lld %03lld\n", first, last);
    }
    return 0;
}
