#include <stdio.h>
#include <stdlib.h>

double compute(int arr[]);

int main() {
	double ans;
	int i, arr[6];
	for (i = 0; i < 6; i++) {
		scanf("%d", &arr[i]);
	}
	ans = compute(arr);
	printf("%.3f", ans);
}

double compute(int arr[]) {
	double min = (double)arr[0] / arr[3];
	int i;
	for (i = 1; i < 3; i++) {
		if ((double)arr[i] / arr[i+3] < min) {
			min = (double)arr[i] / arr[i+3];
		}
	}
	return min;
}
