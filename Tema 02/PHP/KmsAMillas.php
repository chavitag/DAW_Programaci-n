#!/bin/php

<?php
# Escribir un algoritmo que pida un número de Kms e nos visualice o seu valor en millas
#
# PSEUDOCÓDIGO
#
#  Pedir Kms
#  Millas = Kms/1.60934
#  Visualizar Millas

echo "Introduce un número: ";
fscanf(STDIN, "%d\n", $kms); // lee numero de teclado
$millas=$kms/1.60934;
echo "$kms Kms son $millas Millas";
?>
