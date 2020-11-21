// A + B - 9
import java.math.BigInteger;
import java.util.Scanner;

public class Main {

    private static final String SPLIT_STR = " ";
    private static final int ZERO = 0;
    private static final int ONE = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        sum(scanner);
    }

    public static void sum(Scanner scanner) {
        String[] data = scanner.nextLine().split(SPLIT_STR);
        BigInteger a = new BigInteger(data[ZERO]);
        BigInteger b = new BigInteger(data[ONE]);
        System.out.println(a.add(b));
    }
}