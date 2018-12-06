[int]$numero=Read-Host "Introduce un número: "
Write-Host  -NoNewline  "1"
$primo=2 
while ($numero -gt 1) {
	if ($numero % $primo -eq 0) {
		Write-Host  -NoNewline " $primo"
		$numero=$numero/$primo
	} else {
		primo=$primo+1
}
