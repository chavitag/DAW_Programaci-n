#!/bin/bash
#
#	Determiña cal de dous números é o maior
#
# Pedir num1
# Pedir num2
# Si (num1 >  num2) Visualizar "O maior é " num1
# SeNon	Si (num2 > num1) Visualizar "O maior é " num2
# SeNon Visualizar "Son Iguais"

echo -n "Introduce un número: "
read num1
echo -n "Introduce outro número: "
read num2
if [ $num1 -gt $num2 ]; then
	echo "O maior é " $num1
else
	if [ $num2 -gt $num1 ]; then
		echo "O maior é " $num2
	else
		echo "Son Iguais"

	fi
fi

