#include <stdio.h>
#include <stdlib.h>

int compute(int);

int main() {
	int num;
	scanf("%d", &num);
	if (compute(num) == 1) {
		printf("%d is a prime number", num);
	} else {
		printf("%d is not a prime number", num);
	}
	return 0;
}

int compute(int num) {
	int i;
	for (i = 2; i < num; i++) {
		if (num % i == 0) {
			return 0;
		}
	}
	return 1;
}
