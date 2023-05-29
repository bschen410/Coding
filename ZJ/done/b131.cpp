#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int N, m;

int main() {
    cin >> N >> m;
    int v[m], w[m];
    for (int s = 0; s < m; s++) {
        cin >> v[s] >> w[s];
    }
    int dp[N+1];
    memset(dp, 0, sizeof(dp));
    for (int i = 0; i < m; i++) {
        for (int j = N; j >= v[i]; j--) {
            dp[j] = max(dp[j], dp[j-v[i]] + v[i] * w[i]);
        }
    }
    cout << dp[N] << endl;
    return 0;
}
