class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        val stack = mutableListOf<Int>()
        (board.indices).map { x ->
            (board.indices).map {
                board[it][x]
            }.filter { it != 0 }
                .toMutableList()
        }.toList()
            .let {
                moves.forEach { move ->
                    answer += calculate(stack, it[move - 1].removeFirstOrNull())
                }
            }
        return answer
    }

    private fun calculate(stack: MutableList<Int>,
        number: Int?): Int {
        if (stack.isNotEmpty() && stack.last() == number) {
            stack.removeLast()
            return 2
        }
        if (number != null) {
            stack.add(number)
        }
        return 0
    }
}
