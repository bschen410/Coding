#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int m, n;
    cin >> m >> n;
    int dp[m+1][n+1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= m; i++) {
        int input[n], l[n], r[n];
        // memset(l, 0, sizeof(l));
        // memset(r, 0, sizeof(r));
        for (int j = 1; j <= n; j++) {
            cin >> input[j];
        }
        for (int j = 1; j <= n; j++) {
            if (j == 1) l[j] = dp[i-1][j] + input[j];
            else l[j] = max(dp[i-1][j], l[j-1]) + input[j];
        }
        for (int j = n; j >= 1; j--) {
            if (j == n) r[j] = dp[i-1][j] + input[j];
            else r[j] = max(dp[i-1][j], r[j+1]) + input[j];
        }
        for (int j = 1; j <= n; j++) {
            dp[i][j] = max(l[j], r[j]);
        }
    }
    int ans = INT_MIN;
    for (int j = 1; j <= n; j++)
        ans = max(dp[m][j], ans);
    cout << ans << endl;
    return 0;
}
