// 비밀번호 찾기
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final HashMap<String, String> password = new HashMap<>();

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            password.put(scanner.next(), scanner.next());
        }
        for (int i = 0; i < M; i++) {
            System.out.println(password.get(scanner.next()));
        }
    }
}
