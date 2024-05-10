#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n;
    cin >> n;
    vector<int> gg[101];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int tmp;
            cin >> tmp;
            if (tmp == 1) {
                gg[j].push_back(i);
            }
        }
    }
    int a, b;
    cin >> a >> b;
    queue<int> todo;
    todo.push(a);
    int step[101];
    memset(step, 0, sizeof(step));
    int idx = 0;
    while (!todo.empty()) {
        int from = todo.front();
        todo.pop();
        for (auto u : gg[from]) {
            if (u == b) {
                step[idx]++;
                idx++;
                cout << step << endl;
                break;
            }
            //
            step[idx]++;
            todo.push(u);
        }
    }
    int ans = INT_MAX;
    for (int i = 0; i < 101; i++) {
        if (step[i] < ans) ans = step[i];
    }
    cout << step[100] << endl;
    return 0;
}
