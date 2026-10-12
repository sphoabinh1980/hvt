#include <cstdio>
typedef long long ll;
const char DIG[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int val(char c) { return c <= '9' ? c - '0' : c - 'A' + 10; }

int main() {
    if (fopen("DOICOSO.INP", "r")) {
        freopen("DOICOSO.INP", "r", stdin);
        freopen("DOICOSO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b; char s[105];
        scanf("%d %d %s", &a, &b, s);
        ll v = 0;                        // cơ số a -> giá trị: Horner
        for (int i = 0; s[i]; i++) v = v * a + val(s[i]);
        char r[70]; int len = 0;         // giá trị -> cơ số b
        while (v > 0) {                  // BẪY: v = 0 thì in xâu rỗng
            r[len++] = DIG[v % b];
            v /= b;
        }
        for (int i = len - 1; i >= 0; i--) putchar(r[i]);   // đọc ngược
        putchar('\n');
    }
    return 0;
}
