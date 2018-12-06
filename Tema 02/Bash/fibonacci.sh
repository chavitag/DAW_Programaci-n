#!/bin/bash
#
#	Escribir un algoritmo que visualice na pantalla o número de términos da serie de Fibonacci que indique o usuario.
#	A serie de Fibonacci ten a seguinte forma:
#	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
echo "Cantos termos queres ver?: "
read N

t1=1
t2=1
while [ $N -gt 0 ]; do
	echo -n "$t1 ";
	s=$((t1+t2))
	t1=$t2
	t2=$s
	N=$((N-1))
done

