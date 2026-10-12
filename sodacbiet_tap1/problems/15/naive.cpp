#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TONGS.INP", "r")) {
        freopen("TONGS.INP", "r", stdin);
        freopen("TONGS.OUT", "w", stdout);
    }
    long long L, R;
    int S;
    cin >> L >> R >> S;
    long long cnt = 0;
    for (long long x = L; x <= R; x++) {
        int s = 0;
        for (long long y = x; y > 0; y /= 10) s += y % 10;   // tổng chữ số
        if (s == S) cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
