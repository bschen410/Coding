#include <stdio.h>
#include <stdlib.h>

int main() {
	int s;
	scanf("%d", &s);
	switch (s) {
		case 1:
			printf("one");
			break;
		case 2:
			printf("two");
			break;
		case 3:
			printf("three");
			break;
		case 4:
			printf("four");
			break;
		default:
			printf("error");
	}
}

