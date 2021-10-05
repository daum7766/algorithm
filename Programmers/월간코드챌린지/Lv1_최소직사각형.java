import java.util.*;
import java.lang.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxY = 0;
        int maxX = 0;
        for (int[] size : sizes) {
            if (size[0] >= size[1]) {
                int temp = size[0];
                size[0] = size[1];
                size[1] = temp;
            }
            maxY = Math.max(maxY, size[0]);
            maxX = Math.max(maxX, size[1]);
        }
        return maxY * maxX;
    }
}