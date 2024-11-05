package synoh.ch06;

public class Ex4_11 {
	public static void main(String[] args) {
		
		
//		for (int i = 1 ; i<=9 ; i++) {
//			for (int j = 1 ; j <= 9 ; j++ )
//				System.out.println(i+"*" + j + "=" + (i*j));
//			
//		}
//		System.out.println();
		
		for(int i = 10; i>=0; i-- ) {
			for(int j =1 ; j<=i; j++) {
			System.out.print("*");
		}
			System.out.println();

	}
}
}