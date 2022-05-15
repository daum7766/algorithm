class Solution {
    // 시간복잡도 신경 X
    // 두개가 일치하는것 찾기
    // 0의 개수 카운팅하기
    // 최대 최소 결과 찾기
    fun solution(lottos: IntArray, winNums: IntArray): IntArray {
        val matchCount: Int = findMatches(lottos, winNums)
        val zeroCount: Int = zeroCount(lottos)
        return intArrayOf(matchResult(matchCount + zeroCount), matchResult(matchCount))
    }

    private fun findMatches(lottos: IntArray, winNums: IntArray): Int {
        val lottosSet: Set<Int> = lottos.toSet()
        val winNumSet: Set<Int> = winNums.toSet()
        return lottosSet.intersect(winNumSet).size
    }

    private fun zeroCount(lottos: IntArray): Int {
        return lottos.toList().count { it == 0 }
    }

    private fun matchResult(matchCount: Int): Int {
        return when (matchCount) {
            6 -> 1
            5 -> 2
            4 -> 3
            3 -> 4
            2 -> 5
            else -> 6
        }
    }
}

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test

class SolutionTest {

    @Test
    fun test1() {
        // given
        val lottos: IntArray = intArrayOf(44, 1, 0, 0, 31, 25)
        val winNums: IntArray = intArrayOf(31, 10, 45, 1, 6, 19)
        val result: IntArray = intArrayOf(3, 5)

        // when
        val answer: IntArray = Solution().solution(lottos, winNums)

        // then
        assertThat(answer).isEqualTo(result)
    }

    @Test
    fun test2() {
        // given
        val lottos: IntArray = intArrayOf(0, 0, 0, 0, 0, 0)
        val winNums: IntArray = intArrayOf(38, 19, 20, 40, 15, 25)
        val result: IntArray = intArrayOf(1, 6)

        // when
        val answer: IntArray = Solution().solution(lottos, winNums)

        // then
        assertThat(answer).isEqualTo(result)
    }

    @Test
    fun test3() {
        // given
        val lottos: IntArray = intArrayOf(45, 4, 35, 20, 3, 9)
        val winNums: IntArray = intArrayOf(20, 9, 3, 45, 4, 35)
        val result: IntArray = intArrayOf(1, 1)

        // when
        val answer: IntArray = Solution().solution(lottos, winNums)

        // then
        assertThat(answer).isEqualTo(result)
    }
}