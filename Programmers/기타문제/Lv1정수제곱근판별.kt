import kotlin.math.pow
import kotlin.math.sqrt

class Solution {
    fun solution(n: Long): Long {
        val sqrt = sqrt(n.toDouble())
        return when (sqrt % 1.0 == 0.0) {
            true -> (sqrt + 1).pow(2).toLong()
            else -> -1
        }
    }
}