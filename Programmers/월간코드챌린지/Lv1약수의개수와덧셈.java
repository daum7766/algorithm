public class Lv1약수의개수와덧셈 {

    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            if (divisorCountIsEven(i)) {
                answer += i;
            } else {
                answer -= i;
            }
        }
        return answer;
    }

    private boolean divisorCountIsEven(int number) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                answer++;
            }
        }
        return (answer & 1) == 0;
    }

}
