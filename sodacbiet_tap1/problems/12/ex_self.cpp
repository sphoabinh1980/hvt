#include <bits/stdc++.h>
using namespace std;

// Số tự sinh (self number): không viết được dưới dạng m + S(m).
// Chỉ m < n mới có thể sinh ra n, nên đánh dấu m + S(m) với mọi m <= N.
int main() {
    int N;
    cin >> N;
    vector<bool> sinhRa(N + 1, false);
    for (int m = 1; m <= N; m++) {
        int s = m;
        for (int y = m; y > 0; y /= 10) s += y % 10;
        if (s <= N) sinhRa[s] = true;
    }
    for (int n = 1; n <= N; n++)
        if (!sinhRa[n]) cout << n << " ";
    cout << "\n";
    return 0;
}
