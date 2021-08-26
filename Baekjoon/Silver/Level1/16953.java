import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static long N;
    private static long M;

    public static void main(String[] args) throws IOException {
        init();

        long answer = solution();

        System.out.println(answer);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Long.parseLong(stringTokenizer.nextToken());
        M = Long.parseLong(stringTokenizer.nextToken());
    }

    private static long solution() {
        List<Item> queue = new LinkedList<>();
        Set<Long> visited = new HashSet<>();

        visited.add(N);
        queue.add(new Item(N, 1));

        while (!queue.isEmpty()) {
            Item item = queue.remove(0);
            long value1 = item.value * 2;
            long value2 = item.value * 10 + 1;
            if (validateValue(queue, visited, item, value1)) {
                return item.count + 1L;
            }
            if (validateValue(queue, visited, item, value2)) {
                return item.count + 1L;
            }
        }
        return -1;
    }

    private static boolean validateValue(List<Item> queue, Set<Long> visited, Item item,
        long value) {
        if (value <= 1000000000 && !visited.contains(value)) {
            if (value == M) {
                return true;
            }
            visited.add(value);
            queue.add(new Item(value, item.count + 1));
        }
        return false;
    }

    private static class Item {

        private final long value;
        private final int count;

        public Item(long value, int count) {
            this.value = value;
            this.count = count;
        }
    }
}
