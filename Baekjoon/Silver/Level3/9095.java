// 1, 2, 3 더하기
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final int MAX_NUMBER = 11;
    private static final int[] dp = new int[MAX_NUMBER];

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        final int N = scanner.nextInt();
        init();
        for (int i = 0; i < N; i++) {
            sb.append(dp[scanner.nextInt()]);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static void init() {
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i < MAX_NUMBER; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
    }
}
