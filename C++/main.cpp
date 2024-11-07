#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    int a = 13, b = 18;
    (a % 2) && a++;
    (b % 2) && b--;
    cout << a << b;
    return 0;
}
