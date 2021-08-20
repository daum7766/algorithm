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

    private static int N;
    private static int M;
    private static List<Integer> numbers = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        for (int i = 0; i < N; i++) {
            numbers.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        Collections.sort(numbers);

        dfs(0, 0, new ArrayList<>());
        System.out.println(STRING_BUILDER);
    }

    private static void dfs(int depth, int index, List<Integer> list) {
        if (depth == M) {
            for (Integer number : list) {
                STRING_BUILDER.append(number).append(" ");
            }
            STRING_BUILDER.append(NEW_LINE);
            return;
        }
        for (int i = index; i < N; i++) {
            list.add(numbers.get(i));
            dfs(depth + 1, i, list);
            list.remove(list.size() - 1);
        }
    }
}
