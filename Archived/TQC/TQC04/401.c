#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char str1[10], str2[10];
	scanf("%s", &str1);
	scanf("%s", &str2);
	printf("%d\n", strlen(str1));
	printf("%d\n", strlen(str2));
	printf("%s\n", strcat(str1, str2));
}
