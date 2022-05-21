class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val counts = init(n, lost, reserve)
        for (i in counts.indices) {
            search(counts, i)
        }
        return counts.toList()
            .stream()
            .filter { it > 0}
            .count()
            .toInt()
    }

    private fun init(n: Int, lost: IntArray, reserve: IntArray): IntArray {
        val counts = IntArray(n) { 1 }
        for (i in lost) {
            counts[i - 1]--
        }
        for (i in reserve) {
            counts[i - 1]++
        }
        return counts
    }

    private fun search(counts: IntArray, i: Int) {
        if (counts[i] != 0) {
            return
        }
        if (i > 0 && counts[i - 1] > 1) {
            counts[i - 1]--
            counts[i]++
            return
        }
        if (i < counts.size - 1 && counts[i + 1] > 1) {
            counts[i + 1]--
            counts[i]++
        }
    }
}
