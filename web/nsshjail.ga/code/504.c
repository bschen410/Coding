#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, ori, rev, tmp;
	scanf("%d", &num);
	ori = num;
	while (num != 0) {
		tmp = num % 10;
		rev = rev * 10 + tmp;
		num /= 10;
	}
	if (ori == rev) {
		printf("Yes");
	} else {
		printf("No");
	}
	return 0;
}

