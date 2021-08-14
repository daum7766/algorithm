import java.util.Scanner;

public class Main {

    private static final Scanner SCANNER = new Scanner(System.in);
    private static int K;
    private static int[] MONEY;

    public static void main(String[] args) {
        int n = SCANNER.nextInt();
        K = SCANNER.nextInt();
        MONEY = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            MONEY[i] = SCANNER.nextInt();
        }

        int answer = solution();
        System.out.println(answer);
    }

    private static int solution() {
        int answer = 0;
        int leftMoney = K;

        int index = 0;
        while (leftMoney != 0) {
            int value = leftMoney / MONEY[index];
            if (value != 0) {
                answer += value;
                leftMoney -= MONEY[index] * value;
            }
            index++;
        }
        return answer;
    }
}
