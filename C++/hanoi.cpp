#include <bits/stdc++.h>
using namespace std;

void hanoi(int n, char from, char to, char tmp) {
    if (n == 1) {
        cout << "Move ring 1 from " << from << " to " << to << "\n";
    } else {
        hanoi(n - 1, from, tmp, to);
        cout << "Move ring " << n << " from " << from << " to " << to << "\n";
        hanoi(n - 1, tmp, to, from);
    }
}

int main() {
    int n;
    while (cin >> n) {
        hanoi(n, 'A', 'C', 'B');
    }
    return 0;
}
