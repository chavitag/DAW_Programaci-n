#/usr/bin/python
# -*- coding: utf-8 -*-
#
#	funcion capicua(num)
#		num1=Darlle a volta a num
#     devolver num1==num
#  finfuncion
#
#  Pedir num
#  Si e capicua visualizar "e Capicua"
#  Se non Visualizar "NON é Capicua"
#  FinSI

#
#  Consideramos capicúas os números de 1 díxito
#	
def eCapicua(num):
	num1=0
	bknum=num
	while (bknum>0):
		num1=(num1*10)+(bknum%10)
		bknum=bknum/10
#
# Si son iguais retorna True, se non False
#
	return (num==num1)

#--------------------------------------------------

n=int(input("Numero: "));
if (eCapicua(n)):
	print("E Capicúa")
else:
	print("Non é Capicúa");
