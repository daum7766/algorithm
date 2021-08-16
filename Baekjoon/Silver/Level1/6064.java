import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static StringTokenizer stringTokenizer;
    private static int T;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < T; i++) {
            stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int answer = solution();
            System.out.println(answer);
        }
    }

    private static int solution() {
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        int x = Integer.parseInt(stringTokenizer.nextToken());
        int y = Integer.parseInt(stringTokenizer.nextToken());

        int count = x;
        int currentY = x;

        currentY = validateCurrentY(M, currentY);

        while (y != currentY) {
            if (count > N * M) {
                return -1;
            }
            currentY += N;
            count += N;
            currentY = validateCurrentY(M, currentY);
        }
        return count;
    }

    private static int validateCurrentY(int M, int currentY) {
        while (currentY > M) {
            currentY -= M;
        }
        return currentY;
    }
}
