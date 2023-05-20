import java.util.*

private val scanner = Scanner(System.`in`)

fun main() {
    val value = scanner.nextLine()
        .map { upperLowerChange(it) }
        .joinToString("")
    println(value)
}

private fun upperLowerChange(c: Char): Char {
    if (c.isUpperCase()) {
        return c.lowercaseChar()
    }
    return c.uppercaseChar()
}
