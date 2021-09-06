import java.util.HashMap;
import java.util.Map;

public class Lv3JewelryShopping {

    public int[] solution(String[] gems) {
        int start = 0;
        int end = 0;
        int minSize = Integer.MAX_VALUE;
        int gemsCount = 0;

        Map<String, Integer> 보석 = new HashMap<>();
        for (String gem : gems) {
            보석.put(gem, 0);
        }
        int gemTotalSize = 보석.size();

        int currentEnd = 0;
        for (int i = 0; i < gems.length; i++) {
            while (gemsCount != gemTotalSize && currentEnd < gems.length) {
                if (보석.get(gems[currentEnd]) == 0) {
                    gemsCount++;
                }
                보석.put(gems[currentEnd], 보석.get(gems[currentEnd]) + 1);
                currentEnd++;
            }
            if (gemsCount == gemTotalSize && minSize > currentEnd - i) {
                start = i;
                end = currentEnd - 1;
                minSize = currentEnd - i;
            }
            보석.put(gems[i], 보석.get(gems[i]) - 1);
            if (보석.get(gems[i]) == 0) {
                gemsCount -= 1;
            }
        }

        return new int[]{start + 1, end + 1};
    }
}
