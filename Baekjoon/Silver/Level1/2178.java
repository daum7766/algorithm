import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static int N;
    private static int M;
    private static String[] numbers;

    public static void main(String[] args) throws IOException {
        String[] temp = BUFFERED_READER.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        numbers = new String[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = BUFFERED_READER.readLine();
        }
        int answer = solution();
        System.out.println(answer);
    }

    private static int solution() {
        boolean[][] visited = new boolean[N][M];
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        List<Item> items = new LinkedList<>();
        items.add(new Item(0, 0, 1));

        while (!items.isEmpty()) {
            Item item = items.remove(0);
            for (int i = 0; i < 4; i++) {
                int moveY = item.getY() + dy[i];
                int moveX = item.getX() + dx[i];
                if (moveX < 0 | moveX >= M | moveY < 0 | moveY >= N) {
                    continue;
                }
                if (numbers[moveY].charAt(moveX) == '0' || visited[moveY][moveX]) {
                    continue;
                }
                visited[moveY][moveX] = true;
                if (moveY == N - 1 && moveX == M - 1) {
                    return item.getCount() + 1;
                }
                items.add(new Item(moveX, moveY, item.getCount() + 1));
            }
        }
        return -1;
    }

    private static class Item {

        private final int x;
        private final int y;
        private final int count;

        public Item(int x, int y, int count) {
            this.x = x;
            this.y = y;
            this.count = count;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getCount() {
            return count;
        }
    }
}
