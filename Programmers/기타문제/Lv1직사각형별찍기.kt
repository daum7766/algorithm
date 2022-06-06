fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    println((1..b).joinToString("\n") {
        "*".repeat(a)
    })
}