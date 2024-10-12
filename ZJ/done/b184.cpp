#include <bits/stdc++.h>
using namespace std;
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)

const int max_v = 100;

int main() {
    ouo;
    int n;
    while (cin >> n) {
        int v[n+1], c[n+1];
        int dp[n+1][max_v+1];
        memset(v, 0, sizeof(v));
        memset(c, 0, sizeof(c));
        memset(dp, 0, sizeof(dp));
        for (int s = 1; s <= n; s++)
            cin >> v[s] >> c[s];
        // dp
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= max_v; j++) {
                if (v[i] > j) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + c[i]);
                }
            }
        }
        cout << dp[n][max_v] << endl;
    }
    return 0;
}
