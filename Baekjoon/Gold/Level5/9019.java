import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(BUFFERED_READER.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
            int source = Integer.parseInt(stringTokenizer.nextToken());
            int target = Integer.parseInt(stringTokenizer.nextToken());

            String answer = solution(source, target);
            System.out.println(answer);
        }
    }

    private static String solution(int source, int target) {
        List<Item> items = new LinkedList<>();
        items.add(new Item(source, "", new boolean[10000]));
        while (!items.isEmpty()) {
            Item item = items.remove(0);
            List<Item> execute = item.execute();
            for (Item item1 : execute) {
                if (item1.number == target) {
                    return item1.command;
                }
            }
            items.addAll(execute);
        }
        return "-1";
    }

    private static class Item {

        private final boolean[] check;

        private final int number;
        private final String command;

        public Item(int number, String command, boolean[] check) {
            this.number = number;
            this.command = command;
            this.check = check;
        }

        private List<Item> execute() {
            List<Item> returnItems = new LinkedList<>();
            DCommand(returnItems);
            SCommand(returnItems);
            LCommand(returnItems);
            RCommand(returnItems);
            return returnItems;
        }

        private void DCommand(List<Item> returnItems) {
            int doubleNumber = (number * 2) % 10000;
            validateAndAddItem(returnItems, doubleNumber, "D");
        }

        private void validateAndAddItem(List<Item> returnItems, int number, String addCommand) {
            if (!check[number]) {
                check[number] = true;
                returnItems.add(new Item(number, command + addCommand, check));
            }
        }

        private void SCommand(List<Item> returnItems) {
            int sNumber = number - 1;
            if (sNumber < 0) {
                sNumber = 9999;
            }
            validateAndAddItem(returnItems, sNumber, "S");
        }

        private void LCommand(List<Item> returnItems) {
            int left = number / 1000;
            int lNumber = ((number % 1000) * 10) + left;
            validateAndAddItem(returnItems, lNumber, "L");
        }

        private void RCommand(List<Item> returnItems) {
            int right = number % 10;
            int rNumber = (right * 1000) + (number / 10);
            validateAndAddItem(returnItems, rNumber, "R");
        }
    }
}
