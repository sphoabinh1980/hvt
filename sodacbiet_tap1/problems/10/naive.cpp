#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TULUAN.INP", "r")) {
        freopen("TULUAN.INP", "r", stdin);
        freopen("TULUAN.OUT", "w", stdout);
    }
    int K;
    cin >> K;
    long long lim = 1;
    for (int i = 0; i < K; i++) lim *= 10;
    for (long long n = 1; n < lim; n++) {
        int len = 0, d[20];
        for (long long y = n; y > 0; y /= 10) d[len++] = y % 10;
        long long s = 0;
        for (int i = 0; i < len; i++) {
            long long p = 1;
            for (int j = 0; j < len; j++) p *= d[i];   // d[i]^len
            s += p;
        }
        if (s == n) cout << n << "\n";
    }
    return 0;
}
