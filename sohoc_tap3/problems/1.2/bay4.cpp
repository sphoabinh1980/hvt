#include <iostream>
#include <string>
using namespace std;

int main() {
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        string a, b;
        cin >> a >> b;
        int d = a.back() - '0';
        int e = 0;
        for (char c : b) e = (e * 10 + (c - '0')) % 4;   // b mod 4
        int r = 1;
        for (int i = 0; i < e; i++) r = r * d % 10;  // SAI khi e = 0, b > 0
        cout << r << '\n';
    }
    return 0;
}
