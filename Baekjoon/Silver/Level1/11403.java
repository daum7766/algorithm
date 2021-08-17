import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final String NEW_LINE = System.lineSeparator();

    private static int N;
    private static String[][] graph;

    public static void main(String[] args) throws IOException {
        init();

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if ("0".equals(graph[i][j]) && "1".equals(graph[i][k])
                        && "1".equals(graph[k][j])) {
                        graph[i][j] = "1";
                    }
                }
            }
        }
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < N; i++) {
            String join = String.join(" ", graph[i]);
            stringBuilder.append(join)
                .append(NEW_LINE);
        }
        System.out.println(stringBuilder);
    }

    private static void init() throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        graph = new String[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = stringTokenizer.nextToken();
            }
        }
    }
}
