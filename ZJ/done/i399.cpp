#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int cnt[11] = {0};
    int max = 0;
    set<int> st;
    for (int i = 0; i < 3; i++) {
        int tmp;
        cin >> tmp;
        if (!st.count(tmp)) st.insert(tmp);
        cnt[tmp]++;
        if (cnt[tmp] > max) max = cnt[tmp];
    }
    cout << max << " ";
    for (auto it = st.rbegin(); it != st.rend(); it++) cout << *it << " ";
    return 0;
}
