#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
using namespace std;

int a[5];
int b[5];

int a1() {
    cout << "executing f1\n";
    int max = INT_MIN, idx = 0;
    vector<int> idxs;
    for (int i = 0; i < 5; i++) {
        // cout << "a" << a[i] << " ";
        if (a[i] > max) {
            max = a[i];
            idx = i;
        }
    }
    cout << "array a: ";
    for (int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << "\n";
    cout << "array b: ";
    for (int i = 0; i < 5; i++)
        cout << b[i] << " ";
    cout << "\n";
    for (int i = 0; i < 5; i++) {
        if (a[i] == max) {
            idxs.push_back(i);
            cout << "max: " << i << "\n";
        }
    }
    for (int i = 0; i < idxs.size(); i++) {
        a[idx] /= 2;
    }
    return max;
}

int b1() {
    cout << "executing f1\n";
    int max = INT_MIN, idx = 0;
    vector<int> idxs;
    for (int i = 0; i < 5; i++) {
        // cout << "a" << a[i] << " ";
        if (b[i] > max) {
            max = b[i];
            idx = i;
        }
    }
    cout << "array a: ";
    for (int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << "\n";
    cout << "array b: ";
    for (int i = 0; i < 5; i++)
        cout << b[i] << " ";
    cout << "\n";
    for (int i = 0; i < 5; i++) {
        if (b[i] == max) {
            idxs.push_back(i);
            cout << "max: " << i << "\n";
        }
    }
    for (int i = 0; i < idxs.size(); i++) {
        b[idx] /= 2;
    }
    return max;
}

int a2() {
    cout << "executing f2\n";
    int min = INT_MAX, idx = 0;
    vector<int> idxs;
    for (int i = 0; i < 5; i++) {
        if (a[i] < min && a[i] != 0) {
            min = a[i];
            idx = i;
        }
    }
    cout << "array a: ";
    for (int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << "\n";
    cout << "array b: ";
    for (int i = 0; i < 5; i++)
        cout << b[i] << " ";
    cout << "\n";
    for (int i = 0; i < 5; i++) {
        if (a[i] == min) {
            idxs.push_back(i);
            cout << "min: " << i << "\n";
        }
    }
    for (int i = 0; i < idxs.size(); i++) {
        a[idx]--;
    }
    return min;
}

int b2() {
    cout << "executing f2\n";
    int min = INT_MAX, idx = 0;
    vector<int> idxs;
    for (int i = 0; i < 5; i++) {
        if (b[i] < min && b[i] != 0) {
            min = b[i];
            idx = i;
        }
    }
    cout << "array a: ";
    for (int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << "\n";
    cout << "array b: ";
    for (int i = 0; i < 5; i++)
        cout << b[i] << " ";
    cout << "\n";
    for (int i = 0; i < 5; i++) {
        if (b[i] == min) {
            idxs.push_back(i);
            cout << "min: " << i << "\n";
        }
    }
    for (int i = 0; i < idxs.size(); i++) {
        b[idx]--;
    }
    return min;
}

int main() {
    ouo;
    for (int i = 0; i < 5; i++)
        cin >> a[i];
    for (int i = 0; i < 5; i++)
        cin >> b[i];
    int res = 1;
    while (res) {
        if (res % 2 == 1) {
            if (a[0] % 3 == 0)
                res = a1();
            else
                res = a2();
        } else {
            if (b[0] % 3 == 0)
                res = b1();
            else
                res = b2();
        }
        cout << res << "\n";
    }
    return 0;
}
