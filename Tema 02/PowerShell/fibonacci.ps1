[int] $N=Read-Host "Cantos termos queres ver?: "

$t1=1
$t2=1
while ($N -gt 0) {
	Write-Host -NoNewline "$t1 "
	$s=$t1+$t2
	$t1=$t2
	$t2=$s
	$N=$N-1
}
