import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final String NEW_LINE = System.lineSeparator();
    private static final List<Integer> NUMBERS = new ArrayList<>();
    private static final Set<String> NUMBERS_SET = new LinkedHashSet<>();

    private static int N;
    private static int M;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        init();

        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            dfs(numbers);
        }

        List<String> answer = new ArrayList<>(NUMBERS_SET);

        for (String s : answer) {
            STRING_BUILDER.append(s).append(NEW_LINE);
        }

        System.out.println(STRING_BUILDER);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());
        visited = new boolean[N];

        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        for (int i = 0; i < N; i++) {
            NUMBERS.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        Collections.sort(NUMBERS);
    }

    private static void dfs(List<Integer> numbers) {
        if (numbers.size() >= M) {
            StringBuilder stringBuilder = new StringBuilder();
            for (int i = 0; i < numbers.size(); i++) {
                stringBuilder.append(numbers.get(i));
                if (i != numbers.size() - 1) {
                    stringBuilder.append(" ");
                }
            }
            NUMBERS_SET.add(stringBuilder.toString());
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                numbers.add(NUMBERS.get(i));
                dfs(numbers);
                numbers.remove(numbers.size() - 1);
                visited[i] = false;
            }
        }
    }

}
