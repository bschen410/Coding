#include <stdio.h>
#include <stdlib.h>

int main() {
	int dice[10];
	int i;
	for (i = 0; i < 10; i++) {
		int input;
		scanf("%d", &input);
		dice[i] = input;
	}
	
	int count[7] = {0};
	for (i = 0; i < 10; i++) {
		switch (dice[i]) {
			case 1:
				count[0]++;
				break;
			case 2:
				count[1]++;
				break;
			case 3:
				count[2]++;
				break;
			case 4:
				count[3]++;
				break;
			case 5:
				count[4]++;
				break;
			case 6:
				count[5]++;
				break;
			default:
				count[6]++;
				break;
		}
	}
	
	for (i = 0; i < 6; i++) {
		printf("number%d:%d\n", i + 1, count[i]);
	}
	printf("error:%d", count[6]);
}

