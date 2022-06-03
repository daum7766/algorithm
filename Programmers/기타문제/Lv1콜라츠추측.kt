class Solution {
    fun solution(num: Int): Int {
        return collatz(num.toLong(), 0)
    }

    private fun collatz(num: Long, depth: Int): Int {
        return when {
            depth == 500 -> -1
            num == 1L -> depth
            num and 1 == 1L -> collatz(num * 3 + 1, depth + 1)
            else -> collatz(num / 2, depth + 1)
        }
    }
}