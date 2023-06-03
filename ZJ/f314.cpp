#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int m, n, sum = 0;
    cin >> m >> n;
    int ex[m][n];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> ex[m][n];
        }
    }
    cout << ex[0][0];
    // int mx = INT_MIN, tmp = 0;
    // for (int i = 0; i < m; i++) {
    //     // mx = INT_MIN;
    //     // tmp = 0;
    //     for (int j = 0; j < n; j++) {
    //         if (tmp < 0) tmp = 0;
    //         tmp += ex[i][j];
    //         cout << "'" << ex[i][j] << "'";
    //         if (tmp > mx) mx = tmp;
    //     }
    //     sum += mx;
    // }
    // cout << sum << endl;
    return 0;
}
