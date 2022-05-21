class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        val answer = IntArray(commands.size)
        for (i in commands.indices) {
            val command = commands[i]
            answer[i] = (command[0] - 1 until command[1]).asSequence()
                .map { array[it] }
                .sorted()
                .elementAt(command[2] - 1)
        }
        return answer
    }
}