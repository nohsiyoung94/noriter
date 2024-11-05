package synoh.ch06;

import java.util.Scanner;

public class Ex4_5 {
	public static void main(String[] args) {
		
		int score = 0 ;
		char grade = ' ', opt = '0' ;
		
		
		System.out.printf("점수를 입력해주세요 >>");
		Scanner scanner = new Scanner(System.in);
		score = scanner.nextInt();
		
		System.out.printf("당신의 점수는 %d입니다. %n" , score);
		
		if (score >= 90) {
			grade = 'A';
			if (95 <= score || score >= 100) {opt = '+';}
			else if (90 <= score || score > 95 ) { opt = '-';}
			}
		else if(score >= 80) {
			grade = 'B';
			if ( 85 <= score || score > 90) {opt = '+';}
			else if (80 <= score || score > 85) {opt = '-';}
			}
		else {
			grade = 'C';
		}
		System.out.printf("당신의 학점은 %c%c입니다. %n ", grade,opt);
	}
}

	

