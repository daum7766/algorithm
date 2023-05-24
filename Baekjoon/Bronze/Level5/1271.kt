fun main() {
    val (n, m) = readLine()!!.split(" ")
        .map { it.toBigInteger() }

    println(n / m)
    println(n % m)
}
