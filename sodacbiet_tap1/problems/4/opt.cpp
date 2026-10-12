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
        long long len = 1, cnt = 9, start = 1;  // nhóm các số có len chữ số
        while (k > len * cnt) {                  // k nằm sau cả nhóm này
            k -= len * cnt;                      // bỏ qua len * cnt chữ số
            len++; cnt *= 10; start *= 10;
        }
        long long num = start + (k - 1) / len;   // số chứa chữ số thứ k
        string s = to_string(num);
        cout << s[(k - 1) % len] << "\n";        // vị trí trong số đó
    }
    return 0;
}
