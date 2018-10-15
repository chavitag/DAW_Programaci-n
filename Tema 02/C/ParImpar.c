/* Indica si un número é par ou impar

	Pedir numero
	Si (o resto de dividir o número entre dous é igual a 0) entón 
		visualizar "O Número " numero "é Par"
	Se non 
		visualizar "O Número " numero "é IMPAR"
	Fin-Si
*/
#include <stdio.h>

void main() {
	int n;
	printf("Introduce un número: ");
	scanf("%d",&n);
	if ( n%2 == 0 ) printf("El número %d es par\n",n);
	else				 printf("El número %d es impar\n",n);
}
