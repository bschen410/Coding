#include <stdio.h>
#include <stdlib.h>

int compute(int arr[]);

int main() {
	int arr[3], i;
	for (i = 0; i < 3; i++) {
		scanf("%d", &arr[i]);
	}
	printf("%d", compute(arr));
}

int compute(int arr[]) {
	int ans;
	switch (arr[1]) {
		case 1:
			ans = arr[0] + arr[2];
			break;
		case 2:
			ans = arr[0] * arr[2];
			break;
	}
	return ans;
}

