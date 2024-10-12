#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int soldiers[n][2];
    for (int s = 0; s < n; s++) cin >> soldiers[s][0];
    for (int s = 0; s < n; s++) cin >> soldiers[s][1];
    // sort
    for (int i = n - 1; i > 0; i--) {
        for (int j = 0; j <= i - 1; j++) {
            if (soldiers[j][1] > soldiers[j + 1][1]) {
                int tmp;
                tmp = soldiers[j][1];
                soldiers[j][1] = soldiers[j + 1][1];
                soldiers[j + 1][1] = tmp;
                //
                tmp = soldiers[j][0];
                soldiers[j][0] = soldiers[j + 1][0];
                soldiers[j + 1][0] = tmp;
            }
        }
    }

    // verify
    cout << "verify\n";
    for (int s = 0; s < n; s++) {
        cout << soldiers[s][0] << " ";
        cout << soldiers[s][1] << endl;
    }
    cout << "\n";
    // return 0;

    // start
    int avb[n];
    for (int s = 0; s < n; s++) avb[s] = true;
    for (int i = 0; i < n; i++) {
        avb[i] = false;
        // next day
        for (int j = 0; j <= i + 1; j++) soldiers[j][1]--;
        // how many avb
        int count = 0;
        for (int s = 0; s < n; s++)
            if (avb[s] == true) count += soldiers[s][0];
        cout << count << " ";
        // if complete resting
        for (int j = 0; j < n; j++)
            if (soldiers[j][1] == 0) avb[j] = true;
        // verify
        // for (int s = 0; s < n; s++)
        //     cout << "(" << avb[s] << ")";
        // if (i == 4) {
        //     for (int s = 0; s < 5; s++)
        //         cout << "(" << soldiers[s][1] << ")";
        // }
    }
    // verify
    // for (int s = 0; s < n; s++) {
    //     cout << soldiers[s][0] << " ";
    //     cout << soldiers[s][1] << endl;
    // }
}
