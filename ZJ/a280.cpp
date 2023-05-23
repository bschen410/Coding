#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int n, k;

int main() {
    // IO 優化
    ouo;
    while (cin >> n >> k) {
        // input data(Graph)
        vector<int> go_to[105];
        for (int i = 0; i < k; i++) {
            int a, b;
            cin >> a >> b;
            go_to[a].push_back(b);
        }

        bool visit[105] = {false};  // 造訪過後就不用再走了所以用一個 visit 判斷是否走過
        queue<int> todo;            // BFS queue 用來存接下來要走的路
        todo.push(0);               // 一開始的 todo 起點為 0
        visit[0] = true;            // 所以 0 已經走過, 標記為 true
        bool flag = false;          // ?

        // BFS
        while (!todo.empty()) {
            // 取 todo 最前面的值
            int from = todo.front();
            todo.pop();

            // 走訪從第 from 階可以到哪些階梯 (u)
            for (auto u : go_to[from]) {
                // 判斷是否走過 u, 若無, 判斷是否就是目的地(n)
                if (!visit[u]) {
                    if (u == n) {  // 假如是, 退出所有迴圈 (flag 的用意在此)
                        cout << "Ok!\n";
                        flag = true;
                        break;
                    }
                    // 如果不是, 就放進 todo, 同時也將此地視為已走過
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
