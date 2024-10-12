#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, m, i, j;
    scanf("%d%d", &n, &m);
    int arr[n][m];
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            printf("%d", arr[i][j]);
            if (j != m - 1) printf(",");
        }
        printf("\n");
    }
    return 0;
}
