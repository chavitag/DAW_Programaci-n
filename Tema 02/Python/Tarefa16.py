#/usr/bin/python
# -*- coding: utf-8 -*-

def squareRoot(x):
    if (x<0):
       raise Exception("Numero Negativo")
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
            error="Infinitas Soluciones"
        else:
            error="Sin Soluciones"
        raise Exception(error)
    return -c/b

def ec2g(a,b,c):
    if (a==0):
        return [ec1g(b,c)]
    radicando=b*b-4*a*c
    if (radicando<0):
        raise Exception("Sin Soluciones Reais")
    sqr=squareRoot(radicando);
    sol1=(-b+sqr)/2*a
    sol2=(-b-sqr)/2*a
    return [sol1,sol2]

tx2=float(input("Termo de x^2: "))
tx=float(input("Termo de x: "))
i=float(input("Termo independente: "));
try:
	print "As solucions son x=: "+str(ec2g(tx2,tx,i))
except Exception as err:
	print err.args[0]
