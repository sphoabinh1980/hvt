#include <bits/stdc++.h>
using namespace std;

// Đếm số đoạn con S[l..r] chia hết cho m, với gcd(m, 10) = 1
int main() {
    string S;
    long long m;
    cin >> S >> m;
    int n = S.size();
    map<long long, long long> cnt;           // số lần gặp mỗi số dư hậu tố
    long long T = 0, p = 1 % m, ans = 0;     // T = S[i..n] mod m, p = 10^(n-i)
    cnt[0] = 1;                              // hậu tố rỗng T[n+1] = 0
    for (int i = n - 1; i >= 0; i--) {
        T = (T + (S[i] - '0') * p) % m;      // thêm chữ số S[i] vào bên trái
        p = p * 10 % m;
        ans += cnt[T];                       // ghép với mọi hậu tố cùng số dư
        cnt[T]++;
    }
    cout << ans << "\n";
    return 0;
}
