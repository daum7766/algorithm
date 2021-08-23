import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final Map<String, Node> NODES = new HashMap<>();
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final String NEW_LINE = System.lineSeparator();

    public static void main(String[] args) throws IOException {
        init();

        solution();

        System.out.println(STRING_BUILDER);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {
        int n = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            String name = stringTokenizer.nextToken();
            String left = stringTokenizer.nextToken();
            String right = stringTokenizer.nextToken();
            if (!NODES.containsKey(name)) {
                NODES.put(name, new Node(name));
            }
            Node node = NODES.get(name);
            if (!".".equals(left)) {
                if (!NODES.containsKey(left)) {
                    NODES.put(left, new Node(left));
                }
                node.left = NODES.get(left);
            }
            if (!".".equals(right)) {
                if (!NODES.containsKey(right)) {
                    NODES.put(right, new Node(right));
                }
                node.right = NODES.get(right);
            }
        }
    }

    private static void solution() {
        Node node = NODES.get("A");
        first(node);
        STRING_BUILDER.append(NEW_LINE);
        second(node);
        STRING_BUILDER.append(NEW_LINE);
        third(node);
    }

    private static void first(Node node) {
        STRING_BUILDER.append(node.NAME);
        if (!Objects.isNull(node.left)) {
            first(node.left);
        }
        if (!Objects.isNull(node.right)) {
            first(node.right);
        }
    }

    private static void second(Node node) {
        if (!Objects.isNull(node.left)) {
            second(node.left);
        }
        STRING_BUILDER.append(node.NAME);
        if (!Objects.isNull(node.right)) {
            second(node.right);
        }
    }

    private static void third(Node node) {
        if (!Objects.isNull(node.left)) {
            third(node.left);
        }
        if (!Objects.isNull(node.right)) {
            third(node.right);
        }
        STRING_BUILDER.append(node.NAME);
    }

    private static class Node {

        private final String NAME;
        private Node left;
        private Node right;

        public Node(String name) {
            NAME = name;
        }
    }

}
