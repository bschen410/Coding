#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

int main() {
    string name = "Department of Mechanical " "Engineering, National " "Taiwan University";
    string name1 = ", ";
    string name2 = "abcd";
    cout << name.find("e", 5)<< endl;
    cout << name.rfind("e", 25) << endl;
    cout << name.rfind("l", 46) << endl;
    cout << name.find_first_of(name1, 5) << endl;
    cout << name.find_last_of(name2, 20) << endl;
    cout << name.find_first_not_of(name1, 15) << endl;
    cout << name.find_last_not_of(name2, 10) << endl;
    return 0;
}
