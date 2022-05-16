class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer = 0
        for (i in absolutes.indices) {
            answer += getNumber(signs[i], absolutes[i])
        }
        return answer
    }

    private fun getNumber(sign: Boolean, number: Int): Int {
        if (sign) {
            return number
        }
        return -number
    }
}