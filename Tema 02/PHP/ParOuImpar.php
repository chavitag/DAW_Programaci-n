#!/bin/php
<?php
#
# Indica si un número é par ou impar
#
#	Pedir numero
#	Si (o resto de dividir o número entre dous é igual a 0) entón 
#		visualizar "O Número " numero "é Par"
#	Se non 
#		visualizar "O Número " numero "é IMPAR"
#	Fin-Si

echo "Introduce un número: ";
fscanf(STDIN, "%d\n", $num); // lee numero de teclado

if ( $num % 2 == 0) {
	echo "O Número $num é PAR";
} else {
	echo "O Número $num é IMPAR";
}
?>
