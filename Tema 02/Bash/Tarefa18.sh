#!/bin/bash
#
# Temos nunha táboa de 23 elementos as letras T	R	W	A	G	M	Y	F	P	D	X	B	N	J	Z	S	Q	V	H	L	C	K	E
# Pido o numero (sen a letra)
# calculo o resto de dividir entre 23
# visualizo a letra da taboa que está na posición do resto
function letraDNI() {
# En bash, os parámetros das funcións son $1 $2 $3 ... etc
	num=$1
	letras=(T R W A G M Y F P D X B N J Z S Q V H L C K E)
#
#  Mais simple:
#  idx=$((num%23))
#  letra_ok=${letras[$idx]}
#
	letra_ok=${letras[$((num%23))]}
}


echo -n "Numero DNI completo: "
read dni
# Collo os 8 primeiros caracteres (numero)
num=${dni:0:8}
# Collo a letra da posición 9
letra=${dni:8:1}
letraDNI $num
if [ "$letra" == "$letra_ok" ]; then
	echo "Correcto!!!"
else
	echo "Incorrecto!!!"
fi

