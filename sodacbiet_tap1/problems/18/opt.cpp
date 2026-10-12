#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("THANTHIET.INP", "r")) {
        freopen("THANTHIET.INP", "r", stdin);
        freopen("THANTHIET.OUT", "w", stdout);
    }
    int N;
    cin >> N;
    vector<int> s(N + 1, 0);                // s[x]: tổng các ước thực sự
    for (int d = 1; d <= N / 2; d++)     // d là ước thực sự của 2d, 3d, ...
        for (int m = 2 * d; m <= N; m += d) s[m] += d;
    vector<pair<int, int>> res;
    for (int a = 1; a <= N; a++) {
        int b = s[a];
        if (b > a && b <= N && s[b] == a) res.push_back({a, b});
    }
    cout << res.size() << "\n";
    for (auto [a, b] : res) cout << a << " " << b << "\n";
    return 0;
}
