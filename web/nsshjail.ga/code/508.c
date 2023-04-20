#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	char a[8], b[8];
    scanf("%s", a);
    scanf("%s", b);
    int a_val = 0, b_val = 0, i, power = 7;
    for (i = 0; i < 8; i++, power--) {
        if (a[i] == '1')
            a_val += pow(2, power);
        if (b[i] == '1')
            b_val += pow(2, power);
    }
    int ans_val = a_val + b_val;
    printf("%d + %d = %d\n", a_val, b_val, ans_val);
    int ans[8];
    for (i = 7; i >= 0; i--) {
        if (ans_val - pow(2, i) >= 0) {
            ans_val -= pow(2, i);
            ans[i] = 1;
        } else {
            ans[i] = 0;
        }
    }
    for (i = 7; i >= 0; i--) {
        printf("%d", ans[i]);
    }
    return 0;
}
