class Solution {
    fun solution(s: String, n: Int): String {
        return s.map {
            when {
                it.isLowerCase() -> 'a' + (it + n - 'a') % ('z' + 1 - 'a')
                it.isUpperCase() -> 'A' + (it + n - 'A') % ('Z' + 1 - 'A')
                else -> it
            }
        }.joinToString("")
    }
}