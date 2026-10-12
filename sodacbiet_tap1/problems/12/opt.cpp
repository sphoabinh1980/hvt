#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

int main() {
    if (fopen("TUDONGCAU.INP", "r")) {
        freopen("TUDONGCAU.INP", "r", stdin);
        freopen("TUDONGCAU.OUT", "w", stdout);
    }
    int K;
    cin >> K;
    vector<ll> ans = {1};                   // 1^2 = 1
    for (ll x0 : {5LL, 6LL}) {             // hai họ nghiệm không tầm thường
        ll x = x0, p = 10;                  // x^2 ≡ x (mod p), p = 10^k
        for (int k = 1; k <= K; k++) {
            if (x >= p / 10) ans.push_back(x);   // đủ k chữ số (đầu khác 0)
            if (k == K) break;
            for (int d = 0; d <= 9; d++) {  // thêm chữ số d vào bên trái
                ll y = x + d * p;
                lll q = (lll)p * 10;
                if ((lll)y * y % q == y) { x = y; break; }
            }
            p *= 10;
        }
    }
    sort(ans.begin(), ans.end());
    for (ll v : ans) cout << v << "\n";
    return 0;
}
