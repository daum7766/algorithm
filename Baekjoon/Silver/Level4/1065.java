import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int number = scanner.nextInt();
        System.out.println(hanSu(number));
    }

    public static int hanSu(int number) {
        int count = 99;
        int[] a = new int[3];
        // 2자리 수까지는 전부 한수이다.
        if (number < 100) {
            return number;
        }
        if (number == 1000) {
            number -= 1;
        }
        for (int i = 100; i <= number; i++) {
            int temp = i;
            a[0] = temp % 10;
            a[1] = temp / 10 % 10;
            a[2] = temp / 100;
            if (a[0] - a[1] == a[1] - a[2]) {
                count++;
            }
        }
        return count;
    }
}