#!/bin/php
#
# Pedir N
# conta=1
# Mentras conta <= N
#    Visualizar conta*7
# 	  conta=conta+1
# FinMentras
<?php

echo "Numero?: ";
fscanf(STDIN, "%d\n", $N);
$conta=1;
while($conta<=$N) {
	echo ($conta*7)." ";
	$conta=$conta+1;
}

