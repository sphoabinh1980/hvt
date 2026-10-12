#include <bits/stdc++.h>
using namespace std;

// Số chữ số của n! = floor(log10(1) + log10(2) + ... + log10(n)) + 1
int main() {
    long long n;
    while (cin >> n) {
        long double s = 0;
        for (long long i = 2; i <= n; i++) s += log10l((long double)i);
        cout << (long long)floorl(s) + 1 << "\n";
    }
    return 0;
}
