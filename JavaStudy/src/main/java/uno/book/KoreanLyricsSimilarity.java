package src.main.java.uno.book;

public class KoreanLyricsSimilarity {
	private static final List<String> LYRICS_DB = Arrays.asList("그대와 함께한 시간 속에", "널 사랑해 언제나 변치 않아", "이별 후에 남겨진 기억들");

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("가사 일부를 입력하세요: ");
		String userInput = scanner.nextLine();

		printSimilarLyrics(userInput);
	}

	private static void printSimilarLyrics(String input) {
		TreeMap<Integer, List<String>> similarityGroups = new TreeMap<>();

		for (String lyric : LYRICS_DB) {
			int distance = getLevenshteinDistance(input, lyric);
			int commonLength = getLongestCommonSubstringLength(input, lyric);
			int score = -distance * 100 + commonLength;

			similarityGroups.putIfAbsent(score, new ArrayList<>());
			similarityGroups.get(score).add(lyric);
		}

		List<Integer> sortedScores = new ArrayList<>(similarityGroups.descendingKeySet());

		if (sortedScores.isEmpty()) {
			System.out.println("🔹 추천 결과 없음");
			return;
		}

		System.out.println("🔹 가장 추천: " + similarityGroups.get(sortedScores.get(0)));
		if (sortedScores.size() > 1)
			System.out.println("🔹 2차 추천: " + similarityGroups.get(sortedScores.get(1)));
		if (sortedScores.size() > 2)
			System.out.println("🔹 3차 추천: " + similarityGroups.get(sortedScores.get(2)));
	}

	private static int getLevenshteinDistance(String s1, String s2) {
		int len1 = s1.length(), len2 = s2.length();
		int[] prev = new int[len2 + 1], curr = new int[len2 + 1];

		for (int j = 0; j <= len2; j++)
			prev[j] = j;

		for (int i = 1; i <= len1; i++) {
			curr[0] = i;
			for (int j = 1; j <= len2; j++) {
				int cost = (s1.charAt(i - 1) == s2.charAt(j - 1)) ? 0 : 1;
				curr[j] = Math.min(prev[j] + 1, Math.min(curr[j - 1] + 1, prev[j - 1] + cost));
			}
			System.arraycopy(curr, 0, prev, 0, len2 + 1);
		}
		return prev[len2];
	}

	private static int getLongestCommonSubstringLength(String s1, String s2) {
		int len1 = s1.length(), len2 = s2.length();
		int[] prev = new int[len2 + 1], curr = new int[len2 + 1];
		int maxLen = 0;

		for (int i = 1; i <= len1; i++) {
			for (int j = 1; j <= len2; j++) {
				if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
					curr[j] = prev[j - 1] + 1;
					maxLen = Math.max(maxLen, curr[j]);
				} else {
					curr[j] = 0;
				}
			}
			System.arraycopy(curr, 0, prev, 0, len2 + 1);
		}
		return maxLen;
	}
}
