import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final String NEW_LINE = System.lineSeparator();
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final List<Integer> NUMBERS = new ArrayList<>();

    private static int N;
    private static int M;

    public static void main(String[] args) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        for (int i = 0; i < N; i++) {
            NUMBERS.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        Collections.sort(NUMBERS);

        dfs(0, new ArrayList<>(), new boolean[N]);
        System.out.println(STRING_BUILDER);
    }

    private static void dfs(int depth, List<Integer> list, boolean[] visited) {
        if (depth == M) {
            for (Integer number : list) {
                STRING_BUILDER.append(number).append(" ");
            }
            STRING_BUILDER.append(NEW_LINE);
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                list.add(NUMBERS.get(i));
                dfs(depth + 1, list, visited);
                list.remove(list.size() - 1);
                visited[i] = false;
            }
        }
    }
}
