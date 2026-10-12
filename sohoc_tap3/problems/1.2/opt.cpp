#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        string a, b;
        cin >> a >> b;
        if (b == "0") {                     // a^0 = 1, kể cả 0^0
            cout << 1 << '\n';
            continue;
        }
        int d = a.back() - '0';             // chữ số cuối của a
        int e = 0;                          // e = b mod 4 (Horner)
        for (char c : b) e = (e * 10 + (c - '0')) % 4;
        if (e == 0) e = 4;          // b > 0 chia hết cho 4: dùng mũ 4
        int r = 1;
        for (int i = 0; i < e; i++) r = r * d % 10;
        cout << r << '\n';
    }
    return 0;
}
