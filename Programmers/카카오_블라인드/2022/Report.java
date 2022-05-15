import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {

    private int[] answer;
    private Set<String> reports;
    private Map<String, Set<String>> reportDuplicator;
    private Map<String, Integer> reportCount;
    private int k;

    public int[] solution(String[] idList, String[] reports, int k) {
        // init
        init(idList, reports, k);

        // solution
        reports();
        for (int i = 0; i < idList.length; i++) {
            findAnswer(i, reportDuplicator.computeIfAbsent(idList[i], key -> new HashSet<>()));
        }

        return answer;
    }

    private void init(String[] idList, String[] reports, int k) {
        answer = new int[idList.length];
        reportDuplicator = new HashMap<>();
        reportCount = new HashMap<>();
        this.reports = new HashSet<>(Arrays.asList(reports));
        this.k = k;
    }

    private void reports() {
        for (String report : reports) {
            String[] info = report.split(" ");
            String userId = info[0];
            String reportUserId = info[1];
            Set<String> reportUsers = reportDuplicator
                .computeIfAbsent(userId, key -> new HashSet<>());
            calculateCount(reportUsers, reportUserId);
        }
    }

    private void calculateCount(Set<String> reportUsers, String reportUserId) {
        reportUsers.add(reportUserId);
        Integer count = reportCount.getOrDefault(reportUserId, 0);
        reportCount.put(reportUserId, count + 1);
    }

    private void findAnswer(int index, Set<String> reportUsers) {
        for (String userId : reportUsers) {
            if (reportCount.get(userId) >= k) {
                answer[index]++;
            }
        }
    }
}

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class SolutionTest {

    @Test
    void test1() {
        //given
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"};
        int k = 2;
        int[] expected = {2, 1, 1, 0};

        //when
        Solution solution = new Solution();
        int[] answer = solution.solution(id_list, report, k);

        //then
        Assertions.assertArrayEquals(expected, answer);
    }

    @Test
    void test2() {
        //given
        String[] id_list = {"con", "ryan"};
        String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
        int k = 3;
        int[] expected = {0, 0};

        //when
        Solution solution = new Solution();
        int[] answer = solution.solution(id_list, report, k);

        //then
        Assertions.assertArrayEquals(expected, answer);
    }
}
