class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        return arr.filter { it % divisor == 0 }
            .sorted()
            .ifEmpty { listOf(-1) }
            .toIntArray()
    }
}