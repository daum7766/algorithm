import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean visited[] = new boolean[10];
        for (int number : numbers) {
            visited[number] = true;
        }
        for (int i = 0; i < 10; i++) {
            if (visited[i] == false) {
                answer += i;
            }
        }
        return answer;
    }
}