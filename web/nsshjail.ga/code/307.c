#include <stdio.h>
#include <stdlib.h>

int compute(int arr[]);

int main() {
	int arr[5], i, max;
	for (i = 0; i < 5; i++) {
		scanf("%d", &arr[i]);
	}
	printf("%d", compute(arr));
	return 0;
}

int compute(int arr[]) {
	int k, M;
	M = arr[0];
	for (k = 0; k < 5; k++) {
		if (arr[k] > M) {
			M = arr[k];
		}
	}
	return M;
}

