/*
## División mediante Restas
##
## 	Supoñemos que o resultado é positivo
##
signo=1
Visualizar "Dividendo?: "
Pedir dividendo
##
## Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
##
Si (dividendo < 0) 
	signo = -1
	dividendo = -dividendo
Fin-Si
Visualizar "Divisor?: "
Pedir divisor
Si (divisor == 0)
	Visualizar "Non se pode realizar unha división entre 0"
Si-Non
	##
	##	Si o divisior é negativo, cambia o signo do resultado, facemos o cálculo como si fora positivo
	##
	Si (divisor < 0) 
		signo = -signo
		divisor = -divisor
	fin-Si
	cociente = 0
	Mientras dividendo >= divisor
		dividendo = dividendo - divisor
		cociente = cociente + 1
	Fin-Mentras
	##
	##	Axustamos o signo
	##
	dividendo=dividendo*signo
	cociente=cociente*signo
	Visualizar "O resultado é Cociente: " cociente " e Resto: " dividendo
Fin-Si
*/
#include <stdio.h>

void main() {
	int signo=1;
	int dividendo;
	int divisor;
	int cociente;

	printf("Introduce el dividendo: ");
	scanf("%d",&dividendo);
	if (dividendo<0) {
		signo=-1;
		dividendo=-dividendo;
	}
	printf("Introduce el divisor: ");
	scanf("%d",&divisor);
	if (divisor==0) printf("Non se pode realizar unha división entre 0");
	else {
		if (divisor<0) {
			signo=-signo;
			divisor=-divisor;
		}
		cociente=0;
		while(dividendo>=divisor) {
			dividendo=dividendo-divisor;
			cociente=cociente+1;
		}
		dividendo=dividendo*signo;
		cociente=cociente*signo;
		printf("O resultado é Cociente: %d e Resto: %d\n",cociente,dividendo);
	}
}
