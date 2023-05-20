fun main() {
    val input = readLine()!!.split(" ").map { it.toInt() }

    val n = input[0]
    val k = input[1]
    val items = (0 until n).map {
        readLine()!!.split(" ").map { it.toInt() }
    }.sortedBy { it[0] }

    val dp = Array(n + 1) { Array(k + 1) { 0 } }

    (1..n).forEach { i ->
        (1..k).forEach { j ->
            dp[i][j] = findValue(items, i, j, dp)
        }
    }

    println(dp[n][k])
}

private fun findValue(
    items: List<List<Int>>,
    i: Int,
    j: Int,
    dp: Array<Array<Int>>
): Int {
    if (items[i - 1][0] <= j) {
        return dp[i - 1][j].coerceAtLeast(dp[i - 1][j - items[i - 1][0]] + items[i - 1][1])
    }
    return dp[i - 1][j]
}
