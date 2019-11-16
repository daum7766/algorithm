#include <string>
#include <iostream>

using namespace std;

/*
n이 15라고 하자
0. 1조합은 아래와 같이 계산해보세요.

1. 2개조합이라면, 1과 2를 더하고 n에서 빼준다.
2. 15-(1+2) =12 가 되고, 12를 조합개수인 2로 나눈다.
3. 12를 2로나누면 나머지가 0이므로 카운트를 증가시킨다.
검증 :
	12를 2로나누면 몫은 6이고 위에서 사용했던 1과 2를 각각 더한다.
	(6+1) + (6+2) = 7 + 8 =15

4. 3조합을 본다. 1,2,3을 더하고 n에서 빼준다.
5. 15-(1+2+3) = 9 가되고 9를 조합개수인 3으로 나눈다.
6. 9%3 은 0이되므로 카운트를 증가시킨다.
검증 :
	9를 3으로 나누면 몫은 3이되고 위에서 사용한 1,2,3을 각각 더한다.
	(3+1)+(3+2)+(3+3) = 4 + 5 + 6 = 15;

7. 4조합을 본다. 1,2,3,4를 더하고 n에서 빼준다.
8. 15-(1+2+3+4) = 5가 되고, 5를 조합개수인 4로 나눈다.
9. 5%4는 0이 아니므로 다음조합으로 넘어간다..

10. 5조합을 본다. 1,2,3,4,5를 더하고 n에서 빼준다.
11. 15-(1+2+3+4+5) = 0이 되고, 조합개수인 5로 나눈다.
12. 0%5는 0이므로 카운트를 증가시킨다.
검증 :
	몫은 0이고 각각을 더해본다.
	(0+1)+(0+2)+(0+3)+(0+4)+(0+5) = 1+2+3+4+5 = 15

13. 6조합부터는 합이 n보다 커지므로 계산하지 않는다.

*/

int solution(int n) {
	//정답개수, 더하는 개수, 합
	int answer = 0, nums = 1, sum = 0;
	while (true) {
		sum = 0;
		//2개 조합부터 찾아보기
		for (int i = 1; i <= nums; i++)	sum += i;
		//sum이 n보다 커진다면 반복문 탈출
		if (sum > n)	break;
		//n-sum이 더하는 개수로 나누어진다면 카운트 증가
		if ((n - sum) % nums++ == 0)	answer++;
	}
	//자기자신만 더하는 방법이 있으므로 1개추가
	return answer;
}

void print(int n, int answer) {
	int t = solution(n);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print(15, 4);
	return 0;
}