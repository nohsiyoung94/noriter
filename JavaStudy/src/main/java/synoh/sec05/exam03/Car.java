package synoh.sec05.exam03;

public class Car {
	
	int speed;
	
	static void run() {
		Car myCar = new Car();

		myCar.speed=60;

		System.out.println(myCar.speed + "달립니다.");
	}
	public static void main(String[] args) {
		
		Car myCar = new Car(); // 객체
		myCar.speed=60;			// 참조변수
		myCar.run();			// 참조변수
		
	}
}
