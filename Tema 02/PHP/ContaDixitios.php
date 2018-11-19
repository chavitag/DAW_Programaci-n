#!/bin/php
#
# Pedir numero
# Si (numero == 0) Visualizar 1
# Se non
#   Si (numero < 0)
#     numero=-numero
#   FinSi
#   conta=0
#   Mentras numero>0
#     conta=conta+1
#     numero=numero/10
#   FinMentras
#   Visualizar conta
# FinSi
<?php

echo "Numero?: ";
fscanf(STDIN, "%d\n", $numero);
if ($numero == 0) {
	echo "1 díxito";
} else {
	if ($numero < 0) {
		$numero=-$numero;
	}
	$conta=0;
	while($numero>0) {
		$conta=$conta+1;
		// $numero=$numero/10; En PHP divide con decimais. Non sirve. utilizamos a función intdiv
		$numero=intdiv($numero,10);
	}
	echo "$conta díxitos";
}

?>
