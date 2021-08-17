import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final String NEW_LINE = System.lineSeparator();
    private static final PriorityQueue<Item> PRIORITY_QUEUE = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        StringBuilder stringBuilder = new StringBuilder();
        int N = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < N; i++) {
            int input = Integer.parseInt(BUFFERED_READER.readLine());
            if (input != 0) {
                PRIORITY_QUEUE.add(new Item(Math.abs(input), input));
            } else {
                if (PRIORITY_QUEUE.isEmpty()) {
                    stringBuilder.append(0);
                } else {
                    stringBuilder.append(PRIORITY_QUEUE.poll().getValue());
                }
                stringBuilder.append(NEW_LINE);
            }
        }
        System.out.println(stringBuilder);
    }

    private static class Item implements Comparable<Item> {

        private final int absValue;
        private final int value;

        public Item(int absValue, int value) {
            this.absValue = absValue;
            this.value = value;
        }

        @Override
        public int compareTo(Item o) {
            if (absValue < o.getAbsValue()
                || absValue == o.getAbsValue() && value <= o.getValue()) {
                return -1;
            }
            return 1;
        }

        public int getAbsValue() {
            return absValue;
        }

        public int getValue() {
            return value;
        }
    }
}
