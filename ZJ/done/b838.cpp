#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    ouo;
    int n, count;
    string s;
    cin >> n;
    while (n--) {
        cin >> s;
        stack<int> stk;
        count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!stk.empty() && stk.top() == '(' && s[i] == ')') {
                stk.pop();
                count++;
            } else {
                stk.push(s[i]);
            }
        }
        if (!stk.empty()) count = 0;
        cout << count << endl;
    }
    return 0;
}
