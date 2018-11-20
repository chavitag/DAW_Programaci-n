#!/bin/bash
echo "Cantos Alumnos: "
read NC
c=0
while [ $c -lt $NC ]; do
	echo -n "Nome : " 
	read nome[c]
	echo -n "Idade:"
	read idade[c]
	c=$((c+1))
done
echo "------ Consulta de Idades -----"
echo 
echo -n "Nome (FIN para finalizar): "
read nomebuscar;
while [ $nomebuscar != "FIN" ]; do
	c=0;
	# Supoñemos que os nomes non se repiten
	while [ $c -lt $NC ] && [ ${nome[c]} != $nomebuscar ]; do
		c=$((c+1))
	done
	if [ $c -lt $NC ]; then
		echo ${nome[c]} " ten " ${idade[c]} " anos"
	else
		echo "Non se atopa " $nomebuscar 
	fi
	echo -n "Nome (FIN para finalizar): "
	read nomebuscar;
done
