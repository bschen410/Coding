#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int data[n][2];
    for (int s = 0; s < n; s++)
        cin >> data[s][0] >> data[s][1];
    //
    int maxTime = data[0][0], maxScore = data[0][1];
    int error = 0;
    for (int i = 0; i < n; i++) {
        if (data[i][1] == -1) {
            error++;
        }
        if (data[i][1] > maxScore) {
            maxScore = data[i][1];
            maxTime = data[i][0];
        }
        if (data[i][1] == maxScore) {
            if (data[i][0] < maxTime)
                maxTime = data[i][0];
        }
    }
    int sum = maxScore - n - error * 2;
    if (sum < 0) sum  = 0;
    //
    cout << sum << " " << maxTime;
}
