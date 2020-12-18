// 2 * n 타일링 2
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final int[] dp = new int[1001];

    public static void main(String[] args) {
        final int N = scanner.nextInt();
        dp[1] = 1;
        dp[2] = 3;
        for (int i = 3; i <= N; i++) {
            dp[i] = (dp[i - 1] + (2 * dp[i - 2])) % 10007;
        }
        System.out.println(dp[N]);
    }
}