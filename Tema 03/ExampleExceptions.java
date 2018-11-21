class Ec2Grao {
	private static final double error_max=0.000001;
	private double a;
	private double b;
	private double c;

	// Constructor
	public Ec2Grao(double tx2,double tx,double i) {
		a=tx2;
		b=tx;
		c=i;
	}

	// Método que soluciona a ecuación. Non trata as posibles excepcións, se non que as relanza
	// Si quixera tratar as excepcións, poñería o código do método entre try {} catch(ArithmeticException e) {}
	// 	Lanzo un erro "xenérico".... o polimorfismo permite capturar en main as excepcións apropiadas
	public double[] soluciona() throws Exception {
		double[] solucions;
		double radicando;

		if (a==0) {
			solucions=new double[1]; 	// Unha solución, array de 1 elemento
			solucions[0]=ec1grao(b,c); // Si produce unha excepción, a relanzo...... non a trato aquí
		} else {
			solucions=new double[2]; 	// dúas solucións, array de 2 elementos
			radicando=squareRoot(b*b-4*a*c);	// Si produce unha excepción a relanzo... non a trato aquí
			solucions[0]=(-b+radicando)/(2*a);
			solucions[1]=(-b-radicando)/(2*a);
		}
		return solucions;
	}

	// Métodos auxiliares ----- son privados, non forman parte do Interface da clase
	//		ou sexa, son simples funcións
	//
	// Calcula unha raíz cadrada polo algoritmo babilónico
	private double squareRoot(double radix) throws ArithmeticException {
		double b;
		double a;

		if (radix<0) throw new ArithmeticException("Raiz dun número negativo");
		b=radix;
		a=radix/b;  // En realidade comenza sempre en 1....
		while(b > a+error_max) {
        b=(a+b)/2;
        a=radix/b;
		}
    	return b;
	}

	// Soluciona a ecuación de 1º grao, si é posible
	private double ec1grao(double b,double c) throws ArithmeticException {
		String str_error;
		if (b==0) {
			if (c==0) str_error="Infinitas Solucións";
			else		 str_error="Sin Solucións";
			throw new ArithmeticException(str_error);
		}
		return -c/b;
	}
}

public class ExampleExceptions {
	//  Método Principal
	//			Probar as seguintes execucións:
	//				java ExampleException 
	//				java ExampleException test forzar fallo
	//				java ExampleException 0	0 8
	//				java ExampleException 0 0 0
	//				java ExampleException 0 4 -12
	//				java ExampleException 1 2 10
	//				java ExampleException 2 5 2.25
	public static void main(String args[]) {
		double[] s;
		Ec2Grao ec;

		try {
			if (args.length != 3) throw new Exception("Debes escribir: java ExampleException  coeficienteX²  coeficienteX  termoIndependente");
			ec=new Ec2Grao(Double.parseDouble(args[0]),Double.parseDouble(args[1]),Double.parseDouble(args[2]));
			s=ec.soluciona();
			if (s.length == 1) {
				System.out.printf("E unha ecuación de 1º grao %sx+%s=0, con solución: %f\n",args[1],args[2],s[0]);
			} else {
				System.out.printf("As solucións da ecuación de 2º grao %sx²+%sx+%s=0 son %f e %f\n",args[0],args[1],args[2],s[0],s[1]);
			}
		} catch(ArithmeticException e) {
			System.out.println("ERROR Aritmético: "+e.getMessage());
		} catch(NumberFormatException e) { // Esta excepcion pode producirse ao fallar a conversión de string a número
			System.out.println("Number conversion failure "+e.getMessage());
		} catch(Exception e) {
			System.out.println(e.getMessage());
		} finally {
			// Isto se executa ao final SEMPRE, aínda que se produza un erro (excepcion) antes
			System.out.println("O programa rematou!!!");
		}
		// Isto se executa sempre ANTES do finally, sempre que non se produza antes unha excepción
		System.out.println("Finalizando aplicación....");	
	}
}
