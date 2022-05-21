import kotlin.math.max

class Solution {
    fun solution(answers: IntArray): IntArray {
        val supozaType: List<IntArray> = listOf(
            intArrayOf(1, 2, 3, 4, 5),
            intArrayOf(2, 1, 2, 3, 2, 4, 2, 5),
            intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )
        val matchCount = mutableMapOf<Int, Int>()
        var max = 0
        for (i in supozaType.indices) {
            val supoza = supozaType[i]
            val count = (answers.indices).asSequence()
                .filter { supoza[it % supoza.size] == answers[it] }
                .count()
            max = max(max, count)
            matchCount[i] = count
        }

        return matchCount.entries
            .stream()
            .filter { it.value == max }
            .mapToInt { it.key + 1 }
            .sorted()
            .toArray()
    }
}
