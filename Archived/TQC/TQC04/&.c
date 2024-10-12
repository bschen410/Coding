#include <stdio.h>
int main(void) {
    int b = 2;
    printf("變數 b 的值：%d\n", b);
    printf("變數 b 的記憶體位址：%p\n", &b); //%p為印出地址的16進位表示法
    return 0;
}