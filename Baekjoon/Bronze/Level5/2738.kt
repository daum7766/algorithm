import java.util.*

private val scanner = Scanner(System.`in`)

fun main() {
    val nm = lineToLongList()
    val array1 = inputToMatrix(nm[0])
    val array2 = inputToMatrix(nm[0])

    val combined = array1.zip(array2) { a, b ->
        a.zip(b) { c, d ->
            c + d
        }.joinToString(" ")
    }.joinToString(System.lineSeparator())
    println(combined)
}

private fun lineToLongList() = scanner.nextLine()
    .split(" ")
    .map { it.toLong() }

private fun inputToMatrix(size: Long) = (1..size).map {
    lineToLongList()
}
