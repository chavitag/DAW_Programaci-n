#!/bin/bash

# Nos scripts, as liñas que comenzan por # son comentarios salvo a primeira coa
# admiración que indica qué intérprete se debe utilizar.

#  PSEUDOCÓDIGO
#
#	Visualizar "Introduce un número: "
#	Pedir num
#	r=1
#	Visualizar "Calculando " num "!"
#
#	Mientras num > 0 
#		r = r * num
#		num = num - 1
#	Fin-Mientras
#	Visualizar "El factorial es " r


echo "Introduce un número: "
read num
r=1
echo "Calculando $num! ..."

while [ $num -gt 0 ]; do
# let r=r*num
 r=$((r*num))
# let num=num-1
 num=$((num-1))
done
echo "O factorial é $r"
