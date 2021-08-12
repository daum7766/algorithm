import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String data = BUFFERED_READER.readLine();

        int start = 0;
        int answer = 0;
        boolean isMinus = false;
        for (int i = 0; i < data.length(); i++) {
            if (!isMinus) {
                if (data.charAt(i) == '+') {
                    answer += Integer.parseInt(data.substring(start, i));
                    start = i+1;
                }
                else if (data.charAt(i) == '-') {
                    isMinus = true;
                    answer += Integer.parseInt(data.substring(start, i));
                    start = i+1;
                }
            } else if (data.charAt(i) == '+' || data.charAt(i) == '-') {
                    answer -= Integer.parseInt(data.substring(start, i));
                    start = i+1;
            }
        }
        if (!isMinus) {
            answer += Integer.parseInt(data.substring(start));
        } else {
            answer -= Integer.parseInt(data.substring(start));
        }
        System.out.println(answer);
    }
}
