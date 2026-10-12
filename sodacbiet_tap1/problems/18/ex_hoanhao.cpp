#include <bits/stdc++.h>
using namespace std;

// Liệt kê các số hoàn hảo chẵn không vượt quá 2^63 (Euclid–Euler)
bool isPrime(long long x) {
    if (x < 2) return false;
    for (long long d = 2; d * d <= x; d++)
        if (x % d == 0) return false;
    return true;
}

int main() {
    for (int p = 2; p <= 31; p++) {
        long long m = (1LL << p) - 1;       // số Mersenne 2^p - 1
        if (isPrime(m))
            cout << "p = " << p << ": " << (1LL << (p - 1)) * m << "\n";
    }
    return 0;
}
