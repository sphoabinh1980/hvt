#include <bits/stdc++.h>
using namespace std;

// số các x trong [1, n] có căn số d: x = d, d + 9, d + 18, ...
long long dem(long long n, int d) {
    if (n < d) return 0;
    return (n - d) / 9 + 1;
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
        cout << dem(R, d) - dem(L - 1, d) << "\n";
    }
    return 0;
}
