import java.lang.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long maxTime = n * 1_000_000_000L;
        
        long minTime = 1;
        while (minTime <= maxTime) {
            long avg = (maxTime + minTime) / 2;
            long count = 0;
            for (int time : times) {
                count += avg / time;
                if (count >= n) {
                    break;
                }
            }
            if (n <= count) {
                answer = avg;
                maxTime = avg - 1;
            } else {
                minTime = avg + 1;
            }
        }
        return answer;
    }
}
