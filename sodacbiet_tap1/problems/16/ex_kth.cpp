#include <bits/stdc++.h>
using namespace std;

// Số nguyên dương thứ k có tổng chữ số S (đáp số < 10^18)
long long memo[19][163];

long long ways(int k, int t) {             // như Bài 15
    if (t < 0) return 0;
    if (k == 0) return t == 0;
    long long &r = memo[k][t];
    if (r != -1) return r;
    r = 0;
    for (int d = 0; d <= 9; d++) r += ways(k - 1, t - d);
    return r;
}

int main() {
    long long k;
    int S;
    cin >> k >> S;
    memset(memo, -1, sizeof memo);
    if (ways(18, S) < k) { cout << -1 << "\n"; return 0; }
    long long x = 0;
    int need = S;
    for (int i = 0; i < 18; i++) {         // dựng 18 chữ số, cho phép 0 đầu
        for (int d = 0; d <= 9; d++) {
            long long c = ways(17 - i, need - d);   // số cách nếu đặt d
            if (k <= c) { x = x * 10 + d; need -= d; break; }
            k -= c;                        // bỏ qua cả khối bắt đầu bằng d
        }
    }
    cout << x << "\n";
    return 0;
}
