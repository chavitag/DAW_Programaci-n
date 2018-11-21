#/usr/bin/python
# -*- coding: utf-8 -*-
#  suma=0
#  Pedir num
#  num=num-1
#  Mentras num>0
#     Si num e capicua suma=suma+num
#  	num=num-1
#  FinMentras


#
#  Consideramos capicúas os números de 1 díxito
#	
def eCapicua(num):
	num1=0
	bknum=num
	while (bknum>0):
		num1=(num1*10)+(bknum%10)
		bknum=bknum/10
	return (num==num1)
#------------------------------------------------------

suma=0
n=int(input("Numero: "));
n=n-1
while(n>0):
	if (eCapicua(n)):
		suma=suma+n
	n=n-1
print("A suma é: "+str(suma))

