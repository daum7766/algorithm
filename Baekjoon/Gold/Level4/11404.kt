fun main() {
    val n = readLine()!!.toInt()
    val m = readLine()!!.toInt()
    val graph = Array(n) { Array(n) { Long.MAX_VALUE } }
    repeat(m) {
        val info = readLine()!!.split(" ")
            .map { it.toInt() }
        val start = info[0] - 1
        val end = info[1] - 1
        val weight = info[2]
        graph[start][end] = graph[start][end].coerceAtMost(weight.toLong())
    }
    floydWarshall(graph)
    // 갈수없는 곳이 있다면 0으로 출력하라는 조건이 있음
    (graph.indices).forEach { i ->
        (graph.indices).forEach { j ->
            if (graph[i][j] == Long.MAX_VALUE) {
                graph[i][j] = 0
            }
        }
    }
    println(graph.joinToString("\n") {
        it.joinToString(" ")
    })
}

fun floydWarshall(graph: Array<Array<Long>>) {
    (graph.indices).forEach { z ->
        graph[z][z] = 0L
    }
    (graph.indices).forEach { k ->
        (graph.indices).forEach { i ->
            (graph.indices).forEach { j ->
                if (graph[i][k] != Long.MAX_VALUE && graph[k][j] != Long.MAX_VALUE) {
                    graph[i][j] = graph[i][j].coerceAtMost(graph[i][k] + graph[k][j])
                }
            }
        }
    }
}
