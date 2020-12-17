// 패션왕 신해빈
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final HashMap<String, Integer> map = new HashMap<>();
    private static final StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        final int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            map.clear();
            int answer = findCombination();
            sb.append(answer);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static int findCombination() {
        int answer = 1;
        final int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            String item = scanner.next();
            String itemType = scanner.next();
            if (!map.containsKey(itemType)) {
                map.put(itemType, 0);
            }
            map.put(itemType, map.get(itemType) + 1);
        }
        for (String key : map.keySet()) {
            answer *= map.get(key) + 1;
        }
        return answer - 1;
    }
}