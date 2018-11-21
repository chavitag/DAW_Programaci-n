#/usr/bin/python
# -*- coding: utf-8 -*-
#
# Pedir M
# suma=0
# c=1
# Mentras c<=M
#    Si (ePrimo(c)) 
#			suma=suma+c;
#	  FinSi
#    c=c+1
# FinMentras
# Visualizar suma
#

def ePrimo(n):
	c=2;
	primo=True;
	while ((c<n) and (n%c!=0)):
		c=c+1
	if (c<n):
		primo=False;
	return primo;


M=int(input("Numero Máximo: "));
suma=0;
c=1;
while(c<=M):
	if (ePrimo(c)):
		suma=suma+c;
	c=c+1;
print("O resultado é "+str(suma));
