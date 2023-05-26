#include <bits/stdc++.h>
#include <iostream>
#include <string>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
using namespace std;

struct student{
    string id; // 學號
    string name; // 姓名
    string campus; // 學院
    string degree; // 學位
    int order; // 報名順序
};

int main() {
    int num = 0;
    cin >> num;
    student stu[num];
    for (int i = 0; i < num; i++) {
        cin >> stu[i].id >> stu[i].name;
        stu[i].campus = stu[i].id[8];
        stu[i].degree = stu[i].id[1];
        stu[i].order = i;
    }

    for (int i = 0; i < num; i++) { // test
        cout << stu[i].id << " " << stu[i].name << stu[i].campus << " " << stu[i].degree << " " << stu[i].order;
    }
    int degree[3] = {4, 6, 8};
    for (int i = 65; i <= 90; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < num; k++) {
                for (int l = 0; l < num; l++)
                if (stu[l].campus == (char)i && stu[l].degree == degree[j]) {
                    cout << stu[l].id << " " << stu[l].name << endl;
                }
            }
        }
    }
    return 0;
}
