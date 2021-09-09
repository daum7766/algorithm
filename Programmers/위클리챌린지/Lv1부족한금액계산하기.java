public class Lv1부족한금액계산하기 {

    public long solution(int price, int money, int count) {
        long answer = -money;

        for (int i = 1; i <= count; i++) {
            answer += (long) price * i;
        }
        if (answer < 0L) {
            answer = 0L;
        }

        return answer;
    }

}
