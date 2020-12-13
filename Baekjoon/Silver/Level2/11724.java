// 연결 요소의 개수
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static int N = 0;
    private static int M = 0;
    private static ArrayList<ArrayList<Integer>> arrays = new ArrayList<>();
    private static ArrayList<Boolean> visited = new ArrayList<>();

    public static void main(String[] args) {
        N = scanner.nextInt();
        M = scanner.nextInt();
        int count = 0;
        init();
        for (int i = 0; i < N; i++) {
            if (!visited.get(i)) {
                dfs(i);            
                count++;
            }
        }
        System.out.println(count);
    }

    private static void init() {
        for (int i = 0; i < N; i++) {
            visited.add(false);
            arrays.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt() - 1;
            int b = scanner.nextInt() - 1;
            arrays.get(a).add(b);
            arrays.get(b).add(a);
        }
    }

    private static void dfs(int idx) {
        visited.set(idx, true);
        for (int targetNode : arrays.get(idx)) {
            if (!visited.get(targetNode)) {
                dfs(targetNode);
            }
        }
    }
}
