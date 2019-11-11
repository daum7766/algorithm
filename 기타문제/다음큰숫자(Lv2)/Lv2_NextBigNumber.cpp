#include <string>
#include <vector>
#include <iostream>

using namespace std;

int bitcheck(int k) {
	int count = 0;
	//k가 0이될때까지 반복
	while (k) {
		//k와 1과 비트연산(홀수면 참)
		if (k & 1)	count++;
		//k값 쉬프트-> 나누기 2와 동일
		k >>= 1;
	}
	return count;
}

int solution(int n) {
	int answer = n;
	//입력값 1의 개수구하기
	int bit = bitcheck(n);
	//입력된 비트값과 1이 동일한 개수구하면 멈춤
	while (true)
		if (bit == bitcheck(++answer))
			break;
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
	print(78, 83);
	print(15, 23);
	return 0;
}
