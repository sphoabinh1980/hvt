#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BOI01.INP", "r")) {
        freopen("BOI01.INP", "r", stdin);
        freopen("BOI01.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    vector<int> par(n, -1);         // số dư đứng trước trong BFS
    vector<char> dig(n), seen(n, 0); // chữ số vừa thêm để tới số dư này
    queue<int> q;
    int s = 1 % n;                   // số "1"
    seen[s] = 1; dig[s] = '1'; q.push(s);
    while (!q.empty()) {
        int r = q.front(); q.pop();
        if (r == 0) break;           // đã tới một bội của n
        for (int d = 0; d <= 1; d++) {          // thêm 0 trước, rồi 1
            int t = (int)((10LL * r + d) % n);
            if (!seen[t]) {
                seen[t] = 1; par[t] = r; dig[t] = '0' + d;
                q.push(t);
            }
        }
    }
    string ans;                      // lần ngược từ số dư 0 về số "1"
    for (int r = 0; r != -1; r = par[r]) {
        ans += dig[r];
        if (r == s) break;
    }
    reverse(ans.begin(), ans.end());
    cout << ans << "\n";
    return 0;
}
