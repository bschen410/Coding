#include <stdio.h>
#include <stdlib.h>
#include <math.h> 

int main() {
	double result;
	double a, b, c, d, e, f;
	scanf("%lf%lf%lf%lf%lf%lf", &a, &b, &c, &d, &e, &f);
	result = fabs(a) * floor(b) + pow(c, d) * sqrt(e) + log10(f);
	printf("%.2f\n", result);
	return 0;
}

