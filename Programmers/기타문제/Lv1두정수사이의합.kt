import kotlin.math.max
import kotlin.math.min

class Solution {
    fun solution(a: Int, b: Int): Long {
        return (min(a, b) .. max(a, b)).sumOf { it.toLong() }
    }
}