import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < T; i++) {
            solution();
        }
    }

    private static void solution() throws IOException {
        String command = BUFFERED_READER.readLine();
        BUFFERED_READER.readLine();
        String data = BUFFERED_READER.readLine();
        String[] dates = data.substring(1, data.length() - 1).split(",");
        List<String> numbers = new LinkedList<>();
        for (String date : dates) {
            if (date.equals("")) {
                continue;
            }
            numbers.add(date);
        }
        AC ac = new AC(numbers);
        for (int i = 0; i < command.length(); i++) {
            ac.execute(command.charAt(i));
        }
        if (ac.isError()) {
            System.out.println("error");
            return;
        }
        String[] numbersToString = ac.getNumbers().toArray(String[]::new);

        String answer = String.join(",", numbersToString);
        System.out.println("[" + answer + "]");
    }

    private static class AC {

        private static final char REVERSE = 'R';
        private static final char DELETE = 'D';

        private final List<String> numbers;
        private boolean reversed = false;
        private boolean isError = false;

        public AC(List<String> numbers) {
            this.numbers = numbers;
        }

        public void execute(char command) {
            if (command == REVERSE) {
                reversed = !reversed;
            }
            if (command == DELETE) {
                delete();
            }
        }

        private void delete() {
            if (isError) {
                return;
            }
            if (numbers.size() == 0) {
                isError = true;
                return;
            }
            if (reversed) {
                numbers.remove(numbers.size() - 1);
            } else {
                numbers.remove(0);
            }
        }

        public List<String> getNumbers() {
            if (reversed) {
                Collections.reverse(numbers);
            }
            return numbers;
        }

        public boolean isError() {
            return isError;
        }
    }
}
