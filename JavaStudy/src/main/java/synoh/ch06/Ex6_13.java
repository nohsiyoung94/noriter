package synoh.ch06;

public class Ex6_13 {
	public static void main(String[] args) {
		
		Car2 c1 = new Car2 ();
		Car2 c2 = new Car2("red" , "manual");
		
		
		System.out.println("c1의 color = " + c1.color + ", gear = " + c1.gear + ",door= " + c1.door  );
		System.out.println("c2의 color = " + c2.color + ", gear = " + c2.gear + ",door= " + c2.door  );
	}
}


class Car2 {
	String color;
	String gear;
	int door;
	
	Car2(){
		this("white" , "zzzzz" , 4);
		
	}
	Car2(String color , String gear){
		this ( color, gear ,  4);	
	}
	Car2(String color, String gear , int door){
		this.color = color;
		this.gear = gear;
		this.door = door;
	}
}