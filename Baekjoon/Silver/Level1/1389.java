import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final List<List<Integer>> graph = new ArrayList<>();

    private static int N;

    public static void main(String[] args) throws IOException {
        init();

        int answer = solution();
        System.out.println(answer);
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());

        graph.add(new ArrayList<>());
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int index = Integer.parseInt(stringTokenizer.nextToken());
            int value = Integer.parseInt(stringTokenizer.nextToken());
            graph.get(index).add(value);
            graph.get(value).add(index);
        }
    }

    private static int solution() {
        List<Item> queue = new LinkedList<>();
        int minValue = Integer.MAX_VALUE;
        int answer = -1;

        for (int i = 1; i < N + 1; i++) {
            boolean[] visited = new boolean[N + 1];
            visited[i] = true;
            int[] count = new int[1];
            count[0] = 1;
            queue.add(new Item(i, i, visited, count, 1, new int[1]));
        }

        while (!queue.isEmpty()) {
            Item item = queue.remove(0);
            int currentIndex = item.getCurrentIndex();
            List<Integer> ItemGraph = graph.get(currentIndex);
            for (Integer targetNumber : ItemGraph) {
                item.exist(targetNumber);
            }
            if (item.isEnd(N) && minValue > item.getValue()) {
                minValue = item.getValue();
                answer = item.getId();
            }
            queue.addAll(item.nextItems());
        }
        return answer;
    }

    private static class Item {

        private final int id;
        private final int currentIndex;
        private final boolean[] visited;
        private final int[] count;
        private final int depth;
        private final int[] value;
        private final List<Integer> nextIndexes = new LinkedList<>();

        public Item(int id, int currentIndex, boolean[] visited, int[] count, int depth,
            int[] value) {
            this.id = id;
            this.currentIndex = currentIndex;
            this.visited = visited;
            this.count = count;
            this.depth = depth;
            this.value = value;
        }

        public boolean isEnd(int N) {
            return count[0] == N;
        }

        public void exist(int index) {
            if (!visited[index]) {
                visited[index] = true;
                count[0] += 1;
                value[0] += depth;
                nextIndexes.add(index);
            }
        }

        public List<Item> nextItems() {
            List<Item> items = new LinkedList<>();
            for (Integer index : nextIndexes) {
                items.add(new Item(id, index, visited, count, depth + 1, value));
            }
            return items;
        }

        public int getId() {
            return id;
        }

        public int getCurrentIndex() {
            return currentIndex;
        }

        public int getValue() {
            return value[0];
        }
    }
}
