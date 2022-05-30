class Solution {
    fun solution(s: String): String {
        return s.split(" ").joinToString(" ") {
            it.mapIndexed { index, c ->
                when {
                    index % 2 == 0 -> c.uppercaseChar()
                    else -> c.lowercaseChar()
                }
            }.joinToString("")
        }
    }
}
