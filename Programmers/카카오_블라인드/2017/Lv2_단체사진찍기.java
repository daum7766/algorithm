import java.util.*;
import java.lang.*;

// 경우의 수 구하기
// 돌면서 조건 확인하기
// 경우의수 대략 4만개(8!)
// 완전탐색 가능

class Solution {
    
    private final int size = 8;
    private final char[] friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    private final boolean[] visited = new boolean[size];
    private char[] position = new char[size];
    private String[] dates;
    private int answer = 0;
    
    public int solution(int n, String[] data) {
        dates = data;
        
        dfs(0);
        
        return answer;
    }
    
    private void dfs(int index) {
        if (index == size) {
            if (validate()) {
                answer++;
            }
            return;
        }
        for (int i = 0; i < size; i++) {
            if (!visited[i]) {
                visited[i] = true;
                position[index] = friends[i];
                dfs(index + 1);
                visited[i] = false;
            }
        }
    }
    
    private boolean validate() {
        for (String data : dates) {
            char source = data.charAt(0);
            int sourceIndex = findIndex(source);
            char target = data.charAt(2);
            int targetIndex = findIndex(target);
            char operator = data.charAt(3);
            int distance = data.charAt(4) - '0';
            
            if (!check(sourceIndex, targetIndex, operator, distance)) {
                return false;
            }
        }
        return true;
    }
    
    private int findIndex(char data) {
        for (int i = 0; i < size; i++) {
            if (position[i] == data) {
                return i;
            } 
        }
        return 0;
    }
    
    private boolean check(int sourceIndex, int targetIndex, char operator, int distance) {
        int current = Math.abs(sourceIndex - targetIndex) - 1;
        if (operator == '=') {
            return current == distance;
        }
        if (operator == '<') {
            return current < distance;
        }
        if (operator == '>') {
            return current > distance;
        }
        return false;
    }
}
