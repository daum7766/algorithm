import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final int MAX_VALUE = Integer.MAX_VALUE;

    private static int N;
    private static int M;
    private static int start;
    private static int end;
    private static List<List<Node>> graph = new ArrayList<>();
    private static int[] distance;

    public static void main(String[] args) throws IOException {
        init();

        long answer = solution();

        System.out.println(answer);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {
        N = Integer.parseInt(BUFFERED_READER.readLine());
        M = Integer.parseInt(BUFFERED_READER.readLine());

        distance = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
            distance[i] = MAX_VALUE;
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());
            int weight = Integer.parseInt(stringTokenizer.nextToken());
            graph.get(start).add(new Node(end, weight));
        }


        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        start = Integer.parseInt(stringTokenizer.nextToken());
        end = Integer.parseInt(stringTokenizer.nextToken());
        distance[start] = 0;
    }

    private static long solution() {
        boolean[] visited = new boolean[N + 1];

        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node(start, 0));

        while (!priorityQueue.isEmpty()) {
            Node currentNode = priorityQueue.poll();
            int currentIndex = currentNode.currentIndex;

            if (visited[currentIndex]) {
                continue;
            }
            visited[currentIndex] = true;

            List<Node> nodes = graph.get(currentIndex);

            for (Node nextNode : nodes) {
                if (visited[nextNode.currentIndex]) {
                    continue;
                }

                int newDistance = nextNode.distance + distance[currentIndex];
                int currentDistance = distance[nextNode.currentIndex];

                if (newDistance < currentDistance) {
                    distance[nextNode.currentIndex] = newDistance;
                    priorityQueue.add(new Node(nextNode.currentIndex, distance[nextNode.currentIndex]));
                }
            }
        }

        return distance[end];
    }

    private static class Node implements Comparable<Node> {

        private final int currentIndex;
        private final int distance;

        public Node(int currentIndex, int distance) {
            this.currentIndex = currentIndex;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            if (distance == o.distance) {
                return currentIndex - o.currentIndex;
            }
            return distance - o.distance;
        }
    }
}
