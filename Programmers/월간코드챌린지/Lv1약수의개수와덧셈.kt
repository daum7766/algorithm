class Solution {
    fun solution(left: Int, right: Int): Int {
        return (left..right).sumOf { number ->
            when ((1..number).count { number % it == 0 } % 2) {
                1 -> -number
                else -> number
            }
        }
    }
}