import java.math.BigInteger

class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                for (k in j + 1 until nums.size) {
                    val value = BigInteger((nums[i] + nums[j] + nums[k]).toString())
                    if (value.isProbablePrime(10)) {
                        answer++
                    }
                }
            }
        }
        return answer
    }
}