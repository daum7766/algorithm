import kotlin.math.abs

class Solution {
    companion object {
        private val position = mapOf(
            "*" to listOf(0, 0),
            "7" to listOf(1, 0),
            "4" to listOf(2, 0),
            "1" to listOf(3, 0),
            "0" to listOf(0, 1),
            "8" to listOf(1, 1),
            "5" to listOf(2, 1),
            "2" to listOf(3, 1),
            "#" to listOf(0, 2),
            "9" to listOf(1, 2),
            "6" to listOf(2, 2),
            "3" to listOf(3, 2),
        )
    }
    private var left = "*"
    private var right = "#"
    private var hand = ""

    fun solution(numbers: IntArray, hand: String): String {
        this.hand = if (hand == "left") "L" else "R"
        return numbers.joinToString("") {
            movedHand(it.toString())
        }
    }

    private fun movedHand(number: String): String {
        return when (number) {
            "1" ,"4", "7" -> setLeft(number)
            "3", "6", "9", -> setRight(number)
            else -> selectedFinger(number)
        }
    }

    private fun selectedFinger(number: String): String {
        val targetPosition = position[number]!!
        val leftDistance = calculateDistance(position[left]!!, targetPosition)
        val rightDistance = calculateDistance(position[right]!!, targetPosition)

        return when {
            leftDistance == rightDistance -> {
                if (hand == "L") left = number else right = number
                return hand
            }
            leftDistance > rightDistance -> setRight(number)
            else -> setLeft(number)
        }
    }

    private fun calculateDistance(fingerPosition: List<Int>, targetPosition: List<Int>): Int {
        return abs(fingerPosition[0] - targetPosition[0]) + abs(fingerPosition[1] - targetPosition[1])
    }
    
    private fun setLeft(number: String): String {
        left = number
        return "L"
    }
    
    private fun setRight(number: String): String {
        right = number
        return "R"
    }
}
