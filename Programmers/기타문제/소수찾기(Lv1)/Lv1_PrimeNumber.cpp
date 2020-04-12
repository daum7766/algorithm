#include <string>
#include <vector>
#include <iostream>

using namespace std;
bool memo[1000000]{ false };
/*
메모이 제이션과
에라토스테니스의 체를 이용한 문제풀이
*/

int solution(int n) {
	int answer = 0;
	for (int i = 2; i <= n; i++) {
		//어떤 수의 배수였다면 소수가 아니므로 패스
		if (memo[i - 1])		continue;
		//위의 조건을 건너왔다면 소수가 아니므로 카운트 증가
		answer++;
		//현재수의 배수부터 N까지 자신의 배수는 소수가 아닌것으로 변환
		for (int j = i + i; j <= n; j += i)		memo[j - 1] = true;
	}
	return answer;
}

void print(int n, int answer) {
	int t = solution(n);
	if (answer == t)	cout << "정답" << endl;
	else	cout << "틀림" << endl;
}

int main() {
	print(10, 4);
	print(5, 3);
	return 0;
}