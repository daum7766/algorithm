import java.math.BigInteger

fun main() {
    println(factorial(1, readLine()!!.toInt()))
}

fun factorial(a: Int, b: Int): BigInteger {
    var value = a.toBigInteger()
    if (a < b) {
        val m = (a + b) / 2
        value = factorial(a, m) * factorial(m + 1, b)
    }
    return value
}
