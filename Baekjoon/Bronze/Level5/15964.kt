fun main() {
    println(
        readLine()!!.split(" ")
            .map { it.toLong() }
            .reduce { a, b -> (a + b) * (a - b) }
    )
}
