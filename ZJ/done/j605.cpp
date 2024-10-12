#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int n, cnt = 0, sum = 0;
    cin >> n;
    int t[n], s[n];
    int max = INT_MIN, max_t = 0;
    for (int i = 0; i < n; i++) {
        cin >> t[i] >> s[i];
        if (s[i] > max) {
            max = s[i];
            max_t = t[i];
        }
        if (s[i] == -1)
            cnt++;
    }
    int ans = max - n - cnt * 2;
    if (ans < 0) ans = 0;
    cout << ans << " " << max_t << endl;
    return 0;
}
