#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, j;
	char operand;
	scanf("%d%d ", &i, &j);
	scanf("%c", &operand);
	
	switch (operand) {
		case '+':
			printf("%d+%d=%d", i, j, i + j);
			break;
		case '-':
			printf("%d-%d=%d", i, j, i - j);
			break;
		case '*':
			printf("%d*%d=%d", i, j, i * j);
			break;
		case '/':
			printf("%d/%d=%d", i, j, i / j);
			break;
		default:
			printf("error");
			break;
	}
	return 0;
}

