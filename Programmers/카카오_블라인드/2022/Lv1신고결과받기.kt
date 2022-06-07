class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        return report.toSet()
            .map { it.split(" ") }
            .groupBy({ it[1] }, { it[0] })
            .filterValues { it.size >= k }
            .map { it.value }
            .flatten()
            .groupingBy { it }
            .eachCount()
            .run { id_list.map { getOrDefault(it, 0) }
                .toIntArray()
            }
    }
}
