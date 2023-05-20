import java.util.*
import kotlin.math.abs

fun main() {
    val scanner = Scanner(System.`in`)
    val nm = scanner.nextLine()
        .split(" ")
        .map { it.toLong() }
    println(abs(nm[0] - nm[1]))
}
