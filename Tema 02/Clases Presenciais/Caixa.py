#!/bin/python
# -*- coding: utf-8 -*-
#
#Programar unha caixa rexistradora: Menú con opcións venta, e peche de caixa. Na opción de venta nos pedirá o
#importe da venta (PVP), e regresará ao menú. Na opción de peche de caixa nos amosará importe total das ventas,
# o IVA e o importe de venta neto (sen IVA) 
#
#  total=0
#  opcion=0
#  Mentras opcion non sexa 3
#  	Visualizar "1-Venta"
#  	Visualizar "2-Caixa"
#  	Visualizar "3-Sair"
#  	Ler opcion
#	Si opcion == 1
#		Visualizar "Importe: "
#		Ler importe
#		total = total + importe
#	Se non 
#		Si opcion == 2
#			Visualizar "O importe total das ventas foi de " total
#			neto = (total * 100) / 121
#			Visualizar "Importe neto: " neto
#			Visualizar "IVA: " (neto*21/100)
#		Fin Si
#	FinSi
#  FinMentras
total=0.0
opcion=0
while(opcion != 3):
	print("1-Venta")
	print("2-Caixa")
	print("3-Sair")
	opcion=int(input("Elixe opción:"))
	if (opcion == 1):
		importe=float(input("Importe:"))
		total=total+importe
	else:
		if (opcion == 2):
			print("O importe total das ventas foi de "+str(total))
			neto=(total*100)/121
			print("Importe neto: "+str(neto))
			print("IVE: "+str(neto*21/100))

