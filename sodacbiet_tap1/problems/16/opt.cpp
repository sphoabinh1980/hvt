#include <bits/stdc++.h>
using namespace std;

long long cnt[172][172], nxt[172][172];   // [tổng chữ số][số dư mod s]

int main() {
    if (fopen("HARSHAD.INP", "r")) {
        freopen("HARSHAD.INP", "r", stdin);
        freopen("HARSHAD.OUT", "w", stdout);
    }
    long long N;
    cin >> N;
    string d = to_string(N);
    int L = d.size();
    long long ans = 0;
    for (int s = 1; s <= 9 * L; s++) {    // cố định tổng chữ số s
        // cnt: các tiền tố đã "rời khỏi" N (nhỏ hơn), tự do từ đây
        for (int t = 0; t <= s; t++)
            for (int r = 0; r < s; r++) cnt[t][r] = 0;
        int ts = 0, tr = 0;                // tiền tố đang bám sát N
        for (int i = 0; i < L; i++) {
            for (int t = 0; t <= s; t++)
                for (int r = 0; r < s; r++) nxt[t][r] = 0;
            for (int t = 0; t <= s; t++)
                for (int r = 0; r < s; r++) {
                    long long c = cnt[t][r];
                    if (!c) continue;
                    for (int x = 0; x <= 9 && t + x <= s; x++)
                        nxt[t + x][(r * 10 + x) % s] += c;
                }
            int c = d[i] - '0';            // rời khỏi N tại vị trí i
            for (int x = 0; x < c && ts + x <= s; x++)
                nxt[ts + x][(tr * 10 + x) % s]++;
            ts += c;
            tr = (tr * 10 + c) % s;
            swap(cnt, nxt);
        }
        ans += cnt[s][0];                  // các số < N
        if (ts == s && tr == 0) ans++;     // chính N
    }
    cout << ans << "\n";
    return 0;
}
