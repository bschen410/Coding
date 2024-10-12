#include <stdio.h>
#include <stdlib.h>

int main() {
	int num;
	scanf("%d", &num);
	int i, j;
	switch (num) {
		case 0:
			for (i = 1; i < 6; i++) {
				for (j = 1; j < 6; j++) {
					printf("%d x %d = %d\t", i, j, i * j);
				}
				printf("\n");
			}
			break;
		case 1:
			for (j = 1; j < 6; j++) {
				for (i = 1; i < 6; i++) {
					printf("%d x %d = %d\t", i, j, i * j);
				}
				printf("\n");
			}
			break;
		default:
			printf("error");
	}
}

