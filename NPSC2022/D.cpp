#include <iostream>
using namespace std;

int main() {
    int n, ans = 0;
    cin >> n;
    int arv[n], lev[n], sol[1000001];
    for (int s = 0; s < n; s++)
        cin >> arv[s] >> lev[s];
    for (int s = 0; s < 1000001; s++)
        sol[s] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = arv[i]; j < lev[i]; j++) {
            sol[j]++;
        }
    }
    for (int i = 0; i < 1000001; i++) {
        if (sol[i] > 1) {
            ans += sol[i] - 1;
        }
    }
    cout << ans << endl;
    return 0;
}
