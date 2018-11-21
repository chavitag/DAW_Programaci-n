#!/bin/bash
#
# Temos nunha táboa de 23 elementos as letras T	R	W	A	G	M	Y	F	P	D	X	B	N	J	Z	S	Q	V	H	L	C	K	E
# Pido o numero (sen a letra)
# calculo o resto de dividir entre 23
# visualizo a letra da taboa que está na posición do resto
letras=(T R W A G M Y F P D X B N J Z S Q V H L C K E)
echo -n "Numero DNI: "
read num
resto=$((num%23))
echo "A letra que corresponde a $num é ${letras[$resto]}"
