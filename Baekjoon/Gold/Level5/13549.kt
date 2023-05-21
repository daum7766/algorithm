import java.util.*
import kotlin.collections.HashMap

fun main() {
    val input = readLine()!!.split(" ")
        .map { it.toInt() }

    val n = input[0]
    val k = input[1]

    val items = Items()
    items.add(Item(n, 0))
    var answer = Int.MAX_VALUE
    while (items.isNotEmpty()) {
        val item = items.get()
        if (item.isMatchPosition(k)) {
            answer = answer.coerceAtMost(item.count)
        }
        if (answer <= item.count) {
            continue
        }
        items.add(item.doubleItem())
        items.add(item.nextItem())
        items.add(item.beforeItem())
    }
    println(answer)
}

private class Items {

    companion object {
        private const val MAX_POSITION = 150_000
    }

    val visited = HashMap<Int, Int>(131_072)
    val items: Queue<Item> = LinkedList()

    fun add(item: Item) {
        if (visited.getOrDefault(item.position, MAX_POSITION) <= item.count
            || item.position > MAX_POSITION
            || item.position < 0) {
            return
        }
        visited[item.position] = item.count
        items.add(item)
    }

    fun isNotEmpty(): Boolean {
        return items.isNotEmpty()
    }

    fun get(): Item {
        return items.poll()
    }
}

private class Item(val position: Int, val count: Int) {

    fun nextItem(): Item {
        return Item(position + 1, count + 1)
    }

    fun beforeItem(): Item {
        return Item(position - 1, count + 1)
    }

    fun doubleItem(): Item {
        return Item(position * 2, count)
    }

    fun isMatchPosition(position: Int): Boolean {
        return this.position == position
    }
}
