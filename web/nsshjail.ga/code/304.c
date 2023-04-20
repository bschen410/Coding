#include <stdio.h>
#include <stdlib.h>

int compute(int arr[]);

int main() {
	int arr[6], i, times = 0;
	for (i = 0; i <= 5; i++) {
		scanf("%d", &arr[i]);
	}
	times = compute(arr);
	printf("%d", times);
}

int compute(int arr[]) {
	int i, times = 0;
	for (i = 0; i <= 5; i++) {
		if (arr[i] % 3 == 0) {
			times++;
		}
	}
	return times;
}
