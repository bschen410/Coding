#include <stdio.h>
#include <stdlib.h>

int main() {
	char str1[128], str2[128];
	int n, result;
	gets(str1);
	gets(str2);
	scanf("%d", &n);
	if (n <= strlen(str1)) {
		result = strncmp(str1, str2, n);
		if (result > 0)
			printf("%s > %s\n", str1, str2);
		else if (result == 0)
			printf("%s = %s\n", str1, str2);
		else
			printf("%s < %s\n", str1, str2);
	} else {
		printf("error\n");
	}
	return 0;
	// printf("%s", str1);
}
