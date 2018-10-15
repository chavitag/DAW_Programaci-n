#!/bin/bash
#
# Escribir un algoritmo que visualice os factores primos dun número
#
# Pedir numero
# (O 1 é factor de todos os números)
# Visualizar 1   
# primo=2
# Mientras (numero > 1) 
#	Si (numero % primo == 0) 
#		Visualizar primo
#		numero = numero / primo
#	Si No
#		primo = primo + 1
#	FinSi
# Fin-Mientras
echo -n "Introduce un número: "
read num
texto=$num"=1"
primo=2
while [ $num -gt 1 ]; do
	if [ $(($num%primo)) -eq 0 ]; then
		texto=$texto"*"$primo
		num=$((num/primo))
	else
		primo=$((primo+1))
	fi
done
echo $texto
