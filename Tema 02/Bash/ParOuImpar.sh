# Indica si un número é par ou impar
#
#	Pedir numero
#	Si (o resto de dividir o número entre dous é igual a 0) entón 
#		visualizar "O Número " numero "é Par"
#	Se non 
#		visualizar "O Número " numero "é IMPAR"
#	Fin-Si
echo "Introduce un número: "
read num
# let par=num%2
par=$((num%2))
if [ $par -eq 0 ]; then
	echo "O Número $num é PAR"
else
	echo "O Número $num é IMPAR"
fi
