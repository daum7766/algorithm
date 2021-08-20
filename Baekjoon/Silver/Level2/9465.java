import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < t; i++) {
            int answer = solution();
            System.out.println(answer);
        }
    }

    private static int solution() throws IOException {
        int N = Integer.parseInt(BUFFERED_READER.readLine());
        int[][] sticker = new int[2][N];
        for (int j = 0; j < 2; j++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            for (int i = 0; i < N; i++) {
                sticker[j][i] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }
        int[][] dp = new int[2][N + 1];
        dp[0][1] = sticker[0][0];
        dp[1][1] = sticker[1][0];
        for (int i = 0; i < N - 1; i++) {
            dp[0][i + 2] = Math.max(dp[1][i], dp[1][i + 1]) + sticker[0][i + 1];
            dp[1][i + 2] = Math.max(dp[0][i], dp[0][i + 1]) + sticker[1][i + 1];
        }

        return Math.max(dp[0][N], dp[1][N]);
    }
}
