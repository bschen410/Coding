#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int n, m;
int a[1001], b[1001], r[1001];
int ans = INT_MIN;

void f(int x, int y) {
    int sum = 0;
    while (x < n && y < m) {
        sum += a[x] * b[y];
        ans = max(sum, ans);
        if (sum < 0) sum = 0;
        x++;
        y++;
    }
    // ans = max(sum, ans);
}

void r_f(int x, int y) {
    int sum = 0;
    while (x < n && y < m) {
        sum += a[x] * r[y];
        ans = max(sum, ans);
        if (sum < 0) sum = 0;
        x++;
        y++;
    }
    // ans = max(sum, ans);
}

int main() {
    cin >> n >> m;
    for (int s = 0; s < n; s++) {
        cin >> a[s];
    }
    for (int s = 0; s < m; s++) {
        cin >> b[s];
        r[m-s-1] = b[s];
    }
    for (int i = 0; i < n; i++) {
        f(i, 0);
        r_f(i, 0);
    }
    for (int i = 0; i < n; i++) {
        f(0, i);
        r_f(0, i);
    }
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < m; j++) {
    //         f(i, j);
    //         r_f(i, j);
    //     }
    // }
    cout << ans << endl;
    return 0;
}
