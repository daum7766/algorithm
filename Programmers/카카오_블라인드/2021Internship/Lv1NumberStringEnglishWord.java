import java.util.HashMap;
import java.util.Map;

public class Lv1NumberStringEnglishWord {

    private final Map<String, Integer> wordToNumber = new HashMap<>();

    public int solution(String s) {
        StringBuilder answer = new StringBuilder();
        init();

        StringBuilder wordBuilder = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                answer.append(c);
            } else {
                wordBuilder.append(c);
                String word = wordBuilder.toString();
                if (wordToNumber.containsKey(word)) {
                    answer.append(wordToNumber.get(word));
                    wordBuilder = new StringBuilder();
                }
            }
        }
        String word = wordBuilder.toString();
        if (!"".equals(word)) {
            answer.append(wordToNumber.get(word));
        }
        return Integer.parseInt(answer.toString());
    }

    private void init() {
        wordToNumber.put("zero", 0);
        wordToNumber.put("one", 1);
        wordToNumber.put("two", 2);
        wordToNumber.put("three", 3);
        wordToNumber.put("four", 4);
        wordToNumber.put("five", 5);
        wordToNumber.put("six", 6);
        wordToNumber.put("seven", 7);
        wordToNumber.put("eight", 8);
        wordToNumber.put("nine", 9);
    }

}
