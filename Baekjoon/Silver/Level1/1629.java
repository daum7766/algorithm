import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static long a;
    private static long b;
    private static long c;

    public static void main(String[] args) throws IOException {
        init();

        long answer = solution(b);

        System.out.println(answer % c);
        BUFFERED_READER.close();
    }

    private static long solution(long exponent) {
        if (exponent == 0) {
            return 1;
        }

        if (exponent == 1) {
            return a;
        }

        long value = solution(exponent / 2);
        if (exponent % 2 == 1) {
            return (((value * value) % c) * a) % c;
        }

        return (value * value) % c;
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        a = Integer.parseInt(stringTokenizer.nextToken());
        b = Integer.parseInt(stringTokenizer.nextToken());
        c = Integer.parseInt(stringTokenizer.nextToken());
    }
}
