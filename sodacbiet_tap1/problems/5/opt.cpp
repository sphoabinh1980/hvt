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
    int n = S.size();
    vector<long long> P(n + 1), pw(n + 1);
    P[0] = 0; pw[0] = 1 % m;
    for (int i = 1; i <= n; i++) {
        P[i] = (P[i - 1] * 10 + (S[i - 1] - '0')) % m;   // S[1..i] mod m
        pw[i] = pw[i - 1] * 10 % m;                        // 10^i mod m
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        // S[1..r] = S[1..l-1] * 10^(r-l+1) + S[l..r]
        long long res = (P[r] - P[l - 1] * pw[r - l + 1] % m + m) % m;
        cout << res << "\n";
    }
    return 0;
}
