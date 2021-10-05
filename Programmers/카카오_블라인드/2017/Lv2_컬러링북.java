import java.util.*;
import java.lang.*;

class Solution {
    
    private final int[] dy = {0, 0, 1, -1};
    private final int[] dx = {1, -1, 0, 0};
    
    private boolean[][] visited;
    private int[][] picture;
    private int numberOfArea = 0;
    private int maxSizeOfOneArea = 0;
    private int m;
    private int n;
    
    public int[] solution(int m, int n, int[][] picture) {
        this.m = m;
        this.n = n;
        visited = new boolean[m][n];
        this.picture = picture;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    int count = bfs(i, j, picture[i][j]);
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(count, maxSizeOfOneArea);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    private int bfs(int startY, int startX, int number) {
        int count = 0;
        List<Item> items = new LinkedList<>();
        items.add(new Item(startY, startX));
        while (!items.isEmpty()) {
            Item item = items.get(0);
            items.remove(0);
            if (visited[item.y][item.x]) {
                continue;
            }
            visited[item.y][item.x] = true;
            count++;
            for (int i = 0; i < 4; i++) {
                int moveY = item.y + dy[i];
                int moveX = item.x + dx[i];
                if (validateY(moveY) && validateX(moveX) 
                    && !visited[moveY][moveX] && picture[moveY][moveX] == number) {
                    items.add(new Item(moveY, moveX));
                }
            }
        }
        return count;
    }
    
    private boolean validateY(int number) {
        return 0 <= number && number < m;
    }
    
    private boolean validateX(int number) {
        return 0 <= number && number < n;
    }
    
    private static class Item {
        
        private final int x;
        private final int y;
        
        public Item(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
