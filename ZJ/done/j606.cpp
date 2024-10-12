#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
using namespace std;

int main() {
    ouo;
    int k, q, r;
    cin >> k >> q >> r;
    char c[q+1][k+1];
    cin >> c[0];
    for (int i = 1; i <= q; i++) {
        for (int j = 1; j <= k; j++) {
            int pos;
            cin >> pos;
            c[i][pos-1] = c[i-1][j-1];
        }
    }
    // for (int i = 1; i <= q; i++)
    //     for (int j = 1; j <= k; j++)
    //         cout << c[i][j-1] << " ";
    for (int i = 0; i < r; i++) {
        for (int j = 1; j <= q; j++) {
            cout << c[j][i];
        }
        cout << "\n";
    }
    return 0;
}
