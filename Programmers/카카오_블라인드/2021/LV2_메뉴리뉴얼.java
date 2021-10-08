import java.util.*;
import java.lang.*;

class Solution {

    private final Map<String, Integer> countCourse = new HashMap<>();
    private final Map<Integer, Integer> maxCount = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        for (int courseSize : course) {
            char[] courseList = new char[courseSize];
            for (String order : orders) {
                dfs(0, 0,order, courseList);
            }
        }
        for (Map.Entry<String, Integer> entry : countCourse.entrySet()) {
            int max = maxCount.get(entry.getKey().length());
            if (entry.getValue() == max && entry.getValue() > 1) {
                answer.add(entry.getKey());
            }
        }
        return answer.stream().sorted().toArray(String[]::new);
    }

    private void dfs(int depth, int index, String order, char[] courseList) {
        if (depth == courseList.length) {
            char[] temp = Arrays.copyOf(courseList, courseList.length);
            Arrays.sort(temp);
            String key = String.valueOf(temp);
            int count = countCourse.getOrDefault(key, 0) + 1;
            countCourse.put(key, count);

            int max = maxCount.getOrDefault(courseList.length, 0);
            maxCount.put(courseList.length, Math.max(max, count));
            return;
        }
        for (int i = index; i < order.length(); i++) {
            courseList[depth] = order.charAt(i);
            dfs(depth + 1, i + 1, order, courseList);
        }
    }
}
