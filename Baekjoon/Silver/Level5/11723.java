// 집합
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final StringBuilder sb = new StringBuilder();
    private static final int maxNumber = 21;

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int M = scanner.nextInt();
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < M; i++) {
            String command = scanner.next();
            function(command, set);
        }
        System.out.println(sb.toString());
    }

    private static void function(String command, Set<Integer> set) {
        if (command.equals("all")) {
            for (int i = 1; i < maxNumber; i++) {
                set.add(i);
            }
            return;
        }
        if (command.equals("empty")) {
            set.clear();
            return;
        }
        int number = scanner.nextInt();
        if (command.equals("add")) {
            set.add(number);
            return;
        }
        if (command.equals("remove")) {
            set.remove(number);
            return;
        }
        if (command.equals("check")) {
            if (set.contains(number)) {
                sb.append(1);
            }
            else {
                sb.append(0);
            }
            sb.append("\n");
            return;
        }
        if (command.equals("toggle")) {
            if (set.contains(number)) {
                set.remove(number);
            }
            else {
                set.add(number);
            }
        }
    }

}
