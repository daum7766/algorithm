import java.util.HashMap;
import java.util.Map;

public class Lv1상호평가 {

    public String solution(int[][] scores) {
        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < scores.length; i++) {
            int scoreSum = 0;
            int maxScore = 0;
            int minScore = 100;
            Map<Integer, Integer> scoreMap = new HashMap<>();
            for (int j = 0; j < scores.length; j++) {
                int score = scores[j][i];
                scoreSum += score;
                maxScore = Math.max(maxScore, score);
                minScore = Math.min(minScore, score);
                Integer value = scoreMap.getOrDefault(score, 0) + 1;
                scoreMap.put(score, value);
            }
            int scoreAvg = scoreSum / scores.length;
            if (maxScore == scores[i][i] && scoreMap.get(maxScore) == 1) {
                scoreSum -= maxScore;
                scoreAvg = scoreSum / (scores.length - 1);
            } else if(minScore == scores[i][i] && scoreMap.get(minScore) == 1) {
                scoreSum -= minScore;
                scoreAvg = scoreSum / (scores.length - 1);
            }
            stringBuilder.append(intToGrade(scoreAvg));
        }
        return stringBuilder.toString();
    }

    private String intToGrade(int number) {
        if (number >= 90) {
            return "A";
        }
        if (number >= 80) {
            return "B";
        }
        if (number >= 70) {
            return "C";
        }
        if (number >= 50) {
            return "D";
        }
        return "F";
    }
}
