import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(new InputStreamReader(System.in));
    private static final String NEW_LINE = System.lineSeparator();
    private static int M;
    private static int[] dataSum;
    private static StringTokenizer stringTokenizer;

    public static void main(String[] args) throws IOException {
        dataInit();
        StringBuilder stringBuilder = new StringBuilder();
        for(int i = 0; i < M; i++) {
            int answer = solution();
            stringBuilder.append(answer);
            stringBuilder.append(NEW_LINE);
        }
        System.out.println(stringBuilder);
    }

    private static void dataInit() throws IOException {
        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());

        int N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt((stringTokenizer.nextToken()));

        dataSum = new int[N + 1];
        dataSum[0] = 0;
        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());

        for (int i = 1; i <= N; i++) {
            dataSum[i] = dataSum[i - 1] + Integer.parseInt(stringTokenizer.nextToken());
        }
    }

    private static int solution() throws IOException {
        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());

        int start = Integer.parseInt(stringTokenizer.nextToken());
        int end = Integer.parseInt(stringTokenizer.nextToken());

        return dataSum[end] - dataSum[start - 1];
    }
}
