import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static int N;
    private static int[][] numbers;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        init();

        long answer = solution();

        System.out.println(answer);
        BUFFERED_READER.close();
    }

    private static long solution() {
        int answer = numbers[0][0];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                int a = dp[i][j];
                int b = dp[i][j + 1];
                dp[i + 1][j + 1] = Math.max(a, b) + numbers[i][j];
                answer = Math.max(dp[i + 1][j + 1], answer);
            }
        }

        return answer;
    }

    private static void init() throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        numbers = new int[N][N];
        dp = new int[N + 1][N + 1];

        for (int i = 0; i < N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int j = 0; j <= i; j++) {
                numbers[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }
        dp[1][1] = numbers[0][0];
    }

}
