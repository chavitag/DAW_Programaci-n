/*
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
#			Visualizar "IVE: " tiva
#		Fin Si
#	FinSi
#  FinMentras
*/

#include <stdio.h>
#include <stdlib.h>



void main(void) {
	float total;
	float tneto,neto;
	float tiva,iva;
	int opcion;
	int i,c;
	float ticket[1000];

	total=0;
	tneto=0;
	i=0;
	opcion=0;
	while(opcion != 3) {
		printf("1.- Venta\n");
		printf("2.- Caixa\n");
		printf("3.- Saír\n");
		scanf("%d",&opcion);
		if (opcion==1) {
			if (i==1000) {
				printf("No caben más tickets...\n");
				exit(1);
			}
			printf("Importe?: ");
			scanf("%f",&ticket[i]);
			total=total+ticket[i];
			i=i+1;
		} else if (opcion==2) {
			c=0;
			while(c<i) {
				printf("Ticket %d, Importe Total: %f\n",c,ticket[c]);
				neto=(ticket[c]*100)/121;
				iva=ticket[c]-neto;
				printf("Importe neto %f, IVE: %f\n",neto,iva);
				tneto=tneto+neto;
				tiva=tiva+iva;
				c=c+1;
			}
			printf("\nO Importe total das ventas foi %f\n",total);
			printf("Importe neto %f e IVE: %f\n",tneto,tiva);
		}
	}
	
}

