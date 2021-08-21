import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final String NEW_LINE = System.lineSeparator();
    private static final List<List<Integer>> NODES = new ArrayList<>();

    private static int N;
    private static int[] parent;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < N + 1; i++) {
            NODES.add(new ArrayList<>());
        }
        for (int i = 1; i < N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int first = Integer.parseInt(stringTokenizer.nextToken());
            int second = Integer.parseInt(stringTokenizer.nextToken());
            NODES.get(first).add(second);
            NODES.get(second).add(first);
        }

        parent = new int[N + 1];

        dfs(1);

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 2; i <= N; i++) {
            stringBuilder.append(parent[i]).append(NEW_LINE);
        }
        System.out.println(stringBuilder);
        BUFFERED_READER.close();
    }

    private static void dfs(int index) {
        for (int i = 0; i < NODES.get(index).size(); i++) {
            int number = NODES.get(index).get(i);
            if (parent[number] == 0) {
                parent[number] = index;
                dfs(number);
            }
        }
    }
}
