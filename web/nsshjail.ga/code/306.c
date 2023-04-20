#include <stdio.h>
#include <stdlib.h>

int compute(int num);

int main() {
	int num;
	scanf("%d", &num);
	printf("%d!=%d", num, compute(num));
}

int compute(int num) {
	if (num == 0) {
		return 1;
	}
	if (num >= 1) {
		return num * compute(num-1);
	}
}

