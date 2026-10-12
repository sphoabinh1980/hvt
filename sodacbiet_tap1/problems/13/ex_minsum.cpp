#include <bits/stdc++.h>
using namespace std;

// Số nhỏ nhất có đúng k chữ số và tổng chữ số S (in -1 nếu không có)
string nhoNhat(int k, int S) {
    if (S < 1 || S > 9 * k) return "-1";
    string r(k, '0');
    for (int i = k - 1; i >= 0; i--) {     // tô từ hàng đơn vị sang trái
        int need = (i == 0) ? S : min(9, S - 1);  // chữ số đầu cần >= 1
        r[i] = '0' + need;
        S -= need;
    }
    return r;
}

int main() {
    int k, S;
    while (cin >> k >> S) cout << nhoNhat(k, S) << "\n";
    return 0;
}
