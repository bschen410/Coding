#include <bits/stdc++.h>
using namespace std;
long long stair[10000][2];
int n, k;
int able = 1;
void tele(int des) {
    for(int i = 0; i < k; i++) {
        if(stair[i][1] == des) {
            tele(stair[i][0]);
        }
    }

    if(des == 0) { //!problem!!
        able = 0;
    }

    cout << des << " ";
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(0);
    while(cin >> n >> k) {
        for(int i = 0; i < k; i++) {
            cin >> stair[i][0] >> stair[i][1];
        }
        tele(n);
        if(able == 0) cout << "Ok!" << endl;
        if(able == 1) cout << "Impossib1e!" << endl;
    }
}
