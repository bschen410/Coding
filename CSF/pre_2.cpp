#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int item[m];
    for (int s = 0; s < m; s++)
        cin >> item[s];
    //
    int max = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            int tmp = item[i] + item[j];
            if (tmp > max && tmp <= n) max = tmp;
        }
    }
    cout << n - max << endl;
    return 0;
}
