#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int main() {
	int rx2;
	scanf("%d", &rx2);
	double r = rx2 / 2.0;
	
	printf("%-10d\n", rx2);
	printf("%-10.2f\n", r);
	printf("%-10.4f", r * r * 3.1415);
}

