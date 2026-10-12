#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("HARSHAD.INP", "r")) {
        freopen("HARSHAD.INP", "r", stdin);
        freopen("HARSHAD.OUT", "w", stdout);
    }
    long long N;
    cin >> N;
    long long cnt = 0;
    for (long long x = 1; x <= N; x++) {
        int s = 0;
        for (long long y = x; y > 0; y /= 10) s += y % 10;
        if (x % s == 0) cnt++;                 // x chia hết cho tổng chữ số
    }
    cout << cnt << "\n";
    return 0;
}
