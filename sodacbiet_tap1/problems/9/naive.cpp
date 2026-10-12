#include <bits/stdc++.h>
using namespace std;

bool doiXung(long long x) {             // so sánh x với số đảo ngược của nó
    long long y = x, r = 0;
    while (y > 0) { r = r * 10 + y % 10; y /= 10; }
    return r == x;
}

int main() {
    if (fopen("DEMDX.INP", "r")) {
        freopen("DEMDX.INP", "r", stdin);
        freopen("DEMDX.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long L, R, cnt = 0;
        cin >> L >> R;
        for (long long x = L; x <= R; x++)
            if (doiXung(x)) cnt++;
        cout << cnt << "\n";
    }
    return 0;
}
