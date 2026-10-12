#include <bits/stdc++.h>
using namespace std;

// Số lần chữ số d (0..9) xuất hiện khi viết các số 1, 2, ..., n
long long demChuSo(long long n, int d) {
    long long cnt = 0;
    for (long long p = 1; p <= n; p *= 10) {
        long long high = n / (p * 10), cur = n / p % 10, low = n % p;
        if (d > 0) cnt += high * p;
        else cnt += (high - 1) * p;       // chữ số 0 không đứng đầu số
        if (cur > d) cnt += p;
        else if (cur == d) cnt += low + 1;
    }
    return cnt;
}

int main() {
    long long n; int d;
    while (cin >> n >> d) cout << demChuSo(n, d) << "\n";
    return 0;
}
