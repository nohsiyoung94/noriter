package synoh.ch06;

public class Ex6_12 {

	public static void main(String[] args) {

		Car c1 = new Car();	//생성자
		c1.color = "white";
		c1.gear = "auto" ;
		c1.door = 4;
		
	
		Car c2 = new Car("white", "auto", 4);
		System.out.println("c1의 color = " + c1.color + " / gear = "+ c1.gear + " / door= "+ c1.door);
		System.out.println("c2의 color = " + c2.color + ",gear ="+c2.gear + " door= "+c2.door);
	
	}	
}


class Car{
	String color ; 
	String gear;
	int door ;
	
	
	Car (){}
	Car(String c, String g, int d){
		color = c;
		gear = g;
		door = d;
	}
}