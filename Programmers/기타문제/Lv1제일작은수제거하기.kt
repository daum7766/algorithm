class Solution {
    fun solution(arr: IntArray): IntArray {
        return when (arr.size) {
            1 -> intArrayOf(-1)
            else -> {
                val minValue = arr.minOrNull()!!
                arr.filter { it > minValue }
                    .toIntArray()
            }
        }
    }
}