package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Main {

    public static final class Item implements Comparable<Item> {
        private final int index;
        private final int weight;

        public Item(int index, int weight) {
            this.index = index;
            this.weight = weight;
        }

        public int getIndex() {
            return index;
        }

        public int getWeight() {
            return weight;
        }

        @Override
        public int compareTo(Item o) {
            return weight - o.getWeight();
        }
    }

    public static void main(String[] args) throws IOException {
        final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        
        // 데이터 초기 설정
        String[] userInput = bufferedReader.readLine().split(" ");
        final int v = Integer.parseInt(userInput[0]);
        final int u = Integer.parseInt(userInput[1]);
        final int startIndex = Integer.parseInt(bufferedReader.readLine());

        List<List<Item>> graph = new ArrayList<>();
        graph.add(null);

        boolean[] visited = new boolean[v + 1];
        int[] distance = new int[v + 1];
        for (int i = 1; i < v + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
            graph.add(new ArrayList<>());
        }
        distance[startIndex] = 0;

        // 그래프 그리기
        for (int i = 0; i < u; i++) {
            String[] s = bufferedReader.readLine().split(" ");
            int start = Integer.parseInt(s[0]);
            int end = Integer.parseInt(s[1]);
            int weight = Integer.parseInt(s[2]);
            graph.get(start).add(new Item(end, weight));
        }

        // 다익스트라 알고리즘 돌리기
        PriorityQueue<Item> queue = new PriorityQueue<>();
        queue.add(new Item(startIndex, 0));

        while (!queue.isEmpty()) {
            Item it =  queue.poll();

            if (visited[it.getIndex()]) {
                continue;
            }
            visited[it.getIndex()] = true;

            for (Item item : graph.get(it.getIndex())) {
                if (distance[item.getIndex()] > it.getWeight() + item.getWeight()) {
                    distance[item.getIndex()] = it.getWeight() + item.getWeight();
                    queue.add(new Item(item.getIndex(), distance[item.getIndex()]));
                }
            }
        }

        for (int i = 1; i < v + 1; i++) {
            if (distance[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
                continue;
            }
            System.out.println(distance[i]);
        }

        bufferedReader.close();
    }
}
