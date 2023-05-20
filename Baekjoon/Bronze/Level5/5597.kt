import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    val students = BooleanArray(30 + 1)
    (0 .. 27).forEach { _ ->
        students[scanner.nextInt()] = true
    }
    var count = 0
    (1 .. 30).forEach {
        if (!students[it]) {
            println(it)
            count++
        }
        if (count == 2) {
            return
        }
    }
}
