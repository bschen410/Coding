#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int i, j;
    int a[3][3] = {1, 1, 1, 2};
    int b[3][3] = {2, 1, 1};
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++) {
            if (a[i][j] >= 0&&a[i][j] >= 2)
                continue;
            a[i][j] = i * 2+ j;
            if (b[i][j] >= 2)
            b[i][j] = i * j;
        }
        for (i = 0; i < 3; i++) {
            for (j = i; j < 3; j++) {
                cout << a[i][j] + b[i][j] << " ";
            }
            cout << endl;
        }
    return 0;
}
