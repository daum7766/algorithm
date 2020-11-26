// 계단오르기
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final int[] stairs = new int[300];
    private static final int[] arr = new int[300];

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        final int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        stairs[0] = arr[0];
        stairs[1] = arr[0] + arr[1];
        stairs[2] = Math.max(arr[0] + arr[2], arr[1] + arr[2]) ;
        for (int i = 3; i < N; i++) {
            stairs[i] = Math.max(arr[i] + stairs[i-2],  arr[i] + arr[i-1] + stairs[i-3]);  
        }
        System.out.println(stairs[N-1]);
    }
}