#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("KETIEP.INP", "r")) {
        freopen("KETIEP.INP", "r", stdin);
        freopen("KETIEP.OUT", "w", stdout);
    }
    string s;
    cin >> s;
    int L = s.size();
    int i = L - 2;
    while (i >= 0 && s[i] >= s[i + 1]) i--;     // đuôi dài nhất không tăng
    if (i < 0) { cout << -1 << "\n"; return 0; } // s đã là hoán vị lớn nhất
    int j = L - 1;
    while (s[j] <= s[i]) j--;               // chữ số nhỏ nhất > s[i] ở đuôi
    swap(s[i], s[j]);
    reverse(s.begin() + i + 1, s.end());         // đuôi thành tăng dần
    cout << s << "\n";
    return 0;
}
