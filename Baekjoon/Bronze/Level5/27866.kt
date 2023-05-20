import java.util.*

private val scanner = Scanner(System.`in`)

fun main() {
    val word = scanner.nextLine()
    println(word[scanner.nextInt() - 1])
}
