#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	
	if (a >= 60 && a < 100) {
		printf("1\n");
	} else {
		printf("0\n");
	}
//	printf("%d\n", 60 <= a && a < 100);
	
	printf("%.2f\n", (b + 1) / 10.);
	
	if (a >= c) {
		printf("%d\n", a);
	} else {
		printf("%d\n", c);
	}
//	printf("%d\n", a >= c ? a : c);
}

