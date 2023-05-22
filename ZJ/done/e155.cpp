#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n;
    while (cin >> n) {
        if (n == 0) break;
        queue<int> q;
        for (int i = 0; i < n; i++)
            q.push(i + 1);
        cout << "Discarded cards: ";
        for (int i = 0; i < n - 1; i++) {
            cout << q.front();
            if (q.size() != 2) cout << ", ";
            q.pop();
            q.push(q.front());
            q.pop();
        }
        cout << "\nRemaining card: ";
        cout << q.front() << "\n";
    }
    return 0;
}
