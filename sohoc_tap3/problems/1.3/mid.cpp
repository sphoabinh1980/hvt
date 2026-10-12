#include <iostream>
#include <string>
using namespace std;

int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    long long n, m;
    cin >> n >> m;
    string s;                           // n = 10^7: 68 888 897 kí tự!
    for (long long i = 1; i <= n; i++) s += to_string(i);
    long long r = 0;
    for (char c : s) r = (r * 10 + (c - '0')) % m;  // Horner (Tập 1, Bài 1)
    cout << r << '\n';
    return 0;
}
