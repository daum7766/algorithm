import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int[] GRAPH = new int[101];
    private static final Map<Integer, Integer> LADDER = new HashMap<>();

    public static void main(String[] args) throws IOException {
        init();

        int answer = solution();
        System.out.println(answer);
    }

    private static int solution() {
        List<Item> queue = new LinkedList<>();
        queue.add(new Item(1, 0));
        while (!queue.isEmpty()) {
            Item item = queue.remove(0);
            for (int i = 1; i <= 6; i++) {
                int current = item.getCurrent() + i;
                int count = item.getCount() + 1;
                if (current > 100) {
                    break;
                }
                if (LADDER.containsKey(current)) {
                    current = LADDER.get(current);
                }
                if (current == 100) {
                    return count;
                }
                if (GRAPH[current] == 0 || GRAPH[current] > count) {
                    GRAPH[current] = count;
                    queue.add(new Item(current, count));
                }
            }
        }
        return GRAPH[100];
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        for (int i = 0; i < n + m; i++) {
            stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());
            LADDER.put(start, end);
        }
    }

    private static class Item {

        private final int current;
        private final int count;

        public Item(int current, int count) {
            this.current = current;
            this.count = count;
        }

        public int getCurrent() {
            return current;
        }

        public int getCount() {
            return count;
        }
    }
}
