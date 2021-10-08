import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        int answer = 0;
        int maxDistance = 1_000_000_000;
        int minDistance = 1;
        while (minDistance <= maxDistance) {
            int avg = (minDistance + maxDistance) / 2;
            int count = 0;
            int temp = 0;
            // 첫돌과의 거리 계산하기
            if (rocks[0] < avg) {
                count++;
                temp += rocks[0];
            }
            for (int i = 1; i < rocks.length; i++) {
                // 계산 끊기
                if (count > n) {
                    break;
                }
                int currentDistance = rocks[i] - rocks[i - 1];
                if (temp != 0) {
                    currentDistance += temp;
                }
                if (currentDistance < avg) {
                    count++;
                    temp = currentDistance;
                } else {
                    temp = 0;
                }
            }
            // 끝돌과 도착점 거리 계산하기
            if (distance - rocks[rocks.length - 1] + temp < avg) {
                count++;
            }
            
            if (count > n) {
                maxDistance = avg - 1;
            } else {
                answer = avg;
                minDistance = avg + 1;
            }
        }
        
        return answer;
    }
}
