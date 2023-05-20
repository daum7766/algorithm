import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextInt()
    var answer = 1
    (2 .. n).forEach { answer *= it }
    println(answer)
}
