#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int n, min = INT_MAX;
    cin >> n;
    int arr[n];
    for (int s = 0; s < n; s++) {
        cin >> arr[s];
        if (arr[s] < min) {
            min = arr[s];
        }
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
        result += arr[i];
    }
    result -= min;
    cout << result << endl;
    return 0;
}
