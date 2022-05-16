class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        val value: Long = (1L .. count).asSequence()
            .map { it * price }
            .sum() - money

        if (value < 0L) {
            return 0L
        }
        return value
    }
}