import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(BUFFERED_READER.readLine());
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        int[] numbers = new int[n];
        int[] dp = new int[n + 1];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        for (int i = 0; i < n; i++) {
            int max = 0;
            for (int j = 0; j < i; j++) {
                if (numbers[j] < numbers[i] && dp[j + 1] > max) {
                    max = dp[j + 1];
                }
            }
            dp[i + 1] = max + 1;
            answer = Math.max(answer, dp[i + 1]);
        }
        System.out.println(answer);
    }
}
