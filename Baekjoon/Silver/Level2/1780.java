// 종이의 개수
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int[][] arr;
    private static final HashMap<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) throws NumberFormatException, IOException {
        N = Integer.parseInt(bf.readLine());
        init();
        recursiveFunction(0, 0, N, N);
        printResult();
    }

    private static void init() throws NumberFormatException, IOException {
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        map.put(0, 0);
        map.put(-1, 0);
        map.put(1, 0);
    }

    private static void recursiveFunction(int startX, int startY, int endX, int endY) {
        int number = arr[startY][startX];
        for (int i = startY; i < endY; i++) {
            for (int j = startX; j < endX; j++) {
                if (number != arr[i][j]) {
                    int size = (endX - startX) / 3;
                    for (int k = 0; k < 3; k++) {
                        for (int z = 0; z < 3; z++) {
                            recursiveFunction(startX + k * size, startY + z * size,
                                    startX + (k + 1) * size, startY + (z + 1) * size);
                        }
                    }
                    return;
                }
            }
        }
        map.put(number, map.get(number) + 1);
    }

    private static void printResult() {
        System.out.println(map.get(-1));
        System.out.println(map.get(0));
        System.out.println(map.get(1));
    }

}