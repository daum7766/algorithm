class Solution {
    fun solution(s: String): String {
        return s.toCharArray()
            .sortedArrayDescending()
            .joinToString("")
    }
}