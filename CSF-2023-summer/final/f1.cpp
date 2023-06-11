#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n = 0;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    //
    int ans = INT_MAX;
    for (int i = 0; i < n; i++) {
        int a = 0, b = 0;
        for (int j = 0; j <= i; j++) {
            a += arr[j];
        }
        for (int j = n - 1; j > i; j--) {
            b += arr[j];
        }
        int x = abs(a - b);
        ans = min(ans, x);
    }
    cout << ans << endl;
    return 0;
}
