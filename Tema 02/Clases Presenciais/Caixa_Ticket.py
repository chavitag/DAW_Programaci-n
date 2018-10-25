#!/bin/python
# -*- coding: utf-8 -*-
#
#Programar unha caixa rexistradora: Menú con opcións venta, e peche de caixa. Na opción de venta nos pedirá o
#importe da venta (PVP), e regresará ao menú. Na opción de peche de caixa nos amosará importe de cada venta,
# o IVA e o importe de venta neto (sen IVA), e os totais correspondentes 
#
#  total=0
#  tneto=0
#  tiva=0
#  opcion=0
#  i=0
#  Mentras opcion non sexa 3
#  	Visualizar "1-Venta"
#  	Visualizar "2-Caixa"
#  	Visualizar "3-Sair"
#  	Ler opcion
#	Si opcion == 1
#		Visualizar "Importe: "
#		Ler importe
#		ticket[i]=importe
#		total=total+importe
#		i=i+1		
#	Se non 
#		Si opcion == 2
#			c=0
#			Mientras (c<i)
#			  Visualizar "TICKET " c " Importe Total: " ticket [c]
#			  neto=(ticket[c]*100)/121
#			  iva=ticket[c]-neto
#			  Visualiza "Importe neto: " neto
#			  Visualiza "IVA: " iva
#			  tneto=tneto+neto
#			  tiva=tiva+iva
#			  c=c+1
#			FinMientras		 
#
#			Visualizar "O importe total das ventas foi de " total
#			Visualizar "Importe neto: " tneto
#			Visualizar "IVA: " tiva
#		Fin Si
#	FinSi
#  FinMentras
total=0.0
tneto=0.0
tiva=0.0
opcion=0
i=0
ticket=[]
while(opcion != 3):
	print("1-Venta")
	print("2-Caixa")
	print("3-Sair")
	opcion=int(input("Elixe opción:"))
	if (opcion == 1):
		importe=float(input("Importe:"))
		total=total+importe
		ticket.append(importe)
		i=i+1
	else:
		if (opcion == 2):
			c=0
			while(c<i):
				print("TICKET "+str(c)+" Importe total: "+str(ticket[c]))
				neto=(ticket[c]*100)/121
				iva=ticket[c]-neto
				tneto=tneto+neto
				tiva=tiva+iva
				print("Importe NETO "+str(neto)+" IVA: "+str(iva))
				c=c+1
			print("O importe total das ventas foi de "+str(total))
			print("Importe neto: "+str(tneto))
			print("IVE: "+str(tiva))


