#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int n, k;
bool visit[101];
vector<int> route[101];

int dfs(int from) {
    if (from == n) return 1;
    if (visit[from] == true) return 0;
    visit[from] = true;
    bool result = false;
    for (auto u : route[from]) {
        if (result == false) {
            result = dfs(u);
        }
    }
    return result;
}

int main() {
    ouo;
    while (cin >> n >> k) {
        memset(visit, false, sizeof(visit));
        for (int s = 0; s < 101; s++) route[s].clear();
        for (int s = 0; s < k; s++) {
            int a, b;
            cin >> a >> b;
            route[a].push_back(b);
        }
        if (dfs(0)) {
            cout << "Ok!\n";
        } else {
            cout << "Impossib1e!\n";
        }
    }
    return 0;
}
