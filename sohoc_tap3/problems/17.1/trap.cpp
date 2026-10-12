#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// so sánh hai số không âm dạng xâu: -1, 0, 1
int cmp(const string &x, const string &y) {
    return x < y ? -1 : (x > y ? 1 : 0);   // BẪY: "9" > "10"
}

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

string sub(const string &x, const string &y) {   // x >= y
    string r;
    int i = x.size() - 1, j = y.size() - 1, br = 0;
    while (i >= 0) {
        int s = (x[i--] - '0') - br - (j >= 0 ? y[j--] - '0' : 0);
        br = 0;
        if (s < 0) { s += 10; br = 1; }   // mượn 1 ở hàng trên
        r += char('0' + s);
    }
    while (r.size() > 1 && r.back() == '0') r.pop_back();   // xóa 0 thừa
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
    string r; bool neg;
    if (na == nb) { r = add(a, b); neg = na; }       // cùng dấu
    else {
        int c = cmp(a, b);
        if (c == 0) { cout << "0\n"; return 0; }    // a = -b
        if (c > 0) { r = sub(a, b); neg = na; }
        else       { r = sub(b, a); neg = nb; }
    }
    cout << (neg ? "-" : "") << r << "\n";
    return 0;
}
