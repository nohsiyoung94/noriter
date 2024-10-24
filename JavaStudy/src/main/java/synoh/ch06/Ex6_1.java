package synoh.ch06;

public class Ex6_1 {
	public static void main(String[] args) {
		Tv t;				// Tv 인스턴스를 참조하기위한 참조형 변수 t 선언
		t = new Tv();		// Tv 인스턴스를 생성한다 .
		t.channel = 7;		// tv 인스턴스의 멤버 변수를 channel의 값을 7로 한다 .
		t.channelDown();	// tv 인스턴스의 메서드 channelDown()을 호출한다 .
		System.out.println("현재 채널은 " + t.channel + "입니다.");
		
		
	}

}




class Tv{
	// Tv의 속성 (멤버 변수 )
	String color;
	boolean power;
	int channel;
	

	// Tv의 기능(메서드)
	void power() { power = !power;}
	void channelUp() { ++channel;}
	void channelDown() {--channel;}
}
