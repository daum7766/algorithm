import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final String NEW_LINE = System.lineSeparator();

    private static Node root;

    public static void main(String[] args) throws IOException {
        init();

        solution(root);

        System.out.println(STRING_BUILDER);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {

        root = new Node(Integer.parseInt(BUFFERED_READER.readLine()));

        String input;
        while (true) {
            input = BUFFERED_READER.readLine();
            if (Objects.isNull(input) || input.equals("")) {
                break;
            }
            int number = Integer.parseInt(input);
            root.addNode(number);
        }
    }

    private static void solution(Node node) {
        if (!Objects.isNull(node.left)) {
            solution(node.left);
        }
        if (!Objects.isNull(node.right)) {
            solution(node.right);
        }
        STRING_BUILDER.append(node.number)
            .append(NEW_LINE);
    }


    private static class Node {

        private final int number;
        private Node left;
        private Node right;

        public Node(int number) {
            this.number = number;
        }

        public void addNode(int number) {
            if (this.number > number) {
                if (Objects.isNull(left)) {
                    left = new Node(number);
                } else {
                    left.addNode(number);
                }
            } else {
                if (Objects.isNull(right)) {
                    right = new Node(number);
                } else {
                    right.addNode(number);
                }
            }
        }
    }
}
