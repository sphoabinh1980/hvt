#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll p10[20];

ll guong(ll half, int len) {         // nửa đầu -> số đối xứng có len chữ số
    ll x = half;
    if (len % 2 == 1) half /= 10;        // độ dài lẻ: chữ số giữa không lặp
    while (half > 0) { x = x * 10 + half % 10; half /= 10; }
    return x;
}

ll dem(ll n) {                           // số đối xứng trong [1, n]
    if (n <= 0) return 0;
    int len = to_string(n).size();
    ll cnt = 0;
    for (int L = 1; L < len; L++)        // mọi số đối xứng ngắn hơn n
        cnt += 9 * p10[(L + 1) / 2 - 1];
    int h = (len + 1) / 2;
    ll half = n / p10[len - h];          // h chữ số đầu của n
    cnt += half - p10[h - 1];            // nửa đầu nhỏ hơn: số đối xứng < n
    if (guong(half, len) <= n) cnt++;    // nửa đầu bằng: so sánh trực tiếp
    return cnt;
}

int main() {
    if (fopen("DEMDX.INP", "r")) {
        freopen("DEMDX.INP", "r", stdin);
        freopen("DEMDX.OUT", "w", stdout);
    }
    p10[0] = 1;
    for (int i = 1; i < 20; i++) p10[i] = p10[i - 1] * 10;
    int Q;
    cin >> Q;
    while (Q--) {
        ll L, R;
        cin >> L >> R;
        cout << dem(R) - dem(L - 1) << "\n";
    }
    return 0;
}
