class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        stages.toList()
            .groupingBy { it }
            .eachCount()
            .let { score ->
                var people = score.getOrDefault(N + 1, 0)
                (N downTo 1).map {
                    val count = score.getOrDefault(it, 0)
                    people += count
                    val value = count / people.toDouble()
                    Pair(value, it)
                }
                .sortedWith(compareBy<Pair<Double, Int>> {-it.first}.thenBy { it.second })
                    .forEach {
                        answer.add(it.second)
                    }
            }
        return answer.toIntArray()
    }
}