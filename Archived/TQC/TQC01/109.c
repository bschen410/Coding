#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int main() {
	int i;
	scanf("%d", &i);
	
	if (i >= 60 && i <= 100) {
		printf("pass\n");
	} else if (i >= 0 && i < 60) {
		printf("fail\n");
	} else {
		printf("error");
		return 0;
	}
	if (i % 2 == 0) {
		printf("even");
	} else if (i % 2 == 1) {
		printf("odd");
	}
}

