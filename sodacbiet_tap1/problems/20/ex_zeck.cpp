#include <bits/stdc++.h>
using namespace std;

// Biểu diễn Zeckendorf: n = tổng các số Fibonacci không kề nhau
int main() {
    long long n;
    cin >> n;
    vector<long long> F = {1, 2};           // F1 = 1, F2 = 2, 3, 5, 8, ...
    while (F.back() <= n - F[F.size() - 2])
        F.push_back(F.back() + F[F.size() - 2]);
    vector<long long> parts;
    for (int i = F.size() - 1; i >= 0 && n > 0; i--)
        if (F[i] <= n) {                    // tham lam: lấy số lớn nhất
            parts.push_back(F[i]);
            n -= F[i];
        }
    for (size_t i = 0; i < parts.size(); i++)
        cout << parts[i] << (i + 1 < parts.size() ? " + " : "\n");
    return 0;
}
