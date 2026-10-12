#include <bits/stdc++.h>
using namespace std;

// Factorion: n = tổng giai thừa các chữ số của n.
// Số có L >= 8 chữ số có tổng <= 8 * 9! < 10^7 <= n: chỉ cần xét n < 10^7.
int main() {
    int f[10] = {1};
    for (int d = 1; d < 10; d++) f[d] = f[d - 1] * d;
    for (int n = 1; n < 10000000; n++) {
        int s = 0;
        for (int y = n; y > 0; y /= 10) s += f[y % 10];
        if (s == n) cout << n << "\n";
    }
    return 0;
}
