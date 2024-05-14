#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
using namespace std;

int n;
int h, w;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int cnt[26] = {0};

bool cmp(pair<char, int> p1, pair<char, int> p2) {
    if (p1.second == p2.second) return p1.first < p2.first;
    return p1.second > p2.second;
}

void bfs(char world[1000][1000]) {
    queue<pair<int, int> > q;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (world[i][j] != '0') {
                q.push(make_pair(i, j));
                cnt[(int)world[i][j] - 97]++;
                while (!q.empty()) {
                    pair<int, int> now = q.front();
                    q.pop();

                    char crt = world[now.first][now.second];

                    // for (int x = 0; x < h; x++) {
                    //     for (int y = 0; y < w; y++) {
                    //         cout << world[x][y] << " ";
                    //     }
                    //     cout << "\n";
                    // }
                    // cout << "\n";

                    world[now.first][now.second] = '0';
                    for (int k = 0; k < 4; k++) {
                        if (crt == world[now.first + dx[k]][now.second + dy[k]] && crt != '0') {
                            q.push(make_pair(now.first + dx[k], now.second + dy[k]));
                        }
                    }
                }
            }
        }
    }
    return;
}

int main() {
    ouo;
    cin >> n;
    for (int s = 0; s < n; s++) {
        // init
        for (int i = 0; i < 26; i++) cnt[i] = 0;
        char world[1000][1000] = {'0'};
        cin >> h >> w;
        for (int i = 0; i < h; i++) {
            cin >> world[i];
        }
        bfs(world);
        cout << "World #" << s + 1 << "\n";
        vector<pair<char, int> > vec;
        for (int i = 0; i < 26; i++) {
            vec.push_back(make_pair((char)i + 97, cnt[i]));
        }
        sort(vec.begin(), vec.end(), cmp);
        for (int i = 0; i < 26; i++) {
            if (vec[i].second) {
                cout << vec[i].first << ": " << vec[i].second << endl;
            }
        }
    }
    return 0;
}
