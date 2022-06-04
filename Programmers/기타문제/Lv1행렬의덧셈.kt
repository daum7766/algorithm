class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        return arr1.mapIndexed { x, numbers ->
            numbers.mapIndexed { y, number ->
                arr2[x][y] + number
            }.toIntArray()
        }.toTypedArray()
    }
}
