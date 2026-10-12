#include <bits/stdc++.h>
using namespace std;

// Đếm số nguyên tố xoay vòng nhỏ hơn N (N <= 10^7)
int main() {
    int N;
    cin >> N;
    int M = 1;
    while (M < N) M *= 10;                  // các số xoay đều < M
    vector<bool> comp(M + 1, false);        // sàng Eratosthenes tới M
    comp[0] = comp[1] = true;
    for (long long i = 2; i * i <= M; i++)
        if (!comp[i])
            for (long long j = i * i; j <= M; j += i) comp[j] = true;
    int cnt = 0;
    for (int x = 2; x < N; x++) {
        if (comp[x]) continue;
        int len = to_string(x).size(), p = 1;
        for (int i = 1; i < len; i++) p *= 10;  // p = 10^(len-1)
        int y = x;
        bool ok = true;
        for (int i = 1; i < len && ok; i++) {
            y = (y % 10) * p + y / 10;      // đưa chữ số cuối lên đầu
            if (comp[y]) ok = false;
        }
        if (ok) cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
