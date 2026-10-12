#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
typedef __int128 lll;

lll parse(const string &s) {
    lll v = 0;
    for (char ch : s) if (ch != '-') v = v * 10 + (ch - '0');
    return s[0] == '-' ? -v : v;
}

int main() {
    if (fopen("TICHLON.INP", "r")) {
        freopen("TICHLON.INP", "r", stdin);
        freopen("TICHLON.OUT", "w", stdout);
    }
    string a, b;
    cin >> a >> b;
    lll p = parse(a) * parse(b);         // |p| <= 10^36 < 1,7 * 10^38
    if (p == 0) { cout << "0\n"; return 0; }
    string r; bool neg = p < 0;
    if (neg) p = -p;
    while (p > 0) { r += char('0' + (int)(p % 10)); p /= 10; }
    if (neg) r += '-';
    reverse(r.begin(), r.end());
    cout << r << "\n";
    return 0;
}
