package synoh.ch06;
public class Ex6_4 {

	public static void main(String[] args) {
		
		MyMath mm = new MyMath();
		long reuslt = mm.max(5,3);
		
		long result1 = mm.add(5L,3L);
		long result2 = mm.subtract(5L,3L);
		long result3 = mm.multiply(5L,3L);
		double result4 = mm.divide(5L,3L);
		mm.printGugudan(2);
		
			
		System.out.println("max(5L,3L) = " + reuslt);
			
			System.out.println("add(5L,3L) = " + result1);
			System.out.println("subtract(5L,3L) = " + result2);
			System.out.println("multiply(5L,3L) = " + result3);
			System.out.println("divide(5L,3L) = " + result4);
	}

}


class MyMath{ // 메서드는 클래스 영역에만 정의 가능하다 .
	
	void printGugudan ( int dan) {
		if (!(2<=dan && dan <=9))
			return ; 	//입력반은 단이 2~9가 아니면, 메서드가 종료하고 돌아가기
		
			for ( int i =1 ; i <= 9 ; i++) {
			System.out.printf("%d * %d = %d%n" , dan , i , dan * i);
			
		}
	}
	long add(long a , long b) {
		long result1 = a+b;
		return result1;
		
	}
	// 두 값을 받아서 둘중에 큰값을 반환하는 메서들 작성하십시오.
	long max(long a, long b ) {
		long result = 0;
		if (a>b) {
			result = a; 	//조건식이 참일때만 실행
		}else {
			result = b;		// 조건식이 거짓일때 실행
		}
		return result;
		
	}
	long subtract(long a, long b) {return a-b;}
	long multiply(long a, long b) {return a*b;}
	double divide(double a, double b) {return a/b;}
	
}