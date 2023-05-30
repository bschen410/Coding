#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int n, M, S;
    cin >> n >> M >> S;
    int c[n], sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> c[i];
        sum += c[i];
    }

    bool h[M + 1] = {false};
    h[0] = true;
    for (int i = 0; i < n; i++) {
        bool check[M + 1] = {false};
        for (int j = 0; j <= M; j++) {
            if (h[j] && !check[j]) {
                // 這裡是預防連續兩位客人占用的房間一樣
                // 所以會扣 6% 的隱藏測資
                if (h[j + c[i]] == true) {
                    continue;
                }
                h[j + c[i]] = true;
                check[j + c[i]] = true;
            }
        }
    }
    // S - (M - sum) 有可能為負數
    // 所以會扣 7% 的隱藏測資
    int x = S - (M - sum);
    if (x < 0) x = 0;
    for (int i = x; i <= M; i++) {
        if (h[i]) {
            cout << i << "\n";
            break;
        }
    }
    return 0;
}
