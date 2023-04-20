#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    int av = 0, bv = 0, p = 7, i, ansv;
    char a[8], b[8];
    scanf("%s", a);
    scanf("%s", b);
    for (i = 0; i < 8; i++) {
        if (a[i] == '1')
            av += pow(2, p);
        if (b[i] == '1')
            bv += pow(2, p);
        p--;
    }
    ansv = av + bv;
    printf("%d + %d = %d\n", av, bv, ansv);
    int ans[8];
    for (i = 0; i <= 7; i++) {
        if (ansv >= pow(2, 7-i)) {
            ans[7-i] = 1;
        }
    }
}