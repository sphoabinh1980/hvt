#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int L;                       // độ dài đang xét
ll pw[10];                   // pw[d] = d^L
int cnt[10];                 // tập chữ số: chữ số d xuất hiện cnt[d] lần
vector<ll> found;

void check(ll s) {           // s có đúng L chữ số và đúng tập chữ số cnt?
    int c[10] = {0}, len = 0;
    for (ll y = s; y > 0; y /= 10) { c[y % 10]++; len++; }
    if (len != L) return;
    for (int d = 0; d < 10; d++) if (c[d] != cnt[d]) return;
    found.push_back(s);
}

// chọn số lần xuất hiện của chữ số d..9; còn left chữ số chưa chọn
void chon(int d, int left, ll s) {
    if (d == 9) { cnt[9] = left; check(s + left * pw[9]); return; }
    for (int k = 0; k <= left; k++) {
        cnt[d] = k;
        chon(d + 1, left - k, s + k * pw[d]);
    }
}

int main() {
    if (fopen("TULUAN.INP", "r")) {
        freopen("TULUAN.INP", "r", stdin);
        freopen("TULUAN.OUT", "w", stdout);
    }
    int K;
    cin >> K;
    for (L = 1; L <= K; L++) {
        for (int d = 0; d < 10; d++) {
            pw[d] = 1;
            for (int i = 0; i < L; i++) pw[d] *= d;
        }
        chon(0, L, 0);
    }
    sort(found.begin(), found.end());
    found.erase(unique(found.begin(), found.end()), found.end());
    for (ll x : found) cout << x << "\n";
    return 0;
}
