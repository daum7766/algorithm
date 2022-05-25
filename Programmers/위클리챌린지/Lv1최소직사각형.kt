class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        val sortedSize = sizes.map { it.sorted() }
        return sortedSize.maxOf { it[0] } * sortedSize.maxOf { it[1] }
    }
}