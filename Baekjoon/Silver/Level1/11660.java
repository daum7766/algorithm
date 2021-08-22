import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final String NEW_LINE = System.lineSeparator();

    private static int N;
    private static int M;
    private static int[][] numbers;
    private static int[][] sums;

    public static void main(String[] args) throws IOException {
        init();

        for (int i = 0; i < M; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int startY = Integer.parseInt(stringTokenizer.nextToken()) - 1;
            int startX = Integer.parseInt(stringTokenizer.nextToken()) - 1;
            int endY = Integer.parseInt(stringTokenizer.nextToken()) - 1;
            int endX = Integer.parseInt(stringTokenizer.nextToken()) - 1;

            long answer = solution(startX, startY, endX, endY);
            STRING_BUILDER.append(answer).append(NEW_LINE);
        }

        System.out.println(STRING_BUILDER);
        BUFFERED_READER.close();
    }

    private static long solution(int startX, int startY, int endX, int endY) {
        int answer = 0;
        for (int i = startY; i <= endY; i++) {
            answer += sums[i][endX + 1] - sums[i][startX];
        }
        return answer;
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        numbers = new int[N][N];
        sums = new int[N + 1][N + 1];

        for (int i = 0; i < N; i++) {
            stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int j = 0; j < N; j++) {
                numbers[i][j] = Integer.parseInt(stringTokenizer.nextToken());
                sums[i][j + 1] = sums[i][j] + numbers[i][j];
            }
        }
    }

}
