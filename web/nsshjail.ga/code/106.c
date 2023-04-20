#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int main() {
	int x1, y1, x2, y2;
	scanf("%d", &x1);
	scanf("%d", &y1);
	scanf("%d", &x2);
	scanf("%d", &y2);
	
	double x = pow(x2 - x1, 2);
	double y = pow(y2 - y1, 2);
	double result = sqrt(x+y);
	printf("%.2f", result);
}

