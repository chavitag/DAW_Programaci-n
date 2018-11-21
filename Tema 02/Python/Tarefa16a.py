#/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Cada lado dun cadrado é a raíz cadrada da súa area, xa que o área de un cadrado é area=lado*lado
#  o algoritmo se basa en elexir un rectángulo cun área igual ao número do que queremos sacar a raíz cadrada:
#	a=lado1*lado2. Iremos reducindo os lados mantendo o área ata ter un cadrado, a medida do lado é a raíz cadrada
#  area=l1*l2 ==> l1 = area / l2  ---> collemos para empezar l2=area, co que l1 sería area / l2
#  Mentras l1 sexa distinto de l2
#       Reducimos l2  a medida media dos dous lados l2 e l1, (l2+l1)/2 e recalculamos l1..
#
#	funcion raizcadrada(area)
#        error=error máximo que quiera considerar, para no hacer demasiadas iteraciones
#         l2=area
#			 l1=area/l2
#         mentras (l2 > l1 + error)
#            l2=(l1 + l2) / 2
#				 l1=area/l2
#			 finmentras
#			 retornar l2
#  finfuncion
#
#  funcion Ecuacion1grao(b,c)
#     Si (b==0)
#			Si (c==0) 
#				Visualizar "Infinitas Solucións"
#			Senon
#				Visualizar "Sin Solucions"
#			FinSi
#		SeNon
#			Visualizar "A solucion é " -c/b
#		FinSi
#	finfuncion
#
#
#  Pido a,b y c
#	Si a==0
#		Ecuacion1grao(b,c)
#  SiNon
#		Si b*b-4*a*c < 0 
#     	Visualizo "Sin Solucions"
#	   SiNon
#   	   num=raizcadrada(b*b-4*a*c)
#			visualizo "x= " (-b+num)/2*a " e " (-b-num/2*a)
#

def squareRoot(x):
    error=0.000001
    b=x
    a=x/b
    while(b > a+error):
        b=(a+b)/2
        a=x/b
    return b

def ec1g(b,c):
    if (b==0):
        if (c==0): 
           print("Infinitas Soluciones")
        else:
            print("Sin Soluciones")
    else:
        print("A solución é x="+str(-c/b))

def ec2g(a,b,c):
    if (a==0):
        ec1g(b,c)
    else:
       radicando=b*b-4*a*c
       if (radicando<0):
           print("Sin Soluciones Reais")
       else:
           sqr=squareRoot(radicando);
           sol1=(-b+sqr)/2*a
           sol2=(-b-sqr)/2*a
           print("As solucións son x="+str(sol1)+" e "+str(sol2))

tx2=float(input("Termo de x^2: "))
tx=float(input("Termo de x: "))
i=float(input("Termo independente: "));
ec2g(tx2,tx,i)
