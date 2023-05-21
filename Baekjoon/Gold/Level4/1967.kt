var visited: Array<Boolean> = arrayOf()
var nodes = Array(0) { mutableListOf<Item>() }
var maxCount = 0

fun main() {
    val n = readLine()!!.toInt()
    visited = Array(n + 1) { false }
    nodes = Array(n + 1) { mutableListOf() }

    (1 until n).forEach { _ ->
        val info = readLine()!!.split(" ")
            .map { it.toInt() }
        val start = info[0]
        val end = info[1]
        val edge = info[2]
        val node1 = Item(start, edge)
        val node2 = Item(end, edge)
        nodes[start].add(node2)
        nodes[end].add(node1)
    }
    (1..n).forEach { dfs(it) }
    println(maxCount)
}

private fun dfs(index: Int, sum: Int = 0) {
    visited[index] = true
    maxCount = maxCount.coerceAtLeast(sum)
    nodes[index].forEach {
        if (visited[it.node]) {
            return@forEach
        }
        dfs(it.node, sum + it.edge)
    }
    visited[index] = false
}

data class Item(val node: Int, val edge: Int)
