#include <stdio.h>
#include <stdlib.h>

int main() {
	int num;
	scanf("%d", &num);
	int i = num - 1;
	int ifPrime = 1;
	while (i > 1) {
		if (num % i == 0) {
			ifPrime = 0;
			break;
		}
		i--;
	}
	// Output
	if (ifPrime == 1) {
		printf("%d is a prime number", num);
	} else if (ifPrime == 0) {
		printf("%d is not a prime number", num);
	}
}

