class Solution {
    fun solution(n: Int): Int {
        return (2 until n).first { n % it == 1 }
    }
}