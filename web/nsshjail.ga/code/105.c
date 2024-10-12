#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int main() {
	int a, b;
	scanf("%d%d", &a, &b);
	float result = sqrt(a+b);
	printf("result=%.2f", result);
	return 0;
}

