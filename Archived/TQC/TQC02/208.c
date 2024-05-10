#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, i, j;
	scanf("%d", &num);
	for (i = 2; i < num; i++) {
		int ifPrime = 1;
		for (j = 2; j < i; j++) {
			if (i % j == 0) {
				ifPrime = 0;
				break;
			}
		}
		if (ifPrime == 1) {
			printf("%d ", i);
		}
	}
}

