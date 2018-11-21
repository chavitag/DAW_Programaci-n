#/usr/bin/python
# -*- coding: utf-8 -*-
#
# Pedir M
# Pedir N
# suma=0
# c=1
# Mentras c<M
#    Si (ePrimo(c)) 
#			suma=suma+potencia(c,N);
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

def potencia(b,e):
	res=1
	while(e>0):
		res=res*b;
		e=e-1;
	return res;

N=int(input("Expoñente: "));
M=int(input("Numero Máximo: "));
suma=0;
c=1;
while(c<M):
	if (ePrimo(c)):
		suma=suma+potencia(c,N);
	c=c+1;
print("O resultado é "+str(suma));
