#!/bin/bash
# Escribir un algoritmo que pida un número de Kms e nos visualice o seu valor en millas
#
# PSEUDOCÓDIGO
#
#  Pedir Kms
#  Millas = Kms/1.60934
#  Visualizar Millas

echo "Introduce un número: "
read kilometros
# Bash non soporta operacións con decimais, debemos usar o comando bc, que é unha "calculadora". 
# a variable scale indica os decimais a utilizar
millas=$(echo "scale=6; $kilometros/1.60934;" | bc)
echo "$kilometros Kms son $millas Millas"
