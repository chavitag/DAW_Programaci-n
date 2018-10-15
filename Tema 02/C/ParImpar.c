#include <stdio.h>

void main() {
	int n;
	printf("Introduce un número: ");
	scanf("%d",&n);
	if ( n%2 == 0 ) printf("El número %d es par\n",n);
	else				 printf("El número %d es impar\n",n);
}
