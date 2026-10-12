#include <bits/stdc++.h>
using namespace std;

// Ghép n số tự nhiên (dạng xâu) thành số lớn nhất
int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (auto &x : a) cin >> x;
    sort(a.begin(), a.end(), [](const string &x, const string &y) {
        return x + y > y + x;                // x đứng trước y nếu xy > yx
    });
    string r;
    for (auto &x : a) r += x;
    if (r[0] == '0') r = "0";                // toàn số 0
    cout << r << "\n";
    return 0;
}
