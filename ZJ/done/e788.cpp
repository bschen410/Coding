#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

struct stu {
    string id;
    string name;
    int order;
};

bool cmp(stu x, stu y) {
    if (x.id[8] == y.id[8]) {
        if (x.id[0] == y.id[0]) {
            return x.order < y.order;
        } else {
            return x.id[0] < y.id[0];
        }
    } else {
        return x.id[8] < y.id[8];
    }
}

int n;

int main() {
    cin >> n;
    stu p[101];
    for (int s = 0; s < n; s++) {
        cin >> p[s].id >> p[s].name;
        p[s].order = s;
    }
    sort(p, p+n, cmp);
    for (int i = 0; i < n; i++)
        cout << p[i].id[8] << ": " << p[i].name << endl;
    return 0;
}
