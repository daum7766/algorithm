class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        return (a.indices).asSequence()
            .map { a[it] * b[it] }
            .sum()
    }
}