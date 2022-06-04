class Solution {
    fun solution(phone_number: String): String {
        val bound = phone_number.length - 4
        return "*".repeat(bound) + phone_number.substring(bound)
    }
}
