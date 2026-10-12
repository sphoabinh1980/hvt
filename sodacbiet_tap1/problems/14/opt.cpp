#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XOACS.INP", "r")) {
        freopen("XOACS.INP", "r", stdin);
        freopen("XOACS.OUT", "w", stdout);
    }
    string s;
    int k;
    cin >> s >> k;
    string st;                               // ngăn xếp: các chữ số giữ lại
    for (char c : s) {
        while (k > 0 && !st.empty() && st.back() > c) {
            st.pop_back();                 // chữ số lớn hơn đứng trước: xóa
            k--;
        }
        st.push_back(c);
    }
    st.resize(st.size() - k);                // còn lượt xóa: bỏ ở cuối
    size_t p = st.find_first_not_of('0');
    cout << (p == string::npos ? "0" : st.substr(p)) << "\n";
    return 0;
}
