import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[] counts = new int[1001];
        counts[1] = 1;
        counts[2] = 2;

        int number = scanner.nextInt();
        for (int i = 3; i <= number; i++) {
            counts[i] = (counts[i-1] + counts[i-2]) % 10007;
        }
        System.out.println(counts[number]);
    }
}