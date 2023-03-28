#include <iostream>
using namespace std;

int main() {
    int low = 1, hi = 1000;
    for (int s = 0; s < 10; s++) {
        cout << (low + hi) / 2 << endl;
        cout << flush;
        string reply;
        cin >> reply;
        if (reply == "lower") {
            hi = (low + hi) / 2 - 1;
        } else if (reply == "higher") {
            low = (low + hi) / 2 + 1;
        } else if (reply == "correct") {
            return 0;
        }
    }
    return 0;
}
