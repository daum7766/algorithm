import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static int N;
    private static int[][] RGB;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        init();

        int answer = solution();

        System.out.println(answer);
        BUFFERED_READER.close();
    }

    private static int solution() {
        for (int i = 0; i < N; i++) {
            dp[i + 1][0] = Math.min(dp[i][1], dp[i][2]) + RGB[i][0];
            dp[i + 1][1] = Math.min(dp[i][0], dp[i][2]) + RGB[i][1];
            dp[i + 1][2] = Math.min(dp[i][0], dp[i][1]) + RGB[i][2];
        }

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            answer = Math.min(answer, dp[N][i]);
        }
        return answer;
    }

    private static void init() throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        RGB = new int[N][3];
        dp = new int[N + 1][3];
        for (int i = 0; i < N; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            RGB[i][0] = Integer.parseInt(stringTokenizer.nextToken());
            RGB[i][1] = Integer.parseInt(stringTokenizer.nextToken());
            RGB[i][2] = Integer.parseInt(stringTokenizer.nextToken());
        }
    }

}
