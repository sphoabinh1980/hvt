#include <bits/stdc++.h>
using namespace std;

// Đếm bộ ba Pythagoras a < b < c <= N: nguyên thủy và tất cả
int main() {
    long long N;
    cin >> N;
    long long prim = 0, all = 0;
    for (long long m = 2; m * m + 1 <= N; m++)
        for (long long n = 1; n < m; n++) {
            long long c = m * m + n * n;
            if (c > N) break;
            if ((m - n) % 2 == 0 || __gcd(m, n) != 1) continue;
            prim++;                         // (m²-n², 2mn, m²+n²)
            all += N / c;                   // các bội k·(a, b, c)
        }
    cout << prim << " " << all << "\n";
    return 0;
}
