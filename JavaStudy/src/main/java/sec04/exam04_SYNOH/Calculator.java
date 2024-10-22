package sec04.exam04_SYNOH;

public class Calculator {

	//feild 
	//Constructor
	//Method
	
	int plus (int x , int y) {
		int result = x + y;
		return result;
	}
	double avg(int x , int y){
		double sum = plus(x,y);
		double result = sum / 2;
		return result;
	}
	void esecute() {
		double result = avg( 7,10);
		pintln("실행 결과 : " + result);
		
	}
	void pintln(String message) {
		System.out.println(message);
	}
}
