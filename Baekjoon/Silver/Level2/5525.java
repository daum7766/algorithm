import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(new InputStreamReader(System.in));
    private static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        BUFFERED_READER.readLine();
        String data = BUFFERED_READER.readLine();

        String compare = "IO".repeat(Math.max(0, N)) + "I";

        int answer = findCount(data, compare);
        System.out.println(answer);
    }

    private static int findCount(String data, String compare) {
        int answer = 0;
        int patternCount = 0;
        for (int i = 0; i < data.length() - 2; i++) {
            if (data.charAt(i) == 'I' && data.charAt(i + 1) == 'O' && data.charAt(i + 2) == 'I') {
                patternCount++;
                if (patternCount == N) {
                    patternCount--;
                    answer++;
                }
                i++;
            } else {
                patternCount = 0;
            }

        }
        return answer;
    }
}
