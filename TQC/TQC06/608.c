#include <stdio.h>
#include <stdlib.h>

int compute(int *data);

int main() {
    int data[10];
    int i;
    for (i = 0; i < 10; i++)
        scanf("%d", &data[i]);
    printf("score = %d", compute(data));
}

int compute(int *data) {
    int i, j, point = 0, base = 0;
    for (i = 0; i < 10; i++) {
        if (base == 0) {
            base += 1;
            base = base << data[i] - 1;
        } else {
            switch (data[i]) {
                case 0:
                    break;
                case 1:
                    base = base << 1;
                    base += 1;
                    break;
                case 2:
                    base = base << 2;
                    base += 2;
                    break;
                case 3:
                    base = base << 3;
                    base += 4;
                    break;
                case 4:
                    base = base << 4;
                    base += 8;
                    break;
                default:
                    break;
            }
        }
    }
    base = base >> 3;
    while (base != 0) {
        if (base & 1) {
            point++;
            base = base >> 1;
        } else {
            base = base >> 1;
        }
    }
    return point;
}
