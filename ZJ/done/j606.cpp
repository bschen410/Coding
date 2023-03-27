#include <iostream>
using namespace std;

int k, q, r;

int main() {
    cin >> k >> q >> r;
    char c[q+1][k];
    cin >> c[0];
    for (int i = 1; i <= q; i++) {
        int arr[k];
        for (int s = 0; s < k; s++)
            cin >> arr[s];
        for (int j = 0; j < k; j++) {
            c[i][arr[j]-1] = c[i-1][j];
        }
    }
    //
    for (int i = 0; i < r; i++) {
        for (int j = 1; j <= q; j++) {
            cout << c[j][i];
        }
        cout << "\n";
    }
    return 0;
}
