// 팩토리얼 0의 개수
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int N = scanner.nextInt();
        int answer = N / 5 + N / (5 * 5) + N / (5 * 5 * 5);
        System.out.println(answer);
    }
}