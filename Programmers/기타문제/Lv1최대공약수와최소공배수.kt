class Solution {
    fun solution(n: Int, m: Int): IntArray {
        val gcd = gcd(n, m)
        return intArrayOf(gcd, n * m / gcd)
    }

    private fun gcd(n: Int, m: Int): Int {
        return when (m != 0) {
            true -> gcd(m, n % m)
            false -> n
        }
    }
}