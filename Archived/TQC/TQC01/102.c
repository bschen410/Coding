#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int unit;
	double price = 23.34;
	double total;
	
	scanf("%d", &unit);
	total = price * unit;
	printf("%.2f", total);
}

