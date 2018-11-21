	class DivideEnDos {
		public int divide(int num) {
			return num/2;
		}
		public String[] divide(String txt) {
			String[] mitades=new String[2];  // Defino un array de 2 String
			int sz=txt.length();

			mitades[0]=txt.substring(0,sz/2);
			mitades[1]=txt.substring(sz/2);
			return mitades;
		}
	}

	public class ExemploSobrecarga {
		public static void main(String[] args) {
			DivideEnDos d=new DivideEnDos();
			String texto="Texto para dividir en dos";
			String[] dt;

			System.out.println("18 dividido en 2 é "+d.divide(18));
			System.out.println("'"+texto+"' dividido en 2 é ");
			dt=d.divide(texto);
			System.out.println(dt[0]);
			System.out.println(dt[1]);
		}
	}
