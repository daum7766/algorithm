public class Lv1_3진법뒤집기 {

    public int solution(int n) {
        String ternary = decimalToTernary(n);
        return ternaryToDecimal(ternary);
    }

    public String decimalToTernary(int n) {
        StringBuilder stringBuilder = new StringBuilder();
        while (n >= 3) {
            stringBuilder.append(n % 3);
            n /= 3;
        }
        stringBuilder.append(n);
        return stringBuilder.toString();
    }

    public int ternaryToDecimal(String n) {
        int answer = 0;
        for (int i = 0; i < n.length(); i++) {
            char c = n.charAt(n.length() - 1 - i);
            int number = (c - '0');
            answer += number * Math.pow(3, i);
        }
        return answer;
    }
}
