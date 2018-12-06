#!/bin/bash
#
# Escribir un algoritmo que visualice os factores primos dun número
#
echo "Introduce un número: "
read numero
echo -n "1"
primo=2 
while [ $numero -gt 1 ]; do
	divisible=$((numero%primo))
	if [ $divisible -eq 0 ]; then
		echo -n " $primo"
		numero=$((numero/primo))
	else
		primo=$((primo+1))
	fi
done
