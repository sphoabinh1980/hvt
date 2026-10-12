#include <bits/stdc++.h>
using namespace std;

int canSo(long long x) {                 // cộng chữ số tới khi còn 1 chữ số
    while (x >= 10) {
        long long s = 0;
        while (x > 0) { s += x % 10; x /= 10; }
        x = s;
    }
    return x;
}

int main() {
    if (fopen("CANSO.INP", "r")) {
        freopen("CANSO.INP", "r", stdin);
        freopen("CANSO.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long L, R; int d;
        cin >> L >> R >> d;
        long long cnt = 0;
        for (long long x = L; x <= R; x++)
            if (canSo(x) == d) cnt++;
        cout << cnt << "\n";
    }
    return 0;
}
