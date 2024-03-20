#include <bits/stdc++.h>
#define ouo ios_base::sync_with_stdio(false), cin.tie(0)
#define ll long long
#define db double
#define LENGTH 5
#define NUM_RANGE 100
using namespace std;

int arr[LENGTH];
int ans[LENGTH];
ll times = 0;

void print_array(int *a) {
    for (int t = 0; t < LENGTH; t++) {
        if (t == LENGTH - 1)
            cout << a[t];
        else
            cout << a[t] << ", ";
    }
    cout << "\n";
}

int main() {
    srand(time(NULL));
    for (int t = 0; t < LENGTH; t++) {
        arr[t] = rand() % NUM_RANGE;
        ans[t] = arr[t];
    }
    sort(ans, ans + LENGTH);
    cout << "unsorted: ";
    print_array(arr);
    cout << "sorted: ";
    print_array(ans);

    while (true) {
        bool isCorrect = true;
        for (int i = 0; i < LENGTH; i++) {
            if (arr[i] != ans[i]) {
                isCorrect = false;
                break;
            }
        }
        if (isCorrect) {
            cout << "What a nice monkey!\n";
            break;
        }
        times++;
        random_shuffle(arr, arr + LENGTH);
        if (times == 1) {
            cout << times << " time: ";
        } else {
            cout << times << " times: ";
        }
        print_array(arr);
    }
}