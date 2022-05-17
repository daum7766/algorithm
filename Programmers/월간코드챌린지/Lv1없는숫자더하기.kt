class Solution {
    fun solution(numbers: IntArray): Int {
        val intArray = IntArray(10)
        for (number: Int in numbers) {
            intArray[number] = 1
        }
        return (0 until 10).asSequence()
            .filter { intArray[it] == 0 }
            .sum()
    }
}