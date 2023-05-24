#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int n, k;

int main() {
    ouo;
    while (cin >> n >> k) {
        vector<int> gg[101];
        for (int s = 0; s < k; s++) {
            int a, b;
            cin >> a >> b;
            gg[a].push_back(b);
        }

        queue<int> todo;
        todo.push(0);

        bool visit[101] = {false};
        visit[0] = true;

        bool flag = false;

        while (!todo.empty()) {
            int from = todo.front();
            todo.pop();
            for (auto u : gg[from]) {
                if (!visit[u]) {
                    if (u == n) {
                        cout << "Ok!\n";
                        flag = true;
                        break;
                    }
                    //
                    todo.push(u);
                    visit[u] = true;
                }
            }
            if (flag == true) break;
        }
        if (flag == true) continue;
        cout << "Impossib1e!\n";
    }
    return 0;
}
