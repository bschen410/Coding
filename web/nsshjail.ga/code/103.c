#include <stdio.h>
#include <stdlib.h>

int main() {
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	
	double total = a + b + c;
	
	printf("%d+%d+%d=%.0f\n", a, b, c, total);
	printf("%.2f", total / 3);
	return 0;
}

