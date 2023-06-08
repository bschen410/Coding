#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n;
    cin >> n;
    int data[n];
    for (int i = 0; i < n; i++)
        cin >> data[i];
    int l = 0, r = n - 1;
    while (l < r) {
        int min_idx = l;
        for (int i = l + 1; i <= r; i++)
            if (data[i] < data[min_idx])
                min_idx = i;
        int L = 0, R = 0;
        for (int i = l; i < min_idx; i++)
            L += data[i];
        for (int i = r; i > min_idx; i--)
            R += data[i];
        if (L > R) {
            R = min_idx - 1;
        } else {
            L = min_idx + 1;
        }
        cout << min_idx << endl;
        // cout << "L: " << l << " R: " << r << endl;
    }
    cout << data[l] << endl;
    return 0;
}
