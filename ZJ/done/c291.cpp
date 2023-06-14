#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int n, ans = 0;
int frd[50001];
bool visit[50001] = {false};

void dfs(int idx) {
    if (visit[frd[idx]] == true) return;
    else {
        visit[frd[idx]] = true;
        dfs(frd[idx]);
    }
}

int main() {
    ouo;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> frd[i];
    for (int i = 0; i < n; i++) {
        if (visit[i] == false) {
            ans++;
            visit[i] = true;
            dfs(i);
        }
    }
    cout << ans << endl;
    return 0;
}
