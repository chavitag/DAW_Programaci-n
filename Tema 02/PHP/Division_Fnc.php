#!/bin/php
<?php
##
## Función que Realiza a División mediante Restas
##
function divide($dividendo,$divisor,&$cociente,&$resto) {
	$ret=1;
	$signo=1;
	# Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
	if ( $dividendo < 0 ) {
		$signo=-1;
		$dividendo=$dividendo*-1;
	}
	if ( $divisor == 0 ) {
		$ret=0;
	} else {
		##	Si o divisior é negativo, cambia o signo do resultado, facemos o cálculo como si fora positivo
		if ( $divisor < 0 ) {
			$signo=$signo*-1;
			$divisor=$divisor*-1;
		}
   	$cociente=0;
		while ( $dividendo >= $divisor ) {
			$dividendo=$dividendo-$divisor;
			$cociente=$cociente+1;
		}
		$dividendo=$dividendo*$signo;
		$cociente=$cociente*$signo;
		$resto=$dividendo;
	}
	return $ret;
}

##		Programa que calcula a división enteira de dous números
## 
##
echo "Dividendo?: ";
fscanf(STDIN, "%d\n", $dividendo);

echo "Divisor?: ";
fscanf(STDIN, "%d\n", $divisor);

if (divide($dividendo,$divisor,$cociente,$resto) == 0) {
	echo "Non se pode dividir entre 0";
}	else	{
	echo "O resultado é Cociente: $cociente e Resto: $resto";
}
?>
