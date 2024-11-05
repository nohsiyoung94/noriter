package synoh.ch06;

public class Ex4_1 {
	public static void main(String[] args) {
		
		
		int score1 = 90;
		int score2 = 80;
		int score3 = 30;
		
		if (score3 >= 90){
			System.out.println("90점 이상으로 합격입니다.");
		}else if(score3 >= 80) {
			System.out.println("80점 이상으로 합격입니다. ");
		}else if(score3 <= 60 ) {
			System.out.println("60점 이하로 불합격입니다. ");
		}
		
	}
}
