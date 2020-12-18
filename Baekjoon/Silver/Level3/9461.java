// 파도반 수열
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final StringBuilder sb = new StringBuilder();
    private static final int MAX_NUMBER = 101;
    private static final long[] dp = new long[MAX_NUMBER];

    public static void main(String[] args) {
        final int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            init();
            sb.append(dp[scanner.nextInt()]);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static void init() {
        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 1;
        for (int i = 4; i < MAX_NUMBER; i++) {
            dp[i] = dp[i - 2] + dp[i - 3];
        }
    }
}