package sec05.exam01_SYNOH;

public class Car {
	//Field 
	String model;
	int speed;
	
	
	//Constructor
	Car(String model){
		this.model = model;
	}
	
	//Method
	void setSpeed(int speed) {
		this.speed = speed;
		
	}
	
	void run() {
		for ( int i = 10; i <=50; i+=10) {
			this.setSpeed(i);
			System.out.println(this.model + "가 달립니다.(시속 : " + this.speed + "km/h)");
			// 필드값인걸 강조 하기 위해 this 사용
			
		}
			
	}
}
