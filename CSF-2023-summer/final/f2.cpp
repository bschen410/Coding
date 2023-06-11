#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n, m;
    cin >> n >> m;
    char grid[n+1][m+1];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }
    //
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '#') {
                if (grid[i+1][j] == '.') {
                    ans++;
                    grid[i+1][j] = '@';
                }
                if (grid[i-1][j] == '.') {
                    ans++;
                    grid[i-1][j] = '@';
                }
                if (grid[i][j+1] == '.') {
                    ans++;
                    grid[i][j+1] = '@';
                }
                if (grid[i][j-1] == '.') {
                    ans++;
                    grid[i][j-1] = '@';
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
