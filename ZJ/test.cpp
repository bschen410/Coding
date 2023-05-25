#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string s = "eacdb";
    sort(s.begin(), s.end(), less<char>());
    cout << "sort string (increasing):" << endl;
    for (char c : s) {
        cout << c << " ";
    }
    cout << endl;

    return 0;
}
