# Indica si un número é par ou impar
#
#	Pedir numero
#	Si (o resto de dividir o número entre dous é igual a 0) entón 
#		visualizar "O Número " numero "é Par"
#	Se non 
#		visualizar "O Número " numero "é IMPAR"
#	Fin-Si

[int]$num=Read-Host "Introduce un número "
if ($num % 2 -eq 0) {
	Write-Host "O Número $num é PAR"
} else {
	Write-Host "O Número $num é IMPAR"
} 
