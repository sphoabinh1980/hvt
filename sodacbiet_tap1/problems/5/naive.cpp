#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DOANDU.INP", "r")) {
        freopen("DOANDU.INP", "r", stdin);
        freopen("DOANDU.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string S;
    long long m;
    int q;
    cin >> S >> m >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        long long res = 0;
        for (int i = l - 1; i < r; i++)           // Horner trên đoạn [l, r]
            res = (res * 10 + (S[i] - '0')) % m;
        cout << res << "\n";
    }
    return 0;
}
