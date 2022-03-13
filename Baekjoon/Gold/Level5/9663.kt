import java.util.*
import kotlin.math.abs

private val scanner = Scanner(System.`in`)
private var size = 0
private var answer = 0
private var array: IntArray = IntArray(0)
private var visited: IntArray = IntArray(0)

fun main() {
    solution()
    println(answer)
}

private fun solution() {
    size = scanner.nextLine().toInt()
    array = IntArray(size)
    visited = IntArray(size)
    dfs(0)
}

private fun dfs(depth: Int) {
    if (depth == size) {
        answer++
        return
    }
    for (index in 0 until size) {
        if (visited[index] == 1 || possible(depth, index)) {
            continue
        }
        visited[index] = 1
        array[depth] = index
        dfs(depth + 1)
        visited[index] = 0
    }
}

private fun possible(depth: Int, index: Int): Boolean {
    for (i in 0 until depth) {
        if (depth - i == abs(index - array[i])) {
            return true
        }
    }
    return false
}