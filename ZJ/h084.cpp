#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, h, m;
    cin >> n >> h >> m;

    // 初始化柵欄
    vector<int> fence(n, h);

    // 讀入海報信息，更新柵欄高度
    for (int i = 0; i < m; i++) {
        int l, r, x;
        cin >> l >> r >> x;
        for (int j = l - 1; j < r; j++) {
            if (fence[j] > x) {
                fence[j] = x;
            }
        }
    }

    // 計算可張貼的最高高度
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += fence[i] * fence[i];
    }
    cout << sum << endl;

    return 0;
}
