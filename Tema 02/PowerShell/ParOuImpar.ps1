[int]$num=Read-Host "Introduce un número "
if ($num % 2 -eq 0) {
	Write-Host "O Número $num é PAR"
} else {
	Write-Host "O Número $num é IMPAR"
} 
