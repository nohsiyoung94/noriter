package synoh.ch06;

public class Ex3_14 {
	public static void main(String[] args) {
		
		String str1 = "abc";
		String str2 = new String("abc");
		
		System.out.printf("\"abc\"==\"abc\" ? %b%n", "abc"=="abc");
		System.out.printf("str1==\"abc\" ? %b%n",  str1 =="abc");
		System.out.printf("str2==\"abc\" ? %b%n",  str2 =="abc");
	}
}
