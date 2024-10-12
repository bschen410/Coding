#include <iostream>
#include <vector>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
using namespace std;

int main() {
    ouo;
    int n, m, k, now;
    vector<int> p;
    cin >> n >> m >> k;
    p.clear();
    for (int i = 1; i <= n; i++)
        p.push_back(i);
    now = 0;
    for (int i = 0; i < k; i++) {
        now = (now + m - 1) % p.size();
        p.erase(p.begin() + now);
    }
    now = now % p.size();
    cout << p[now] << endl;
    return 0;
}
