# Escribir un algoritmo que pida un número de Kms e nos visualice o seu valor en millas
#
# PSEUDOCÓDIGO
#
#  Pedir Kms
#  Millas = Kms/1.60934

[int]$kilometros=Read-Host "Introduce o número de Kms "
[double]$millas=$kilometros/1.60934
Write-Host "$kilometros Kms son $millas Millas"
