import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Lv1두개뽑아서더하기 {

    public int[] solution(int[] numbers) {
        Set<Integer> answer = new HashSet<>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                answer.add(numbers[i] + numbers[j]);
            }
        }
        List<Integer> numberList = new ArrayList<>(answer);
        Collections.sort(numberList);

        return numberList.stream().mapToInt(Integer::intValue).toArray();
    }
}
