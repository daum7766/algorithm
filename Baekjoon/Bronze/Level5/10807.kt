import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    scanner.nextLine()
    val numbers = scanner.nextLine()
        .split(" ")
        .groupingBy { it.toLong() }
        .eachCount()
    println(numbers.getOrDefault(scanner.nextLong(), 0))
}
