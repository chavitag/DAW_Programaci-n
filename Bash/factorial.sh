#!/bin/bash
echo "Introduce un número: "
read num
r=1
echo "Calculando " $num"!"

while [[ $num > 0 ]]; do
 r=$(($r*$num))
 num=$(($num-1))
done
echo "El factorial es " $r
