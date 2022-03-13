import java.util.*

private val scanner = Scanner(System.`in`)

fun main() {
    for (i in 0 until scanner.nextLine().toInt()) {
        println(solution())
    }
}

fun solution(): String {
    val treeMap = TreeMap<Int, Int>()

    for (i in 0 until scanner.nextLine().toInt()) {
        val command = scanner.nextLine().split(" ")
        val value = command[1].toInt()
        execute(command, treeMap, value)
    }
    if (treeMap.isEmpty()) {
        return "EMPTY"
    }
    return "${treeMap.lastKey()} ${treeMap.firstKey()}"
}

private fun execute(
    command: List<String>,
    treeMap: TreeMap<Int, Int>,
    value: Int
) {
    if ("I" == command[0]) {
        treeMap[value] = treeMap.getOrDefault(value, 0) + 1
    } else if (treeMap.isNotEmpty()) {
        val entry: Map.Entry<Int, Int> = getEntry(value, treeMap)
        deleteValue(entry, treeMap)
    }
}


private fun getEntry(
    value: Int,
    treeMap: TreeMap<Int, Int>
): Map.Entry<Int, Int> {
    return if (value == 1) {
        treeMap.lastEntry()
    } else {
        treeMap.firstEntry()
    }
}

private fun deleteValue(
    entry: Map.Entry<Int, Int>,
    treeMap: TreeMap<Int, Int>
) {
    if (entry.value == 1) {
        treeMap.remove(entry.key)
    } else {
        treeMap[entry.key] = entry.value - 1
    }
}
