#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int i[4] = {1,1,0,1}, j = 0;
    for (i[0] = 1; i[0] <= 2; ++i[0]){
        if (i[1] >= 2)
            break;
        for (i[2] = 1; i[2] <= 2; i[2]++){
            for (i[3] = 1; i[3] <= 2; ++i[3]){
                for (j = 0; j < 3; j++)
                    if (j < 2) continue;
                    for (j = 0; j < 3; j++)
                    cout << i[j] << " ";
                    cout << endl;
            }
        }
    }
    return 0;
}
