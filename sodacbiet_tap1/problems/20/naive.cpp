#include <bits/stdc++.h>
using namespace std;

bool ok(long long x) {                    // x chỉ có ước nguyên tố 2, 3, 5?
    for (int p : {2, 3, 5})
        while (x % p == 0) x /= p;
    return x == 1;
}

int main() {
    if (fopen("HAMMING.INP", "r")) {
        freopen("HAMMING.INP", "r", stdin);
        freopen("HAMMING.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    long long x = 0;
    for (int k = 0; k < n;) {
        x++;
        if (ok(x)) k++;                     // x là số thứ k
    }
    cout << x << "\n";
    return 0;
}
