#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, sum = 0;
        int maximum = INT_MIN;
        cin >> n;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            sum += x;
            maximum = max(maximum, sum);
            if (sum < 0) sum = 0;
        }
        cout << maximum << endl;
    }
    return 0;
}
