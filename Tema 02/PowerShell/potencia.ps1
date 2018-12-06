[int] $base=Read-Host "Base?: "
[int] $exp=Read-Host "Espoñente?: "

Write-Host  -NoNewline "O resultado de $base elevado a $exp é: "
if ($exp -lt 0) {
	Write-Host  -NoNewline  "1/"
	$exp=$exp*-1
}

$resultado=1
while ($exp -gt 0) {
	$resultado=$resultado*$base
	$exp=$exp-1
}
Write-Host $resultado
