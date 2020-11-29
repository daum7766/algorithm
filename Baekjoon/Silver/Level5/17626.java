// Four Squares
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        final int n = scanner.nextInt();
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            int minNumber = Integer.MAX_VALUE;
            for (int j = 1; j * j <= i; j++) {
                minNumber = Math.min(minNumber, dp[i - (j * j)]);
            }
            dp[i] = minNumber + 1;
        }
        System.out.println(dp[n]);
    }
}