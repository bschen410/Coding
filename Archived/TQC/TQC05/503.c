#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int x, y, i;
	scanf("%d%d", &x, &y);
	int xx = sqrt(x);
	for (i = 1; i < xx; i++) {
		printf("%.lf\n", pow(i, y));
	}
	return 0;
}

