fun main() {
    val word1 = readLine()!!
    val word2 = readLine()!!

    println(lcs(word1, word2))
}

private fun lcs(x: String, y: String): Int {
    val m = x.length
    val n = y.length

    val dp = Array(m + 1) { Array(n + 1) { 0 } }

    for (i in 1..m) {
        for (j in 1..n) {
            if (x[i - 1] == y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = dp[i - 1][j].coerceAtLeast(dp[i][j - 1])
            }
        }
    }

    return dp[m][n]
}
