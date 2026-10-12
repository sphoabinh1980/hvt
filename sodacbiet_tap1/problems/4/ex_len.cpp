#include <bits/stdc++.h>
using namespace std;

// Tổng số chữ số khi viết liền 1, 2, ..., n  (n <= 10^17)
long long tongDoDai(long long n) {
    long long total = 0;
    for (long long len = 1, start = 1; start <= n; len++, start *= 10) {
        long long end = min(n, start * 10 - 1);   // nhóm [start, end]
        total += (end - start + 1) * len;
    }
    return total;
}

int main() {
    long long n;
    while (cin >> n) cout << tongDoDai(n) << "\n";
    return 0;
}
