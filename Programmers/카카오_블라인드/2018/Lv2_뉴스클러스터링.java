import java.util.*;
import java.lang.*;

class Solution {
    
    private static final int NUMBER = 65536;
    
    private final Map<String, Integer> set1 = new HashMap<>();
    private final Map<String, Integer> set2 = new HashMap<>();
    
    public int solution(String str1, String str2) {
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        findSet(str1, set1);
        findSet(str2, set2);
        
        List<String> intersection = findIntersectionSet();
        List<String> union = findUnionSet();
        if (union.isEmpty()) {
            return NUMBER;
        }
        double answer = intersection.size() / (double) union.size();
        return (int) (answer * NUMBER);
    }
    
    private void findSet(String str, Map<String, Integer> set) {
        for (int i = 0; i < str.length() - 1; i++) {
            char first = str.charAt(i);
            char second = str.charAt(i + 1);
            if (isEnglish(first) && isEnglish(second)) {
                String word = first + String.valueOf(second);
                int count = set.computeIfAbsent(word, key -> 0);
                set.put(word, count + 1);
            }
        }
    }
    
    private boolean isEnglish(char c) {
        return c >= 'A' && c <= 'Z';
    }
    
    private List<String> findIntersectionSet() {
        List<String> intersectionSet = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : set1.entrySet()) {
            int size = Math.min(entry.getValue(), set2.getOrDefault(entry.getKey(), 0));
            for (int i = 0; i < size; i++) {
                intersectionSet.add(entry.getKey());
            }
        }
        return intersectionSet;
    }
    
    private List<String> findUnionSet() {
        Set<String> keys = new HashSet<>();
        keys.addAll(set1.keySet());
        keys.addAll(set2.keySet());
        List<String> unionSet = new ArrayList<>();
        for (String key : keys) {
            int size1 = set1.getOrDefault(key, 0);
            int size2 = set2.getOrDefault(key, 0);
            int maxSize = Math.max(size1, size2);
            for (int i = 0; i < maxSize; i++) {
                unionSet.add(key);
            }
        }
        return unionSet;
    }
}
