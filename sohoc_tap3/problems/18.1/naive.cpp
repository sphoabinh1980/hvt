#include <cstdio>
typedef long long ll;

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
        ll v = 0;
        for (int i = 0; s[i]; i++) v = v * a + val(s[i]);   // Horner
        printf("%lld\n", v);            // chỉ đúng khi b = 10
    }
    return 0;
}
