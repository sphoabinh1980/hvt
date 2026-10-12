#include <bits/stdc++.h>
using namespace std;

// Đếm x trong [1, N] mà xâu chữ số không chứa mẫu P
string s, P;
int go_[20][10];                       // máy KMP: khớp j, đọc c -> khớp mới
long long memo[20][20][2];

long long dfs(int pos, int j, bool started, bool tight) {
    if (j == (int)P.size()) return 0;      // đã chứa mẫu: loại
    if (pos == (int)s.size()) return started;
    long long &m = memo[pos][j][started];
    if (!tight && m != -1) return m;
    int hi = tight ? s[pos] - '0' : 9;
    long long r = 0;
    for (int d = 0; d <= hi; d++) {
        bool st = started || d != 0;       // 0 ở đầu không phải chữ số thật
        int nj = st ? go_[j][d] : 0;
        r += dfs(pos + 1, nj, st, tight && d == hi);
    }
    if (!tight) m = r;
    return r;
}

int main() {
    long long N;
    cin >> N >> P;
    s = to_string(N);
    int m = P.size();
    vector<int> pi(m, 0);                  // hàm tiền tố của P
    for (int i = 1; i < m; i++) {
        int k = pi[i - 1];
        while (k > 0 && P[i] != P[k]) k = pi[k - 1];
        if (P[i] == P[k]) k++;
        pi[i] = k;
    }
    for (int j = 0; j < m; j++)
        for (int c = 0; c < 10; c++) {
            int k = j;
            while (k > 0 && P[k] - '0' != c) k = pi[k - 1];
            go_[j][c] = (P[k] - '0' == c) ? k + 1 : 0;
        }
    memset(memo, -1, sizeof memo);
    cout << dfs(0, 0, false, true) << "\n";
    return 0;
}
