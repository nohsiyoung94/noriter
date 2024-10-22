package synoh.sec05.exam02;

public class CalculatorExample {

	public static void main(String[] args) {
		
		double result1 = 10 * 10 * Calculator.pi;
		
		int result2 = Calculator.puls(10,5);
		
		int result3 = Calculator.minus(100, 9);
		
		System.out.println("result1 : "+ result1);
		System.out.println("result2 : "+ result2);
		System.out.println("result3 : "+ result3);
	}

}
