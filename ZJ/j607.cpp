#include <bits/stdc++.h>
#define ll long long
#define ft first
#define sc second
using namespace std;
ll f(string s) {        // 模擬
    ll cur = 0;         // 紀錄
    vector<ll> mul;     // 紀錄最後有哪些數字需要乘起來
    string num = "";    // 紀錄現在的數字
    string func = "";   // 紀錄 f 函式以便之後整個遞迴下去算
    int cnt = 0;        // 紀錄有幾個括號 （判斷要在什麼時候停下來)
    if (s[0] == 'f') {  // 如果我們現在要處理 f 字串
        ll mn = INT_MAX, mx = 0;
        cnt = 1;                              // 從第二個開始跑
        for (int i = 2; i < s.size(); i++) {  // 所以第一個括號先加上去 (cnt = 1)
            if (s[i] == '(') cnt++;
            if (s[i] == ')') cnt--;                                // 遇到左括號 + 1 右括號 - 1
            if (i == s.size() - 1 || (cnt == 1 && s[i] == ',')) {  // 在這之前的所有括號都匹配完了
                ll tmp = f(num);
                mn = min(mn, tmp);
                mx = max(mx, tmp);
                num = "";
            } else {
                num += s[i];
            }
        }
        return mx - mn;
    } else {
        bool found = false;
        for (int i = 0; i <= s.size(); i++) {
            if (s[i] == 'f' || found) {
                func += s[i];
                found = true;
                if (s[i] == '(') {
                    cnt++;
                } else if (s[i] == ')') {
                    cnt--;
                    if (cnt == 0) {      // f 函數結束
                        cur += f(func);  // 遞迴找到這段的答案
                        func = "";
                        found = false;
                    }
                }
            } else {
                if (i == s.size() || s[i] == '*') {
                    if (!num.empty()) cur += stoi(num);
                    mul.push_back(cur);  // 將數字加進去
                    num = "";
                    cur = 0;
                } else if (s[i] == '+') {
                    if (!num.empty()) cur += stoi(num);  // 將數字加起來
                    num = "";
                } else if ('0' <= s[i] && s[i] <= '9') {
                    num += s[i];
                }
            }
        }
        // 最後在一併把所有數字乘起來
        if (mul.empty())
            return 0;
        else {
            ll ans = 1;
            for (ll x : mul) ans *= x;
            return ans;
        }
    }
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    cout << f(s) << '\n';
}