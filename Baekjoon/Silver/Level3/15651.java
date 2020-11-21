// N과 M(3)
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final StringBuilder stringBuilder = new StringBuilder();
    private static final String SPACE = " ";
    private static final int ZERO = 0;
    private static int N;
    private static int M;
    private static int[] sequence;

    public static void main(String[] args) {
        N = scanner.nextInt();
        M = scanner.nextInt();
        findSequence();
        System.out.println(stringBuilder);
    }

    public static void findSequence() {
        sequence = new int[M];
        dfs(ZERO);
    }

    public static void dfs(int index) {
        if (index == M) {
            appendArrayData(sequence);
            return;
        }
        for (int i = 1; i <= N; i++) {
            sequence[index] = i;
            dfs(index + 1);
        }
    }

    public static void appendArrayData(int[] array) {
        for (int i = 0; i < array.length; i++) {
            stringBuilder.append(array[i] + SPACE);
        }
        stringBuilder.append("\n");
    }
}