#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int grid[n][m];
    int nn[n], mm[m];
    for (int s = 0; s < n; s++)
        cin >> nn[s];
    for (int s = m-1; s >= 0; s--)
        cin >> mm[s];
    memset(grid, 0, sizeof(grid));
    for (int i = 0; i < n; i++)
        grid[i][0] = mm[0] * nn[i];
    for (int i = 0; i < m; i++)
        grid[0][i] = mm[i] * nn[0];
    //
    int max = grid[0][0];
    for (int j = 1; j < m; j++) {
        for (int i = 1; i < n; i++) {
            grid[i][j] = nn[i] * mm[j];
            if (grid[i-1][j-1] > 0)
                grid[i][j] += grid[i-1][j-1];
            if (grid[i][j] > max)
                max = grid[i][j];
        }
    }
    //
    reverse(mm, mm + m);
    memset(grid, 0, sizeof(grid));
    for (int i = 0; i < n; i++)
        grid[i][0] = mm[0] * nn[i];
    for (int i = 0; i < m; i++)
        grid[0][i] = mm[i] * nn[0];
    //
    for (int j = 1; j < m; j++) {
        for (int i = 1; i < n; i++) {
            grid[i][j] = nn[i] * mm[j];
            if (grid[i-1][j-1] > 0)
                grid[i][j] += grid[i-1][j-1];
            if (grid[i][j] > max)
                max = grid[i][j];
        }
    }
    cout << max;
}
