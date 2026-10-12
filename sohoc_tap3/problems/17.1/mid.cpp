#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string add(const string &x, const string &y) {
    string r;
    int i = x.size() - 1, j = y.size() - 1, c = 0;
    while (i >= 0 || j >= 0 || c) {
        int s = c;
        if (i >= 0) s += x[i--] - '0';
        if (j >= 0) s += y[j--] - '0';
        r += char('0' + s % 10);
        c = s / 10;                       // số nhớ 0 hoặc 1
    }
    reverse(r.begin(), r.end());
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    if (fopen("TONGLON.INP", "r")) {
        freopen("TONGLON.INP", "r", stdin);
        freopen("TONGLON.OUT", "w", stdout);
    }
    string a, b;
    cin >> a >> b;
    bool na = a[0] == '-', nb = b[0] == '-';
    if (na) a = a.substr(1);
    if (nb) b = b.substr(1);
    // coi như a, b cùng dấu: cộng trị tuyệt đối, lấy dấu của a
    cout << (na ? "-" : "") << add(a, b) << "\n";
    return 0;
}
