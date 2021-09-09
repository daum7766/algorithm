public class Lv1LottoMaxAndMin {

    public int[] solution(int[] lottos, int[] win_nums) {
        int matchCount = 0;
        int zeroCount = 0;
        for (int number : lottos) {
            if (number == 0) {
                zeroCount++;
                continue;
            }
            for (int winNumber : win_nums) {
                if (number == winNumber) {
                    matchCount++;
                    break;
                }
            }
        }
        int max = 7 - matchCount - zeroCount;
        int min = 7 - matchCount;

        if (max == 7) {
            max = 6;
        }
        if(min == 7) {
            min = 6;
        }
        return new int[] {max, min};
    }
}
