#	Cálculo do factorial dun nÃºmero
#
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


[int]$num=Read-Host "Introduce un número "
$r=1
Write-Host "Calculando $num!.... "

while ( $num -gt 0 ) {
 $r=$r*$num
 $num=$num-1
}
Write-Host "O factorial é $r"
