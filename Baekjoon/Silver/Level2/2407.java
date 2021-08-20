import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));

    private static long N;
    private static long M;

    public static void main(String[] args) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Long.parseLong(stringTokenizer.nextToken());
        M = Long.parseLong(stringTokenizer.nextToken());

        BigInteger answer = solution();
        System.out.println(answer);
    }

    private static BigInteger solution() {
        BigInteger answer = BigInteger.valueOf(N);
        for (int i = 1; i < M; i++) {
            BigInteger number = BigInteger.valueOf(N - i);
            answer = answer.multiply(number);
        }
        BigInteger divide = BigInteger.valueOf(M);
        for (int i = 2; i < M; i++) {
            BigInteger number = BigInteger.valueOf(i);
            divide = divide.multiply(number);
        }
        return answer.divide(divide);
    }
}
