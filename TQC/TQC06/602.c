#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
    char s[50] = {-1};
    int i, count = 0;
    scanf("%s", s);
    for (i = 0; i < sizeof(s); i++) {
        if (isupper(s[i])) {
            printf("%c", s[i]);
            count++;
        }
    }
    printf("\n");
    for (i = 0; i < sizeof(s); i++) {
        if (islower(s[i]))
            printf("%c", s[i]);
    }
    printf("\n");
    printf("%d", count);
    return 0;
}
