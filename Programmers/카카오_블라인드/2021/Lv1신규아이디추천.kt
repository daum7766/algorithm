class Solution {
    fun solution(new_id: String): String {
        return new_id.lowercase()
            .filter { it.isDigit() || it == '-' || it == '_' || it == '.' || it.isLowerCase() }
            .replace("[.]*[.]".toRegex(), ".")
            .removePrefix(".")
            .removeSuffix(".")
            .ifEmpty { "a" }
            .let { if (it.length > 15) it.substring(0 until 15) else it }
            .removeSuffix(".")
            .let {
                if (it.length < 3) {
                    it + it.last()
                        .toString()
                        .repeat(3 - it.length)
                } else it
            }
        
    }
}
