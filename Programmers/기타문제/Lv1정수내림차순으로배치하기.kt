class Solution {
    fun solution(n: Long): Long {
        return n.toString()
            .toCharArray()
            .sortedArrayDescending()
            .joinToString("")
            .toLong()
    }
}