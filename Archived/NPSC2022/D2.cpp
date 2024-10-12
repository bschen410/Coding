// by Bosi
#include <iostream>
using namespace std;

int main() {
    int n;
    long long ans = 0;
    cin >> n;
    int arv[n], lev[n], sol[1000000] = {0};
    for (int s = 0; s < n; s++)
        cin >> arv[s] >> lev[s];
    for (int i = 0; i < n; i++) {
        for (int j = arv[i]; j < lev[i]; j++) {
            if (sol[j] > 0) ans += sol[j];
            sol[j]++;
        }
    }
    cout << ans << endl;
    return 0;
}
