#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TUDONGCAU.INP", "r")) {
        freopen("TUDONGCAU.INP", "r", stdin);
        freopen("TUDONGCAU.OUT", "w", stdout);
    }
    int K;
    cin >> K;
    long long lim = 1;
    for (int i = 0; i < K; i++) lim *= 10;
    long long p = 10;                       // 10^(số chữ số của n)
    for (long long n = 1; n < lim; n++) {
        if (n == p) p *= 10;
        __int128 sq = (__int128)n * n;      // n^2 tới 10^36
        if ((long long)(sq % p) == n) cout << n << "\n";
    }
    return 0;
}
