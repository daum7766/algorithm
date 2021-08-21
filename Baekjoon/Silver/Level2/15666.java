import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader BUFFERED_READER = new BufferedReader(
        new InputStreamReader(System.in));
    private static final StringBuilder STRING_BUILDER = new StringBuilder();
    private static final String NEW_LINE = System.lineSeparator();
    private static final Set<String> NUMBERS_SET = new LinkedHashSet<>();

    private static int N;
    private static int M;
    private static List<Integer> numbers = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();

        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            dfs(numbers);
        }

        List<String> answer = new ArrayList<>(NUMBERS_SET);

        for (String s : answer) {
            STRING_BUILDER.append(s).append(NEW_LINE);
        }

        System.out.println(STRING_BUILDER);
        BUFFERED_READER.close();
    }

    private static void init() throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(BUFFERED_READER.readLine());
        Set<Integer> numbersSet = new HashSet<>();
        for (int i = 0; i < N; i++) {
            numbersSet.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        numbers = new ArrayList<>(numbersSet);
        Collections.sort(numbers);
    }

    private static void dfs(List<Integer> answerList) {
        if (answerList.size() >= M) {
            StringBuilder stringBuilder = new StringBuilder();
            for (int i = 0; i < answerList.size(); i++) {
                stringBuilder.append(answerList.get(i));
                if (i != answerList.size() - 1) {
                    stringBuilder.append(" ");
                }
            }
            NUMBERS_SET.add(stringBuilder.toString());
            return;
        }
        for (Integer number : numbers) {
            if (answerList.size() != 0 && answerList.get(answerList.size() - 1) > number) {
                continue;
            }
            answerList.add(number);
            dfs(answerList);
            answerList.remove(answerList.size() - 1);
        }
    }

}
