#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DAUCUOI.INP", "r")) {
        freopen("DAUCUOI.INP", "r", stdin);
        freopen("DAUCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        long long a, b;
        cin >> a >> b;
        vector<long long> d(1, 1);          // số lớn, mỗi ô 9 chữ số
        const long long BASE = 1000000000;
        for (long long k = 0; k < b; k++) { // nhân b lần với a
            long long c = 0;
            for (size_t i = 0; i < d.size(); i++) {
                long long t = d[i] * a + c;
                d[i] = t % BASE;
                c = t / BASE;
            }
            if (c > 0) d.push_back(c);
        }
        // viết a^b thành xâu rồi cắt 3 chữ số đầu, 3 chữ số cuối
        string s = to_string(d.back());
        for (int i = (int)d.size() - 2; i >= 0; i--) {
            string part = to_string(d[i]);
            s += string(9 - part.size(), '0') + part;
        }
        cout << s.substr(0, 3) << " " << s.substr(s.size() - 3) << "\n";
    }
    return 0;
}
