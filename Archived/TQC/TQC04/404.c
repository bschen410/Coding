#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int a[30] = {0};
	char str[50];
	int i, max = 0, max_num;
	scanf("%s", str);
	for (i = 0; i < strlen(str); i++) {
		a[str[i]-97]++;
	}
	max_num = a[0];
	for (i = 1; i < 26; i++) {
		if (a[i] > max_num) {
			max = i;
			max_num = a[i];
		}
	}
	printf("%c\n", max+97);
	printf("%d\n", max_num);
	return 0;
}
