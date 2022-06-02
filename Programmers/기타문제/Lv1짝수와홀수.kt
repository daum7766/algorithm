class Solution {
    fun solution(num: Int): String {
        return when (num and 1) {
            1 -> "Odd"
            else -> "Even"
        }
    }
}