import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int[] DY = {1, -1, 0, 0};
    private static final int[] DX = {0, 0, 1, -1};
    private static final List<Item> ITEMS = new ArrayList<>();

    private static int N;
    private static int M;
    private static int[][] grades;

    public static void main(String[] args) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());
        grades = new int[N][M];

        for (int i = 0; i < N; i++) {
            stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int j = 0; j < M; j++) {
                grades[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }

        dfs(0, 0, 0, new ArrayList<>());
        other();

        int answer = solution();
        System.out.println(answer);
    }

    private static void dfs(int depth, int y, int x, List<Point> points) {
        if (depth == 3) {
            Point[] items = new Point[3];
            for (int i = 0; i < 3; i++) {
                items[i] = points.get(i);
            }
            ITEMS.add(new Item(items));
            return;
        }

        for (int i = 0; i < 4; i++) {
            int moveY = y + DY[i];
            int moveX = x + DX[i];
            Point point = new Point(moveY, moveX);
            if (points.contains(point) || Point.D_POINT.equals(point)) {
                continue;
            }
            points.add(new Point(moveY, moveX));
            dfs(depth + 1, moveY, moveX, points);
            points.remove(points.size() - 1);
        }
    }

    private static void other() {
        Point[] points1 = {new Point(0, -1), new Point(1, 0), new Point(0, 1)};
        Point[] points2 = {new Point(0, -1), new Point(-1, 0), new Point(0, 1)};
        Point[] points3 = {new Point(-1, 0), new Point(0, 1), new Point(1, 0)};
        Point[] points4 = {new Point(-1, 0), new Point(0, -1), new Point(1, 0)};

        ITEMS.add(new Item(points1));
        ITEMS.add(new Item(points2));
        ITEMS.add(new Item(points3));
        ITEMS.add(new Item(points4));
    }

    private static int solution() {
        int answer = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                for (Item item : ITEMS) {
                    int sum = grades[y][x];
                    for (int i = 0; i < 3; i++) {
                        int moveY = item.points[i].y + y;
                        int moveX = item.points[i].x + x;
                        if (moveY < 0 || moveY >= N || moveX < 0 || moveX >= M) {
                            sum = -1;
                            break;
                        }
                        sum += grades[moveY][moveX];
                    }
                    if (answer < sum) {
                        answer = sum;
                    }
                }
            }
        }
        return answer;
    }

    private static class Point {

        private static final Point D_POINT = new Point(0, 0);

        private final int y;
        private final int x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }
            Point point = (Point) o;
            return y == point.y && x == point.x;
        }

        @Override
        public int hashCode() {
            return Objects.hash(y, x);
        }
    }

    private static class Item {

        private final Point[] points;

        public Item(Point[] points) {
            this.points = points;
        }
    }
}
