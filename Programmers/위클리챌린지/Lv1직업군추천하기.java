import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class Lv1직업군추천하기 {

    public String solution(String[] table, String[] languages, int[] preference) {
        Map<String, Map<String, Integer>> languageValues = new HashMap<>();
        for (String dates : table) {
            String[] date = dates.split(" ");
            Map<String, Integer> languageValue = new HashMap<>();
            for (int i = 1; i < date.length; i++) {
                languageValue.put(date[i] ,6 - i);
            }
            languageValues.put(date[0], languageValue);
        }
        
        Map<String, Integer> userLanguageValue = new HashMap<>();
        int maxValue = 0;
        for (String key : languageValues.keySet()) {
            int value = 0;
            Map<String, Integer> languageValue = languageValues.get(key);
            for (int i = 0; i < languages.length; i++) {
                value += languageValue.getOrDefault(languages[i], 0) * preference[i];
            }
            userLanguageValue.put(key, value);
            maxValue = Math.max(value, maxValue);
        }

        List<String> answerList = new ArrayList<>();
        for (Entry<String, Integer> entry : userLanguageValue.entrySet()) {
            if (entry.getValue() == maxValue) {
                answerList.add(entry.getKey());
            }
        }
        Collections.sort(answerList);

        return answerList.get(0);
    }
}
