#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll f(ll x) {
    ll s = 0;
    for (; x > 0; x /= 10) s += (x % 10) * (x % 10);
    return s;
}

int main() {
    if (fopen("DAYLAP.INP", "r")) {
        freopen("DAYLAP.INP", "r", stdin);
        freopen("DAYLAP.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        ll x, K;
        cin >> x >> K;
        if (K == 0) { cout << x << "\n"; continue; }
        x = f(x); K--;                       // sau một bước, x <= 19 * 81
        vector<int> first(2000, -1);        // first[v]: bước đầu tiên gặp v
        vector<ll> seq;
        while (first[x] == -1 && (ll)seq.size() <= K) {
            first[x] = seq.size();
            seq.push_back(x);
            x = f(x);
        }
        if (K < (ll)seq.size()) { cout << seq[K] << "\n"; continue; }
        ll mu = first[x];                    // độ dài đuôi
        ll lam = seq.size() - mu;            // độ dài chu trình
        cout << seq[mu + (K - mu) % lam] << "\n";
    }
    return 0;
}
