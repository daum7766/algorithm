// 최대힙
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final PriorityQueue<Integer> PQ =
            new PriorityQueue<>(Collections.reverseOrder());
    private static final StringBuilder SB = new StringBuilder();

    public static void main(String[] args) {
        final int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            maxHeap();
        }
        System.out.println(SB.toString());
    }

    private static void maxHeap() {
        int userInput = scanner.nextInt();
        if (userInput == 0) {
            if (PQ.isEmpty()) {
                addString(0);
                return;
            }
            addString(PQ.poll());
            return;
        }
        PQ.add(userInput);
    }

    private static void addString(int number) {
        SB.append(number);
        SB.append("\n");
    }
}