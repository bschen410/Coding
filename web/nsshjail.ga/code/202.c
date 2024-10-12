#include <stdio.h>
#include <stdlib.h>

int main() {
	int i;
	scanf("%d", &i);
	if (i > 60 && i <= 100) {
		printf("%d", i + 10);
	} else if (i >= 0 && i <= 60) {
		printf("%d", i + 5);
	} else {
		printf("error");
	}
}

