import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    val sum = scanner.nextLine()
        .split(" ")
        .sumOf { it.toLong() }
    println(sum)
}
