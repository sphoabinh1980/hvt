#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUKY.INP", "r")) {
        freopen("CHUKY.INP", "r", stdin);
        freopen("CHUKY.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long n;
        cin >> n;
        unordered_map<long long, long long> pos;  // số dư -> lần gặp đầu
        long long r = 1 % n, i = 0;
        while (r != 0 && !pos.count(r)) {       // chia tay: số dư tiếp theo
            pos[r] = i++;
            r = r * 10 % n;
        }
        if (r == 0) cout << i << " 0\n";           // số thập phân hữu hạn
        else cout << pos[r] << " " << i - pos[r] << "\n";
    }
    return 0;
}
