// 토마토
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static int N = 0;
    private static int M = 0;
    private static final Queue<Point> queue = new LinkedList<>();
    private static int[] moveX = {0, 1, 0, -1};
    private static int[] moveY = {1, 0, -1, 0};
    private static final int MOVE_NUMBER = 4;

    public static void main(String[] args) {
        N = scanner.nextInt();
        M = scanner.nextInt();
        int[][] arr = new int[M][N];
        init(arr);
        int count = bfs(arr);
        System.out.println(count);
    }

    private static void init(int[][] arr) {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = scanner.nextInt();
                if (arr[i][j] == 1) {
                    Point point = new Point();
                    point.setPoint(j, i);
                    queue.add(point);
                }
            }
        }
    }

    private static int bfs(int[][] arr) {
        int count = 0;
        while (!queue.isEmpty()) {
            Point tempPoint = queue.poll();
            for (int i = 0; i < MOVE_NUMBER; i++) {
                int dx = tempPoint.getPointX() + moveX[i];
                int dy = tempPoint.getPointY() + moveY[i];
                if (dx >= 0 && dx < N && dy >= 0 && dy < M && arr[dy][dx] == 0) {
                    int day = tempPoint.getDay() + 1;
                    arr[dy][dx] = 1;
                    Point createPoint = new Point();
                    createPoint.setPoint(dx, dy);
                    createPoint.setDay(day);
                    queue.add(createPoint);
                    if (day > count) {
                        count = day;
                    }
                }
            }
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0) {
                    return -1;
                }
            }
        }
        return count;
    }
}


class Point {
    private int x;
    private int y;
    private int day = 0;

    public void setPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getPointX() {
        return x;
    }

    public int getPointY() {
        return y;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public int getDay() {
        return day;
    }
}
