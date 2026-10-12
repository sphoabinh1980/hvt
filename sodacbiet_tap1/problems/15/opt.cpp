#include <bits/stdc++.h>
using namespace std;

int S;
long long memo[20][200];   // memo[còn k chữ số][cần tổng t], -1 = chưa tính

// số cách điền k chữ số tự do (0..9) có tổng đúng t
long long ways(int k, int t) {
    if (t < 0) return 0;
    if (k == 0) return t == 0;
    long long &r = memo[k][t];
    if (r != -1) return r;
    r = 0;
    for (int d = 0; d <= 9; d++) r += ways(k - 1, t - d);
    return r;
}

// đếm x trong [0, N] có tổng chữ số bằng S
long long f(long long N) {
    if (N < 0) return 0;
    string s = to_string(N);
    int L = s.size(), need = S;             // need: tổng còn phải đạt
    long long cnt = 0;
    for (int i = 0; i < L && need >= 0; i++) {
        int c = s[i] - '0';
        for (int d = 0; d < c; d++)          // đặt d < c: phần sau tự do
            cnt += ways(L - 1 - i, need - d);
        need -= c;                           // đặt d = c: vẫn bám sát N
    }
    if (need == 0) cnt++;                    // chính số N
    return cnt;
}

int main() {
    if (fopen("TONGS.INP", "r")) {
        freopen("TONGS.INP", "r", stdin);
        freopen("TONGS.OUT", "w", stdout);
    }
    long long L, R;
    cin >> L >> R >> S;
    memset(memo, -1, sizeof memo);
    cout << f(R) - f(L - 1) << "\n";
    return 0;
}
