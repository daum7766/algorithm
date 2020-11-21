// 4673 셀프넘버

public class Main {

    static final int startNumber = 1;
    static final int maxNumber = 10001;

    public static void main(String[] args) {

        boolean[] selfNumbers = new boolean[maxNumber];
        for (int i = startNumber; i < maxNumber; i++) {
            int n = addNumber(i);
            if (n < maxNumber) {
                selfNumbers[n] = true;
            }
            if (!selfNumbers[i]) {
                System.out.println(i);
            }
        }
    }

    public static int addNumber(int number) {
        int sum = number;
        while (number != 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
}