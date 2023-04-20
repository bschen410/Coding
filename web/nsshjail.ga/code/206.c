#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, j, total = 0;
	scanf("%d%d", &i, &j);
	if (i % 2 == 0) {
		i++;
	}
	for (; i <= j; i += 2) {
		total += i;
	}
	printf("%d", total);
	return 0;
}

