class Solution {
    fun solution(n: Int): String {
        return (0 until n).joinToString("") { if (it % 2 == 0) "수" else "박" }
    }
}