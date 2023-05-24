import java.util.*

fun main() {
    val (n, m) = readLine()!!.split(" ")
        .map { it.toInt() }

    val map = Array(n) {
        readLine()!!.map { it.digitToInt() }
            .toIntArray()
    }
    val items = Items(n, m, map)
    items.add(Item(0, 0, 1))
    items.find()
    println(items.getAnswer())
}

private class Items(val n: Int, val m: Int, val map: Array<IntArray>) {
    private val visited = Array(n) { Array(m) { Array(2) { false } } }
    private val queue: Queue<Item> = LinkedList()
    private var answer = -1

    fun add(item: Item) {
        if (item.y == n - 1 && item.x == m - 1) {
            answer = item.count
            return
        }
        if (item.y < 0 || item.x < 0 || item.y >= n || item.x >= m) {
            return
        }
        if (map[item.y][item.x] == 1 && item.broken) {
            return
        }
        if (visited[item.y][item.x][1] || visited[item.y][item.x][0] && item.broken) {
            return
        }
        if (!item.broken) {
            visited[item.y][item.x][1] = true
        }
        visited[item.y][item.x][0] = true
        if (map[item.y][item.x] == 1 && !item.broken) {
            queue.add(item.brokenItem())
            return
        }
        queue.add(item)
    }

    fun find() {
        visited[0][0][0] = true
        visited[0][0][1] = true
        while (queue.isNotEmpty() && answer == -1) {
            val item = queue.poll()
            add(item.up())
            add(item.down())
            add(item.left())
            add(item.right())
        }
    }

    fun getAnswer(): Int {
        return answer
    }
}

private class Item(val y: Int, val x: Int, val count: Int = 1, val broken: Boolean = false) {

    fun up(): Item {
        return Item(y - 1, x, count + 1, broken)
    }

    fun down(): Item {
        return Item(y + 1, x, count + 1, broken)
    }

    fun left(): Item {
        return Item(y, x - 1, count + 1, broken)
    }

    fun right(): Item {
        return Item(y, x + 1, count + 1, broken)
    }

    fun brokenItem(): Item {
        return Item(y, x, count, true)
    }
}
