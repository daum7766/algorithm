class Solution {
    fun solution(numbers: IntArray): IntArray {
        return (numbers.indices).flatMap { i ->
            (i + 1 until numbers.size)
                .filter { i != it }
                .map { numbers[i] + numbers[it] }
        }
            .distinct()
            .sorted()
            .toIntArray()
    }
}