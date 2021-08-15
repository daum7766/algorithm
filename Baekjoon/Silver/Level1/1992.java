import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final StringBuilder STRING_BUILDER = new StringBuilder();

    private static int N;
    private static String[] dates;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        dates = new String[N];
        for (int i = 0; i < N; i++) {
            dates[i] = BUFFERED_READER.readLine();
        }

        solution(0, N, 0, N);
        System.out.println(STRING_BUILDER);
    }

    private static void solution(int startX, int endX, int startY, int endY) {
        char value = dates[startY].charAt(startX);
        for (int y = startY; y < endY; y++) {
            for (int x = startX; x < endX; x++) {
                if (dates[y].charAt(x) != value) {
                    STRING_BUILDER.append("(");
                    solution(startX, (startX + endX) / 2, startY, (startY + endY) / 2);
                    solution((startX + endX) / 2, endX, startY, (startY + endY) / 2);
                    solution(startX, (startX + endX) / 2, (startY + endY) / 2, endY);
                    solution((startX + endX) / 2, endX, (startY + endY) / 2, endY);
                    STRING_BUILDER.append(")");
                    return;
                }
            }
        }
        STRING_BUILDER.append(value);
    }
}
