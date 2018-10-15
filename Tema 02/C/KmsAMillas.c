/* 
Para instalar o compilador de C: 
	apt-get install gcc

Para compilar o código:
	gcc KmsAMillas.c -o KmsAMillas

Para executar:
	./KmsAMillas

	Escribir un algoritmo que pida un número de Kms e nos visualice o seu valor en millas

  Pedir Kms
  Millas = Kms/1.60934
  Visualizar Millas
*/
#include <stdio.h>

void main() {
	float kms;
	float millas;

	printf("Introduce Kms: ");
	scanf("%f",&kms);
	millas=kms/1.60394;
	printf("%f Kms son %f Millas\n",kms,millas);	
}
