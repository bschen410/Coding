#include <algorithm>
#include <iostream>

using namespace std;

class student {
   public:
    int id;

    string no;

    string name;
};

bool cmp(student i, student j) {
    if (i.no[8] == j.no[8]) {
        if (i.no[0] == j.no[0]) {
            return i.id < j.id;

        }

        else {
            return i.no[0] < j.no[0];
        }

    }

    else {
        return i.no[8] < j.no[8];
    }
}

int main() {
    ios::sync_with_stdio(0);

    cin.tie(0);

    int n;

    string s;

    student a[100];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> a[i].no >> a[i].name, a[i].id = i;
    }

    sort(a, a + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << a[i].no[8] << ": " << a[i].name << endl;
    }
}