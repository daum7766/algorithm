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
    private static final int[] DZ = {0, 0, 0, 0, 1, -1};
    private static final int[] DY = {1, -1, 0, 0, 0, 0};
    private static final int[] DX = {0, 0, 1, -1, 0, 0};
    private static final List<List<List<Integer>>> TOMATOES = new ArrayList<>();
    private static final List<Item> QUEUE = new LinkedList<>();

    private static int N;
    private static int M;
    private static int H;
    private static int tomatoCount = 0;

    public static void main(String[] args) throws IOException {
        init();

        int answer = bfs();
        System.out.println(answer);
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());
        H = Integer.parseInt(stringTokenizer.nextToken());

        for (int z = 0; z < H; z++) {
            TOMATOES.add(new ArrayList<>());
            for (int y = 0; y < M; y++) {
                TOMATOES.get(z).add(new ArrayList<>());
                List<Integer> tomatoes = TOMATOES.get(z).get(y);
                stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
                for (int x = 0; x < N; x++) {
                    int value = Integer.parseInt(stringTokenizer.nextToken());
                    if (value == 0) {
                        tomatoCount++;
                    } else if (value == 1) {
                        QUEUE.add(new Item(z, y, x, 0));
                    }
                    tomatoes.add(value);
                }
            }
        }
    }

    private static int bfs() {
        int count = 0;
        while (!QUEUE.isEmpty()) {
            Item item = QUEUE.remove(0);
            for (int i = 0; i < 6; i++) {
                int moveZ = item.getZ() + DZ[i];
                int moveY = item.getY() + DY[i];
                int moveX = item.getX() + DX[i];
                if (validate(moveZ, moveY, moveX)) {
                    continue;
                }
                TOMATOES.get(moveZ).get(moveY).set(moveX, 1);
                tomatoCount--;
                QUEUE.add(new Item(moveZ, moveY, moveX, item.getCount() + 1));
            }
            if (count < item.getCount()) {
                count = item.getCount();
            }
        }
        if (tomatoCount != 0) {
            return -1;
        }
        return count;
    }

    private static boolean validate(int moveZ, int moveY, int moveX) {
        return moveZ < 0 || moveZ >= H || moveY < 0 || moveY >= M || moveX < 0 || moveX >= N
            || TOMATOES.get(moveZ).get(moveY).get(moveX) != 0;
    }

    private static class Item {

        private final int z;
        private final int y;
        private final int x;
        private final int count;

        public Item(int z, int y, int x, int count) {
            this.z = z;
            this.y = y;
            this.x = x;
            this.count = count;
        }

        public int getZ() {
            return z;
        }

        public int getY() {
            return y;
        }

        public int getX() {
            return x;
        }

        public int getCount() {
            return count;
        }
    }
}
