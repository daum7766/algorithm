import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int[] DY = {0, 0, 1, -1};
    private static final int[] DX = {1, -1, 0, 0};

    private static int N;
    private static final List<List<Integer>> numbers = new LinkedList<>();
    private static final List<Integer> answers = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());

        for (int i = 0; i < N; i++) {
            String dates = BUFFERED_READER.readLine();
            numbers.add(new LinkedList<>());
            for (int j = 0; j < dates.length(); j++) {
                numbers.get(i).add(dates.charAt(j) - '0');
            }
        }

        solution();

        Collections.sort(answers);
        System.out.println(answers.size());
        for (Integer answer : answers) {
            System.out.println(answer);
        }
    }

    private static void solution() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (numbers.get(i).get(j) == 1) {
                    bfs(i, j);
                }
            }
        }
    }

    private static void bfs(int i, int j) {
        int count = 1;
        List<Item> queue = new LinkedList<>();
        queue.add(new Item(i, j));
        numbers.get(i).set(j, 0);

        while (!queue.isEmpty()) {
            Item item = queue.remove(0);
            for (int k = 0; k < 4; k++) {
                int moveY = item.getY() + DY[k];
                int moveX = item.getX() + DX[k];
                if (moveY < 0 || moveY >= N || moveX < 0 || moveX >= N
                    || numbers.get(moveY).get(moveX) == 0) {
                    continue;
                }
                queue.add(new Item(moveY, moveX));
                count++;
                numbers.get(moveY).set(moveX, 0);
            }
        }
        answers.add(count);
    }

    private static class Item {

        private final int y;
        private final int x;

        public Item(int y, int x) {
            this.y = y;
            this.x = x;
        }

        public int getY() {
            return y;
        }

        public int getX() {
            return x;
        }
    }
}
