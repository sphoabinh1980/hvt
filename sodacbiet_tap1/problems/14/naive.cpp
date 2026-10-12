#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XOACS.INP", "r")) {
        freopen("XOACS.INP", "r", stdin);
        freopen("XOACS.OUT", "w", stdout);
    }
    string s;
    int k;
    cin >> s >> k;
    for (int t = 0; t < k; t++) {            // mỗi lượt xóa một chữ số
        size_t i = 0;
        while (i + 1 < s.size() && s[i] <= s[i + 1]) i++;   // đỉnh đầu tiên
        s.erase(i, 1);                       // O(L) mỗi lần xóa
    }
    size_t p = s.find_first_not_of('0');     // bỏ các chữ số 0 ở đầu
    cout << (p == string::npos ? "0" : s.substr(p)) << "\n";
    return 0;
}
