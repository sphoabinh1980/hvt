#include <bits/stdc++.h>
using namespace std;

// Đếm x trong [1, N] không có hai chữ số kề nhau bằng nhau
string s;
long long memo[20][11];                   // memo[pos][last], chỉ khi tự do

// last = 10: chưa bắt đầu (toàn số 0 ở đầu)
long long go(int pos, int last, bool tight) {
    if (pos == (int)s.size()) return last != 10;      // bỏ x = 0
    if (!tight && memo[pos][last] != -1) return memo[pos][last];
    int hi = tight ? s[pos] - '0' : 9;
    long long r = 0;
    for (int d = 0; d <= hi; d++) {
        if (d == last) continue;                       // kề nhau bằng nhau
        int nl = (last == 10 && d == 0) ? 10 : d;      // vẫn chưa bắt đầu
        r += go(pos + 1, nl, tight && d == hi);
    }
    if (!tight) memo[pos][last] = r;
    return r;
}

int main() {
    long long N;
    cin >> N;
    s = to_string(N);
    memset(memo, -1, sizeof memo);
    cout << go(0, 10, true) << "\n";
    return 0;
}
