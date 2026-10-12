#include <bits/stdc++.h>
using namespace std;

bool isPal(long long x) {
    long long r = 0;
    for (long long y = x; y > 0; y /= 10) r = r * 10 + y % 10;
    return r == x;
}

bool isPrime(long long x) {
    if (x < 2) return false;
    for (long long d = 2; d * d <= x; d++)
        if (x % d == 0) return false;
    return true;
}

int main() {
    if (fopen("NTDX.INP", "r")) {
        freopen("NTDX.INP", "r", stdin);
        freopen("NTDX.OUT", "w", stdout);
    }
    long long L, R;
    cin >> L >> R;
    long long cnt = 0;
    for (long long x = L; x <= R; x++)
        if (isPal(x) && isPrime(x)) cnt++;   // đối xứng trước: rẻ hơn
    cout << cnt << "\n";
    return 0;
}
