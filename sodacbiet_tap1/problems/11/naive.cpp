#include <bits/stdc++.h>
using namespace std;

long long f(long long x) {                  // tổng bình phương các chữ số
    long long s = 0;
    for (; x > 0; x /= 10) s += (x % 10) * (x % 10);
    return s;
}

int main() {
    if (fopen("DAYLAP.INP", "r")) {
        freopen("DAYLAP.INP", "r", stdin);
        freopen("DAYLAP.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long x, K;
        cin >> x >> K;
        for (long long i = 0; i < K; i++) x = f(x);   // đi đúng K bước
        cout << x << "\n";
    }
    return 0;
}
