// 좌표압축
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final HashMap<Integer, Integer> map = new HashMap<>();
    private static final StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        final int N = scanner.nextInt();
        int[] arr = new int[N];
        int[] sortArr = new int[N];
        for (int i = 0; i < N; i++) {
            int a = scanner.nextInt();
            arr[i] = a;
            sortArr[i] = a;
        }
        Arrays.sort(sortArr);
        for (int i = 0, count = 0; i < N; i++) {
            if (!map.containsKey(sortArr[i])) {
                map.put(sortArr[i], count++);
            }
        }
        for (int i = 0; i < N - 1; i++) {
            sb.append(map.get(arr[i]));
            sb.append(" ");
        }
        sb.append(map.get(arr[N - 1]));
        System.out.println(sb.toString());
    }
}