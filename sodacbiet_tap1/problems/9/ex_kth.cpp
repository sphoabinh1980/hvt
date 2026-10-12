#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Số đối xứng dương thứ k (k = 1 -> 1, k = 10 -> 11), k <= 10^9
string kthDoiXung(ll k) {
    for (int L = 1;; L++) {
        int h = (L + 1) / 2;                       // độ dài nửa đầu
        ll cnt = 9;
        for (int i = 1; i < h; i++) cnt *= 10;      // 9 * 10^(h-1) số
        if (k > cnt) { k -= cnt; continue; }
        ll start = cnt / 9;                         // 10^(h-1)
        string s = to_string(start + k - 1);        // nửa đầu thứ k
        string t = s.substr(0, L / 2);
        reverse(t.begin(), t.end());
        return s + t;                               // lật nửa đầu
    }
}

int main() {
    ll k;
    while (cin >> k) cout << kthDoiXung(k) << "\n";
    return 0;
}
