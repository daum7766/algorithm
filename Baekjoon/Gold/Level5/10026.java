import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int[] DY = {0, 0, 1, -1};
    private static final int[] DX = {1, -1, 0, 0};
    private static boolean[][] visited;
    private static boolean[][] rgVisited;

    private static int N;
    private static String[] rgb;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        rgb = new String[N];
        visited = new boolean[N][N];
        rgVisited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            rgb[i] = BUFFERED_READER.readLine();
        }

        solution();
    }

    private static void solution() {
        int normal = 0;
        int rg = 0;

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (rgb[y].charAt(x) == 'R' || rgb[y].charAt(x) == 'G') {
                    if (!visited[y][x]) {
                        bfs(y, x, false);
                        normal++;
                    }
                    if (!rgVisited[y][x]) {
                        bfs(y, x, true);
                        rg++;
                    }
                } else if (!visited[y][x]) {
                    bfs(y, x, false);
                    normal++;
                    rg++;
                }
            }
        }
        System.out.println(normal + " " + rg);
    }

    private static void bfs(int y, int x, boolean isRgb) {
        List<Item> queue = new LinkedList<>();
        queue.add(new Item(y, x));
        char color = rgb[y].charAt(x);
        boolean[][] currentVisited;
        if (!isRgb) {
            currentVisited = visited;
        } else {
            currentVisited = rgVisited;
        }
        currentVisited[y][x] = true;

        while (!queue.isEmpty()) {
            Item item = queue.remove(0);
            for (int i = 0; i < 4; i++) {
                int moveY = item.y + DY[i];
                int moveX = item.x + DX[i];
                if (moveY < 0 || moveY >= N || moveX < 0 || moveX >= N
                    || currentVisited[moveY][moveX]) {
                    continue;
                }
                if (!isRgb && color != rgb[moveY].charAt(moveX)) {
                    continue;
                }
                if (isRgb && rgb[moveY].charAt(moveX) == 'B') {
                    continue;
                }
                currentVisited[moveY][moveX] = true;
                queue.add(new Item(moveY, moveX));
            }
        }
    }

    private static class Item {

        private final int y;
        private final int x;

        public Item(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
