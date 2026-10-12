#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUSOK.INP", "r")) {
        freopen("CHUSOK.INP", "r", stdin);
        freopen("CHUSOK.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long k;
        cin >> k;
        long long x = 1;
        while (true) {                     // đi qua từng số 1, 2, 3, ...
            string s = to_string(x);
            if (k <= (long long)s.size()) {  // chữ số cần tìm nằm trong x
                cout << s[k - 1] << "\n";
                break;
            }
            k -= s.size();                  // bỏ qua cả số x
            x++;
        }
    }
    return 0;
}
