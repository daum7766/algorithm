class Solution {
    fun solution(x: Int, n: Int): LongArray {
        return (1L .. n.toLong()).map { it * x }
            .toLongArray()
    }
}