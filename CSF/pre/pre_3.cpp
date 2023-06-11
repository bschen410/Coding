#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int h = 0, v = 0;
    for (int i = 0; i < s.size(); i++) {
        switch (s[i]) {
            case 'L':
                h--;
                break;
            case 'R':
                h++;
                break;
            case 'U':
                v++;
                break;
            case 'D':
                v--;
                break;
        }
    }
    h = abs(h);
    v = abs(v);
    cout << h + v << endl;
    return 0;
}
