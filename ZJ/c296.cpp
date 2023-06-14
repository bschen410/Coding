#include <iostream>
using namespace std;

int main() {
    int N, M, K;
    while (cin >> N >> M >> K) {
        int ans = 0;
        for (int i = N-K+1; i <= N; i++)
            ans = (ans + M) % i;
        cout << ans + 1 << endl;
    }
}
