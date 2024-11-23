#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int mm[3][3] = {{1, -1, 0}, {1, 0, 1}, {1, 0, 0}};
    int count = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int dir[3][3] = {{1, 1, 0}, {1, 0, 1}, {1, 0, 1}};
            for (int d = 0; d < 2; d++) {
                if (mm[i][j] + dir[i][j] > 1) {
                    count++;
                }
            }
        }
    }
    cout << count << endl;
    return 0;
}
