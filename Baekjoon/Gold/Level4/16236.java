import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int[] DY = {-1, 0, 1, 0};
    private static final int[] DX = {0, -1, 0, 1};

    private static int N;
    private static int fishCount = 0;
    private static int[][] fish;

    public static void main(String[] args) throws IOException {
        List<Item> queue = init();
        PriorityQueue<Item> priorityQueue = new PriorityQueue<>();

        int answer = 0;
        int eat = 0;
        while (!queue.isEmpty() && fishCount != 0) {
            Item item = queue.remove(0);
            for (int i = 0; i < 4; i++) {
                int moveY = item.y + DY[i];
                int moveX = item.x + DX[i];
                int size = item.size;
                if (moveY < 0 || moveY >= N || moveX < 0 || moveX >= N
                    || fish[moveY][moveX] > size || item.visited[moveY][moveX]) {
                    continue;
                }
                item.visited[moveY][moveX] = true;
                if (fish[moveY][moveX] != 0 && fish[moveY][moveX] != item.size) {
                    priorityQueue.add(new Item(moveY, moveX, size, item.time + 1, item.visited));
                } else {
                    queue.add(new Item(moveY, moveX, size, item.time + 1, item.visited));
                }

            }
            if (!priorityQueue.isEmpty() && queue.isEmpty()) {
                Item nextItem = priorityQueue.peek();
                eat++;
                fishCount--;
                fish[nextItem.y][nextItem.x] = 0;
                answer = nextItem.time;
                int size = nextItem.size;
                if (eat == size) {
                    size++;
                    eat = 0;
                }
                boolean[][] visited = new boolean[N][N];
                visited[nextItem.y][nextItem.x] = true;
                queue.add(new Item(nextItem.y, nextItem.x, size, nextItem.time, visited));
                priorityQueue.clear();
            }
        }
        System.out.println(answer);
    }

    private static List<Item> init() throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        fish = new int[N][N];
        List<Item> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int j = 0; j < N; j++) {
                int number = Integer.parseInt(stringTokenizer.nextToken());
                if (number == 9) {
                    queue.add(new Item(i, j, 2, 0, new boolean[N][N]));
                    number = 0;
                } else if (number != 0) {
                    fishCount++;
                }
                fish[i][j] = number;
            }
        }
        return queue;
    }

    private static class Item implements Comparable<Item> {

        private final int y;
        private final int x;
        private final int size;
        private final int time;
        private final boolean[][] visited;

        public Item(int y, int x, int size, int time, boolean[][] visited) {
            this.y = y;
            this.x = x;
            this.size = size;
            this.time = time;
            this.visited = visited;
        }

        @Override
        public int compareTo(Item o) {
            if (time < o.time) {
                return -1;
            }
            if (time == o.time) {
                if (y < o.y) {
                    return -1;
                }
                if (y == o.y && x < o.x) {
                    return -1;
                }
            }
            return 1;
        }
    }
}
