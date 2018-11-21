#!/bin/bash
# Visualizar “Cantos alumnos? :”
# Ler n_alumnos;
# c=0 // Para a conta dos alumnos
# c_aprobados=0 // Para a conta dos aprobados
# c_suspensos=0 // Para a conta dos suspensos
# suma=0 // Para levar a suma de todas as notas e poder calcular a media
# Mentres (c<n_alumnos)
#   Visualizar “Nome :? “
#   Ler nome[c]; // Cando c vale 0, se almacenará en nome[0], cando valga 1 en nome[1]... etc.
#   Visualizar “Nota:?”
#   Ler nota[c]; // Cando c vale 0 se almacenará en nota[0], cando valga 1 en nome[1]... etc.
#   suma = suma + nota[c]
#   Se (nota[c] >= 5) // Aprobado
#     aprobados[c_aprobados]=c; // Gardo o índice do alumno aprobado
#     c_aprobados=c_aprobados+1 // Teño un alumno aprobado máis
#   Se-Non // Suspenso
#     suspensos[c_suspensos]=c; // Gardo o índice do alumno suspenso
#     c_suspensos=c_suspensos+1 // Teño un alumno suspenso máis
#   Fin-Se
#   c = c + 1 // Contamos un alumno máis
# Fin-Mentres
# Visualizar “A Nota Media é de “ suma/n_alumnos
# Visualizar “Aprobados: “ c_aprobados “, Suspensos: “ c_suspensos
# Visualizar “Lista de Aprobados: “
# c=0 // Conta dos aprobados
# Mentres (c < c_aprobados)
# // en aprobados[c] teño o índice do alumno aprobado
# Visualizar “Nome: “ nome[aprobados[c]] “ --- Nota: “ nota[aprobados[c]]
# c = c + 1 // Seguinte aprobado
# Fin-Mentres
echo -n "Cantos Alumnos?: "
read n_alumnos
c=0
c_aprobados=0
c_suspensos=0
suma=0
#
# Introducimos os datos dos n_alumnos alumnos
#
while [ $c -lt $n_alumnos ]; do
	echo -n "Nome: "
	read nome[$c]
	echo -n "Nota: "
	read nota[$c]
	suma=$((suma+nota[c]))
	if [ ${nota[c]} -ge 5 ]; then
		aprobados[$c_aprobados]=$c
		c_aprobados=$((c_aprobados+1))
	else
		suspensos[$c_suspensos]=$c
		c_suspensos=$((c_suspensos+1))
	fi
	c=$((c+1))
done
#
# Listamos resultados
#
# Bash non divide con decimais, necesitamos unha utilidade externa como bc
# echo "A nota media é " $((suma/n_alumnos))
echo -n "A nota media é "
echo "scale=2; $suma/$n_alumnos" | bc 
echo "Aprobados: $c_aprobados, Suspensos: $c_suspensos"
echo "Lista de Aprobados:"
c=0
while [ $c -lt $c_aprobados ]; do
	idx=${aprobados[c]}
	echo "Nome: ${nome[$idx]} --- Nota: ${nota[$idx]}"
	c=$((c+1))
done

