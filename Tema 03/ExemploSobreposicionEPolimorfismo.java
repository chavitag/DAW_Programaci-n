class Animal {
	public void talk() {
		System.out.println("Os animais non falan");
	}
}

class Can extends Animal {
	public void talk() {
		System.out.println("Guau! Guau!");
	}
}

class Gato extends Animal {
	public void talk() {
		System.out.println("Miau! Miau!");
	}
}

public class ExemploSobreposicionEPolimorfismo {
	// En 'a' se pode almacenar calqueira Animal. E os Can e Gato, SON Animal (extends...)
	public static void testPolimorfismo(Animal a) {
		a.talk(); // O polimorfismo permite tratar os Can, Gatos e Animal de modo apropiado. Si o método está sobreposto determiña cal debe chamar
	}

	public static void main(String[] args) {
		Animal a=new Animal();
		Gato g=new Gato();
		Can c=new Can();

		a.talk(); 	// Visualiza "Os animais non falan"
		c.talk();	// Visualiza "Guau! Guau!", xa que variei o comportamento do método talk de Animal (Sobreposicion)
		g.talk();	// Visualiza "Miau! Miau!", xa que variei o comportamento do método talk de Animal (Sobreposicion)
		testPolimorfismo(a);  // Visualiza "Os animais non falan"
		testPolimorfismo(c);	 // Visualiza "Guau! Guau!"
		testPolimorfismo(g);	 // Visualiza "Miau! Miau!"
	}
}
